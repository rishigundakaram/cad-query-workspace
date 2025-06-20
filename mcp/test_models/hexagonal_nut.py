"""Hexagonal nut example for testing CAD-Query workflow."""

import cadquery as cq

# Create a hexagonal nut
nut_diameter = 15  # Distance across flats
nut_height = 8
hole_diameter = 6

# Create hexagonal profile
hex_radius = nut_diameter / 2
result = (cq.Workplane("XY")
          .polygon(6, hex_radius)  # 6-sided polygon (hexagon)
          .extrude(nut_height)     # Extrude to create height
          .faces(">Z")             # Select top face
          .hole(hole_diameter))    # Create threaded hole

show_object(result)  # noqa: F821