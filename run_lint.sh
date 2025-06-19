#!/bin/bash
set -e

echo "🔍 Running all CI/CD checks locally..."
echo

# Linting with Ruff
echo "📝 Running Ruff linter..."
uv run ruff check src/ tests/
echo "✅ Ruff linting passed"
echo

# Code formatting check with Ruff
echo "🎨 Checking code formatting..."
uv run ruff format --check src/ tests/
echo "✅ Code formatting is correct"
echo

# Type checking with MyPy
echo "🔍 Running MyPy type checking..."
uv run mypy src/
echo "✅ Type checking passed"
echo

# Running tests with coverage
echo "🧪 Running tests with coverage..."
uv run pytest --cov=src --cov-report=term-missing --cov-fail-under=30
echo "✅ All tests passed with sufficient coverage"
echo

echo "🎉 All CI/CD checks passed! Ready to push and create PR."
