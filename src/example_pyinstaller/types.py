from collections.abc import Callable, Sequence
from dataclasses import dataclass
from enum import Enum


class TestStatus(Enum):
    SUCCESS = "success"
    WARNING = "warning"
    FAILURE = "failure"


@dataclass
class TestResult:
    status: TestStatus
    message: str


@dataclass
class RuntimeTest:
    name: str
    description: str
    run_test: Callable[[], Sequence[TestResult]]
