#!/usr/bin/env python3
"""Generate 4 standard orthographic views from a CAD-Query script."""

import subprocess
import sys
from pathlib import Path


def main() -> bool:
    if len(sys.argv) != 2:
        print("Usage: python render_views.py model.py")
        print("Example: python render_views.py examples/box.py")
        sys.exit(1)

    script_path = Path(sys.argv[1])
    if not script_path.exists():
        print(f"Error: Script {script_path} not found")
        sys.exit(1)

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

    print(f"Generating views for {script_path}...")

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
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✓ Generated {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to generate {view} view: {e.stderr}")
            return False

    print(f"\nAll views generated in {output_dir}/")
    return True


if __name__ == "__main__":
    main()
