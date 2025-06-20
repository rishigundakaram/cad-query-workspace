"""Pyramid example for testing CAD-Query workflow."""

import cadquery as cq

# Create a square pyramid by lofting from a square base to a point
base_size = 20
height = 15

# Create square base
base = cq.Workplane("XY").rect(base_size, base_size)

# Create top point by moving up and making a tiny square
top = cq.Workplane("XY").workplane(offset=height).rect(0.1, 0.1)

# Loft between base and top to create pyramid
result = base.loft(top)

show_object(result)  # noqa: F821