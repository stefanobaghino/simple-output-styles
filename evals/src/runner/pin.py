"""The pinned Claude CLI version.

A leaf module without imports on purpose: the hermetic layer and
the provenance layer both need the pin, and the provenance imports
the hermetic module, so the pin cannot live in either.
"""

CLI_VERSION_PIN = "2.1.226 (Claude Code)"
"""The Claude CLI version that every live invocation must run under.

The CLI auto-updates, so the installed version drifts silently; the
pin turns the drift into a stop before the first billed call. A pin
move is a deliberate PR, and it opens a comparability era: the
comparison warns when two runs store different versions.
"""

# The managed store and the installer store key on the bare number;
# the version check always compares the whole string.
CLI_VERSION_BARE = CLI_VERSION_PIN.split()[0]
