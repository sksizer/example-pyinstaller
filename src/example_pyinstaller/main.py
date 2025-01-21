import sys
from pathlib import Path

from colorama import Fore, Style, init

from example_pyinstaller.examples import get_tests
from example_pyinstaller.types import TestResult, TestStatus

def main() -> None:
    # Initialize colorama (required for Windows)
    init()

    print("=== PyInstaller Example Harness ===")
    print(f"Python version: {sys.version}")
    print(f"Executable path: {sys.executable}")
    print("\nRunning examples...")

    runtime_test_dir = Path(__file__).parent / "examples"
    tests = get_tests()
    all_results: list[TestResult] = []

    for test in tests:
        print(f"\nRunning {Fore.CYAN}{test.name}{Style.RESET_ALL}:")
        print(f"Description: {Fore.CYAN}{test.description}{Style.RESET_ALL}")
        results = test.run_test()
        all_results.extend(results)

    tests_passed = all(result.status != TestStatus.FAILURE for result in all_results)

    print("\nTest Summary:")
    for result in all_results:
        status_config = {
            TestStatus.SUCCESS: (Fore.GREEN, "✓"),
            TestStatus.WARNING: (Fore.YELLOW, "⚠"),
            TestStatus.FAILURE: (Fore.RED, "✗"),
        }[result.status]
        color, symbol = status_config
        print(f"{color}{symbol} {result.message}{Style.RESET_ALL}")

    result_color = Fore.GREEN if tests_passed else Fore.RED
    result_message = "All tests passed!" if tests_passed else "Some tests failed."
    print(f"\n{result_color}{result_message}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
