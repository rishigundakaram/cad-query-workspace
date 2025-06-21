# Documentation

This directory contains comprehensive documentation for the AI 3D Print system.

## CAD-Query Reference (`cadquery/`)

Complete CAD-Query documentation converted to searchable markdown format. Key files:

- **`index.md`** - Main CAD-Query documentation overview
- **`primer.md`** - Core CAD-Query concepts and API layers  
- **`examples.md`** - Comprehensive examples gallery
- **`classreference.md`** - Complete API reference with all classes and methods
- **`quickstart.md`** - Getting started guide
- **`workplane.md`** - Workplane operations and methods
- **`selectors.md`** - Object selection and filtering
- **`sketch.md`** - 2D sketching operations
- **`assy.md`** - Assembly modeling
- **`importexport.md`** - File import/export formats

## Searching the Documentation

Use your editor's search functionality or `grep` to find specific CAD-Query methods, classes, or concepts across all markdown files:

```bash
# Search for specific method
grep -r "box(" docs/cadquery/

# Search for class definitions  
grep -r "class.*Workplane" docs/cadquery/

# Search for examples
grep -r "Example:" docs/cadquery/
```

## Additional Documentation

- **Project setup and usage**: See main `README.md`
- **Development guidelines**: See `CLAUDE.md`
- **MCP server setup**: See `mcp/README.md`
- **MCP integration guide**: See `mcp/INTEGRATION_GUIDE.md`