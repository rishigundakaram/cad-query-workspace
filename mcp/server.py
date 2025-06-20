#!/usr/bin/env python3
"""
MCP Server for CAD Verification

This server provides a verification tool for CAD-Query generated models.
It integrates with Claude to validate 3D models before presenting results to users.
"""

import base64
import io
import logging
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict

import cairosvg
import openai
from mcp.server.fastmcp import FastMCP
from PIL import Image
from pydantic import BaseModel
import pyvista as pv

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


def generate_stl_and_images(script_path: Path) -> Dict[str, Any]:
    """Generate STL file and colored images from CAD-Query script.
    
    Returns dict with 'stl_file' and 'image_files' keys.
    """
    base_name = script_path.stem
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    
    # First, generate STL file using cq-cli
    stl_file = output_dir / f"{base_name}.stl"
    cmd = [
        "uv", "run", "cq-cli",
        "--codec",
        "stl",
        "--infile",
        str(script_path),
        "--outfile",
        str(stl_file),
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        logger.debug(f"Generated STL file: {stl_file}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to generate STL: {e.stderr}")
        raise Exception(f"Failed to generate STL: {e.stderr}")
    
    # Now generate colored images using PyVista
    try:
        image_files = render_stl_to_images(stl_file, output_dir)
        logger.debug(f"Generated {len(image_files)} colored images")
        
        return {
            "stl_file": stl_file,
            "image_files": list(image_files.values())
        }
    except Exception as e:
        logger.error(f"Failed to render STL to images: {e}")
        raise Exception(f"Failed to render STL to images: {e}")


def render_stl_to_images(stl_path: Path, output_dir: Path) -> Dict[str, Path]:
    """Render STL file to colored images using PyVista.
    
    Returns dict mapping view names to image file paths.
    """
    # Load STL mesh
    try:
        mesh = pv.read(str(stl_path))
        logger.debug(f"Loaded STL: {mesh.n_points} points, {mesh.n_cells} cells")
    except Exception as e:
        raise Exception(f"Failed to load STL file: {e}")
    
    # Standard view directions
    views = {
        "front": {"position": (0, -10, 0), "viewup": (0, 0, 1)},
        "right": {"position": (10, 0, 0), "viewup": (0, 0, 1)},
        "top": {"position": (0, 0, 10), "viewup": (0, 1, 0)},
        "iso": {"position": (7, -7, 7), "viewup": (0, 0, 1)},
    }
    
    rendered_views = {}
    base_name = stl_path.stem
    
    for view_name, view_config in views.items():
        output_path = output_dir / f"{base_name}_{view_name}_colored.png"
        
        # Create off-screen plotter
        plotter = pv.Plotter(off_screen=True, window_size=[1000, 1000])
        
        # Add mesh with realistic material properties
        plotter.add_mesh(
            mesh,
            color="lightblue",
            lighting=True,
            smooth_shading=True,
            metallic=0.3,
            roughness=0.5,
            specular=0.8,
            ambient=0.2,
        )
        
        # Setup realistic lighting
        plotter.remove_all_lights()
        
        # Key light
        key_light = pv.Light(
            position=(10, 10, 10),
            focal_point=(0, 0, 0),
            color="white",
            intensity=0.8,
            light_type="scene light"
        )
        plotter.add_light(key_light)
        
        # Fill light
        fill_light = pv.Light(
            position=(-5, -5, 5),
            focal_point=(0, 0, 0),
            color="white",
            intensity=0.3,
            light_type="scene light"
        )
        plotter.add_light(fill_light)
        
        # Ambient light
        ambient_light = pv.Light(intensity=0.2, light_type="headlight")
        plotter.add_light(ambient_light)
        
        # Set camera position
        plotter.camera.position = view_config["position"]
        plotter.camera.focal_point = (0, 0, 0)
        plotter.camera.view_up = view_config["viewup"]
        plotter.reset_camera()
        
        # Set background
        plotter.set_background("white")
        
        # Render and save
        plotter.show(screenshot=str(output_path))
        plotter.close()
        
        rendered_views[view_name] = output_path
        logger.debug(f"Rendered {view_name} view to {output_path}")
    
    return rendered_views


def generate_svg_views(script_path: Path) -> list[Path]:
    """Legacy function - Generate 4 standard orthographic views as SVG files."""
    # Generate STL and images, then return just the image files for backward compatibility
    result = generate_stl_and_images(script_path)
    return result["image_files"]


class VerificationResult(BaseModel):
    """Structured output for CAD verification results."""
    status: str  # "PASS" or "FAIL"
    confidence: float  # 0.0 to 1.0
    analysis: str  # Detailed reasoning
    specific_issues: list[str]  # List of specific problems if FAIL
    matching_features: list[str]  # List of features that match criteria


def analyze_with_colored_images(image_files: list[Path], criteria: str) -> dict[str, str]:
    """Analyze colored PyVista images with GPT-4.1 vision to determine if CAD model meets criteria."""
    
    # Convert PNG images to base64 encoded images
    image_messages = []
    view_names = []
    
    for image_file in image_files:
        try:
            # Load PNG image directly
            with open(image_file, 'rb') as f:
                png_data = f.read()
            
            # Convert to base64
            base64_png = base64.b64encode(png_data).decode('utf-8')
            
            # Extract view name from filename (e.g., "coffee_mug_front_colored.png" -> "front")
            parts = image_file.stem.split('_')
            if len(parts) >= 3 and parts[-1] == "colored":
                view_name = parts[-2]  # Get second-to-last part
            else:
                view_name = "unknown"
            view_names.append(view_name)
            
            image_messages.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{base64_png}",
                    "detail": "high"
                }
            })
        except Exception as e:
            logger.warning(f"Could not load image {image_file}: {e}")
    
    if not image_messages:
        raise Exception("No image files could be loaded for analysis")
    
    # Enhanced prompt for colored 3D images
    text_content = f"""You are analyzing realistic 3D CAD model visualizations to verify if they meet specific criteria.

Criteria to verify: {criteria}

I have provided {len(image_messages)} high-quality rendered views of a 3D CAD model:
{', '.join([f'{name} view' for name in view_names])}

These are realistic colored 3D renderings with:
- Proper lighting and shading to show depth and form
- Smooth surfaces with realistic materials
- Clear visibility of all geometric features
- Professional 3D rendering quality

Please analyze these realistic 3D visualizations and determine:
1. Does this CAD model meet the specified criteria? (PASS/FAIL)
2. Provide detailed reasoning for your decision, taking advantage of the realistic 3D appearance
3. If it fails, list specifically what is wrong or missing
4. If it passes, list what features correctly match the criteria
5. Rate your confidence in this assessment (0.0 to 1.0)

Be thorough in your analysis, examining dimensions, features, geometry, surface quality, and overall design using the high-quality 3D rendering.

Respond with a structured analysis that clearly states PASS or FAIL and provides detailed reasoning."""
    
    # Build message with text and images
    message_content = [{"type": "text", "text": text_content}] + image_messages
    
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o",  # GPT-4.1 with vision
            messages=[{
                "role": "user", 
                "content": message_content
            }],
            max_tokens=2000,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "verification_result",
                    "schema": VerificationResult.model_json_schema()
                }
            }
        )
        
        # Parse structured response
        import json
        response_data = json.loads(response.choices[0].message.content)
        verification = VerificationResult(**response_data)
        
        return {
            "status": verification.status,
            "analysis": verification.analysis,
            "confidence": verification.confidence,
            "specific_issues": verification.specific_issues,
            "matching_features": verification.matching_features
        }
        
    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        raise Exception(f"Failed to analyze with GPT-4.1 vision: {e}")


def analyze_with_gpt4_vision(svg_files: list[Path], criteria: str) -> dict[str, str]:
    """Legacy function - analyze SVG files with GPT-4.1 vision."""
    # For backward compatibility, try to handle PNG files if passed
    if svg_files and str(svg_files[0]).endswith('.png'):
        return analyze_with_colored_images(svg_files, criteria)
    
    # Original SVG analysis code (kept for fallback)
    image_messages = []
    view_names = []
    
    for svg_file in svg_files:
        try:
            # Convert SVG to PNG using cairosvg
            png_data = cairosvg.svg2png(url=str(svg_file), output_width=800, output_height=800)
            
            # Convert to base64
            base64_png = base64.b64encode(png_data).decode('utf-8')
            
            # Extract view name from filename
            view_name = svg_file.stem.split('_')[-1]  # e.g., "coffee_mug_top" -> "top"
            view_names.append(view_name)
            
            image_messages.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{base64_png}",
                    "detail": "high"
                }
            })
        except Exception as e:
            logger.warning(f"Could not convert {svg_file} to PNG: {e}")
    
    if not image_messages:
        raise Exception("No SVG files could be converted to PNG for analysis")
    
    # Prepare prompt for GPT-4.1 vision
    text_content = f"""You are analyzing CAD model visualizations to verify if they meet specific criteria.

Criteria to verify: {criteria}

I have provided {len(image_messages)} orthographic views of a 3D CAD model as SVG images:
{', '.join([f'{name} view' for name in view_names])}

Please analyze these views and determine:
1. Does this CAD model meet the specified criteria? (PASS/FAIL)
2. Provide detailed reasoning for your decision  
3. If it fails, list specifically what is wrong or missing
4. If it passes, list what features correctly match the criteria
5. Rate your confidence in this assessment (0.0 to 1.0)

Be thorough in your analysis, examining dimensions, features, geometry, and overall design.

Respond with a structured analysis that clearly states PASS or FAIL and provides detailed reasoning."""
    
    # Build message with text and images
    message_content = [{"type": "text", "text": text_content}] + image_messages
    
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o",  # GPT-4.1 with vision
            messages=[{
                "role": "user", 
                "content": message_content
            }],
            max_tokens=2000,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "verification_result",
                    "schema": VerificationResult.model_json_schema()
                }
            }
        )
        
        # Parse structured response
        import json
        response_data = json.loads(response.choices[0].message.content)
        verification = VerificationResult(**response_data)
        
        return {
            "status": verification.status,
            "analysis": verification.analysis,
            "confidence": verification.confidence,
            "specific_issues": verification.specific_issues,
            "matching_features": verification.matching_features
        }
        
    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        raise Exception(f"Failed to analyze with GPT-4.1 vision: {e}")


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
    
    # Generate STL and colored images for visual inspection
    try:
        generation_result = generate_stl_and_images(path)
        image_files = generation_result["image_files"]
        stl_file = generation_result["stl_file"]
        logger.info(f"📸 Generated STL and {len(image_files)} colored images")
    except Exception as e:
        logger.error(f"❌ Failed to generate STL and images: {e}")
        return {
            "status": "FAIL",
            "file_path": file_path,
            "criteria": verification_criteria,
            "analysis": f"Could not generate visual representations of the CAD model: {e}"
        }
    
    # Analyze with GPT-4.1 vision using colored images
    try:
        analysis_result = analyze_with_colored_images(image_files, verification_criteria)
        logger.info(f"🧠 GPT-4.1 vision analysis completed with colored images")
        
        result = {
            "status": analysis_result["status"],
            "file_path": file_path,
            "criteria": verification_criteria,
            "analysis": analysis_result["analysis"]
        }
        
        logger.info(f"✅ Verification result: {result['status']}")
        return result
        
    except Exception as e:
        logger.error(f"❌ Failed to analyze with GPT-4.1 vision using colored images: {e}")
        return {
            "status": "FAIL",
            "file_path": file_path,
            "criteria": verification_criteria,
            "analysis": f"Visual analysis failed: {e}",
            "confidence": 0.0,
            "specific_issues": ["Analysis could not be completed"],
            "matching_features": []
        }


if __name__ == "__main__":
    # Run the server
    mcp.run()