<a id="apireference"></a>

# API Reference

The CadQuery API is made up of 4 main objects:

* **Sketch** – Construct 2D sketches
* **Workplane** – Wraps a topological entity and provides a 2D modelling context.
* **Selector** – Filter and select things
* **Assembly** – Combine objects into assemblies.

This page lists  methods of these objects grouped by **functional area**

#### SEE ALSO
This page lists api methods grouped by functional area.
Use [CadQuery Class Summary](classreference.md#classreference) to see methods alphabetically by class.

## Sketch initialization

Creating new sketches.

| [`Sketch`](classreference.md#cadquery.Sketch)(parent, locs, obj)                                 | 2D sketch.                                               |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [`Sketch.importDXF`](classreference.md#cadquery.Sketch.importDXF)(filename[, tol, exclude, ...]) | Import a DXF file and construct face(s)                  |
| [`Workplane.sketch`](classreference.md#cadquery.Workplane.sketch)()                              | Initialize and return a sketch                           |
| [`Sketch.finalize`](classreference.md#cadquery.Sketch.finalize)()                                | Finish sketch construction and return the parent.        |
| [`Sketch.copy`](classreference.md#cadquery.Sketch.copy)()                                        | Create a partial copy of the sketch.                     |
| [`Sketch.located`](classreference.md#cadquery.Sketch.located)(loc)                               | Create a partial copy of the sketch with a new location. |
| [`Sketch.moved`](classreference.md#cadquery.Sketch.moved)()                                      | Create a partial copy of the sketch with moved \_faces.  |

## Sketch selection

Selecting, tagging and manipulating elements.

| [`Sketch.tag`](classreference.md#cadquery.Sketch.tag)(tag)                | Tag current selection.   |
|---------------------------------------------------------------------------|--------------------------|
| [`Sketch.select`](classreference.md#cadquery.Sketch.select)(\*tags)       | Select based on tags.    |
| [`Sketch.reset`](classreference.md#cadquery.Sketch.reset)()               | Reset current selection. |
| [`Sketch.delete`](classreference.md#cadquery.Sketch.delete)()             | Delete selected object.  |
| [`Sketch.faces`](classreference.md#cadquery.Sketch.faces)([s, tag])       | Select faces.            |
| [`Sketch.edges`](classreference.md#cadquery.Sketch.edges)([s, tag])       | Select edges.            |
| [`Sketch.vertices`](classreference.md#cadquery.Sketch.vertices)([s, tag]) | Select vertices.         |

## Sketching with faces

Sketching using the face-based API.

| [`Sketch.face`](classreference.md#cadquery.Sketch.face)(b[, angle, mode, tag, ...])                   | Construct a face from a wire or edges.                        |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| [`Sketch.rect`](classreference.md#cadquery.Sketch.rect)(w, h[, angle, mode, tag])                     | Construct a rectangular face.                                 |
| [`Sketch.circle`](classreference.md#cadquery.Sketch.circle)(r[, mode, tag])                           | Construct a circular face.                                    |
| [`Sketch.ellipse`](classreference.md#cadquery.Sketch.ellipse)(a1, a2[, angle, mode, tag])             | Construct an elliptical face.                                 |
| [`Sketch.trapezoid`](classreference.md#cadquery.Sketch.trapezoid)(w, h, a1[, a2, angle, ...])         | Construct a trapezoidal face.                                 |
| [`Sketch.slot`](classreference.md#cadquery.Sketch.slot)(w, h[, angle, mode, tag])                     | Construct a slot-shaped face.                                 |
| [`Sketch.regularPolygon`](classreference.md#cadquery.Sketch.regularPolygon)(r, n[, angle, mode, tag]) | Construct a regular polygonal face.                           |
| [`Sketch.polygon`](classreference.md#cadquery.Sketch.polygon)(pts[, angle, mode, tag])                | Construct a polygonal face.                                   |
| [`Sketch.rarray`](classreference.md#cadquery.Sketch.rarray)(xs, ys, nx, ny)                           | Generate a rectangular array of locations.                    |
| [`Sketch.parray`](classreference.md#cadquery.Sketch.parray)(r, a1, da, n[, rotate])                   | Generate a polar array of locations.                          |
| [`Sketch.distribute`](classreference.md#cadquery.Sketch.distribute)(n[, start, stop, rotate])         | Distribute locations along selected edges or wires.           |
| [`Sketch.each`](classreference.md#cadquery.Sketch.each)(callback[, mode, tag, ...])                   | Apply a callback on all applicable entities.                  |
| [`Sketch.push`](classreference.md#cadquery.Sketch.push)(locs[, tag])                                  | Set current selection to given locations or points.           |
| [`Sketch.hull`](classreference.md#cadquery.Sketch.hull)([mode, tag])                                  | Generate a convex hull from current selection or all objects. |
| [`Sketch.offset`](classreference.md#cadquery.Sketch.offset)(d[, mode, tag])                           | Offset selected wires or edges.                               |
| [`Sketch.fillet`](classreference.md#cadquery.Sketch.fillet)(d)                                        | Add a fillet based on current selection.                      |
| [`Sketch.chamfer`](classreference.md#cadquery.Sketch.chamfer)(d)                                      | Add a chamfer based on current selection.                     |
| [`Sketch.clean`](classreference.md#cadquery.Sketch.clean)()                                           | Remove internal wires.                                        |

## Sketching with edges and constraints

Sketching using the edge-based API.

| [`Sketch.edge`](classreference.md#cadquery.Sketch.edge)(val[, tag, forConstruction])          | Add an edge to the sketch.                           |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------|
| [`Sketch.segment`](classreference.md#cadquery.Sketch.segment)(self, p1, p2[, tag, ...])       | Construct a segment.                                 |
| [`Sketch.arc`](classreference.md#cadquery.Sketch.arc)(self, p1, p2, p3[, tag, ...])           | Construct an arc.                                    |
| [`Sketch.spline`](classreference.md#cadquery.Sketch.spline)(self, pts, tangents, periodic)    | Construct a spline edge.                             |
| [`Sketch.close`](classreference.md#cadquery.Sketch.close)([tag])                              | Connect last edge to the first one.                  |
| [`Sketch.assemble`](classreference.md#cadquery.Sketch.assemble)([mode, tag])                  | Assemble edges into faces.                           |
| [`Sketch.constrain`](classreference.md#cadquery.Sketch.constrain)(self, tag, constraint, arg) | Add a constraint.                                    |
| [`Sketch.solve`](classreference.md#cadquery.Sketch.solve)()                                   | Solve current constraints and update edge positions. |

## Initialization

Creating new workplanes and object chains

| [`Workplane`](classreference.md#cadquery.Workplane)(, obj=None))   | Defines a coordinate system in space, in which 2D coordinates can be used.   |
|--------------------------------------------------------------------|------------------------------------------------------------------------------|

<a id="doperations"></a>

## 2D Operations

Creating 2D constructs that can be used to create 3D features.

All 2D operations require a **Workplane** object to be created.

| [`Workplane.center`](classreference.md#cadquery.Workplane.center)(x, y)                                    | Shift local coordinates to the specified location.                                                                                    |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [`Workplane.lineTo`](classreference.md#cadquery.Workplane.lineTo)(x, y[, forConstruction])                 | Make a line from the current point to the provided point                                                                              |
| [`Workplane.line`](classreference.md#cadquery.Workplane.line)(xDist, yDist[, forConstruction])             | Make a line from the current point to the provided point, using dimensions relative to the current point                              |
| [`Workplane.vLine`](classreference.md#cadquery.Workplane.vLine)(distance[, forConstruction])               | Make a vertical line from the current point the provided distance                                                                     |
| [`Workplane.vLineTo`](classreference.md#cadquery.Workplane.vLineTo)(yCoord[, forConstruction])             | Make a vertical line from the current point to the provided y coordinate.                                                             |
| [`Workplane.hLine`](classreference.md#cadquery.Workplane.hLine)(distance[, forConstruction])               | Make a horizontal line from the current point the provided distance                                                                   |
| [`Workplane.hLineTo`](classreference.md#cadquery.Workplane.hLineTo)(xCoord[, forConstruction])             | Make a horizontal line from the current point to the provided x coordinate.                                                           |
| [`Workplane.polarLine`](classreference.md#cadquery.Workplane.polarLine)(distance, angle[, ...])            | Make a line of the given length, at the given angle from the current point                                                            |
| [`Workplane.polarLineTo`](classreference.md#cadquery.Workplane.polarLineTo)(distance, angle[, ...])        | Make a line from the current point to the given polar coordinates                                                                     |
| [`Workplane.moveTo`](classreference.md#cadquery.Workplane.moveTo)([x, y])                                  | Move to the specified point, without drawing.                                                                                         |
| [`Workplane.move`](classreference.md#cadquery.Workplane.move)([xDist, yDist])                              | Move the specified distance from the current point, without drawing.                                                                  |
| [`Workplane.spline`](classreference.md#cadquery.Workplane.spline)(listOfXYTuple[, tangents, ...])          | Create a spline interpolated through the provided points (2D or 3D).                                                                  |
| [`Workplane.parametricCurve`](classreference.md#cadquery.Workplane.parametricCurve)(func[, N, start, ...]) | Create a spline curve approximating the provided function.                                                                            |
| [`Workplane.parametricSurface`](classreference.md#cadquery.Workplane.parametricSurface)(func[, N, ...])    | Create a spline surface approximating the provided function.                                                                          |
| [`Workplane.threePointArc`](classreference.md#cadquery.Workplane.threePointArc)(point1, point2[, ...])     | Draw an arc from the current point, through point1, and ending at point2                                                              |
| [`Workplane.sagittaArc`](classreference.md#cadquery.Workplane.sagittaArc)(endPoint, sag[, ...])            | Draw an arc from the current point to endPoint with an arc defined by the sag (sagitta).                                              |
| [`Workplane.radiusArc`](classreference.md#cadquery.Workplane.radiusArc)(endPoint, radius[, ...])           | Draw an arc from the current point to endPoint with an arc defined by the radius.                                                     |
| [`Workplane.tangentArcPoint`](classreference.md#cadquery.Workplane.tangentArcPoint)(endpoint[, ...])       | Draw an arc as a tangent from the end of the current edge to endpoint.                                                                |
| [`Workplane.mirrorY`](classreference.md#cadquery.Workplane.mirrorY)()                                      | Mirror entities around the y axis of the workplane plane.                                                                             |
| [`Workplane.mirrorX`](classreference.md#cadquery.Workplane.mirrorX)()                                      | Mirror entities around the x axis of the workplane plane.                                                                             |
| [`Workplane.wire`](classreference.md#cadquery.Workplane.wire)([forConstruction])                           | Returns a CQ object with all pending edges connected into a wire.                                                                     |
| [`Workplane.rect`](classreference.md#cadquery.Workplane.rect)(xLen, yLen[, centered, ...])                 | Make a rectangle for each item on the stack.                                                                                          |
| [`Workplane.circle`](classreference.md#cadquery.Workplane.circle)(radius[, forConstruction])               | Make a circle for each item on the stack.                                                                                             |
| [`Workplane.ellipse`](classreference.md#cadquery.Workplane.ellipse)(x_radius, y_radius[, ...])             | Make an ellipse for each item on the stack.                                                                                           |
| [`Workplane.ellipseArc`](classreference.md#cadquery.Workplane.ellipseArc)(x_radius, y_radius[, ...])       | Draw an elliptical arc with x and y radiuses either with start point at current point or or current point being the center of the arc |
| [`Workplane.polyline`](classreference.md#cadquery.Workplane.polyline)(listOfXYTuple[, ...])                | Create a polyline from a list of points                                                                                               |
| [`Workplane.close`](classreference.md#cadquery.Workplane.close)()                                          | End construction, and attempt to build a closed wire.                                                                                 |
| [`Workplane.rarray`](classreference.md#cadquery.Workplane.rarray)(xSpacing, ySpacing, xCount, ...)         | Creates an array of points and pushes them onto the stack.                                                                            |
| [`Workplane.polarArray`](classreference.md#cadquery.Workplane.polarArray)(radius, startAngle, ...)         | Creates a polar array of points and pushes them onto the stack.                                                                       |
| [`Workplane.slot2D`](classreference.md#cadquery.Workplane.slot2D)(length, diameter[, angle])               | Creates a rounded slot for each point on the stack.                                                                                   |
| [`Workplane.offset2D`](classreference.md#cadquery.Workplane.offset2D)(d[, kind, forConstruction])          | Creates a 2D offset wire.                                                                                                             |
| [`Workplane.placeSketch`](classreference.md#cadquery.Workplane.placeSketch)(\*sketches)                    | Place the provided sketch(es) based on the current items on the stack.                                                                |

<a id="id1"></a>

## 3D Operations

Some 3D operations also require an active 2D workplane, but some do not.

3D operations that require a 2D workplane to be active:

| [`Workplane.cboreHole`](classreference.md#cadquery.Workplane.cboreHole)(diameter, cboreDiameter, ...)   | Makes a counterbored hole for each item on the stack.                                                                          |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [`Workplane.cskHole`](classreference.md#cadquery.Workplane.cskHole)(diameter, cskDiameter, ...)         | Makes a countersunk hole for each item on the stack.                                                                           |
| [`Workplane.hole`](classreference.md#cadquery.Workplane.hole)(diameter[, depth, clean])                 | Makes a hole for each item on the stack.                                                                                       |
| [`Workplane.extrude`](classreference.md#cadquery.Workplane.extrude)(until[, combine, clean, ...])       | Use all un-extruded wires in the parent chain to create a prismatic solid.                                                     |
| [`Workplane.cut`](classreference.md#cadquery.Workplane.cut)(toCut[, clean, tol])                        | Cuts the provided solid from the current solid, IE, perform a solid subtraction.                                               |
| [`Workplane.cutBlind`](classreference.md#cadquery.Workplane.cutBlind)(until[, clean, both, taper])      | Use all un-extruded wires in the parent chain to create a prismatic cut from existing solid.                                   |
| [`Workplane.cutThruAll`](classreference.md#cadquery.Workplane.cutThruAll)([clean, taper])               | Use all un-extruded wires in the parent chain to create a prismatic cut from existing solid.                                   |
| [`Workplane.box`](classreference.md#cadquery.Workplane.box)(length, width, height[, ...])               | Return a 3d box with specified dimensions for each object on the stack.                                                        |
| [`Workplane.sphere`](classreference.md#cadquery.Workplane.sphere)(radius[, direct, angle1, ...])        | Returns a 3D sphere with the specified radius for each point on the stack.                                                     |
| [`Workplane.wedge`](classreference.md#cadquery.Workplane.wedge)(dx, dy, dz, xmin, zmin, ...)            | Returns a 3D wedge with the specified dimensions for each point on the stack.                                                  |
| [`Workplane.cylinder`](classreference.md#cadquery.Workplane.cylinder)(height, radius[, direct, ...])    | Returns a cylinder with the specified radius and height for each point on the stack                                            |
| [`Workplane.union`](classreference.md#cadquery.Workplane.union)([toUnion, clean, glue, tol])            | Unions all of the items on the stack of toUnion with the current solid.                                                        |
| [`Workplane.combine`](classreference.md#cadquery.Workplane.combine)([clean, glue, tol])                 | Attempts to combine all of the items on the stack into a single item.                                                          |
| [`Workplane.intersect`](classreference.md#cadquery.Workplane.intersect)(toIntersect[, clean, tol])      | Intersects the provided solid from the current solid.                                                                          |
| [`Workplane.loft`](classreference.md#cadquery.Workplane.loft)([ruled, combine, clean])                  | Make a lofted solid, through the set of wires.                                                                                 |
| [`Workplane.sweep`](classreference.md#cadquery.Workplane.sweep)(path[, multisection, ...])              | Use all un-extruded wires in the parent chain to create a swept solid.                                                         |
| [`Workplane.twistExtrude`](classreference.md#cadquery.Workplane.twistExtrude)(distance, angleDegrees)   | Extrudes a wire in the direction normal to the plane, but also twists by the specified angle over the length of the extrusion. |
| [`Workplane.revolve`](classreference.md#cadquery.Workplane.revolve)([angleDegrees, axisStart, ...])     | Use all un-revolved wires in the parent chain to create a solid.                                                               |
| [`Workplane.text`](classreference.md#cadquery.Workplane.text)(txt, fontsize, distance[, ...])           | Returns a 3D text.                                                                                                             |

3D operations that do NOT require a 2D workplane to be active:

| [`Workplane.shell`](classreference.md#cadquery.Workplane.shell)(thickness[, kind])                         | Remove the selected faces to create a shell of the specified thickness.                                |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [`Workplane.fillet`](classreference.md#cadquery.Workplane.fillet)(radius)                                  | Fillets a solid on the selected edges.                                                                 |
| [`Workplane.chamfer`](classreference.md#cadquery.Workplane.chamfer)(length[, length2])                     | Chamfers a solid on the selected edges.                                                                |
| [`Workplane.split`](classreference.md#cadquery.Workplane.split)()                                          | Splits a solid on the stack into two parts, optionally keeping the separate parts.                     |
| [`Workplane.rotate`](classreference.md#cadquery.Workplane.rotate)(axisStartPoint, ...)                     | Returns a copy of all of the items on the stack rotated through and angle around the axis of rotation. |
| [`Workplane.rotateAboutCenter`](classreference.md#cadquery.Workplane.rotateAboutCenter)(axisEndPoint, ...) | Rotates all items on the stack by the specified angle, about the specified axis                        |
| [`Workplane.translate`](classreference.md#cadquery.Workplane.translate)(vec)                               | Returns a copy of all of the items on the stack moved by the specified translation vector.             |
| [`Workplane.mirror`](classreference.md#cadquery.Workplane.mirror)([mirrorPlane, ...])                      | Mirror a single CQ object.                                                                             |

## File Management and Export

| [`Workplane.toSvg`](classreference.md#cadquery.Workplane.toSvg)([opts])           | Returns svg text that represents the first item on the stack.   |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------|
| [`Workplane.exportSvg`](classreference.md#cadquery.Workplane.exportSvg)(fileName) | Exports the first item on the stack as an SVG file              |

| `importers.importStep`(fileName)                                                                             | Accepts a file name and loads the STEP file into a cadquery Workplane   |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [`importers.importDXF`](importexport.md#cadquery.importers.importDXF)(filename[, tol, ...])                  | Loads a DXF file into a Workplane.                                      |
| `exporters.export`(w, fname[, exportType, ...])                                                              | Export Workplane or Shape to file.                                      |
| [`occ_impl.exporters.dxf.DxfDocument`](classreference.md#cadquery.occ_impl.exporters.dxf.DxfDocument)([...]) | Create DXF document from CadQuery objects.                              |

## Iteration Methods

Methods that allow iteration over the stack or objects

| [`Workplane.each`](classreference.md#cadquery.Workplane.each)(callback[, ...])      | Runs the provided function on each value in the stack, and collects the return values into a new CQ object.   |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [`Workplane.eachpoint`](classreference.md#cadquery.Workplane.eachpoint)(arg[, ...]) | Same as each(), except arg is translated by the positions on the stack.                                       |

<a id="stackmethods"></a>

## Stack and Selector Methods

CadQuery methods that operate on the stack

| [`Workplane.all`](classreference.md#cadquery.Workplane.all)()                            | Return a list of all CQ objects on the stack.                                    |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [`Workplane.size`](classreference.md#cadquery.Workplane.size)()                          | Return the number of objects currently on the stack                              |
| [`Workplane.vals`](classreference.md#cadquery.Workplane.vals)()                          | get the values in the current list                                               |
| [`Workplane.add`](classreference.md#cadquery.Workplane.add)()                            | Adds an object or a list of objects to the stack                                 |
| [`Workplane.val`](classreference.md#cadquery.Workplane.val)()                            | Return the first value on the stack.                                             |
| [`Workplane.first`](classreference.md#cadquery.Workplane.first)()                        | Return the first item on the stack                                               |
| [`Workplane.item`](classreference.md#cadquery.Workplane.item)(i)                         | Return the ith item on the stack.                                                |
| [`Workplane.last`](classreference.md#cadquery.Workplane.last)()                          | Return the last item on the stack.                                               |
| [`Workplane.end`](classreference.md#cadquery.Workplane.end)([n])                         | Return the nth parent of this CQ element                                         |
| [`Workplane.vertices`](classreference.md#cadquery.Workplane.vertices)([selector, tag])   | Select the vertices of objects on the stack, optionally filtering the selection. |
| [`Workplane.faces`](classreference.md#cadquery.Workplane.faces)([selector, tag])         | Select the faces of objects on the stack, optionally filtering the selection.    |
| [`Workplane.edges`](classreference.md#cadquery.Workplane.edges)([selector, tag])         | Select the edges of objects on the stack, optionally filtering the selection.    |
| [`Workplane.wires`](classreference.md#cadquery.Workplane.wires)([selector, tag])         | Select the wires of objects on the stack, optionally filtering the selection.    |
| [`Workplane.solids`](classreference.md#cadquery.Workplane.solids)([selector, tag])       | Select the solids of objects on the stack, optionally filtering the selection.   |
| [`Workplane.shells`](classreference.md#cadquery.Workplane.shells)([selector, tag])       | Select the shells of objects on the stack, optionally filtering the selection.   |
| [`Workplane.compounds`](classreference.md#cadquery.Workplane.compounds)([selector, tag]) | Select compounds on the stack, optionally filtering the selection.               |

<a id="selectors"></a>

## Selectors

Objects that filter and select CAD objects. Selectors are used to select existing geometry
as a basis for further operations.

| [`NearestToPointSelector`](classreference.md#cadquery.selectors.NearestToPointSelector)(pnt)                     | Selects object nearest the provided point.                                                                              |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [`BoxSelector`](classreference.md#cadquery.selectors.BoxSelector)(point0, point1[, boundingbox])                 | Selects objects inside the 3D box defined by 2 points.                                                                  |
| [`BaseDirSelector`](classreference.md#cadquery.selectors.BaseDirSelector)(vector[, tolerance])                   | A selector that handles selection on the basis of a single direction vector.                                            |
| [`ParallelDirSelector`](classreference.md#cadquery.selectors.ParallelDirSelector)(vector[, tolerance])           | Selects objects parallel with the provided direction.                                                                   |
| [`DirectionSelector`](classreference.md#cadquery.selectors.DirectionSelector)(vector[, tolerance])               | Selects objects aligned with the provided direction.                                                                    |
| [`DirectionNthSelector`](classreference.md#cadquery.selectors.DirectionNthSelector)(vector, n[, ...])            | Filters for objects parallel (or normal) to the specified direction then returns the Nth one.                           |
| [`LengthNthSelector`](classreference.md#cadquery.selectors.LengthNthSelector)(n[, directionMax, tolerance])      | Select the object(s) with the Nth length                                                                                |
| [`AreaNthSelector`](classreference.md#cadquery.selectors.AreaNthSelector)(n[, directionMax, tolerance])          | Selects the object(s) with Nth area                                                                                     |
| [`RadiusNthSelector`](classreference.md#cadquery.selectors.RadiusNthSelector)(n[, directionMax, tolerance])      | Select the object with the Nth radius.                                                                                  |
| [`PerpendicularDirSelector`](classreference.md#cadquery.selectors.PerpendicularDirSelector)(vector[, tolerance]) | Selects objects perpendicular with the provided direction.                                                              |
| [`TypeSelector`](classreference.md#cadquery.selectors.TypeSelector)(typeString)                                  | Selects objects having the prescribed geometry type.                                                                    |
| [`DirectionMinMaxSelector`](classreference.md#cadquery.selectors.DirectionMinMaxSelector)(vector[, ...])         | Selects objects closest or farthest in the specified direction.                                                         |
| [`CenterNthSelector`](classreference.md#cadquery.selectors.CenterNthSelector)(vector, n[, directionMax, ...])    | Sorts objects into a list with order determined by the distance of their center projected onto the specified direction. |
| [`BinarySelector`](classreference.md#cadquery.selectors.BinarySelector)(left, right)                             | Base class for selectors that operates with two other selectors.                                                        |
| [`AndSelector`](classreference.md#cadquery.selectors.AndSelector)(left, right)                                   | Intersection selector.                                                                                                  |
| [`SumSelector`](classreference.md#cadquery.selectors.SumSelector)(left, right)                                   | Union selector.                                                                                                         |
| [`SubtractSelector`](classreference.md#cadquery.selectors.SubtractSelector)(left, right)                         | Difference selector.                                                                                                    |
| [`InverseSelector`](classreference.md#cadquery.selectors.InverseSelector)(selector)                              | Inverts the selection of given selector.                                                                                |
| [`StringSyntaxSelector`](classreference.md#cadquery.selectors.StringSyntaxSelector)(selectorString)              | Filter lists objects using a simple string syntax.                                                                      |

<a id="assembly"></a>

## Assemblies

Workplane and Shape objects can be connected together into assemblies

| [`Assembly`](classreference.md#cadquery.Assembly)([obj, loc, name, color, metadata])       | Nested assembly of Workplane and Shape objects defining their relative positions.   |
|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [`Assembly.add`](classreference.md#cadquery.Assembly.add)()                                | Add a subassembly to the current assembly.                                          |
| [`Assembly.save`](classreference.md#cadquery.Assembly.save)(path[, exportType, mode, ...]) | Save assembly to a file.                                                            |
| [`Assembly.constrain`](classreference.md#cadquery.Assembly.constrain)()                    | Define a new constraint.                                                            |
| [`Assembly.solve`](classreference.md#cadquery.Assembly.solve)([verbosity])                 | Solve the constraints.                                                              |
| [`Constraint`](classreference.md#cadquery.Constraint)                                      | alias of `ConstraintSpec`                                                           |
| [`Color`](classreference.md#cadquery.Color)()                                              | Wrapper for the OCCT color object Quantity_ColorRGBA.                               |
