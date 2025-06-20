"""Intentionally broken model for testing FAIL cases."""

import cadquery as cq

# This model has invalid syntax - missing show_object
result = cq.Workplane("XY").box(10, 10, 10)
# Missing show_object(result) - should FAIL