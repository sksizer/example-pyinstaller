from example_pyinstaller.examples import example
from example_pyinstaller.types import RuntimeTest

import example_pyinstaller.examples.example as example
import example_pyinstaller.examples.tmpdir_io as tmpdir_io
import example_pyinstaller.examples.userdir_io as userdir_io

# Explicit list of example/test modules
REGISTRY = [
    example.TEST,
    tmpdir_io.TEST,
    userdir_io.TEST
]


def get_tests() -> list[RuntimeTest]:
    """Get all runtime tests

    Returns:
        List of RuntimeTest instances
    """
    return REGISTRY