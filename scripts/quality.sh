#!/bin/bash
set -e  # Exit on any error

# Parse arguments
FIX_MODE=false
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -f|--fix) FIX_MODE=true ;;
        *) echo "Unknown parameter: $1"; exit 1 ;;
    esac
    shift
done

echo "🧹 Running code quality checks..."

if [ "$FIX_MODE" = true ]; then
    echo "Running in FIX mode..."
    
    echo -e "\n📝 Running black (formatting)..."
    poetry run black .
    
    echo -e "\n🔍 Running ruff --fix (linting)..."
    poetry run ruff check . --fix
    
    echo -e "\n✨ All fixes applied!"
else
    echo "Running in CHECK mode..."
    
    echo -e "\n📝 Running black (formatting)..."
    poetry run black . --check
    
    echo -e "\n🔍 Running ruff (linting)..."
    poetry run ruff check .
    
    echo -e "\n🏷️ Running mypy (type checking)..."
    poetry run mypy src tests
    
    echo -e "\n🧪 Running pytest (tests)..."
    poetry run pytest
    
    echo -e "\n✨ All quality checks passed!"
fi 