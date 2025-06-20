"""L-shaped bracket example for testing CAD-Query workflow."""

import cadquery as cq

# Create an L-shaped mounting bracket
bracket_thickness = 5
bracket_width = 15
vertical_height = 25
horizontal_length = 30
hole_diameter = 4

# Create the vertical part
vertical_part = (cq.Workplane("XY")
                 .box(bracket_thickness, bracket_width, vertical_height)
                 .translate((0, 0, vertical_height/2)))

# Create the horizontal part
horizontal_part = (cq.Workplane("XY")
                   .box(horizontal_length, bracket_width, bracket_thickness)
                   .translate((horizontal_length/2 - bracket_thickness/2, 0, bracket_thickness/2)))

# Union the two parts to create L-shape
bracket = vertical_part.union(horizontal_part)

# Add mounting holes to vertical part
bracket = (bracket
           .faces(">X")  # Select the face facing positive X direction
           .workplane()
           .rarray(1, bracket_width - 6, 1, 2)  # Two holes vertically spaced
           .hole(hole_diameter))

# Add mounting holes to horizontal part
bracket = (bracket
           .faces(">Z")  # Select the top face of horizontal part
           .workplane()
           .rarray(horizontal_length - 8, 1, 2, 1)  # Two holes horizontally spaced
           .hole(hole_diameter))

result = bracket

show_object(result)  # noqa: F821