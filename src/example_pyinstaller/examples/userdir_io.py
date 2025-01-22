import shutil
from collections.abc import Sequence
from pathlib import Path

from example_pyinstaller.model import RuntimeTest, TestResult, TestStatus


def run_userdir_test() -> Sequence[TestResult]:
    """Test file operations in user's home directory"""
    results = []
    test_dir = Path.home() / ".example-pyinstaller"
    test_file = test_dir / "test.txt"

    try:
        # Test 1: Create directory in user's home
        test_dir.mkdir(exist_ok=True)
        if test_dir.exists() and test_dir.is_dir():
            results.append(
                TestResult(status=TestStatus.SUCCESS, message=f"Created directory at {test_dir}")
            )
        else:
            results.append(
                TestResult(
                    status=TestStatus.FAILURE, message=f"Failed to create directory at {test_dir}"
                )
            )
            return results  # Early return if we can't create directory

        # Test 2: Write file in the directory
        test_content = "Hello from PyInstaller!"
        test_file.write_text(test_content)
        if test_file.exists():
            results.append(
                TestResult(status=TestStatus.SUCCESS, message=f"Created file at {test_file}")
            )

        # Test 3: Read file content
        content = test_file.read_text()
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

        # Test 4: Clean up
        test_file.unlink()  # Remove file
        shutil.rmtree(test_dir)  # Remove directory and any remaining contents
        if not test_dir.exists():
            results.append(TestResult(status=TestStatus.SUCCESS, message="Cleanup successful"))
        else:
            results.append(
                TestResult(
                    status=TestStatus.WARNING, message="Cleanup incomplete - directory still exists"
                )
            )

    except Exception as e:
        results.append(
            TestResult(
                status=TestStatus.FAILURE, message=f"User directory operation failed: {str(e)}"
            )
        )
        # Attempt cleanup
        try:
            if test_file.exists():
                test_file.unlink()
            if test_dir.exists():
                shutil.rmtree(test_dir)
        except Exception as cleanup_error:
            results.append(
                TestResult(
                    status=TestStatus.WARNING,
                    message=f"Cleanup after error failed: {str(cleanup_error)}",
                )
            )

    return results


# Create the RuntimeTest instance
TEST = RuntimeTest(
    name="User Directory I/O Test",
    description="Tests file operations in user's home directory (~/.example-pyinstaller)",
    run_test=run_userdir_test,
)
