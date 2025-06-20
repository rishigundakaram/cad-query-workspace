"""Model missing show_object for testing."""

import cadquery as cq

# Create a simple box but forget to call show_object
result = cq.Workplane("XY").box(5, 5, 5)
# Missing show_object(result)