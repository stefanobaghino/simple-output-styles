"""Provision the pinned Claude CLI into the managed store.

The hermetic resolution serves the managed binary of the pin ahead
of the PATH, so an auto-update on the machine stops touching the
runs — once this command fills the store. Two routes: the version
store of the native installer, offline; else a download from the
release endpoint of the official installer, verified against the
manifest checksum. This module is the only place where the harness
touches the network, and only inside this explicit command: run
time stays offline, and a machine without the managed binary falls
back to the PATH plus the version check.

Both routes end in one verification — the candidate must report the
pinned version — and an atomic rename, so the store never holds a
partial or unverified binary.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import sys
import tempfile
import urllib.request
from collections.abc import Callable
from pathlib import Path

from runner.hermetic import MANAGED_STORE
from runner.pin import CLI_VERSION_BARE, CLI_VERSION_PIN
from runner.provenance import claude_version, sha256_of

# The version store of the native installer: one self-contained
# binary per version, named after the bare number.
INSTALLER_STORE = Path(".local/share/claude/versions")

# The release endpoint of the official installer bootstrap. The
# bootstrap itself is unusable here: it runs the CLI's own install
# subcommand, which flips the machine default. The endpoint under
# it serves the manifest and the per-platform binary directly.
RELEASE_BASE = "https://downloads.claude.ai/claude-code-releases"

# The platform keys of the release manifest. The musl and win32
# variants exist in the manifest but stay out of scope here.
PLATFORM_KEYS = {
    ("Darwin", "arm64"): "darwin-arm64",
    ("Darwin", "x86_64"): "darwin-x64",
    ("Linux", "x86_64"): "linux-x64",
    ("Linux", "aarch64"): "linux-arm64",
}

Fetcher = Callable[[str, Path], None]


def http_fetch(url: str, dest: Path) -> None:
    with urllib.request.urlopen(url, timeout=60) as response, dest.open("wb") as out:
        shutil.copyfileobj(response, out)


def _download(dest: Path, fetch: Fetcher) -> str | None:
    """Fetch the pinned binary from the release endpoint.

    Returns None on success, else the reason the route cannot serve.
    A failure can leave bytes in dest; the caller owns the cleanup.
    """
    key = PLATFORM_KEYS.get((platform.system(), platform.machine()))
    if key is None:
        return f"no release platform key exists for {platform.system()}/{platform.machine()}"
    manifest_url = f"{RELEASE_BASE}/{CLI_VERSION_BARE}/manifest.json"
    try:
        with tempfile.TemporaryDirectory(prefix="style-provision-") as scratch:
            manifest_path = Path(scratch) / "manifest.json"
            fetch(manifest_url, manifest_path)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        entry = manifest["platforms"][key]
        fetch(f"{RELEASE_BASE}/{CLI_VERSION_BARE}/{key}/{entry['binary']}", dest)
    except (OSError, KeyError, ValueError) as error:
        return f"the download from {manifest_url} failed: {error!r}"
    if sha256_of(dest) != entry["checksum"]:
        return f"the downloaded binary does not match the checksum of {manifest_url}"
    return None


def _status(managed_path: Path, installer_path: Path) -> int:
    print(f"pin: {CLI_VERSION_PIN}")
    installer = "present" if installer_path.is_file() else "absent"
    print(f"installer store: {installer_path} ({installer})")
    print(f"managed binary: {managed_path}")
    if not managed_path.is_file():
        print("not provisioned")
        return 1
    found = claude_version(str(managed_path))
    if found != CLI_VERSION_PIN:
        print(f"provisioned binary reports {found!r} — run style-provision again")
        return 1
    print("provisioned")
    return 0


def main(argv: list[str] | None = None, fetch: Fetcher = http_fetch) -> int:
    parser = argparse.ArgumentParser(
        description="provision the pinned Claude CLI into the managed store"
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="report the store without provisioning: exit 0 when the pin is served",
    )
    args = parser.parse_args(argv)

    home = os.environ.get("HOME")
    if not home:
        print("HOME is not set, so no store location exists", file=sys.stderr)
        return 2
    managed_path = Path(home) / MANAGED_STORE / CLI_VERSION_BARE / "claude"
    installer_path = Path(home) / INSTALLER_STORE / CLI_VERSION_BARE

    if args.status:
        return _status(managed_path, installer_path)

    if managed_path.is_file() and claude_version(str(managed_path)) == CLI_VERSION_PIN:
        print(f"already provisioned: {managed_path}")
        return 0

    managed_path.parent.mkdir(parents=True, exist_ok=True)
    # The candidate lands next to its target, so the final rename is
    # atomic: no reader of the store ever sees a partial binary.
    tmp = managed_path.parent / f".provision-{os.getpid()}"
    try:
        if installer_path.is_file():
            shutil.copyfile(installer_path, tmp)
            route = f"installer store {installer_path}"
        else:
            reason = _download(tmp, fetch)
            if reason is not None:
                print(
                    f"no source serves the pin {CLI_VERSION_PIN!r}: the installer "
                    f"store holds no {installer_path}, and {reason}; the harness "
                    "still runs through the PATH plus the version check",
                    file=sys.stderr,
                )
                return 2
            route = "release download"
        tmp.chmod(0o755)
        found = claude_version(str(tmp))
        if found != CLI_VERSION_PIN:
            print(
                f"the candidate from the {route} reports {found!r} instead of "
                f"{CLI_VERSION_PIN!r}; nothing landed in the store",
                file=sys.stderr,
            )
            return 2
        os.replace(tmp, managed_path)
    finally:
        tmp.unlink(missing_ok=True)
    print(f"provisioned {CLI_VERSION_PIN!r} from the {route} into {managed_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
