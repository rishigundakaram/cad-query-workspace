"""Simple gear example for testing CAD-Query workflow."""

import cadquery as cq
import math

# Create a simple gear with 8 teeth
tooth_count = 8
gear_radius = 10
tooth_height = 2
tooth_width = 1.5

# Create the main gear body (cylinder)
gear_body = cq.Workplane("XY").cylinder(height=5, radius=gear_radius)

# Create teeth around the circumference
for i in range(tooth_count):
    angle = i * 360 / tooth_count
    x = (gear_radius + tooth_height/2) * math.cos(math.radians(angle))
    y = (gear_radius + tooth_height/2) * math.sin(math.radians(angle))
    
    # Create tooth as a small box
    tooth = (cq.Workplane("XY")
             .center(x, y)
             .box(tooth_width, tooth_width, 5))
    
    gear_body = gear_body.union(tooth)

# Add center hole for axle
result = gear_body.faces(">Z").hole(3)

show_object(result)  # noqa: F821