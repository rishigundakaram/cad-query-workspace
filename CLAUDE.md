# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this CAD workspace.

## Project Overview

This is a Claude Code workspace for conversational 3D modeling using CAD-Query via MCP (Model Context Protocol). The workspace provides documentation, examples, and structure for generating parametric CAD models that can be exported as STL files for 3D printing.

## Architecture

This workspace uses an external CAD-Query MCP server that provides:

- **`generate_cad_query`** - Tool for generating CAD-Query Python scripts from descriptions *(currently stub implementation)*
- **`verify_cad_query`** - Tool for validating generated CAD models before presentation

### Local Resources

- **`docs/cadquery/`** - Complete CAD-Query reference documentation for Claude to study
- **`examples/`** - Sample CAD-Query scripts demonstrating modeling techniques
- **`outputs/`** - Directory where generated STL files and visualizations are saved

### CAD Generation Workflow

1. **Study Documentation**: Reference `docs/cadquery/` to understand CAD-Query syntax and methods
2. **Review Examples**: Study `examples/` for modeling patterns and best practices
3. **Generate CAD Code**: Use the `generate_cad_query` MCP tool to create Python scripts
4. **Verify Models**: Use the `verify_cad_query` MCP tool to validate designs
5. **Output Files**: MCP server exports STL files to `outputs/` directory

### CAD-Query Script Requirements

All CAD-Query scripts must end with `show_object(result)` for MCP server processing:

```python
import cadquery as cq
result = cq.Workplane("XY").box(10, 10, 10)
show_object(result)  # Required for MCP server
```

## MCP Tools Available

This workspace uses a CAD-Query MCP server that provides these tools:

### `generate_cad_query`
Generates CAD-Query Python scripts from natural language descriptions.

**Parameters:**
- `description`: Natural language description of the desired 3D model
- `parameters`: Optional specific dimensions or constraints

**Usage Example:**
```python
# Claude calls this MCP tool
generate_cad_query(
    description="Create a coffee mug with a handle, 10cm tall and 8cm diameter",
    parameters="height=100mm, diameter=80mm, handle_width=15mm"
)
```

### `verify_cad_query`
Validates generated CAD models before presenting to users.

**Parameters:**
- `file_path`: Path to the CAD-Query Python file to verify
- `verification_criteria`: Description of what aspects to verify

**Usage Example:**
```python
# Claude calls this MCP tool
verify_cad_query(
    file_path="outputs/coffee_mug.py",
    verification_criteria="coffee mug with handle, 10cm height, 8cm diameter"
)
```

## Documentation Resources

### CAD-Query Reference (`docs/cadquery/`)

Complete CAD-Query documentation converted to searchable markdown format:

- **`classreference.md`** - Complete API reference with all classes and methods
- **`examples.md`** - Comprehensive examples gallery  
- **`primer.md`** - Core CAD-Query concepts and API layers
- **`workplane.md`** - Workplane operations and methods
- **`selectors.md`** - Object selection and filtering
- **`sketch.md`** - 2D sketching operations

### Example Models (`examples/`)

Study these sample CAD-Query scripts:
- **`box.py`** - Simple box with hole (basic operations)
- **`coffee_mug.py`** - Coffee mug with handle (revolve, union operations)
- **`donut.py`** - Torus shape (revolve operations)
- **`snowman.py`** - Multi-sphere assembly (assembly modeling)

## Essential Development Commands

```bash
# Install workspace dependencies
uv sync

# Run tests
uv run pytest

# Code quality checks
./run_lint.sh
```

## Output Structure

The MCP server generates files in the `outputs/` directory:
- `{model_name}.py` - Generated CAD-Query Python script
- `{model_name}.stl` - STL export for 3D printing
- `{model_name}.step` - STEP export for CAD software
- `{model_name}_*.svg` - Visualization files (optional)

## Workflow Best Practices

### Step 1: Study Documentation
```python
# Before generating any CAD model, study the relevant documentation
# Read docs/cadquery/classreference.md for API methods
# Read docs/cadquery/examples.md for modeling patterns
# Study examples/ directory for similar models
```

### Step 2: Generate CAD Code
```python
# NOTE: generate_cad_query is currently a stub implementation
# For now, manually create CAD-Query scripts based on documentation and examples
# Use the generate_cad_query MCP tool with clear descriptions
generate_cad_query(
    description="Clear, detailed description of the 3D model",
    parameters="Specific dimensions and constraints"
)
```

### Step 3: Always Verify
```python
# CRITICAL: Always verify before presenting results to users
verify_cad_query(
    file_path="path/to/generated/model.py", 
    verification_criteria="Description of what to verify"
)
```

### Step 4: Present Results
Only after verification passes, present the generated STL file and model description to the user.

## Development Workflow

### Feature Branch Development
```bash
# Create feature branch for workspace changes
git checkout -b feature/workspace-improvements

# Make changes and commit
git add . && git commit -m "Improve workspace documentation"

# Create PR
gh pr create --title "Workspace improvements"
```

## Critical Guidelines

### MCP Tool Usage
- **ALWAYS** use `verify_cad_query` before presenting any CAD outputs to users
- **NEVER** skip verification - it ensures quality and correctness
- Use clear, detailed descriptions in MCP tool calls
- Reference documentation and examples before generating complex models

### Documentation Usage
- Study `docs/cadquery/` extensively for CAD-Query syntax
- Review `examples/` for modeling patterns and best practices
- Use the Read tool to search documentation for specific methods or techniques