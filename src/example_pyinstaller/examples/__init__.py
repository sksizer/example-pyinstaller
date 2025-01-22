import example_pyinstaller.examples.example as example
import example_pyinstaller.examples.sqlite_io as sqlite_io
import example_pyinstaller.examples.tmpdir_io as tmpdir_io
import example_pyinstaller.examples.userdir_io as userdir_io
import example_pyinstaller.examples.asset_io as asset_io
from example_pyinstaller.model import RuntimeTest

# Explicit list of example/test modules
REGISTRY = [
    example.TEST,
    tmpdir_io.TEST,
    userdir_io.TEST,
    sqlite_io.TEST,
    asset_io.TEST,
]


def get_tests() -> list[RuntimeTest]:
    """Get all runtime tests

    Returns:
        List of RuntimeTest instances
    """
    return REGISTRY
