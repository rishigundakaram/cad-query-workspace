#!/usr/bin/env python3
"""Generate a custom angle view from a CAD-Query script."""

import subprocess
import sys
from pathlib import Path


def main() -> bool:
    if len(sys.argv) != 5:
        print("Usage: python view_direction.py model.py x y z")
        print("Example: python view_direction.py examples/box.py 1 1 0.5")
        print("\nCommon viewing angles:")
        print("  Top: 0 0 1")
        print("  Front: 0 1 0")
        print("  Right: 1 0 0")
        print("  Isometric: 1 1 1")
        print("  Angled: 0.7 0.7 0.2")
        sys.exit(1)

    script_path = Path(sys.argv[1])
    if not script_path.exists():
        print(f"Error: Script {script_path} not found")
        sys.exit(1)

    try:
        x, y, z = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
    except ValueError:
        print("Error: x, y, z must be numbers")
        sys.exit(1)

    base_name = script_path.stem
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / f"{base_name}_custom.svg"

    cmd = [
        "cq-cli",
        "--codec",
        "svg",
        "--infile",
        str(script_path),
        "--outfile",
        str(output_file),
        "--outputopts",
        f"projectionDir:({x},{y},{z});width:400;height:400",
    ]

    print(f"Generating custom view from direction ({x},{y},{z})...")

    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✓ Generated {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to generate custom view: {e.stderr}")
        return False


if __name__ == "__main__":
    main()
