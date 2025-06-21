# AI 3D Print - Claude Code Workspace

A Claude Code workspace for conversational 3D modeling using CAD-Query via MCP (Model Context Protocol). This workspace provides documentation, examples, and structure for Claude to generate parametric CAD models that can be exported as STL files for 3D printing.

## Features

- **CAD-Query Documentation**: Complete searchable reference documentation for Claude to use
- **Example Models**: Sample CAD-Query scripts demonstrating various modeling techniques
- **MCP Integration**: Uses CAD-Query MCP server for model generation and verification
- **Output Management**: Organized structure for generated STL and visualization files

## Prerequisites

This workspace requires a CAD-Query MCP server to be running. The MCP server handles:
- CAD-Query code generation (`generate_cad_query` tool)
- Model verification (`verify_cad_query` tool)  
- STL/STEP file exports
- Visualization generation

## Workspace Structure

```
├── docs/cadquery/          # CAD-Query reference documentation (for Claude)
├── examples/               # Sample CAD-Query scripts
├── outputs/                # Generated STL files and visualizations
└── CLAUDE.md              # Instructions for Claude Code
```

## Usage for Claude Code

1. **Reference Documentation**: Use `docs/cadquery/` to understand CAD-Query syntax and methods
2. **Study Examples**: Review `examples/` for CAD modeling patterns and techniques  
3. **Use MCP Tools**: Call MCP server tools to generate and verify CAD models
4. **Output Files**: Generated STL files will be saved to `outputs/` directory

### Example Workflow

```
1. Claude references docs/cadquery/classreference.md for Workplane methods
2. Claude studies examples/box.py for basic modeling patterns
3. Claude uses generate_cad_query MCP tool to create new CAD script
4. Claude uses verify_cad_query MCP tool to validate the generated model
5. MCP server exports STL file to outputs/ directory
```

### Example Models

The `examples/` directory contains sample CAD-Query scripts:
- `box.py` - Simple box with hole
- `coffee_mug.py` - Coffee mug with handle  
- `donut.py` - Torus shape
- `snowman.py` - Multi-sphere assembly

### CAD-Query Script Requirements

All CAD-Query scripts must end with `show_object(result)` for compatibility:

```python
import cadquery as cq
result = cq.Workplane("XY").box(10, 10, 10)
show_object(result)  # Required for processing
```

## Documentation

- **Claude Instructions**: See `CLAUDE.md` for detailed usage guidelines
- **CAD-Query Reference**: Browse `docs/cadquery/` for comprehensive API documentation
- **Documentation Guide**: See `docs/README.md` for navigation help

## Development

This workspace includes basic development tools:

```bash
# Run tests
uv run pytest

# Code quality checks  
./run_lint.sh
```