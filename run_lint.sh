#!/bin/bash
set -e

echo "🔍 Running all CI/CD checks locally..."
echo

# Code formatting with Ruff (fixes issues automatically)
echo "🎨 Formatting code with Ruff..."
uv run ruff format src/ tests/
echo "✅ Code formatting applied"
echo

# Linting with Ruff
echo "📝 Running Ruff linter..."
uv run ruff check src/ tests/
echo "✅ Ruff linting passed"
echo

# Type checking with MyPy
echo "🔍 Running MyPy type checking..."
uv run mypy src/
echo "✅ Type checking passed"
echo

# Running tests (without coverage requirement)
echo "🧪 Running tests..."
uv run pytest
echo "✅ All tests passed"
echo

echo "🎉 All CI/CD checks passed! Ready to push and create PR."
