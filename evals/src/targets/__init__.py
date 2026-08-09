"""The regression-targets check.

The harness measures each style on several axes, but a measurement
without a target lets a style change regress silently. The targets
file pre-commits the numbers a style version must hold, and this
check compares one stored run against them.
"""

from .check import CheckResult, check_run
from .config import StyleTargets, TargetsConfig, load_targets_config

__all__ = ["CheckResult", "StyleTargets", "TargetsConfig", "check_run", "load_targets_config"]
