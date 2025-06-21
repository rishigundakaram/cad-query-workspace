#!/bin/bash
set -e

echo "🔍 Running all CI/CD checks locally..."
echo

# Code formatting with Ruff (fixes issues automatically)
echo "🎨 Formatting code with Ruff..."
uv run ruff format examples/
echo "✅ Code formatting applied"
echo

# Linting with Ruff
echo "📝 Running Ruff linter..."
uv run ruff check examples/
echo "✅ Ruff linting passed"
echo

echo "🎉 All CI/CD checks passed! Ready to push and create PR."
