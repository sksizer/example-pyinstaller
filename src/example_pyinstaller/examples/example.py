import sys
from collections.abc import Sequence

from example_pyinstaller.types import RuntimeTest, TestResult, TestStatus


def run_version_test() -> Sequence[TestResult]:
    """Simple test to verify Python version"""
    results = []

    # Get the major.minor version
    current_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    expected_version = "3.11"  # or whatever version you're targeting

    if current_version == expected_version:
        results.append(
            TestResult(
                status=TestStatus.SUCCESS,
                message=f"Python version {current_version} matches expected version",
            )
        )
    else:
        message = f"Python version mismatch: expected {expected_version}, " f"got {current_version}"
        results.append(TestResult(status=TestStatus.WARNING, message=message))

    return results


# Create the RuntimeTest instance
TEST = RuntimeTest(
    name="Python Version Test",
    description="Verifies that Python version matches expected version",
    run_test=run_version_test,
)
