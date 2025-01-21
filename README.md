# Example PyInstaller

This is intended as an example model of how to use PyInstaller.

I wanted to use pyinstaller for an application I am building, and I find it is generally easier
to understand a new framework in a 'clean' environment. Then when the functionality and how
to use it is understood, at that point bring it over to an existing project.

There is a very simple pattern for adding some examples. 

It also is configured to build for Mac, Ubuntu and Windows with Github Workflows.

## Purpose

This repository demonstrates various PyInstaller packaging scenarios and provides a framework for testing them. It helps you:
- understand with a simple environtment various pyinstaller 
- see best practices for PyInstaller configuration

## Examples

Each example in `src/example_pyinstaller/examples/` demonstrates some python
application functionality used with pyinstaller.

## Usage

Run the example harness to see all examples in action:
```bash
# Using Poetry
poetry run example-pyinstaller

# Or after activating virtual environment
poetry shell
example-pyinstaller
```

### Adding New Examples

Create a new example module in `src/example_pyinstaller/examples/`:

```python
from example_pyinstaller.runtime_test_utils import TestResult, TestStatus, RuntimeTest

def run_my_example() -> Sequence[TestResult]:
    results = []
    # Add your example logic here
    return results

TEST = RuntimeTest(
    name="My PyInstaller Example",
    description="Description of what this example demonstrates",
    run_test=run_my_example
)
```

## Development

### Prerequisites
- Python 3.11+
- Poetry

### Setup Development Environment

```bash
# Install dependencies
poetry install
```

### Quality Checks

Run all quality checks:
```bash
./scripts/quality.sh
```

The project uses modern Python tooling:
- `black` for code formatting
- `ruff` for linting and import sorting
- `mypy` for type checking
- `pytest` for testing

## Project Structure

```
src/
  example_pyinstaller/
    examples/          # PyInstaller usage examples
    runtime_test_utils.py   # Test utilities
    main.py            # Example runner
tests/                 # pytest test suite
```

## License

MIT License - see LICENSE file for details

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run quality checks (`./scripts/quality.sh`)
5. Submit a pull request