"""Tests for the provision command.

provision.cli stays out of the pinned_cli_version fixture of
conftest.py on purpose: these tests run real stub executables under
the scratch HOME, and a patched claude_version would blind the
verify-failure paths.
"""

import hashlib
import json
import os
import platform
import sys
from pathlib import Path

from provision.cli import INSTALLER_STORE, PLATFORM_KEYS, RELEASE_BASE, main
from runner.hermetic import MANAGED_STORE, hermetic_call
from runner.pin import CLI_VERSION_BARE, CLI_VERSION_PIN


def stub_bytes(version=CLI_VERSION_PIN):
    return f'#!{sys.executable}\nprint("{version}")\n'.encode()


def make_installer_store(version_body=None):
    store = Path(os.environ["HOME"]) / INSTALLER_STORE
    store.mkdir(parents=True)
    binary = store / CLI_VERSION_BARE
    binary.write_bytes(version_body or stub_bytes())
    binary.chmod(0o755)
    return binary


def managed_path():
    return Path(os.environ["HOME"]) / MANAGED_STORE / CLI_VERSION_BARE / "claude"


class FakeFetcher:
    """Serves prepared bytes per URL and records every request."""

    def __init__(self, files=None):
        self.files = files or {}
        self.calls = []

    def __call__(self, url, dest):
        self.calls.append(url)
        payload = self.files[url]
        if isinstance(payload, Exception):
            raise payload
        dest.write_bytes(payload)


def release_urls():
    key = PLATFORM_KEYS[(platform.system(), platform.machine())]
    return f"{RELEASE_BASE}/{CLI_VERSION_BARE}/manifest.json", (
        f"{RELEASE_BASE}/{CLI_VERSION_BARE}/{key}/claude"
    )


def make_release(body=None, checksum=None):
    body = body or stub_bytes()
    key = PLATFORM_KEYS[(platform.system(), platform.machine())]
    manifest = {
        "version": CLI_VERSION_BARE,
        "platforms": {
            key: {
                "binary": "claude",
                "checksum": checksum or hashlib.sha256(body).hexdigest(),
                "size": len(body),
            }
        },
    }
    manifest_url, binary_url = release_urls()
    return FakeFetcher({manifest_url: json.dumps(manifest).encode(), binary_url: body})


def test_provision_copies_the_installer_binary_into_the_managed_store(capsys):
    make_installer_store()
    fetcher = FakeFetcher()

    assert main([], fetch=fetcher) == 0
    assert fetcher.calls == []
    target = managed_path()
    assert target.is_file()
    assert os.access(target, os.X_OK)
    assert "installer store" in capsys.readouterr().out
    # The acceptance hop: a live invocation now resolves the managed
    # binary, through the scratch HOME of the test.
    with hermetic_call("test") as h:
        assert h.binary == str(target)
        assert h.binary_source == "managed"


def test_provision_is_idempotent_when_the_store_already_holds_the_pin(capsys):
    make_installer_store()
    assert main([], fetch=FakeFetcher()) == 0
    first_stat = managed_path().stat()

    assert main([], fetch=FakeFetcher()) == 0
    assert "already provisioned" in capsys.readouterr().out
    assert managed_path().stat().st_mtime_ns == first_stat.st_mtime_ns


def test_provision_downloads_when_the_installer_store_lacks_the_version(capsys):
    fetcher = make_release()

    assert main([], fetch=fetcher) == 0
    assert fetcher.calls == list(release_urls())
    assert managed_path().is_file()
    assert "release download" in capsys.readouterr().out


def test_provision_rejects_a_checksum_mismatch(capsys):
    fetcher = make_release(checksum="0" * 64)

    assert main([], fetch=fetcher) == 2
    assert not any(managed_path().parent.iterdir())
    assert "checksum" in capsys.readouterr().err


def test_provision_rejects_a_binary_that_reports_another_version(capsys):
    make_installer_store(version_body=stub_bytes("9.9.9 (test)"))

    assert main([], fetch=FakeFetcher()) == 2
    assert not any(managed_path().parent.iterdir())
    err = capsys.readouterr().err
    assert "9.9.9 (test)" in err
    assert CLI_VERSION_PIN in err


def test_provision_reports_both_routes_when_neither_serves(capsys):
    manifest_url, _ = release_urls()
    fetcher = FakeFetcher({manifest_url: OSError("connection refused")})

    assert main([], fetch=fetcher) == 2
    err = capsys.readouterr().err
    assert str(Path(INSTALLER_STORE) / CLI_VERSION_BARE) in err
    assert manifest_url in err
    assert "PATH plus the version check" in err
    assert not managed_path().is_file()


def test_provision_status_reports_the_store(capsys):
    assert main(["--status"], fetch=FakeFetcher()) == 1
    assert "not provisioned" in capsys.readouterr().out

    make_installer_store()
    assert main([], fetch=FakeFetcher()) == 0
    assert main(["--status"], fetch=FakeFetcher()) == 0
    assert "provisioned" in capsys.readouterr().out
