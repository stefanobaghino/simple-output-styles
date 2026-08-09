"""One hermetic config directory per tool invocation.

The flag-level and workdir-level isolation leaves one hole: the user
configuration enters every call, because the CLI reads plugins and
settings from the user config directory. This module closes the hole.
A tool invocation gets a fresh config directory, the CLI reads it
through CLAUDE_CONFIG_DIR, and the call runs under a whitelisted
environment instead of the inherited one. Thus zero user plugins
load, and a config edit on the machine cannot change a call.

The credential has three routes. When ANTHROPIC_API_KEY is set, the
key passes through in the environment, the calls bill the Console
account of the key, and the subscription credential stays out. Else,
when CLAUDE_CODE_OAUTH_TOKEN is set, the token passes through in
the environment and nothing is written. Else, an existing
~/.claude/.credentials.json is copied into the hermetic directory
with mode 600 and removed with it. The credential never lands in
the run data. Without a credential, the invocation warns and
proceeds: a call without a valid credential fails with zero tokens
spent, so the failure is cheap and loud.

The environment also forces the 5-minute prompt-cache lifetime on
every call, because caching is a billing condition, not a call
condition: see CACHE_TTL_VAR.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import tempfile
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

from .generate import isolated_workdir

# The config mode of a call, recorded in the provenance: the mode
# marks the comparability era of a run, because a user plugin in the
# context changes the input of every call. WORKDIR_MODE is the
# precedent.
CONFIG_MODE = "hermetic"

CONFIG_DIR_VAR = "CLAUDE_CONFIG_DIR"
# The API key routes the bill of a call to the Console account of
# the key instead of the subscription of the machine. When the key
# is set, it is the only credential a call sees: the token and the
# credential file stay out, so which account pays is never a race
# between two credentials. The route changes the bill of a call and
# never its answer, so it stays outside the manifest declaration
# below, like CACHE_TTL_VAR: no comparability era opens.
API_KEY_VAR = "ANTHROPIC_API_KEY"
TOKEN_VAR = "CLAUDE_CODE_OAUTH_TOKEN"
CREDENTIALS_FILE = ".credentials.json"

# The environment of a call: these variables pass through from the
# parent, plus CONFIG_DIR_VAR, plus at most one credential variable
# when set, plus CACHE_TTL_VAR. Everything else stays out.
ENV_WHITELIST = ("HOME", "PATH", "TERM", "USER")

# Every call forces the 5-minute prompt-cache lifetime. On
# subscription billing the CLI requests the 1-hour lifetime, whose
# cache writes cost 2 times an uncached token against 1.25 for the
# 5-minute lifetime. The harness re-reads its cache within minutes,
# and a cache read refreshes the lifetime, so the shorter lifetime
# loses no reads and cuts the write bill. The variable changes the
# billing of a call and never its answer, so it stays outside the
# manifest declaration below on purpose: no comparability era opens.
CACHE_TTL_VAR = "FORCE_PROMPT_CACHING_5M"

# The declared file inputs of the hermetic directory, as a map from
# relative path to sha256. The map is empty at this time, because an
# empty directory needs no onboarding. The credential stays out by
# design, so the manifest hash is identical on every machine.
DECLARED_FILES: dict[str, str] = {}


@dataclass(frozen=True)
class Hermetic:
    """The isolation state of one tool invocation."""

    workdir: Path
    config_dir: Path
    env: dict[str, str]
    binary: str | None
    manifest_sha256: str
    credential_source: str


def manifest_sha256() -> str:
    """The hash of the declared inputs of a call.

    The hash covers the declaration, not the runtime contents: the
    config mode, the environment names, and the declared files. A
    change in any declared input changes the hash and thus opens a
    visible era. The reuse key of the result store builds on this
    hash.
    """
    manifest = {
        "config_mode": CONFIG_MODE,
        "env": [*ENV_WHITELIST, CONFIG_DIR_VAR],
        "files": DECLARED_FILES,
    }
    payload = json.dumps(manifest, sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def resolve_credential(environ: Mapping[str, str]) -> tuple[str, str | None]:
    """Find the credential of a call.

    Returns the route and the file payload: ("api_key", None) when
    the API key variable is set, ("token", None) when the token
    variable is set, ("file", payload) when the user credentials
    file exists, ("none", None) otherwise. The first match wins, so
    the API key silences the subscription routes.
    """
    if environ.get(API_KEY_VAR):
        return "api_key", None
    if environ.get(TOKEN_VAR):
        return "token", None
    home = environ.get("HOME")
    if home:
        source = Path(home) / ".claude" / CREDENTIALS_FILE
        if source.is_file():
            return "file", source.read_text(encoding="utf-8")
    return "none", None


def build_env(config_dir: Path, environ: Mapping[str, str]) -> dict[str, str]:
    """The whitelisted environment of a call."""
    env = {name: environ[name] for name in ENV_WHITELIST if name in environ}
    env[CONFIG_DIR_VAR] = str(config_dir)
    if environ.get(API_KEY_VAR):
        env[API_KEY_VAR] = environ[API_KEY_VAR]
    elif environ.get(TOKEN_VAR):
        env[TOKEN_VAR] = environ[TOKEN_VAR]
    env[CACHE_TTL_VAR] = "1"
    return env


@contextmanager
def hermetic_call(tool: str, environ: Mapping[str, str] = os.environ) -> Iterator[Hermetic]:
    """The workdir plus the hermetic config directory of one invocation.

    The config directory lives as long as the workdir: one tool
    invocation, shared by every parallel call. The drift sessions of
    one invocation thus resume against the same directory. The
    credential file, when written, is removed with the directory.
    """
    with (
        isolated_workdir(tool) as workdir,
        tempfile.TemporaryDirectory(prefix=f"style-config-{tool}-") as name,
    ):
        config_dir = Path(name)
        source, payload = resolve_credential(environ)
        if payload is not None:
            target = config_dir / CREDENTIALS_FILE
            target.write_text(payload, encoding="utf-8")
            target.chmod(0o600)
        if source == "none":
            print(
                "no credential found: live calls will fail without spending tokens",
                file=sys.stderr,
            )
        env = build_env(config_dir, environ)
        yield Hermetic(
            workdir=workdir,
            config_dir=config_dir,
            env=env,
            binary=shutil.which("claude", path=env.get("PATH")),
            manifest_sha256=manifest_sha256(),
            credential_source=source,
        )
