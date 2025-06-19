# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI-powered CAD system that enables conversational 3D modeling using CAD-Query. The core innovation is a visual feedback loop where AI can generate parametric CAD code, render multiple viewing angles, inspect the visual output, and iterate on designs based on visual analysis.

## Architecture

The system consists of two primary visualization scripts that wrap CAD-Query's `cq-cli` tool:

- **`src/ai_3d_print/render_views.py`** - Generates 4 standard orthographic views (top, front, right, isometric) for comprehensive model inspection
- **`src/ai_3d_print/view_direction.py`** - Creates custom angle views with arbitrary direction vectors for detailed analysis

### CAD-Query Script Requirements

All CAD-Query scripts must end with `show_object(result)` to work with `cq-cli`. The CQGI (CadQuery Gateway Interface) system requires this function call to export shapes for processing.

Example structure:
```python
import cadquery as cq
result = cq.Workplane("XY").box(10, 10, 10)
show_object(result)  # Required for cq-cli
```

### Visual Feedback Workflow

1. **Generate**: Write parametric CAD-Query Python scripts
2. **Execute**: Use visualization scripts to render multiple viewing angles
3. **Inspect**: Read generated SVG files to analyze design accuracy
4. **Iterate**: Modify CAD code based on visual feedback
5. **Export**: Generate final STL/STEP files for manufacturing

## Essential Commands

### Environment Setup
```bash
uv sync  # Install all dependencies including CAD-Query and cq-cli
```

### Model Visualization
```bash
# Generate 4 standard orthographic views
uv run python src/ai_3d_print/render_views.py examples/box.py

# Generate custom angle view (x, y, z direction vector)
uv run python src/ai_3d_print/view_direction.py examples/box.py 0.7 0.7 0.2

# Export STL for 3D printing
uv run cq-cli --codec stl --infile examples/box.py --outfile outputs/model.stl

# Export STEP for CAD software
uv run cq-cli --codec step --infile examples/box.py --outfile outputs/model.step
```

### Development Commands
```bash
# Run tests
uv run pytest

# Run single test
uv run pytest tests/test_main.py::test_specific_function

# Lint code
uv run ruff check

# Format code
uv run ruff format

# Type checking
uv run mypy src/
```

## Key Dependencies

- **CAD-Query ≥2.4.0**: Parametric 3D CAD modeling library
- **cq-cli**: Command-line interface for executing CAD-Query scripts (installed from GitHub)
- **hatchling**: Build backend with direct reference support enabled

The `cq-cli` dependency is installed from GitHub and requires `allow-direct-references = true` in the hatchling configuration.

## Output Structure

All generated files are placed in the `outputs/` directory:
- `{model_name}_top.svg` - Top view (0,0,1)
- `{model_name}_front.svg` - Front view (0,1,0)
- `{model_name}_right.svg` - Right view (1,0,0)
- `{model_name}_iso.svg` - Isometric view (1,1,1)
- `{model_name}_custom.svg` - Custom direction view
- `{model_name}.stl` - STL export for 3D printing
- `{model_name}.step` - STEP export for CAD software

## Visual Inspection Capability

The system enables AI to perform visual feedback by reading generated SVG files. SVG files contain vector graphics showing:
- Solid lines for visible edges (stroke="rgb(0,0,0)")
- Dashed lines for hidden edges (stroke="rgb(160,160,160)" with dash pattern)
- Geometric paths representing the 3D model projection

This allows AI to validate design intent, check dimensions, verify feature placement, and identify issues before iteration.

## Development Workflow

### Always Use Feature Branches
```bash
# Create feature branch for all changes
git checkout -b feature/descriptive-name

# Make changes, then commit
git add .
git commit -m "Your descriptive commit message"

# Push branch and create PR
git push -u origin feature/descriptive-name
gh pr create --title "Your PR Title" --body "PR description"
```

### Pre-commit Validation
```bash
# Option 1: Run all CI/CD checks manually
./run_lint.sh

# Option 2: Install automated pre-commit hooks (recommended)
uv run pre-commit install
uv run pre-commit run --all-files  # Test all hooks
```

Pre-commit hooks automatically run `./run_lint.sh` on every commit, ensuring code quality and preventing CI failures.

The `./run_lint.sh` script runs all checks with the proper sequence: format → lint → type check → test. Both manual execution and pre-commit will fail if any check doesn't pass.

Note: CAD-Query example scripts use `show_object()` which is provided by the CQGI execution environment.
