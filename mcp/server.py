#!/usr/bin/env python3
"""
MCP Server for CAD Verification

This server provides a verification tool for CAD-Query generated models.
It integrates with Claude to validate 3D models before presenting results to users.
"""

import logging
import subprocess
import sys
from pathlib import Path
from typing import Any

import openai
from mcp.server.fastmcp import FastMCP

# Configure detailed logging for debugging
log_file = Path(__file__).parent / 'mcp_server.log'
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stderr),
        logging.FileHandler(log_file, mode='a')
    ]
)
logger = logging.getLogger(__name__)

# Create FastMCP server
mcp = FastMCP("CAD Verification Server")


def generate_svg_views(script_path: Path) -> list[Path]:
    """Generate 4 standard orthographic views as SVG files."""
    base_name = script_path.stem
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    
    # Generate 4 standard orthographic views
    views = [
        ("top", "(0,0,1)"),
        ("front", "(0,1,0)"),
        ("right", "(1,0,0)"),
        ("iso", "(1,1,1)"),
    ]
    
    svg_files = []
    
    for view, direction in views:
        output_file = output_dir / f"{base_name}_{view}.svg"
        cmd = [
            "cq-cli",
            "--codec",
            "svg",
            "--infile",
            str(script_path),
            "--outfile",
            str(output_file),
            "--outputopts",
            f"projectionDir:{direction};width:800;height:800",
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            logger.debug(f"Generated {view} view: {output_file}")
            svg_files.append(output_file)
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to generate {view} view: {e.stderr}")
            raise Exception(f"Failed to generate {view} view: {e.stderr}")
    
    return svg_files


def analyze_with_o3_mini(svg_files: list[Path], criteria: str) -> dict[str, str]:
    """Analyze SVG files with o3-mini to determine if CAD model meets criteria."""
    
    # Read all SVG files
    svg_contents = {}
    for svg_file in svg_files:
        try:
            with open(svg_file, 'r') as f:
                svg_contents[svg_file.stem] = f.read()
        except Exception as e:
            logger.warning(f"Could not read {svg_file}: {e}")
    
    if not svg_contents:
        raise Exception("No SVG files could be read for analysis")
    
    # Prepare prompt for o3-mini
    prompt = f"""You are analyzing CAD model visualizations to verify if they meet specific criteria.

Criteria to verify: {criteria}

I have provided 4 orthographic views of a 3D CAD model as SVG files:
- Top view (looking down from above)
- Front view (looking from the front)
- Right view (looking from the right side)  
- Isometric view (3D perspective view)

Please analyze these views and determine:
1. Does this CAD model meet the specified criteria? (PASS/FAIL)
2. Provide detailed reasoning for your decision
3. If it fails, explain specifically what is wrong or missing
4. If it passes, explain what features correctly match the criteria

Be thorough in your analysis, examining dimensions, features, geometry, and overall design.

SVG Contents:
"""
    
    for view_name, svg_content in svg_contents.items():
        prompt += f"\n--- {view_name.upper()} VIEW ---\n{svg_content}\n"
    
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="o1-mini",
            messages=[{
                "role": "user", 
                "content": prompt
            }],
            max_completion_tokens=2000
        )
        
        analysis_text = response.choices[0].message.content
        
        # Determine status from analysis
        status = "PASS" if "PASS" in analysis_text.upper() else "FAIL"
        
        return {
            "status": status,
            "analysis": analysis_text
        }
        
    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        raise Exception(f"Failed to analyze with o3-mini: {e}")


@mcp.tool()
def cad_verify(file_path: str, verification_criteria: str) -> dict[str, Any]:
    """
    Verify a CAD-Query generated model against specified criteria.
    
    This tool should be called before presenting any CAD model outputs to users
    to ensure the generated model meets the specified requirements.
    
    Args:
        file_path: Path to the CAD-Query Python file to verify
        verification_criteria: Description of what aspects to verify 
                              (e.g., "coffee mug with handle, 10cm height, 8cm diameter")
    
    Returns:
        Dict containing verification status and details
    """
    logger.info(f"🔍 MCP Tool Called: cad_verify")
    logger.info(f"📁 File path: {file_path}")
    logger.info(f"📋 Verification criteria: {verification_criteria}")
    
    # Check if file exists
    path = Path(file_path)
    if not path.exists():
        logger.error(f"❌ File not found: {file_path}")
        return {
            "status": "FAIL",
            "message": f"File not found: {file_path}",
            "criteria": verification_criteria
        }
    
    if not path.suffix == ".py":
        logger.error(f"❌ Invalid file type: {path.suffix}")
        return {
            "status": "FAIL", 
            "message": f"File must be a Python file, got: {path.suffix}",
            "criteria": verification_criteria
        }
    
    # Read file content for logging
    try:
        content = path.read_text()
        logger.debug(f"📄 File content preview: {content[:200]}...")
    except Exception as e:
        logger.warning(f"⚠️  Could not read file content: {e}")
    
    # Generate SVG views for visual inspection
    try:
        svg_files = generate_svg_views(path)
        logger.info(f"📸 Generated {len(svg_files)} SVG views")
    except Exception as e:
        logger.error(f"❌ Failed to generate SVG views: {e}")
        return {
            "status": "FAIL",
            "file_path": file_path,
            "criteria": verification_criteria,
            "analysis": f"Could not generate visual representations of the CAD model: {e}"
        }
    
    # Analyze with o3-mini
    try:
        analysis_result = analyze_with_o3_mini(svg_files, verification_criteria)
        logger.info(f"🧠 O3-mini analysis completed")
        
        result = {
            "status": analysis_result["status"],
            "file_path": file_path,
            "criteria": verification_criteria,
            "analysis": analysis_result["analysis"]
        }
        
        logger.info(f"✅ Verification result: {result['status']}")
        return result
        
    except Exception as e:
        logger.error(f"❌ Failed to analyze with o3-mini: {e}")
        return {
            "status": "FAIL",
            "file_path": file_path,
            "criteria": verification_criteria,
            "analysis": f"Visual analysis failed: {e}"
        }


if __name__ == "__main__":
    # Run the server
    mcp.run()