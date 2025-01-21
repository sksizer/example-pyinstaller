#!/bin/bash
set -e  # Exit on any error

echo "🧹 Cleaning Python artifacts..."

# Remove Python file artifacts
find . -type f -name "*.py[co]" -delete
find . -type d -name "__pycache__" -exec rm -r {} +

# Remove test artifacts
find . -type d -name ".pytest_cache" -exec rm -r {} +
find . -type d -name ".mypy_cache" -exec rm -r {} +
find . -type d -name ".ruff_cache" -exec rm -r {} +

# Remove build artifacts
rm -rf build/
rm -rf dist/
rm -rf .eggs/
find . -type d -name "*.egg-info" -exec rm -r {} +

# Remove coverage artifacts
rm -f .coverage
rm -rf htmlcov/

# Remove PyInstaller artifacts
rm -rf *.spec

echo "✨ Clean complete!" 