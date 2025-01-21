from example_pyinstaller.examples import (
    example,
    tmpdir_io,
)
from example_pyinstaller.types import RuntimeTest


# Explicit list of example/test modules
REGISTRY = [
    example,
    tmpdir_io,
]


def get_tests() -> list[RuntimeTest]:
    """Get all runtime tests

    Returns:
        List of RuntimeTest instances
    """
    return [
        module.TEST for module in REGISTRY if hasattr(module, "TEST")
    ]
