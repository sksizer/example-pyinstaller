from collections.abc import Sequence
from pathlib import Path

from example_pyinstaller.model import RuntimeTest, TestResult, TestStatus
from example_pyinstaller.util import get_resource_path


def run_asset_test() -> Sequence[TestResult]:
    """Test access to bundled assets"""
    results = []
    image_path = "assets/images/pyinstaller-draft1a-100_trans.webp"

    try:
        resource_path = Path(get_resource_path(image_path))

        if resource_path.exists():
            results.append(
                TestResult(
                    status=TestStatus.SUCCESS,
                    message=f"Found asset at: {resource_path}"
                )
            )
            
            if resource_path.is_file() and resource_path.stat().st_size > 0:
                results.append(
                    TestResult(
                        status=TestStatus.SUCCESS,
                        message=f"Asset verified: {resource_path.stat().st_size} bytes"
                    )
                )
            else:
                results.append(
                    TestResult(
                        status=TestStatus.FAILURE,
                        message="Asset exists but appears to be invalid"
                    )
                )
        else:
            results.append(
                TestResult(
                    status=TestStatus.FAILURE,
                    message=f"Asset not found at: {resource_path}"
                )
            )

    except Exception as e:
        results.append(
            TestResult(
                status=TestStatus.FAILURE,
                message=f"Asset check failed: {str(e)}"
            )
        )

    return results


TEST = RuntimeTest(
    name="Asset Access Test",
    description="Tests access to bundled assets (images) in PyInstaller executable",
    run_test=run_asset_test,
) 