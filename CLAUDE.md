# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI-powered CAD system that enables conversational 3D modeling using CAD-Query. The core innovation is a visual feedback loop where AI can generate parametric CAD code, render multiple viewing angles, inspect the visual output, and iterate on designs based on visual analysis.

## Architecture

The system integrates MCP (Model Context Protocol) for automated CAD verification and includes visualization scripts that wrap CAD-Query's `cq-cli` tool:

- **`mcp/server.py`** - MCP server providing the `cad_verify` tool for automated model validation
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

### CAD Generation Workflow

1. **Generate**: Write parametric CAD-Query Python scripts
2. **Execute**: Use visualization scripts to render multiple viewing angles (if needed)
3. **Inspect**: Read generated SVG files to analyze design accuracy (if needed)
4. **Iterate**: Modify CAD code based on visual feedback
5. **Export**: Generate final STL/STEP files for manufacturing

## Essential Commands

### Environment Setup
```bash
uv sync  # Install all dependencies including CAD-Query and cq-cli
uv sync --extra docs  # Install additional documentation generation dependencies
```

### MCP Server Setup
```bash
# See mcp/CLAUDE.md for complete setup instructions
cd mcp && pip install -r requirements.txt
```

### Model Operations
```bash
# Export STL for 3D printing
uv run cq-cli --codec stl --infile examples/box.py --outfile outputs/model.stl

# Export STEP for CAD software
uv run cq-cli --codec step --infile examples/box.py --outfile outputs/model.step

# Generate 4 standard orthographic views (optional)
uv run python src/ai_3d_print/render_views.py examples/box.py

# Generate custom angle view (optional)
uv run python src/ai_3d_print/view_direction.py examples/box.py 0.7 0.7 0.2
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

### CAD-Query Documentation Generation

To improve Claude's understanding of CAD-Query syntax, this project includes tools to generate comprehensive reference documentation from the official CAD-Query documentation.

```bash
# Generate CAD-Query reference documentation (run when needed)
cd docs-generation && uv run sphinx-build -M markdown . _build
```

The generated markdown files provide Claude with:
- **Complete API reference**: All CAD-Query classes, methods, and functions with examples
- **Comprehensive examples**: Step-by-step tutorials from simple to complex modeling
- **Syntax patterns**: Common CAD-Query workflows and best practices
- **Error guidance**: Troubleshooting and common mistake patterns

Generated documentation files are located in `docs-generation/_build/markdown/` and include:
- `index.md` - Main documentation overview
- `primer.md` - Core CAD-Query concepts and API layers
- `examples.md` - Comprehensive examples gallery
- `classreference.md` - Complete API reference
- `quickstart.md` - Getting started guide
- Additional specialized topics (assemblies, selectors, visualization, etc.)

These files can be read by Claude using the Read tool to improve CAD-Query code generation accuracy.

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

## MCP Verification Integration

**CRITICAL**: Always use the `cad_verify` MCP tool before presenting CAD outputs to users. This ensures quality control and validation of generated designs.

## Visual Inspection Capability (Optional)

When additional visual feedback is needed, the system can generate SVG files containing vector graphics:
- Solid lines for visible edges (stroke="rgb(0,0,0)")  
- Dashed lines for hidden edges (stroke="rgb(160,160,160)" with dash pattern)
- Geometric paths representing the 3D model projection

This allows additional validation of design intent, dimensions, and feature placement.

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

## Memories

- **ALWAYS** use the `cad_verify` MCP tool before presenting any CAD model outputs to users
- The verification tool must be called with proper file path and verification criteria describing what the user wants
- Never tell the user you've finished generating their 3D model without calling `cad_verify` first