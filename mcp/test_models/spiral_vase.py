"""Spiral vase example for testing CAD-Query workflow."""

import cadquery as cq
import math

# Create a vase with a spiral profile
height = 20
base_radius = 8
top_radius = 4
wall_thickness = 2

# Create the main vase body using loft between multiple circular profiles
profiles = []
num_sections = 10

for i in range(num_sections + 1):
    z = i * height / num_sections
    # Radius varies from base to top
    radius = base_radius - (base_radius - top_radius) * (i / num_sections)
    # Add slight spiral twist
    angle = i * 15  # 15 degrees per section
    
    # Create profile at this height with rotation
    profile = (cq.Workplane("XY")
               .workplane(offset=z)
               .transformed(rotate=(0, 0, angle))
               .circle(radius))
    profiles.append(profile)

# Loft all profiles to create the vase shape
vase_solid = profiles[0]
for i in range(1, len(profiles)):
    vase_solid = vase_solid.loft(profiles[i])

# Hollow out the vase by creating inner profiles and subtracting
inner_profiles = []
for i in range(num_sections + 1):
    z = i * height / num_sections
    inner_radius = base_radius - wall_thickness - (base_radius - top_radius - wall_thickness) * (i / num_sections)
    if inner_radius > 0:
        angle = i * 15
        profile = (cq.Workplane("XY")
                   .workplane(offset=z + 1)  # Start slightly above bottom
                   .transformed(rotate=(0, 0, angle))
                   .circle(inner_radius))
        inner_profiles.append(profile)

if inner_profiles:
    inner_solid = inner_profiles[0]
    for i in range(1, len(inner_profiles)):
        inner_solid = inner_solid.loft(inner_profiles[i])
    
    result = vase_solid.cut(inner_solid)
else:
    result = vase_solid

show_object(result)  # noqa: F821