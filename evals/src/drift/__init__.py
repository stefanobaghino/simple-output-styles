"""Drift measurement: does rule obedience decay as a session grows?

A scripted session runs per style, several times, and the linter
checks every turn. The report shows the violation-rate series over
turn positions and a verdict per style: flat or growing.
"""

from .analysis import (
    CONTEXT_WINDOW,
    DEPTH_TARGET,
    DriftResult,
    context_tokens,
    load_sessions,
    score_sessions,
)
from .estimate import estimate_deep_run, estimate_lines, project_script
from .report import build_drift_report, build_drift_summary
from .session import (
    SESSION_FLAGS,
    SessionTurn,
    build_session_argv,
    deep_script,
    generate_turn,
    load_session_script,
    run_session,
    session_script,
)

__all__ = [
    "CONTEXT_WINDOW",
    "DEPTH_TARGET",
    "SESSION_FLAGS",
    "DriftResult",
    "SessionTurn",
    "build_drift_report",
    "build_drift_summary",
    "build_session_argv",
    "context_tokens",
    "deep_script",
    "estimate_deep_run",
    "estimate_lines",
    "generate_turn",
    "load_session_script",
    "load_sessions",
    "project_script",
    "run_session",
    "score_sessions",
    "session_script",
]
