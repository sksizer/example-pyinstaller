import tempfile
from collections.abc import Sequence
from pathlib import Path

from example_pyinstaller.model import RuntimeTest, TestResult, TestStatus


def tmp_dir_io() -> Sequence[TestResult]:
    """Test tmpdir access and I/O"""
    results = []
    tmp_path = None

    try:
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp_file:
            test_content = "Hello, PyInstaller!"
            tmp_file.write(test_content)
            tmp_path = Path(tmp_file.name)
        results.append(
            TestResult(status=TestStatus.SUCCESS, message=f"File creation successful at {tmp_path}")
        )

        content = tmp_path.read_text()
        if content == test_content:
            results.append(
                TestResult(status=TestStatus.SUCCESS, message=f"File content verified: '{content}'")
            )
        else:
            results.append(
                TestResult(
                    status=TestStatus.FAILURE,
                    message=f"Content mismatch. Expected: '{test_content}', Got: '{content}'",
                )
            )

        tmp_path.unlink()
        if not tmp_path.exists():
            results.append(TestResult(status=TestStatus.SUCCESS, message="File cleanup successful"))
        else:
            results.append(TestResult(status=TestStatus.WARNING, message="File deletion failed"))

    except Exception as e:
        results.append(
            TestResult(status=TestStatus.FAILURE, message=f"File I/O operation failed: {str(e)}")
        )
        if tmp_path and tmp_path.exists():
            try:
                tmp_path.unlink()
            except Exception as e:
                results.append(
                    TestResult(
                        status=TestStatus.WARNING, message="Failed to clean up temporary file"
                    )
                )

    return results


# Create the RuntimeTest instance
TEST = RuntimeTest(
    name="Tmpdir I/O Test",
    description="Tests basic file operations (create, read, delete) in a temporary directory",
    run_test=tmp_dir_io,
)
