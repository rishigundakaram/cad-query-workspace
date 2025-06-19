# CAD Verification MCP Server

This MCP (Model Context Protocol) server provides CAD verification capabilities for Claude, enabling automated validation of CAD-Query generated models.

## Overview

The server exposes a `cad_verify` tool that Claude can use to validate 3D models before presenting results to users. This ensures quality control and verification of generated CAD designs.

## Installation

1. Install dependencies:
```bash
cd mcp
pip install -r requirements.txt
```

2. Test the server:
```bash
mcp dev server.py
```

## Claude Desktop Configuration

Add this to your Claude Desktop configuration file:

### macOS
Location: `~/Library/Application Support/Claude/claude_desktop_config.json`

### Windows
Location: `%APPDATA%/Claude/claude_desktop_config.json`

### Configuration
```json
{
  "mcpServers": {
    "cad-verification": {
      "command": "python",
      "args": ["/path/to/your/project/mcp/server.py"],
      "env": {}
    }
  }
}
```

Replace `/path/to/your/project` with the actual path to this project.

## Tool Usage

The server provides one tool:

### `cad_verify`

Verifies a CAD-Query model against specified criteria.

**Parameters:**
- `file_path` (string): Path to the CAD-Query Python file
- `verification_criteria` (string): Description of what to verify

**Example:**
```
file_path: "examples/coffee_mug.py"
verification_criteria: "coffee mug with handle, 10cm height, 8cm diameter"
```

**Returns:**
```json
{
  "status": "PASS" | "FAIL",
  "message": "Description of result",
  "file_path": "Path to verified file",
  "criteria": "Verification criteria used",
  "details": "Additional verification details"
}
```

## Development

To modify the verification logic, edit the `cad_verify` function in `server.py`. The current implementation is a dummy that always returns "PASS" - you can enhance it to:

- Parse CAD-Query code
- Execute model generation
- Analyze resulting geometry
- Check dimensions and features
- Validate against specific criteria

## Testing

Use the MCP Inspector to test the server:

```bash
# Install MCP Inspector (if not already installed)
pip install mcp

# Test the server
mcp dev server.py
```

This will open an interactive interface to test the `cad_verify` tool.