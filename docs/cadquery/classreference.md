<a id="classreference"></a>

# CadQuery Class Summary

This page documents all of the methods and functions of the CadQuery classes, organized alphabetically.

#### SEE ALSO
For a listing organized by functional area, see the [API Reference](apireference.md#apireference)

## Core Classes

| [`Sketch`](#cadquery.Sketch)(parent, locs, obj)                     | 2D sketch.                                                                        |
|---------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [`Workplane`](#cadquery.Workplane)(, obj=None))                     | Defines a coordinate system in space, in which 2D coordinates can be used.        |
| [`Assembly`](#cadquery.Assembly)([obj, loc, name, color, metadata]) | Nested assembly of Workplane and Shape objects defining their relative positions. |
| [`Constraint`](#cadquery.Constraint)                                | alias of `ConstraintSpec`                                                         |

## Topological Classes

| [`Shape`](#cadquery.Shape)(obj)                                           | Represents a shape in the system.                                  |
|---------------------------------------------------------------------------|--------------------------------------------------------------------|
| [`Vertex`](#cadquery.Vertex)(obj[, forConstruction])                      | A Single Point in Space                                            |
| [`Edge`](#cadquery.Edge)(obj)                                             | A trimmed curve that represents the border of a face               |
| [`cadquery.occ_impl.shapes.Mixin1D`](#cadquery.occ_impl.shapes.Mixin1D)() |                                                                    |
| [`Wire`](#cadquery.Wire)(obj)                                             | A series of connected, ordered Edges, that typically bounds a Face |
| [`Face`](#cadquery.Face)(obj)                                             | a bounded surface that represents part of the boundary of a solid  |
| [`Shell`](#cadquery.Shell)(obj)                                           | the outer boundary of a surface                                    |
| [`cadquery.occ_impl.shapes.Mixin3D`](#cadquery.occ_impl.shapes.Mixin3D)() |                                                                    |
| [`Solid`](#cadquery.Solid)(obj)                                           | a single solid                                                     |
| [`Compound`](#cadquery.Compound)(obj)                                     | a collection of disconnected solids                                |

## Geometry Classes

| [`Vector`](#cadquery.Vector)()                     | Create a 3-dimensional vector     |
|----------------------------------------------------|-----------------------------------|
| [`Matrix`](#cadquery.Matrix)()                     | A 3d , 4x4 transformation matrix. |
| [`Plane`](#cadquery.Plane)(origin[, xDir, normal]) | A 2D coordinate system in space   |
| [`Location`](#cadquery.Location)(t)                | Location in 3D space.             |

## Selector Classes

| [`Selector`](#cadquery.selectors.Selector)()                                                    | Filters a list of objects.                                                                                              |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [`NearestToPointSelector`](#cadquery.selectors.NearestToPointSelector)(pnt)                     | Selects object nearest the provided point.                                                                              |
| [`BoxSelector`](#cadquery.selectors.BoxSelector)(point0, point1[, boundingbox])                 | Selects objects inside the 3D box defined by 2 points.                                                                  |
| [`BaseDirSelector`](#cadquery.selectors.BaseDirSelector)(vector[, tolerance])                   | A selector that handles selection on the basis of a single direction vector.                                            |
| [`ParallelDirSelector`](#cadquery.selectors.ParallelDirSelector)(vector[, tolerance])           | Selects objects parallel with the provided direction.                                                                   |
| [`DirectionSelector`](#cadquery.selectors.DirectionSelector)(vector[, tolerance])               | Selects objects aligned with the provided direction.                                                                    |
| [`PerpendicularDirSelector`](#cadquery.selectors.PerpendicularDirSelector)(vector[, tolerance]) | Selects objects perpendicular with the provided direction.                                                              |
| [`TypeSelector`](#cadquery.selectors.TypeSelector)(typeString)                                  | Selects objects having the prescribed geometry type.                                                                    |
| [`RadiusNthSelector`](#cadquery.selectors.RadiusNthSelector)(n[, directionMax, tolerance])      | Select the object with the Nth radius.                                                                                  |
| [`CenterNthSelector`](#cadquery.selectors.CenterNthSelector)(vector, n[, directionMax, ...])    | Sorts objects into a list with order determined by the distance of their center projected onto the specified direction. |
| [`DirectionMinMaxSelector`](#cadquery.selectors.DirectionMinMaxSelector)(vector[, ...])         | Selects objects closest or farthest in the specified direction.                                                         |
| [`DirectionNthSelector`](#cadquery.selectors.DirectionNthSelector)(vector, n[, ...])            | Filters for objects parallel (or normal) to the specified direction then returns the Nth one.                           |
| [`LengthNthSelector`](#cadquery.selectors.LengthNthSelector)(n[, directionMax, tolerance])      | Select the object(s) with the Nth length                                                                                |
| [`AreaNthSelector`](#cadquery.selectors.AreaNthSelector)(n[, directionMax, tolerance])          | Selects the object(s) with Nth area                                                                                     |
| [`BinarySelector`](#cadquery.selectors.BinarySelector)(left, right)                             | Base class for selectors that operates with two other selectors.                                                        |
| [`AndSelector`](#cadquery.selectors.AndSelector)(left, right)                                   | Intersection selector.                                                                                                  |
| [`SumSelector`](#cadquery.selectors.SumSelector)(left, right)                                   | Union selector.                                                                                                         |
| [`SubtractSelector`](#cadquery.selectors.SubtractSelector)(left, right)                         | Difference selector.                                                                                                    |
| [`InverseSelector`](#cadquery.selectors.InverseSelector)(selector)                              | Inverts the selection of given selector.                                                                                |
| [`StringSyntaxSelector`](#cadquery.selectors.StringSyntaxSelector)(selectorString)              | Filter lists objects using a simple string syntax.                                                                      |

## Class Details

### *class* cadquery.Assembly(obj: [Shape](#cadquery.occ_impl.shapes.Shape) | [Workplane](#cadquery.Workplane) | None = None, loc: [Location](#cadquery.Location) | None = None, name: str | None = None, color: [Color](#cadquery.Color) | None = None, metadata: Dict[str, Any] | None = None)

Bases: `object`

Nested assembly of Workplane and Shape objects defining their relative positions.

* **Parameters:**
  * **obj** ([*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Workplane*](#cadquery.Workplane) *|* *None*)
  * **loc** ([*Location*](#cadquery.Location))
  * **name** (*str*)
  * **color** ([*Color*](#cadquery.Color) *|* *None*)
  * **metadata** (*Dict* *[**str* *,* *Any* *]*)

#### \_\_init_\_(obj: [Shape](#cadquery.occ_impl.shapes.Shape) | [Workplane](#cadquery.Workplane) | None = None, loc: [Location](#cadquery.Location) | None = None, name: str | None = None, color: [Color](#cadquery.Color) | None = None, metadata: Dict[str, Any] | None = None)

construct an assembly

* **Parameters:**
  * **obj** ([*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Workplane*](#cadquery.Workplane) *|* *None*) – root object of the assembly (default: None)
  * **loc** ([*Location*](#cadquery.Location) *|* *None*) – location of the root object (default: None, interpreted as identity transformation)
  * **name** (*str* *|* *None*) – unique name of the root object (default: None, resulting in an UUID being generated)
  * **color** ([*Color*](#cadquery.Color) *|* *None*) – color of the added object (default: None)
  * **metadata** (*Dict* *[**str* *,* *Any* *]*  *|* *None*) – a store for user-defined metadata (default: None)
* **Returns:**
  An Assembly object.

To create an empty assembly use:

```default
assy = Assembly(None)
```

To create one constraint a root object:

```default
b = Workplane().box(1, 1, 1)
assy = Assembly(b, Location(Vector(0, 0, 1)), name="root")
```

#### \_\_iter_\_(loc: [Location](#cadquery.Location) | None = None, name: str | None = None, color: [Color](#cadquery.Color) | None = None) → Iterator[Tuple[[Shape](#cadquery.occ_impl.shapes.Shape), str, [Location](#cadquery.Location), [Color](#cadquery.Color) | None]]

Assembly iterator yielding shapes, names, locations and colors.

* **Parameters:**
  * **loc** ([*Location*](#cadquery.Location) *|* *None*)
  * **name** (*str* *|* *None*)
  * **color** ([*Color*](#cadquery.Color) *|* *None*)
* **Return type:**
  *Iterator*[*Tuple*[[*Shape*](#cadquery.occ_impl.shapes.Shape), str, [*Location*](#cadquery.Location), [*Color*](#cadquery.Color) | None]]

#### \_\_weakref_\_

list of weak references to the object

#### add(arg, \*\*kwargs)

Add a subassembly to the current assembly.

#### constrain(\*args, param=None)

Define a new constraint.

#### export(path: str, exportType: Literal['STEP', 'XML', 'GLTF', 'VTKJS', 'VRML', 'STL'] | None = None, mode: Literal['default', 'fused'] = 'default', tolerance: float = 0.1, angularTolerance: float = 0.1, \*\*kwargs) → [Assembly](#cadquery.Assembly)

Save assembly to a file.

* **Parameters:**
  * **path** (*str*) – Path and filename for writing.
  * **exportType** (*Literal* *[* *'STEP'* *,*  *'XML'* *,*  *'GLTF'* *,*  *'VTKJS'* *,*  *'VRML'* *,*  *'STL'* *]*  *|* *None*) – export format (default: None, results in format being inferred form the path)
  * **mode** (*Literal* *[* *'default'* *,*  *'fused'* *]*) – STEP only - See [`exportAssembly()`](#cadquery.occ_impl.exporters.assembly.exportAssembly).
  * **tolerance** (*float*) – the deflection tolerance, in model units. Only used for glTF, VRML. Default 0.1.
  * **angularTolerance** (*float*) – the angular tolerance, in radians. Only used for glTF, VRML. Default 0.1.
  * **\*\*kwargs** – Additional keyword arguments.  Only used for STEP, glTF and STL.
    See [`exportAssembly()`](#cadquery.occ_impl.exporters.assembly.exportAssembly).
  * **ascii** (*bool*) – STL only - Sets whether or not STL export should be text or binary
* **Return type:**
  [*Assembly*](#cadquery.Assembly)

#### save(path: str, exportType: Literal['STEP', 'XML', 'GLTF', 'VTKJS', 'VRML', 'STL'] | None = None, mode: Literal['default', 'fused'] = 'default', tolerance: float = 0.1, angularTolerance: float = 0.1, \*\*kwargs) → [Assembly](#cadquery.Assembly)

Save assembly to a file.

* **Parameters:**
  * **path** (*str*) – Path and filename for writing.
  * **exportType** (*Literal* *[* *'STEP'* *,*  *'XML'* *,*  *'GLTF'* *,*  *'VTKJS'* *,*  *'VRML'* *,*  *'STL'* *]*  *|* *None*) – export format (default: None, results in format being inferred form the path)
  * **mode** (*Literal* *[* *'default'* *,*  *'fused'* *]*) – STEP only - See [`exportAssembly()`](#cadquery.occ_impl.exporters.assembly.exportAssembly).
  * **tolerance** (*float*) – the deflection tolerance, in model units. Only used for glTF, VRML. Default 0.1.
  * **angularTolerance** (*float*) – the angular tolerance, in radians. Only used for glTF, VRML. Default 0.1.
  * **\*\*kwargs** – Additional keyword arguments.  Only used for STEP, glTF and STL.
    See [`exportAssembly()`](#cadquery.occ_impl.exporters.assembly.exportAssembly).
  * **ascii** (*bool*) – STL only - Sets whether or not STL export should be text or binary
* **Return type:**
  [*Assembly*](#cadquery.Assembly)

#### *property* shapes *: List[[Shape](#cadquery.occ_impl.shapes.Shape)]*

List of Shape objects in the .obj field

#### solve(verbosity: int = 0) → [Assembly](#cadquery.Assembly)

Solve the constraints.

* **Parameters:**
  **verbosity** (*int*)
* **Return type:**
  [*Assembly*](#cadquery.Assembly)

#### toCompound() → [Compound](#cadquery.occ_impl.shapes.Compound)

Returns a Compound made from this Assembly (including all children) with the
current Locations applied. Usually this method would only be used after solving.

* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### traverse() → Iterator[Tuple[str, [Assembly](#cadquery.Assembly)]]

Yield (name, child) pairs in a bottom-up manner

* **Return type:**
  *Iterator*[*Tuple*[str, [*Assembly*](#cadquery.Assembly)]]

### *class* cadquery.BoundBox(bb: Bnd_Box)

Bases: `object`

A BoundingBox for an object or set of objects. Wraps the OCP one

* **Parameters:**
  **bb** (*Bnd_Box*)

#### \_\_init_\_(bb: Bnd_Box) → None

* **Parameters:**
  **bb** (*Bnd_Box*)
* **Return type:**
  None

#### \_\_weakref_\_

list of weak references to the object

#### add(obj: Tuple[float, float, float] | [Vector](#cadquery.Vector) | [BoundBox](#cadquery.BoundBox), tol: float | None = None) → [BoundBox](#cadquery.BoundBox)

Returns a modified (expanded) bounding box

obj can be one of several things:
: 1. a 3-tuple corresponding to x,y, and z amounts to add
  2. a vector, containing the x,y,z values to add
  3. another bounding box, where a new box will be created that
     encloses both.

This bounding box is not changed.

* **Parameters:**
  * **obj** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *|* [*BoundBox*](#cadquery.BoundBox))
  * **tol** (*float* *|* *None*)
* **Return type:**
  [*BoundBox*](#cadquery.BoundBox)

#### enlarge(tol: float) → [BoundBox](#cadquery.BoundBox)

Returns a modified (expanded) bounding box, expanded in all
directions by the tolerance value.

This means that the minimum values of its X, Y and Z intervals
of the bounding box are reduced by the absolute value of tol, while
the maximum values are increased by the same amount.

* **Parameters:**
  **tol** (*float*)
* **Return type:**
  [*BoundBox*](#cadquery.BoundBox)

#### *static* findOutsideBox2D(bb1: [BoundBox](#cadquery.BoundBox), bb2: [BoundBox](#cadquery.BoundBox)) → [BoundBox](#cadquery.BoundBox) | None

Compares bounding boxes

Compares bounding boxes. Returns none if neither is inside the other.
Returns the outer one if either is outside the other.

BoundBox.isInside works in 3d, but this is a 2d bounding box, so it
doesn’t work correctly plus, there was all kinds of rounding error in
the built-in implementation i do not understand.

* **Parameters:**
  * **bb1** ([*BoundBox*](#cadquery.BoundBox))
  * **bb2** ([*BoundBox*](#cadquery.BoundBox))
* **Return type:**
  [*BoundBox*](#cadquery.BoundBox) | None

#### isInside(b2: [BoundBox](#cadquery.BoundBox)) → bool

Is the provided bounding box inside this one?

* **Parameters:**
  **b2** ([*BoundBox*](#cadquery.BoundBox))
* **Return type:**
  bool

### cadquery.CQ

alias of [`Workplane`](#cadquery.Workplane)

### *class* cadquery.Color(name: str)

### *class* cadquery.Color(r: float, g: float, b: float, a: float = 0)

### *class* cadquery.Color

Bases: `object`

Wrapper for the OCCT color object Quantity_ColorRGBA.

#### \_\_eq_\_(other)

Return self==value.

#### \_\_hash_\_()

Return hash(self).

#### \_\_init_\_(\*args, \*\*kwargs)

#### \_\_weakref_\_

list of weak references to the object

#### toTuple() → Tuple[float, float, float, float]

Convert Color to RGB tuple.

* **Return type:**
  *Tuple*[float, float, float, float]

### *class* cadquery.Compound(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape), [`Mixin3D`](#cadquery.occ_impl.shapes.Mixin3D)

a collection of disconnected solids

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### \_\_bool_\_() → bool

Check if empty.

* **Return type:**
  bool

#### ancestors(shape: [Shape](#cadquery.occ_impl.shapes.Shape), kind: Literal['Vertex', 'Edge', 'Wire', 'Face', 'Shell', 'Solid', 'CompSolid', 'Compound']) → [Compound](#cadquery.occ_impl.shapes.Compound)

Iterate over ancestors, i.e. shapes of same kind within shape that contain elements of self.

* **Parameters:**
  * **shape** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **kind** (*Literal* *[* *'Vertex'* *,*  *'Edge'* *,*  *'Wire'* *,*  *'Face'* *,*  *'Shell'* *,*  *'Solid'* *,*  *'CompSolid'* *,*  *'Compound'* *]*)
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### cut(\*toCut: [Shape](#cadquery.occ_impl.shapes.Shape), tol: float | None = None) → [Compound](#cadquery.occ_impl.shapes.Compound)

Remove the positional arguments from this Shape.

* **Parameters:**
  * **tol** (*float* *|* *None*) – Fuzzy mode tolerance
  * **toCut** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### fuse(\*toFuse: [Shape](#cadquery.occ_impl.shapes.Shape), glue: bool = False, tol: float | None = None) → [Compound](#cadquery.occ_impl.shapes.Compound)

Fuse shapes together

* **Parameters:**
  * **toFuse** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **glue** (*bool*)
  * **tol** (*float* *|* *None*)
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### intersect(\*toIntersect: [Shape](#cadquery.occ_impl.shapes.Shape), tol: float | None = None) → [Compound](#cadquery.occ_impl.shapes.Compound)

Intersection of the positional arguments and this Shape.

* **Parameters:**
  * **tol** (*float* *|* *None*) – Fuzzy mode tolerance
  * **toIntersect** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### *classmethod* makeCompound(listOfShapes: Iterable[[Shape](#cadquery.occ_impl.shapes.Shape)]) → [Compound](#cadquery.occ_impl.shapes.Compound)

Create a compound out of a list of shapes

* **Parameters:**
  **listOfShapes** (*Iterable* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *]*)
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### *classmethod* makeText(text: str, size: float, height: float, font: str = 'Arial', fontPath: str | None = None, kind: Literal['regular', 'bold', 'italic'] = 'regular', halign: Literal['center', 'left', 'right'] = 'center', valign: Literal['center', 'top', 'bottom'] = 'center', position: [Plane](#cadquery.Plane) = Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))) → [Shape](#cadquery.occ_impl.shapes.Shape)

Create a 3D text

* **Parameters:**
  * **text** (*str*)
  * **size** (*float*)
  * **height** (*float*)
  * **font** (*str*)
  * **fontPath** (*str* *|* *None*)
  * **kind** (*Literal* *[* *'regular'* *,*  *'bold'* *,*  *'italic'* *]*)
  * **halign** (*Literal* *[* *'center'* *,*  *'left'* *,*  *'right'* *]*)
  * **valign** (*Literal* *[* *'center'* *,*  *'top'* *,*  *'bottom'* *]*)
  * **position** ([*Plane*](#cadquery.Plane))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### remove(shape: [Shape](#cadquery.occ_impl.shapes.Shape))

Remove the specified shape.

* **Parameters:**
  **shape** ([*Shape*](#cadquery.occ_impl.shapes.Shape))

#### siblings(shape: [Shape](#cadquery.occ_impl.shapes.Shape), kind: Literal['Vertex', 'Edge', 'Wire', 'Face', 'Shell', 'Solid', 'CompSolid', 'Compound'], level: int = 1) → [Compound](#cadquery.occ_impl.shapes.Compound)

Iterate over siblings, i.e. shapes within shape that share subshapes of kind with the elements of self.

* **Parameters:**
  * **shape** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **kind** (*Literal* *[* *'Vertex'* *,*  *'Edge'* *,*  *'Wire'* *,*  *'Face'* *,*  *'Shell'* *,*  *'Solid'* *,*  *'CompSolid'* *,*  *'Compound'* *]*)
  * **level** (*int*)
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

### cadquery.Constraint

alias of `ConstraintSpec`

### *class* cadquery.DirectionMinMaxSelector(vector: [Vector](#cadquery.Vector), directionMax: bool = True, tolerance: float = 0.0001)

Bases: [`CenterNthSelector`](#cadquery.selectors.CenterNthSelector)

Selects objects closest or farthest in the specified direction.

Applicability:
: All object types. for a vertex, its point is used. for all other kinds
  of objects, the center of mass of the object is used.

You can use the string shortcuts >(X|Y|Z) or <(X|Y|Z) if you want to select
based on a cardinal direction.

For example this:

```default
CQ(aCube).faces(DirectionMinMaxSelector((0, 0, 1), True))
```

Means to select the face having the center of mass farthest in the positive
z direction, and is the same as:

```default
CQ(aCube).faces(">Z")
```

* **Parameters:**
  * **vector** ([*Vector*](#cadquery.Vector))
  * **directionMax** (*bool*)
  * **tolerance** (*float*)

#### \_\_init_\_(vector: [Vector](#cadquery.Vector), directionMax: bool = True, tolerance: float = 0.0001)

* **Parameters:**
  * **vector** ([*Vector*](#cadquery.Vector))
  * **directionMax** (*bool*)
  * **tolerance** (*float*)

### *class* cadquery.DirectionSelector(vector: [Vector](#cadquery.Vector), tolerance: float = 0.0001)

Bases: [`BaseDirSelector`](#cadquery.selectors.BaseDirSelector)

Selects objects aligned with the provided direction.

Applicability:
: Linear Edges
  Planar Faces

Use the string syntax shortcut +/-(X|Y|Z) if you want to select based on a cardinal direction.

Example:

```default
CQ(aCube).faces(DirectionSelector((0, 0, 1)))
```

selects faces with the normal in the z direction, and is equivalent to:

```default
CQ(aCube).faces("+Z")
```

* **Parameters:**
  * **vector** ([*Vector*](#cadquery.Vector))
  * **tolerance** (*float*)

#### test(vec: [Vector](#cadquery.Vector)) → bool

Test a specified vector. Subclasses override to provide other implementations

* **Parameters:**
  **vec** ([*Vector*](#cadquery.Vector))
* **Return type:**
  bool

### *class* cadquery.Edge(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape), [`Mixin1D`](#cadquery.occ_impl.shapes.Mixin1D)

A trimmed curve that represents the border of a face

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### arcCenter() → [Vector](#cadquery.Vector)

Center of an underlying circle or ellipse geometry.

* **Return type:**
  [*Vector*](#cadquery.Vector)

#### close() → [Edge](#cadquery.occ_impl.shapes.Edge) | [Wire](#cadquery.occ_impl.shapes.Wire)

Close an Edge

* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge) | [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### *classmethod* makeBezier(points: List[[Vector](#cadquery.Vector)]) → [Edge](#cadquery.occ_impl.shapes.Edge)

Create a cubic Bézier Curve from the points.

* **Parameters:**
  **points** (*List* *[*[*Vector*](#cadquery.Vector) *]*) – a list of Vectors that represent the points.
  The edge will pass through the first and the last point,
  and the inner points are Bézier control points.
* **Returns:**
  An edge
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### *classmethod* makeEllipse(x_radius: float, y_radius: float, pnt: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0), xdir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (1.0, 0.0, 0.0), angle1: float = 360.0, angle2: float = 360.0, sense: ~typing.Literal[-1, 1] = 1) → [Edge](#cadquery.occ_impl.shapes.Edge)

Makes an Ellipse centered at the provided point, having normal in the provided direction.

* **Parameters:**
  * **cls**
  * **x_radius** (*float*) – x radius of the ellipse (along the x-axis of plane the ellipse should lie in)
  * **y_radius** (*float*) – y radius of the ellipse (along the y-axis of plane the ellipse should lie in)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – vector representing the center of the ellipse
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – vector representing the direction of the plane the ellipse should lie in
  * **angle1** (*float*) – start angle of arc
  * **angle2** (*float*) – end angle of arc (angle2 == angle1 return closed ellipse = default)
  * **sense** (*Literal* *[* *-1* *,* *1* *]*) – clockwise (-1) or counter clockwise (1)
  * **xdir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Returns:**
  an Edge
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### *classmethod* makeLine(v1: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], v2: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Edge](#cadquery.occ_impl.shapes.Edge)

Create a line between two points

* **Parameters:**
  * **v1** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – Vector that represents the first point
  * **v2** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – Vector that represents the second point
* **Returns:**
  A linear edge between the two provided points
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### *classmethod* makeSpline(listOfVector: List[[Vector](#cadquery.Vector)], tangents: Sequence[[Vector](#cadquery.Vector)] | None = None, periodic: bool = False, parameters: Sequence[float] | None = None, scale: bool = True, tol: float = 1e-06) → [Edge](#cadquery.occ_impl.shapes.Edge)

Interpolate a spline through the provided points.

* **Parameters:**
  * **listOfVector** (*List* *[*[*Vector*](#cadquery.Vector) *]*) – a list of Vectors that represent the points
  * **tangents** (*Sequence* *[*[*Vector*](#cadquery.Vector) *]*  *|* *None*) – tuple of Vectors specifying start and finish tangent
  * **periodic** (*bool*) – creation of periodic curves
  * **parameters** (*Sequence* *[**float* *]*  *|* *None*) – the value of the parameter at each interpolation point. (The interpolated
    curve is represented as a vector-valued function of a scalar parameter.) If periodic ==
    True, then len(parameters) must be len(intepolation points) + 1, otherwise len(parameters)
    must be equal to len(interpolation points).
  * **scale** (*bool*) – whether to scale the specified tangent vectors before interpolating. Each
    tangent is scaled, so it’s length is equal to the derivative of the Lagrange interpolated
    curve. I.e., set this to True, if you want to use only the direction of the tangent
    vectors specified by `tangents`, but not their magnitude.
  * **tol** (*float*) – tolerance of the algorithm (consult OCC documentation). Used to check that the
    specified points are not too close to each other, and that tangent vectors are not too
    short. (In either case interpolation may fail.)
* **Returns:**
  an Edge
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### *classmethod* makeSplineApprox(listOfVector: List[[Vector](#cadquery.Vector)], tol: float = 0.001, smoothing: Tuple[float, float, float] | None = None, minDeg: int = 1, maxDeg: int = 6) → [Edge](#cadquery.occ_impl.shapes.Edge)

Approximate a spline through the provided points.

* **Parameters:**
  * **listOfVector** (*List* *[*[*Vector*](#cadquery.Vector) *]*) – a list of Vectors that represent the points
  * **tol** (*float*) – tolerance of the algorithm (consult OCC documentation).
  * **smoothing** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* *None*) – optional tuple of 3 weights use for variational smoothing (default: None)
  * **minDeg** (*int*) – minimum spline degree. Enforced only when smothing is None (default: 1)
  * **maxDeg** (*int*) – maximum spline degree (default: 6)
* **Returns:**
  an Edge
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### *classmethod* makeTangentArc(v1: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], v2: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], v3: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Edge](#cadquery.occ_impl.shapes.Edge)

Makes a tangent arc from point v1, in the direction of v2 and ends at v3.

* **Parameters:**
  * **cls**
  * **v1** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – start vector
  * **v2** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – tangent vector
  * **v3** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – end vector
* **Returns:**
  an edge
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### *classmethod* makeThreePointArc(v1: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], v2: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], v3: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Edge](#cadquery.occ_impl.shapes.Edge)

Makes a three point arc through the provided points

* **Parameters:**
  * **cls**
  * **v1** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – start vector
  * **v2** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – middle vector
  * **v3** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – end vector
* **Returns:**
  an edge object through the three points
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### trim(u0: float | int, u1: float | int) → [Edge](#cadquery.occ_impl.shapes.Edge)

Trim the edge in the parametric space to (u0, u1).

NB: this operation is done on the base geometry.

* **Parameters:**
  * **u0** (*float* *|* *int*)
  * **u1** (*float* *|* *int*)
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

### *class* cadquery.Face(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape)

a bounded surface that represents part of the boundary of a solid

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### Center() → [Vector](#cadquery.Vector)

* **Returns:**
  The point of the center of mass of this Shape
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### chamfer2D(d: float, vertices: Iterable[[Vertex](#cadquery.occ_impl.shapes.Vertex)]) → [Face](#cadquery.occ_impl.shapes.Face)

Apply 2D chamfer to a face

* **Parameters:**
  * **d** (*float*)
  * **vertices** (*Iterable* *[*[*Vertex*](#cadquery.occ_impl.shapes.Vertex) *]*)
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### fillet2D(radius: float, vertices: Iterable[[Vertex](#cadquery.occ_impl.shapes.Vertex)]) → [Face](#cadquery.occ_impl.shapes.Face)

Apply 2D fillet to a face

* **Parameters:**
  * **radius** (*float*)
  * **vertices** (*Iterable* *[*[*Vertex*](#cadquery.occ_impl.shapes.Vertex) *]*)
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### isoline(param: float | int, direction: Literal['u', 'v'] = 'v') → [Edge](#cadquery.occ_impl.shapes.Edge)

Construct an isoline.

* **Parameters:**
  * **param** (*float* *|* *int*)
  * **direction** (*Literal* *[* *'u'* *,*  *'v'* *]*)
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### isolines(params: Iterable[float | int], direction: Literal['u', 'v'] = 'v') → List[[Edge](#cadquery.occ_impl.shapes.Edge)]

Construct multiple isolines.

* **Parameters:**
  * **params** (*Iterable* *[**float* *|* *int* *]*)
  * **direction** (*Literal* *[* *'u'* *,*  *'v'* *]*)
* **Return type:**
  *List*[[*Edge*](#cadquery.occ_impl.shapes.Edge)]

#### *classmethod* makeFromWires(outerWire: [Wire](#cadquery.occ_impl.shapes.Wire), innerWires: List[[Wire](#cadquery.occ_impl.shapes.Wire)] = []) → [Face](#cadquery.occ_impl.shapes.Face)

Makes a planar face from one or more wires

* **Parameters:**
  * **outerWire** ([*Wire*](#cadquery.occ_impl.shapes.Wire))
  * **innerWires** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*)
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### *classmethod* makeNSidedSurface(edges: ~typing.Iterable[~cadquery.occ_impl.shapes.Edge | ~cadquery.occ_impl.shapes.Wire], constraints: ~typing.Iterable[~cadquery.occ_impl.shapes.Edge | ~cadquery.occ_impl.shapes.Wire | ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] | ~OCP.gp.gp_Pnt], continuity: ~OCP.GeomAbs.GeomAbs_Shape = <GeomAbs_Shape.GeomAbs_C0: 0>, degree: int = 3, nbPtsOnCur: int = 15, nbIter: int = 2, anisotropy: bool = False, tol2d: float = 1e-05, tol3d: float = 0.0001, tolAng: float = 0.01, tolCurv: float = 0.1, maxDeg: int = 8, maxSegments: int = 9) → [Face](#cadquery.occ_impl.shapes.Face)

Returns a surface enclosed by a closed polygon defined by ‘edges’ and ‘constraints’.

* **Parameters:**
  * **edges** (*list* *of* *edges* *or* *wires*) – edges
  * **constraints** (*list* *of* *points* *or* *edges*) – constraints
  * **continuity** (*GeomAbs_Shape*) – OCC.Core.GeomAbs continuity condition
  * **degree** (*int*) – >=2
  * **nbPtsOnCur** (*int*) – number of points on curve >= 15
  * **nbIter** (*int*) – number of iterations >= 2
  * **anisotropy** (*bool*) – bool Anisotropy
  * **tol2d** (*float*) – 2D tolerance >0
  * **tol3d** (*float*) – 3D tolerance >0
  * **tolAng** (*float*) – angular tolerance
  * **tolCurv** (*float*) – tolerance for curvature >0
  * **maxDeg** (*int*) – highest polynomial degree >= 2
  * **maxSegments** (*int*) – greatest number of segments >= 2
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### *classmethod* makeRuledSurface(edgeOrWire1, edgeOrWire2)

makeRuledSurface(Edge|Wire,Edge|Wire) – Make a ruled surface
Create a ruled surface out of two edges or wires. If wires are used then
these must have the same number of edges

#### *classmethod* makeSplineApprox(points: List[List[[Vector](#cadquery.Vector)]], tol: float = 0.01, smoothing: Tuple[float, float, float] | None = None, minDeg: int = 1, maxDeg: int = 3) → [Face](#cadquery.occ_impl.shapes.Face)

Approximate a spline surface through the provided points.

* **Parameters:**
  * **points** (*List* *[**List* *[*[*Vector*](#cadquery.Vector) *]* *]*) – a 2D list of Vectors that represent the points
  * **tol** (*float*) – tolerance of the algorithm (consult OCC documentation).
  * **smoothing** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* *None*) – optional tuple of 3 weights use for variational smoothing (default: None)
  * **minDeg** (*int*) – minimum spline degree. Enforced only when smothing is None (default: 1)
  * **maxDeg** (*int*) – maximum spline degree (default: 6)
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### normalAt(self, locationVector: ForwardRef('Vector') | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float] | NoneType = None) → [cadquery.occ_impl.geom.Vector](#cadquery.Vector)

> Computes the normal vector at the desired location on the face.

> * **returns:**
>   a vector representing the direction
> * **param locationVector:**
>   the location to compute the normal at. If none, the center of the face is used.
> * **type locationVector:**
>   a vector that lies on the surface.

normalAt(self, u: Union[float, int], v: Union[float, int]) -> Tuple[cadquery.occ_impl.geom.Vector, cadquery.occ_impl.geom.Vector]

> Computes the normal vector at the desired location in the u,v parameter space.

> * **returns:**
>   a vector representing the normal direction and the position
> * **param u:**
>   the u parametric location to compute the normal at.
> * **param v:**
>   the v parametric location to compute the normal at.
* **Parameters:**
  **locationVector** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*  *|* *None*)
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### normals(us: Iterable[float | int], vs: Iterable[float | int]) → Tuple[List[[Vector](#cadquery.Vector)], List[[Vector](#cadquery.Vector)]]

Computes the normal vectors at the desired locations in the u,v parameter space.

* **Returns:**
  a tuple of list of vectors representing the normal directions and the positions
* **Parameters:**
  * **us** (*Iterable* *[**float* *|* *int* *]*) – the u parametric locations to compute the normal at.
  * **vs** (*Iterable* *[**float* *|* *int* *]*) – the v parametric locations to compute the normal at.
* **Return type:**
  *Tuple*[*List*[[*Vector*](#cadquery.Vector)], *List*[[*Vector*](#cadquery.Vector)]]

#### thicken(thickness: float) → [Solid](#cadquery.occ_impl.shapes.Solid)

Return a thickened face

* **Parameters:**
  **thickness** (*float*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### toArcs(tolerance: float = 0.001) → [Face](#cadquery.occ_impl.shapes.Face)

Approximate planar face with arcs and straight line segments.

* **Parameters:**
  **tolerance** (*float*) – Approximation tolerance.
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### toPln() → gp_Pln

Convert this face to a gp_Pln.

Note the Location of the resulting plane may not equal the center of this face,
however the resulting plane will still contain the center of this face.

* **Return type:**
  *gp_Pln*

#### trim(u0: float | int, u1: float | int, v0: float | int, v1: float | int, tol: float | int = 1e-06) → [Face](#cadquery.occ_impl.shapes.Face)

Trim the face in the parametric space to (u0, u1).

NB: this operation is done on the base geometry.

* **Parameters:**
  * **u0** (*float* *|* *int*)
  * **u1** (*float* *|* *int*)
  * **v0** (*float* *|* *int*)
  * **v1** (*float* *|* *int*)
  * **tol** (*float* *|* *int*)
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

### *class* cadquery.Location(t: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float])

Bases: `object`

Location in 3D space. Depending on usage can be absolute or relative.

This class wraps the TopLoc_Location class from OCCT. It can be used to move Shape
objects in both relative and absolute manner. It is the preferred type to locate objects
in CQ.

* **Parameters:**
  **t** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)

#### \_\_init_\_(self, t: ForwardRef('Vector') | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → None

Location with translation t with respect to the original location.

\_\_init_\_(self, x: Union[int, float] = 0, y: Union[int, float] = 0, z: Union[int, float] = 0, rx: Union[int, float] = 0, ry: Union[int, float] = 0, rz: Union[int, float] = 0) -> None
: Location with translation (x,y,z) and 3 rotation angles.

\_\_init_\_(self, t: cadquery.occ_impl.geom.Plane) -> None
: Location corresponding to the location of the Plane t.

\_\_init_\_(self, t: cadquery.occ_impl.geom.Plane, v: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]) -> None
: Location corresponding to the angular location of the Plane t with translation v.

\_\_init_\_(self, T: OCP.TopLoc.TopLoc_Location) -> None
: Location wrapping the low-level TopLoc_Location object t

\_\_init_\_(self, T: OCP.gp.gp_Trsf) -> None
: Location wrapping the low-level gp_Trsf object t

\_\_init_\_(self, t: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]], ax: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]], angle: Union[int, float]) -> None
: Location with translation t and rotation around ax by angle
  : with respect to the original location.

\_\_init_\_(self, t: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]], angles: Tuple[Union[int, float], Union[int, float], Union[int, float]]) -> None
: Location with translation t and 3 rotation angles.

* **Parameters:**
  **t** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Return type:**
  None

#### \_\_weakref_\_

list of weak references to the object

#### toTuple() → Tuple[Tuple[float, float, float], Tuple[float, float, float]]

Convert the location to a translation, rotation tuple.

* **Return type:**
  *Tuple*[*Tuple*[float, float, float], *Tuple*[float, float, float]]

### *class* cadquery.Matrix

### *class* cadquery.Matrix(matrix: gp_GTrsf | gp_Trsf)

### *class* cadquery.Matrix(matrix: Sequence[Sequence[float]])

Bases: `object`

A 3d , 4x4 transformation matrix.

Used to move geometry in space.

The provided “matrix” parameter may be None, a gp_GTrsf, or a nested list of
values.

If given a nested list, it is expected to be of the form:

> [[m11, m12, m13, m14],
> : [m21, m22, m23, m24],
>   [m31, m32, m33, m34]]

A fourth row may be given, but it is expected to be: [0.0, 0.0, 0.0, 1.0]
since this is a transform matrix.

#### \_\_getitem_\_(rc: Tuple[int, int]) → float

Provide Matrix[r, c] syntax for accessing individual values. The row
and column parameters start at zero, which is consistent with most
python libraries, but is counter to gp_GTrsf(), which is 1-indexed.

* **Parameters:**
  **rc** (*Tuple* *[**int* *,* *int* *]*)
* **Return type:**
  float

#### \_\_init_\_(matrix=None)

#### \_\_repr_\_() → str

Generate a valid python expression representing this Matrix

* **Return type:**
  str

#### \_\_weakref_\_

list of weak references to the object

#### transposed_list() → Sequence[float]

Needed by the cqparts gltf exporter

* **Return type:**
  *Sequence*[float]

### *class* cadquery.NearestToPointSelector(pnt)

Bases: [`Selector`](#cadquery.selectors.Selector)

Selects object nearest the provided point.

If the object is a vertex or point, the distance
is used. For other kinds of shapes, the center of mass
is used to to compute which is closest.

Applicability: All Types of Shapes

Example:

```default
CQ(aCube).vertices(NearestToPointSelector((0, 1, 0)))
```

returns the vertex of the unit cube closest to the point x=0,y=1,z=0

#### \_\_init_\_(pnt)

#### filter(objectList: Sequence[Shape])

Filter the provided list.

The default implementation returns the original list unfiltered.

* **Parameters:**
  **objectList** (*list* *of* *OCCT primitives*) – list to filter
* **Returns:**
  filtered list

### *class* cadquery.ParallelDirSelector(vector: [Vector](#cadquery.Vector), tolerance: float = 0.0001)

Bases: [`BaseDirSelector`](#cadquery.selectors.BaseDirSelector)

Selects objects parallel with the provided direction.

Applicability:
: Linear Edges
  Planar Faces

Use the string syntax shortcut |(X|Y|Z) if you want to select based on a cardinal direction.

Example:

```default
CQ(aCube).faces(ParallelDirSelector((0, 0, 1)))
```

selects faces with the normal parallel to the z direction, and is equivalent to:

```default
CQ(aCube).faces("|Z")
```

* **Parameters:**
  * **vector** ([*Vector*](#cadquery.Vector))
  * **tolerance** (*float*)

#### test(vec: [Vector](#cadquery.Vector)) → bool

Test a specified vector. Subclasses override to provide other implementations

* **Parameters:**
  **vec** ([*Vector*](#cadquery.Vector))
* **Return type:**
  bool

### *class* cadquery.PerpendicularDirSelector(vector: [Vector](#cadquery.Vector), tolerance: float = 0.0001)

Bases: [`BaseDirSelector`](#cadquery.selectors.BaseDirSelector)

Selects objects perpendicular with the provided direction.

Applicability:
: Linear Edges
  Planar Faces

Use the string syntax shortcut #(X|Y|Z) if you want to select based on a
cardinal direction.

Example:

```default
CQ(aCube).faces(PerpendicularDirSelector((0, 0, 1)))
```

selects faces with the normal perpendicular to the z direction, and is equivalent to:

```default
CQ(aCube).faces("#Z")
```

* **Parameters:**
  * **vector** ([*Vector*](#cadquery.Vector))
  * **tolerance** (*float*)

#### test(vec: [Vector](#cadquery.Vector)) → bool

Test a specified vector. Subclasses override to provide other implementations

* **Parameters:**
  **vec** ([*Vector*](#cadquery.Vector))
* **Return type:**
  bool

### *class* cadquery.Plane(origin: Tuple[float, float, float] | [Vector](#cadquery.Vector), xDir: Tuple[float, float, float] | [Vector](#cadquery.Vector) | None = None, normal: Tuple[float, float, float] | [Vector](#cadquery.Vector) = (0, 0, 1))

Bases: `object`

A 2D coordinate system in space

A 2D coordinate system in space, with the x-y axes on the plane, and a
particular point as the origin.

A plane allows the use of 2D coordinates, which are later converted to
global, 3d coordinates when the operations are complete.

Frequently, it is not necessary to create work planes, as they can be
created automatically from faces.

* **Parameters:**
  * **origin** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector))
  * **xDir** ([*Vector*](#cadquery.Vector))
  * **normal** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector))

#### \_\_eq_\_(other)

Return self==value.

#### \_\_hash_\_ *= None*

#### \_\_init_\_(origin: Tuple[float, float, float] | [Vector](#cadquery.Vector), xDir: Tuple[float, float, float] | [Vector](#cadquery.Vector) | None = None, normal: Tuple[float, float, float] | [Vector](#cadquery.Vector) = (0, 0, 1))

Create a Plane with an arbitrary orientation

* **Parameters:**
  * **origin** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector)) – the origin in global coordinates
  * **xDir** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *|* *None*) – an optional vector representing the xDirection.
  * **normal** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector)) – the normal direction for the plane
* **Raises:**
  **ValueError** – if the specified xDir is not orthogonal to the provided normal

#### \_\_ne_\_(other)

Return self!=value.

#### \_\_repr_\_()

Return repr(self).

#### \_\_weakref_\_

list of weak references to the object

#### *classmethod* named(stdName: str, origin=(0, 0, 0)) → [Plane](#cadquery.Plane)

Create a predefined Plane based on the conventional names.

* **Parameters:**
  * **stdName** (*string*) – one of (XY|YZ|ZX|XZ|YX|ZY|front|back|left|right|top|bottom)
  * **origin** (*3-tuple* *of* *the origin* *of* *the new plane* *,* *in global coordinates.*) – the desired origin, specified in global coordinates
* **Return type:**
  [*Plane*](#cadquery.Plane)

Available named planes are as follows. Direction references refer to
the global directions.

| Name   | xDir   | yDir   | zDir   |
|--------|--------|--------|--------|
| XY     | +x     | +y     | +z     |
| YZ     | +y     | +z     | +x     |
| ZX     | +z     | +x     | +y     |
| XZ     | +x     | +z     | -y     |
| YX     | +y     | +x     | -z     |
| ZY     | +z     | +y     | -x     |
| front  | +x     | +y     | +z     |
| back   | -x     | +y     | -z     |
| left   | +z     | +y     | -x     |
| right  | -z     | +y     | +x     |
| top    | +x     | -z     | +y     |
| bottom | +x     | +z     | -y     |

#### rotated(rotate=(0, 0, 0))

Returns a copy of this plane, rotated about the specified axes

Since the z axis is always normal the plane, rotating around Z will
always produce a plane that is parallel to this one.

The origin of the workplane is unaffected by the rotation.

Rotations are done in order x, y, z. If you need a different order,
manually chain together multiple rotate() commands.

* **Parameters:**
  **rotate** – Vector [xDegrees, yDegrees, zDegrees]
* **Returns:**
  a copy of this plane rotated as requested.

#### setOrigin2d(x, y)

Set a new origin in the plane itself

Set a new origin in the plane itself. The plane’s orientation and
xDrection are unaffected.

* **Parameters:**
  * **x** (*float*) – offset in the x direction
  * **y** (*float*) – offset in the y direction
* **Returns:**
  void

The new coordinates are specified in terms of the current 2D system.
As an example:

p = Plane.XY()
p.setOrigin2d(2, 2)
p.setOrigin2d(2, 2)

results in a plane with its origin at (x, y) = (4, 4) in global
coordinates. Both operations were relative to local coordinates of the
plane.

#### toLocalCoords(obj)

Project the provided coordinates onto this plane

* **Parameters:**
  **obj** – an object or vector to convert
* **Returns:**
  an object of the same type, but converted to local coordinates

Most of the time, the z-coordinate returned will be zero, because most
operations based on a plane are all 2D. Occasionally, though, 3D
points outside of the current plane are transformed. One such example is
[`Workplane.box()`](#cadquery.Workplane.box), where 3D corners of a box are transformed to
orient the box in space correctly.

#### toWorldCoords(tuplePoint) → [Vector](#cadquery.Vector)

Convert a point in local coordinates to global coordinates

* **Parameters:**
  **tuplePoint** (*a 2* *or* *three tuple* *of* *float. The third value is taken to be zero if not supplied.*) – point in local coordinates to convert.
* **Returns:**
  a Vector in global coordinates
* **Return type:**
  [*Vector*](#cadquery.Vector)

### *class* cadquery.Selector

Bases: `object`

Filters a list of objects.

Filters must provide a single method that filters objects.

#### \_\_weakref_\_

list of weak references to the object

#### filter(objectList: Sequence[Shape]) → List[Shape]

Filter the provided list.

The default implementation returns the original list unfiltered.

* **Parameters:**
  **objectList** (*list* *of* *OCCT primitives*) – list to filter
* **Returns:**
  filtered list
* **Return type:**
  *List*[*Shape*]

### *class* cadquery.Shape(obj: TopoDS_Shape)

Bases: `object`

Represents a shape in the system. Wraps TopoDS_Shape.

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### Area() → float

* **Returns:**
  The surface area of all faces in this Shape
* **Return type:**
  float

#### BoundingBox(tolerance: float | None = None) → [BoundBox](#cadquery.BoundBox)

Create a bounding box for this Shape.

* **Parameters:**
  **tolerance** (*float* *|* *None*) – Tolerance value passed to [`BoundBox`](#cadquery.BoundBox)
* **Returns:**
  A [`BoundBox`](#cadquery.BoundBox) object for this Shape
* **Return type:**
  [*BoundBox*](#cadquery.BoundBox)

#### Center() → [Vector](#cadquery.Vector)

* **Returns:**
  The point of the center of mass of this Shape
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### CenterOfBoundBox(tolerance: float | None = None) → [Vector](#cadquery.Vector)

* **Parameters:**
  **tolerance** (*float* *|* *None*) – Tolerance passed to the [`BoundingBox()`](#cadquery.Shape.BoundingBox) method
* **Returns:**
  Center of the bounding box of this shape
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### Closed() → bool

* **Returns:**
  The closedness flag
* **Return type:**
  bool

#### *static* CombinedCenter(objects: Iterable[[Shape](#cadquery.occ_impl.shapes.Shape)]) → [Vector](#cadquery.Vector)

Calculates the center of mass of multiple objects.

* **Parameters:**
  **objects** (*Iterable* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *]*) – A list of objects with mass
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### *static* CombinedCenterOfBoundBox(objects: List[[Shape](#cadquery.occ_impl.shapes.Shape)]) → [Vector](#cadquery.Vector)

Calculates the center of a bounding box of multiple objects.

* **Parameters:**
  **objects** (*List* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *]*) – A list of objects
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### CompSolids() → List[[CompSolid](#cadquery.occ_impl.shapes.CompSolid)]

* **Returns:**
  All the compsolids in this Shape
* **Return type:**
  *List*[[*CompSolid*](#cadquery.occ_impl.shapes.CompSolid)]

#### Compounds() → List[[Compound](#cadquery.occ_impl.shapes.Compound)]

* **Returns:**
  All the compounds in this Shape
* **Return type:**
  *List*[[*Compound*](#cadquery.occ_impl.shapes.Compound)]

#### Edges() → List[[Edge](#cadquery.occ_impl.shapes.Edge)]

* **Returns:**
  All the edges in this Shape
* **Return type:**
  *List*[[*Edge*](#cadquery.occ_impl.shapes.Edge)]

#### Faces() → List[[Face](#cadquery.occ_impl.shapes.Face)]

* **Returns:**
  All the faces in this Shape
* **Return type:**
  *List*[[*Face*](#cadquery.occ_impl.shapes.Face)]

#### Shells() → List[[Shell](#cadquery.occ_impl.shapes.Shell)]

* **Returns:**
  All the shells in this Shape
* **Return type:**
  *List*[[*Shell*](#cadquery.occ_impl.shapes.Shell)]

#### Solids() → List[[Solid](#cadquery.occ_impl.shapes.Solid)]

* **Returns:**
  All the solids in this Shape
* **Return type:**
  *List*[[*Solid*](#cadquery.occ_impl.shapes.Solid)]

#### Vertices() → List[[Vertex](#cadquery.occ_impl.shapes.Vertex)]

* **Returns:**
  All the vertices in this Shape
* **Return type:**
  *List*[[*Vertex*](#cadquery.occ_impl.shapes.Vertex)]

#### Volume() → float

* **Returns:**
  The volume of this Shape
* **Return type:**
  float

#### Wires() → List[[Wire](#cadquery.occ_impl.shapes.Wire)]

* **Returns:**
  All the wires in this Shape
* **Return type:**
  *List*[[*Wire*](#cadquery.occ_impl.shapes.Wire)]

#### \_\_add_\_(other: [Shape](#cadquery.occ_impl.shapes.Shape)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Fuse self and other.

* **Parameters:**
  **other** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### \_\_eq_\_(other) → bool

Return self==value.

* **Return type:**
  bool

#### \_\_hash_\_() → int

Return hash(self).

* **Return type:**
  int

#### \_\_init_\_(obj: TopoDS_Shape)

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### \_\_iter_\_() → Iterator[[Shape](#cadquery.occ_impl.shapes.Shape)]

Iterate over subshapes.

* **Return type:**
  *Iterator*[[*Shape*](#cadquery.occ_impl.shapes.Shape)]

#### \_\_mul_\_(other: [Shape](#cadquery.occ_impl.shapes.Shape)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Intersect self and other.

* **Parameters:**
  **other** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### \_\_sub_\_(other: [Shape](#cadquery.occ_impl.shapes.Shape)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Subtract other from self.

* **Parameters:**
  **other** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### \_\_truediv_\_(other: [Shape](#cadquery.occ_impl.shapes.Shape)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Split self with other.

* **Parameters:**
  **other** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### \_\_weakref_\_

list of weak references to the object

#### ancestors(shape: [Shape](#cadquery.occ_impl.shapes.Shape), kind: Literal['Vertex', 'Edge', 'Wire', 'Face', 'Shell', 'Solid', 'CompSolid', 'Compound']) → [Compound](#cadquery.occ_impl.shapes.Compound)

Iterate over ancestors, i.e. shapes of same kind within shape that contain self.

* **Parameters:**
  * **shape** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **kind** (*Literal* *[* *'Vertex'* *,*  *'Edge'* *,*  *'Wire'* *,*  *'Face'* *,*  *'Shell'* *,*  *'Solid'* *,*  *'CompSolid'* *,*  *'Compound'* *]*)
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### *classmethod* cast(obj: TopoDS_Shape, forConstruction: bool = False) → [Shape](#cadquery.occ_impl.shapes.Shape)

Returns the right type of wrapper, given a OCCT object

* **Parameters:**
  * **obj** (*TopoDS_Shape*)
  * **forConstruction** (*bool*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### *static* centerOfMass(obj: [Shape](#cadquery.occ_impl.shapes.Shape)) → [Vector](#cadquery.Vector)

Calculates the center of ‘mass’ of an object.

* **Parameters:**
  **obj** ([*Shape*](#cadquery.occ_impl.shapes.Shape)) – Compute the center of mass of this object
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### clean() → T

Experimental clean using ShapeUpgrade

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### *static* computeMass(obj: [Shape](#cadquery.occ_impl.shapes.Shape)) → float

Calculates the ‘mass’ of an object.

* **Parameters:**
  **obj** ([*Shape*](#cadquery.occ_impl.shapes.Shape)) – Compute the mass of this object
* **Return type:**
  float

#### copy(mesh: bool = False) → T

Creates a new object that is a copy of this object.

* **Parameters:**
  * **self** (*T*)
  * **mesh** (*bool*) – should I copy the triangulation too (default: False)
* **Returns:**
  a copy of the object
* **Return type:**
  *T*

#### cut(\*toCut: [Shape](#cadquery.occ_impl.shapes.Shape), tol: float | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Remove the positional arguments from this Shape.

* **Parameters:**
  * **tol** (*float* *|* *None*) – Fuzzy mode tolerance
  * **toCut** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### distance(other: [Shape](#cadquery.occ_impl.shapes.Shape)) → float

Minimal distance between two shapes

* **Parameters:**
  **other** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  float

#### distances(\*others: [Shape](#cadquery.occ_impl.shapes.Shape)) → Iterator[float]

Minimal distances to between self and other shapes

* **Parameters:**
  **others** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  *Iterator*[float]

#### edges(selector: [Selector](#cadquery.selectors.Selector) | str | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Select edges.

* **Parameters:**
  **selector** ([*Selector*](#cadquery.selectors.Selector) *|* *str* *|* *None*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### export(fname: str, tolerance: float = 0.1, angularTolerance: float = 0.1, opt: Dict[str, Any] | None = None)

Export Shape to file.

* **Parameters:**
  * **self** (*T*)
  * **fname** (*str*)
  * **tolerance** (*float*)
  * **angularTolerance** (*float*)
  * **opt** (*Dict* *[**str* *,* *Any* *]*  *|* *None*)

#### exportBin(f: str | BytesIO) → bool

Export this shape to a binary BREP file.

* **Parameters:**
  **f** (*str* *|* *BytesIO*)
* **Return type:**
  bool

#### exportBrep(f: str | BytesIO) → bool

Export this shape to a BREP file

* **Parameters:**
  **f** (*str* *|* *BytesIO*)
* **Return type:**
  bool

#### exportStep(fileName: str, \*\*kwargs) → IFSelect_ReturnStatus

Export this shape to a STEP file.

kwargs is used to provide optional keyword arguments to configure the exporter.

* **Parameters:**
  * **fileName** (*str*) – Path and filename for writing.
  * **write_pcurves** (*bool*) – 

    Enable or disable writing parametric curves to the STEP file. Default True.

    If False, writes STEP file without pcurves. This decreases the size of the resulting STEP file.
  * **precision_mode** (*int*) – Controls the uncertainty value for STEP entities. Specify -1, 0, or 1. Default 0.
    See OCCT documentation.
* **Return type:**
  *IFSelect_ReturnStatus*

#### exportStl(fileName: str, tolerance: float = 0.001, angularTolerance: float = 0.1, ascii: bool = False, relative: bool = True, parallel: bool = True) → bool

Exports a shape to a specified STL file.

* **Parameters:**
  * **fileName** (*str*) – The path and file name to write the STL output to.
  * **tolerance** (*float*) – A linear deflection setting which limits the distance between a curve and its tessellation.
    Setting this value too low will result in large meshes that can consume computing resources.
    Setting the value too high can result in meshes with a level of detail that is too low.
    Default is 1e-3, which is a good starting point for a range of cases.
  * **angularTolerance** (*float*) – Angular deflection setting which limits the angle between subsequent segments in a polyline. Default is 0.1.
  * **ascii** (*bool*) – Export the file as ASCII (True) or binary (False) STL format.  Default is binary.
  * **relative** (*bool*) – If True, tolerance will be scaled by the size of the edge being meshed. Default is True.
    Setting this value to True may cause large features to become faceted, or small features dense.
  * **parallel** (*bool*) – If True, OCCT will use parallel processing to mesh the shape. Default is True.
* **Return type:**
  bool

#### faces(selector: [Selector](#cadquery.selectors.Selector) | str | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Select faces.

* **Parameters:**
  **selector** ([*Selector*](#cadquery.selectors.Selector) *|* *str* *|* *None*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### facesIntersectedByLine(point: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], axis: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], tol: float = 0.0001, direction: Literal['AlongAxis', 'Opposite'] | None = None)

Computes the intersections between the provided line and the faces of this Shape

* **Parameters:**
  * **point** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – Base point for defining a line
  * **axis** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – Axis on which the line rests
  * **tol** (*float*) – Intersection tolerance
  * **direction** (*Literal* *[* *'AlongAxis'* *,*  *'Opposite'* *]*  *|* *None*) – Valid values: “AlongAxis”, “Opposite”;
    If specified, will ignore all faces that are not in the specified direction
    including the face where the point lies if it is the case
* **Returns:**
  A list of intersected faces sorted by distance from point

#### fix() → T

Try to fix shape if not valid

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### fuse(\*toFuse: [Shape](#cadquery.occ_impl.shapes.Shape), glue: bool = False, tol: float | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Fuse the positional arguments with this Shape.

* **Parameters:**
  * **glue** (*bool*) – Sets the glue option for the algorithm, which allows
    increasing performance of the intersection of the input shapes
  * **tol** (*float* *|* *None*) – Fuzzy mode tolerance
  * **toFuse** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### geomType() → Literal['Vertex', 'Wire', 'Shell', 'Solid', 'Compound', 'PLANE', 'CYLINDER', 'CONE', 'SPHERE', 'TORUS', 'BEZIER', 'BSPLINE', 'REVOLUTION', 'EXTRUSION', 'OFFSET', 'OTHER', 'LINE', 'CIRCLE', 'ELLIPSE', 'HYPERBOLA', 'PARABOLA']

Gets the underlying geometry type.

Implementations can return any values desired, but the values the user
uses in type filters should correspond to these.

As an example, if a user does:

```default
CQ(object).faces("%mytype")
```

The expectation is that the geomType attribute will return ‘mytype’

The return values depend on the type of the shape:

Vertex:  always ‘Vertex’
<br/>
Edge:   LINE, CIRCLE, ELLIPSE, HYPERBOLA, PARABOLA, BEZIER,
<br/>
BSPLINE, OFFSET, OTHER
<br/>
Face:   PLANE, CYLINDER, CONE, SPHERE, TORUS, BEZIER, BSPLINE,
<br/>
REVOLUTION, EXTRUSION, OFFSET, OTHER
<br/>
Solid:  ‘Solid’
<br/>
Shell:  ‘Shell’
<br/>
Compound: ‘Compound’
<br/>
Wire:   ‘Wire’
<br/>
* **Returns:**
  A string according to the geometry type
* **Return type:**
  *Literal*[‘Vertex’, ‘Wire’, ‘Shell’, ‘Solid’, ‘Compound’, ‘PLANE’, ‘CYLINDER’, ‘CONE’, ‘SPHERE’, ‘TORUS’, ‘BEZIER’, ‘BSPLINE’, ‘REVOLUTION’, ‘EXTRUSION’, ‘OFFSET’, ‘OTHER’, ‘LINE’, ‘CIRCLE’, ‘ELLIPSE’, ‘HYPERBOLA’, ‘PARABOLA’]

#### hashCode() → int

Returns a hashed value denoting this shape. It is computed from the
TShape and the Location. The Orientation is not used.

* **Return type:**
  int

#### *classmethod* importBin(f: str | BytesIO) → [Shape](#cadquery.occ_impl.shapes.Shape)

Import shape from a binary BREP file.

* **Parameters:**
  **f** (*str* *|* *BytesIO*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### *classmethod* importBrep(f: str | BytesIO) → [Shape](#cadquery.occ_impl.shapes.Shape)

Import shape from a BREP file

* **Parameters:**
  **f** (*str* *|* *BytesIO*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### intersect(\*toIntersect: [Shape](#cadquery.occ_impl.shapes.Shape), tol: float | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Intersection of the positional arguments and this Shape.

* **Parameters:**
  * **tol** (*float* *|* *None*) – Fuzzy mode tolerance
  * **toIntersect** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### isEqual(other: [Shape](#cadquery.occ_impl.shapes.Shape)) → bool

Returns True if two shapes are equal, i.e. if they share the same
TShape with the same Locations and Orientations. Also see
[`isSame()`](#cadquery.Shape.isSame).

* **Parameters:**
  **other** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  bool

#### isNull() → bool

Returns true if this shape is null. In other words, it references no
underlying shape with the potential to be given a location and an
orientation.

* **Return type:**
  bool

#### isSame(other: [Shape](#cadquery.occ_impl.shapes.Shape)) → bool

Returns True if other and this shape are same, i.e. if they share the
same TShape with the same Locations. Orientations may differ. Also see
[`isEqual()`](#cadquery.Shape.isEqual)

* **Parameters:**
  **other** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  bool

#### isValid() → bool

Returns True if no defect is detected on the shape S or any of its
subshapes. See the OCCT docs on BRepCheck_Analyzer::IsValid for a full
description of what is checked.

* **Return type:**
  bool

#### locate(loc: [Location](#cadquery.Location)) → T

Apply a location in absolute sense to self.

* **Parameters:**
  * **self** (*T*)
  * **loc** ([*Location*](#cadquery.Location))
* **Return type:**
  *T*

#### located(loc: [Location](#cadquery.Location)) → T

Apply a location in absolute sense to a copy of self.

* **Parameters:**
  * **self** (*T*)
  * **loc** ([*Location*](#cadquery.Location))
* **Return type:**
  *T*

#### location() → [Location](#cadquery.Location)

Return the current location

* **Return type:**
  [*Location*](#cadquery.Location)

#### *static* matrixOfInertia(obj: [Shape](#cadquery.occ_impl.shapes.Shape)) → List[List[float]]

Calculates the matrix of inertia of an object.
Since the part’s density is unknown, this result is inertia/density with units of [1/length].
:param obj: Compute the matrix of inertia of this object

* **Parameters:**
  **obj** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  *List*[*List*[float]]

#### mesh(tolerance: float, angularTolerance: float = 0.1)

Generate triangulation if none exists.

* **Parameters:**
  * **tolerance** (*float*)
  * **angularTolerance** (*float*)

#### mirror(mirrorPlane: Literal['XY', 'YX', 'XZ', 'ZX', 'YZ', 'ZY'] | [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float] = 'XY', basePointVector: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float] = (0, 0, 0)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Applies a mirror transform to this Shape. Does not duplicate objects
about the plane.

* **Parameters:**
  * **mirrorPlane** (*Literal* *[* *'XY'* *,*  *'YX'* *,*  *'XZ'* *,*  *'ZX'* *,*  *'YZ'* *,*  *'ZY'* *]*  *|*  *~cadquery.occ_impl.geom.Vector* *|*  *~typing.Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|*  *~typing.Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – The direction of the plane to mirror about - one of
    ‘XY’, ‘XZ’ or ‘YZ’
  * **basePointVector** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – The origin of the plane to mirror about
* **Returns:**
  The mirrored shape
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### move(self: T, loc: [cadquery.occ_impl.geom.Location](#cadquery.Location)) → T

> Apply a location in relative sense (i.e. update current location) to self.

move(self: ~T, x: Union[float, int] = 0, y: Union[float, int] = 0, z: Union[float, int] = 0, rx: Union[float, int] = 0, ry: Union[float, int] = 0, rz: Union[float, int] = 0) -> ~T

> Apply translation and rotation in relative sense (i.e. update current location) to self.

move(self: ~T, loc: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]) -> ~T

> Apply a VectorLike in relative sense (i.e. update current location) to self.
* **Parameters:**
  * **self** (*T*)
  * **loc** ([*Location*](#cadquery.Location))
* **Return type:**
  *T*

#### moved(self: T, loc: [cadquery.occ_impl.geom.Location](#cadquery.Location)) → T

> Apply a location in relative sense (i.e. update current location) to a copy of self.

moved(self: ~T, loc1: cadquery.occ_impl.geom.Location, loc2: cadquery.occ_impl.geom.Location, 

```
*
```

locs: cadquery.occ_impl.geom.Location) -> ~T

> Apply multiple locations.

moved(self: ~T, locs: Sequence[cadquery.occ_impl.geom.Location]) -> ~T

> Apply multiple locations.

moved(self: ~T, x: Union[float, int] = 0, y: Union[float, int] = 0, z: Union[float, int] = 0, rx: Union[float, int] = 0, ry: Union[float, int] = 0, rz: Union[float, int] = 0) -> ~T

> Apply translation and rotation in relative sense to a copy of self.

moved(self: ~T, loc: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]) -> ~T

> Apply a VectorLike in relative sense to a copy of self.

moved(self: ~T, loc1: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]], loc2: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]], 

```
*
```

locs: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]) -> ~T

> Apply multiple VectorLikes in relative sense to a copy of self.

moved(self: ~T, loc: Sequence[Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]]) -> ~T

> Apply multiple VectorLikes in relative sense to a copy of self.
* **Parameters:**
  * **self** (*T*)
  * **loc** ([*Location*](#cadquery.Location))
* **Return type:**
  *T*

#### rotate(startVector: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], endVector: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], angleDegrees: float) → T

Rotates a shape around an axis.

* **Parameters:**
  * **self** (*T*)
  * **startVector** (*either a 3-tuple* *or* *a Vector*) – start point of rotation axis
  * **endVector** (*either a 3-tuple* *or* *a Vector*) – end point of rotation axis
  * **angleDegrees** (*float*) – angle to rotate, in degrees
* **Returns:**
  a copy of the shape, rotated
* **Return type:**
  *T*

#### scale(factor: float) → [Shape](#cadquery.occ_impl.shapes.Shape)

Scales this shape through a transformation.

* **Parameters:**
  **factor** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### shells(selector: [Selector](#cadquery.selectors.Selector) | str | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Select shells.

* **Parameters:**
  **selector** ([*Selector*](#cadquery.selectors.Selector) *|* *str* *|* *None*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### siblings(shape: [Shape](#cadquery.occ_impl.shapes.Shape), kind: Literal['Vertex', 'Edge', 'Wire', 'Face', 'Shell', 'Solid', 'CompSolid', 'Compound'], level: int = 1) → [Compound](#cadquery.occ_impl.shapes.Compound)

Iterate over siblings, i.e. shapes within shape that share subshapes of kind with self.

* **Parameters:**
  * **shape** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **kind** (*Literal* *[* *'Vertex'* *,*  *'Edge'* *,*  *'Wire'* *,*  *'Face'* *,*  *'Shell'* *,*  *'Solid'* *,*  *'CompSolid'* *,*  *'Compound'* *]*)
  * **level** (*int*)
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### solids(selector: [Selector](#cadquery.selectors.Selector) | str | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Select solids.

* **Parameters:**
  **selector** ([*Selector*](#cadquery.selectors.Selector) *|* *str* *|* *None*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### split(\*splitters: [Shape](#cadquery.occ_impl.shapes.Shape)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Split this shape with the positional arguments.

* **Parameters:**
  **splitters** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### toSplines(degree: int = 3, tolerance: float = 0.001, nurbs: bool = False) → T

Approximate shape with b-splines of the specified degree.

* **Parameters:**
  * **self** (*T*)
  * **degree** (*int*) – Maximum degree.
  * **tolerance** (*float*) – Approximation tolerance.
  * **nurbs** (*bool*) – Use rational splines.
* **Return type:**
  *T*

#### toVtkPolyData(tolerance: float | None = None, angularTolerance: float | None = None, normals: bool = False) → vtkPolyData

Convert shape to vtkPolyData

* **Parameters:**
  * **tolerance** (*float* *|* *None*)
  * **angularTolerance** (*float* *|* *None*)
  * **normals** (*bool*)
* **Return type:**
  *vtkPolyData*

#### transformGeometry(tMatrix: [Matrix](#cadquery.Matrix)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Transforms this shape by tMatrix.

WARNING: transformGeometry will sometimes convert lines and circles to
splines, but it also has the ability to handle skew and stretching
transformations.

If your transformation is only translation and rotation, it is safer to
use [`transformShape()`](#cadquery.Shape.transformShape), which doesn’t change the underlying type
of the geometry, but cannot handle skew transformations.

* **Parameters:**
  **tMatrix** ([*Matrix*](#cadquery.Matrix)) – The transformation matrix
* **Returns:**
  a copy of the object, but with geometry transformed instead
  of just rotated.
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### transformShape(tMatrix: [Matrix](#cadquery.Matrix)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Transforms this Shape by tMatrix. Also see [`transformGeometry()`](#cadquery.Shape.transformGeometry).

* **Parameters:**
  **tMatrix** ([*Matrix*](#cadquery.Matrix)) – The transformation matrix
* **Returns:**
  a copy of the object, transformed by the provided matrix,
  with all objects keeping their type
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### translate(vector: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → T

Translates this shape through a transformation.

* **Parameters:**
  * **self** (*T*)
  * **vector** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Return type:**
  *T*

#### vertices(selector: [Selector](#cadquery.selectors.Selector) | str | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Select vertices.

* **Parameters:**
  **selector** ([*Selector*](#cadquery.selectors.Selector) *|* *str* *|* *None*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### wires(selector: [Selector](#cadquery.selectors.Selector) | str | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Select wires.

* **Parameters:**
  **selector** ([*Selector*](#cadquery.selectors.Selector) *|* *str* *|* *None*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### *class* cadquery.Shell(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape)

the outer boundary of a surface

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### *classmethod* makeShell(listOfFaces: Iterable[[Face](#cadquery.occ_impl.shapes.Face)]) → [Shell](#cadquery.occ_impl.shapes.Shell)

Makes a shell from faces.

* **Parameters:**
  **listOfFaces** (*Iterable* *[*[*Face*](#cadquery.occ_impl.shapes.Face) *]*)
* **Return type:**
  [*Shell*](#cadquery.occ_impl.shapes.Shell)

### *class* cadquery.Sketch(parent: ~typing.Any = None, locs: ~typing.Iterable[~cadquery.occ_impl.geom.Location] = (<cadquery.occ_impl.geom.Location object>, ), obj: ~cadquery.occ_impl.shapes.Compound | None = None)

Bases: `object`

2D sketch. Supports faces, edges and edges with constraints based construction.

* **Parameters:**
  * **parent** (*Any*)
  * **locs** (*List* *[*[*Location*](#cadquery.Location) *]*)
  * **obj** ([*Compound*](#cadquery.occ_impl.shapes.Compound) *|* *None*)

#### \_\_add_\_(other: [Sketch](#cadquery.Sketch)) → T

Fuse self and other.

* **Parameters:**
  * **self** (*T*)
  * **other** ([*Sketch*](#cadquery.Sketch))
* **Return type:**
  *T*

#### \_\_init_\_(parent: ~typing.Any = None, locs: ~typing.Iterable[~cadquery.occ_impl.geom.Location] = (<cadquery.occ_impl.geom.Location object>, ), obj: ~cadquery.occ_impl.shapes.Compound | None = None)

Construct an empty sketch.

* **Parameters:**
  * **self** (*T*)
  * **parent** (*Any*)
  * **locs** (*Iterable* *[*[*Location*](#cadquery.Location) *]*)
  * **obj** ([*Compound*](#cadquery.occ_impl.shapes.Compound) *|* *None*)

#### \_\_iter_\_() → Iterator[[Face](#cadquery.occ_impl.shapes.Face)]

Iterate over faces-locations combinations. If not faces are present
iterate over edges:

* **Return type:**
  *Iterator*[[*Face*](#cadquery.occ_impl.shapes.Face)]

#### \_\_mul_\_(other: [Sketch](#cadquery.Sketch)) → T

Intersect self and other.

* **Parameters:**
  * **self** (*T*)
  * **other** ([*Sketch*](#cadquery.Sketch))
* **Return type:**
  *T*

#### \_\_sub_\_(other: [Sketch](#cadquery.Sketch)) → T

Subtract other from self.

* **Parameters:**
  * **self** (*T*)
  * **other** ([*Sketch*](#cadquery.Sketch))
* **Return type:**
  *T*

#### \_\_truediv_\_(other: [Sketch](#cadquery.Sketch)) → T

Split self with other.

* **Parameters:**
  * **self** (*T*)
  * **other** ([*Sketch*](#cadquery.Sketch))
* **Return type:**
  *T*

#### \_\_weakref_\_

list of weak references to the object

#### add() → T

Add selection to the underlying faces.

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### apply(f: Callable[[Iterable[[Shape](#cadquery.occ_impl.shapes.Shape) | [Location](#cadquery.Location)]], Iterable[[Shape](#cadquery.occ_impl.shapes.Shape) | [Location](#cadquery.Location)]])

Apply a callable to all items at once.

* **Parameters:**
  * **self** (*T*)
  * **f** (*Callable* *[* *[**Iterable* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Location*](#cadquery.Location) *]* *]* *,* *Iterable* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Location*](#cadquery.Location) *]* *]*) – Callable to be applied.
* **Returns:**
  Sketch object with f applied to all items.

#### arc(self: T, p1: [cadquery.occ_impl.geom.Vector](#cadquery.Vector) | Tuple[int | float, int | float], p2: [cadquery.occ_impl.geom.Vector](#cadquery.Vector) | Tuple[int | float, int | float], p3: [cadquery.occ_impl.geom.Vector](#cadquery.Vector) | Tuple[int | float, int | float], tag: str | None = None, forConstruction: bool = False) → T

Construct an arc.

* **Parameters:**
  * **self** (*T*)
  * **p1** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*)
  * **p2** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*)
  * **p3** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*)
  * **tag** (*str* *|* *None*)
  * **forConstruction** (*bool*)
* **Return type:**
  *T*

#### assemble(mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None) → T

Assemble edges into faces.

* **Parameters:**
  * **self** (*T*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### bezier(pts: Iterable[[Vector](#cadquery.Vector) | Tuple[int | float, int | float]], tag: str | None = None, forConstruction: bool = False) → T

Construct an bezier curve.

The edge will pass through the last points, and the inner points
are bezier control points.

* **Parameters:**
  * **self** (*T*)
  * **pts** (*Iterable* *[*[*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]* *]*)
  * **tag** (*str* *|* *None*)
  * **forConstruction** (*bool*)
* **Return type:**
  *T*

#### chamfer(d: int | float) → T

Add a chamfer based on current selection.

* **Parameters:**
  * **self** (*T*)
  * **d** (*int* *|* *float*)
* **Return type:**
  *T*

#### circle(r: int | float, mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None) → T

Construct a circular face.

* **Parameters:**
  * **self** (*T*)
  * **r** (*int* *|* *float*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### clean() → T

Remove internal wires.

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### close(tag: str | None = None) → T

Connect last edge to the first one.

* **Parameters:**
  * **self** (*T*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### constrain(self: T, tag: str, constraint: Literal['Fixed', 'FixedPoint', 'Coincident', 'Angle', 'Length', 'Distance', 'Radius', 'Orientation', 'ArcAngle'], arg: Any) → T

Add a constraint.

* **Parameters:**
  * **self** (*T*)
  * **tag** (*str*)
  * **constraint** (*Literal* *[* *'Fixed'* *,*  *'FixedPoint'* *,*  *'Coincident'* *,*  *'Angle'* *,*  *'Length'* *,*  *'Distance'* *,*  *'Radius'* *,*  *'Orientation'* *,*  *'ArcAngle'* *]*)
  * **arg** (*Any*)
* **Return type:**
  *T*

#### copy() → T

Create a partial copy of the sketch.

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### delete() → T

Delete selected object.

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### distribute(n: int, start: int | float = 0, stop: int | float = 1, rotate: bool = True) → T

Distribute locations along selected edges or wires.

* **Parameters:**
  * **self** (*T*)
  * **n** (*int*)
  * **start** (*int* *|* *float*)
  * **stop** (*int* *|* *float*)
  * **rotate** (*bool*)
* **Return type:**
  *T*

#### each(callback: Callable[[[Location](#cadquery.Location)], [Face](#cadquery.occ_impl.shapes.Face) | [Sketch](#cadquery.Sketch) | [Compound](#cadquery.occ_impl.shapes.Compound)], mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None, ignore_selection: bool = False) → T

Apply a callback on all applicable entities.

* **Parameters:**
  * **self** (*T*)
  * **callback** (*Callable* *[* *[*[*Location*](#cadquery.Location) *]* *,* [*Face*](#cadquery.occ_impl.shapes.Face) *|* [*Sketch*](#cadquery.Sketch) *|* [*Compound*](#cadquery.occ_impl.shapes.Compound) *]*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
  * **ignore_selection** (*bool*)
* **Return type:**
  *T*

#### edge(val: [Edge](#cadquery.occ_impl.shapes.Edge), tag: str | None = None, forConstruction: bool = False) → T

Add an edge to the sketch.

* **Parameters:**
  * **self** (*T*)
  * **val** ([*Edge*](#cadquery.occ_impl.shapes.Edge))
  * **tag** (*str* *|* *None*)
  * **forConstruction** (*bool*)
* **Return type:**
  *T*

#### edges(s: str | [Selector](#cadquery.selectors.Selector) | None = None, tag: str | None = None) → T

Select edges.

* **Parameters:**
  * **self** (*T*)
  * **s** (*str* *|* [*Selector*](#cadquery.selectors.Selector) *|* *None*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### ellipse(a1: int | float, a2: int | float, angle: int | float = 0, mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None) → T

Construct an elliptical face.

* **Parameters:**
  * **self** (*T*)
  * **a1** (*int* *|* *float*)
  * **a2** (*int* *|* *float*)
  * **angle** (*int* *|* *float*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### export(fname: str, tolerance: float = 0.1, angularTolerance: float = 0.1, opt: Dict[str, Any] | None = None) → T

Export Sketch to file.

* **Parameters:**
  * **self** (*T*)
  * **path** – Filename.
  * **tolerance** (*float*) – the deflection tolerance, in model units. Default 0.1.
  * **angularTolerance** (*float*) – the angular tolerance, in radians. Default 0.1.
  * **opt** (*Dict* *[**str* *,* *Any* *]*  *|* *None*) – additional options passed to the specific exporter. Default None.
  * **fname** (*str*)
* **Returns:**
  Self.
* **Return type:**
  *T*

#### face(b: [Wire](#cadquery.occ_impl.shapes.Wire) | Iterable[[Edge](#cadquery.occ_impl.shapes.Edge)] | [Shape](#cadquery.occ_impl.shapes.Shape) | T, angle: int | float = 0, mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None, ignore_selection: bool = False) → T

Construct a face from a wire or edges.

* **Parameters:**
  * **self** (*T*)
  * **b** ([*Wire*](#cadquery.occ_impl.shapes.Wire) *|* *Iterable* *[*[*Edge*](#cadquery.occ_impl.shapes.Edge) *]*  *|* [*Shape*](#cadquery.occ_impl.shapes.Shape) *|* *T*)
  * **angle** (*int* *|* *float*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
  * **ignore_selection** (*bool*)
* **Return type:**
  *T*

#### faces(s: str | [Selector](#cadquery.selectors.Selector) | None = None, tag: str | None = None) → T

Select faces.

* **Parameters:**
  * **self** (*T*)
  * **s** (*str* *|* [*Selector*](#cadquery.selectors.Selector) *|* *None*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### fillet(d: int | float) → T

Add a fillet based on current selection.

* **Parameters:**
  * **self** (*T*)
  * **d** (*int* *|* *float*)
* **Return type:**
  *T*

#### filter(f: Callable[[[Shape](#cadquery.occ_impl.shapes.Shape) | [Location](#cadquery.Location)], bool]) → T

Filter items using a boolean predicate.

* **Parameters:**
  * **self** (*T*)
  * **f** (*Callable* *[* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Location*](#cadquery.Location) *]* *,* *bool* *]*) – Callable to be used for filtering.
* **Returns:**
  Sketch object with filtered items.
* **Return type:**
  *T*

#### finalize() → Any

Finish sketch construction and return the parent.

* **Return type:**
  *Any*

#### hull(mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None) → T

Generate a convex hull from current selection or all objects.

* **Parameters:**
  * **self** (*T*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### importDXF(filename: str, tol: float = 1e-06, exclude: List[str] = [], include: List[str] = [], angle: int | float = 0, mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None) → T

Import a DXF file and construct face(s)

* **Parameters:**
  * **self** (*T*)
  * **filename** (*str*)
  * **tol** (*float*)
  * **exclude** (*List* *[**str* *]*)
  * **include** (*List* *[**str* *]*)
  * **angle** (*int* *|* *float*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### invoke(f: Callable[[T], T] | Callable[[T], None] | Callable[[], None])

Invoke a callable mapping Sketch to Sketch or None. Supports also
callables that take no arguments such as breakpoint. Returns self if callable
returns None.

* **Parameters:**
  * **self** (*T*)
  * **f** (*Callable* *[* *[**T* *]* *,* *T* *]*  *|* *Callable* *[* *[**T* *]* *,* *None* *]*  *|* *Callable* *[* *[* *]* *,* *None* *]*) – Callable to be invoked.
* **Returns:**
  Sketch object.

#### located(loc: [Location](#cadquery.Location)) → T

Create a partial copy of the sketch with a new location.

* **Parameters:**
  * **self** (*T*)
  * **loc** ([*Location*](#cadquery.Location))
* **Return type:**
  *T*

#### map(f: Callable[[[Shape](#cadquery.occ_impl.shapes.Shape) | [Location](#cadquery.Location)], [Shape](#cadquery.occ_impl.shapes.Shape) | [Location](#cadquery.Location)])

Apply a callable to every item separately.

* **Parameters:**
  * **self** (*T*)
  * **f** (*Callable* *[* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Location*](#cadquery.Location) *]* *,* [*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Location*](#cadquery.Location) *]*) – Callable to be applied to every item separately.
* **Returns:**
  Sketch object with f applied to all items.

#### moved(\*args, \*\*kwargs) → T

Create a partial copy of the sketch with moved \_faces.

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### offset(d: int | float, mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None) → T

Offset selected wires or edges.

* **Parameters:**
  * **self** (*T*)
  * **d** (*int* *|* *float*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### parray(r: int | float, a1: int | float, da: int | float, n: int, rotate: bool = True) → T

Generate a polar array of locations.

* **Parameters:**
  * **self** (*T*)
  * **r** (*int* *|* *float*)
  * **a1** (*int* *|* *float*)
  * **da** (*int* *|* *float*)
  * **n** (*int*)
  * **rotate** (*bool*)
* **Return type:**
  *T*

#### polygon(pts: Iterable[[Vector](#cadquery.Vector) | Tuple[int | float, int | float]], angle: int | float = 0, mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None) → T

Construct a polygonal face.

* **Parameters:**
  * **self** (*T*)
  * **pts** (*Iterable* *[*[*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]* *]*)
  * **angle** (*int* *|* *float*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### push(locs: Iterable[[Location](#cadquery.Location) | [Vector](#cadquery.Vector) | Tuple[int | float, int | float]], tag: str | None = None) → T

Set current selection to given locations or points.

* **Parameters:**
  * **self** (*T*)
  * **locs** (*Iterable* *[*[*Location*](#cadquery.Location) *|* [*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]* *]*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### rarray(xs: int | float, ys: int | float, nx: int, ny: int) → T

Generate a rectangular array of locations.

* **Parameters:**
  * **self** (*T*)
  * **xs** (*int* *|* *float*)
  * **ys** (*int* *|* *float*)
  * **nx** (*int*)
  * **ny** (*int*)
* **Return type:**
  *T*

#### rect(w: int | float, h: int | float, angle: int | float = 0, mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None) → T

Construct a rectangular face.

* **Parameters:**
  * **self** (*T*)
  * **w** (*int* *|* *float*)
  * **h** (*int* *|* *float*)
  * **angle** (*int* *|* *float*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### regularPolygon(r: int | float, n: int, angle: int | float = 0, mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None) → T

Construct a regular polygonal face.

* **Parameters:**
  * **self** (*T*)
  * **r** (*int* *|* *float*)
  * **n** (*int*)
  * **angle** (*int* *|* *float*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### replace() → T

Replace the underlying faces with the selection.

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### reset() → T

Reset current selection.

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### segment(self: T, p1: [cadquery.occ_impl.geom.Vector](#cadquery.Vector) | Tuple[int | float, int | float], p2: [cadquery.occ_impl.geom.Vector](#cadquery.Vector) | Tuple[int | float, int | float], tag: str | None = None, forConstruction: bool = False) → T

Construct a segment.

* **Parameters:**
  * **self** (*T*)
  * **p1** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*)
  * **p2** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*)
  * **tag** (*str* *|* *None*)
  * **forConstruction** (*bool*)
* **Return type:**
  *T*

#### select(\*tags: str) → T

Select based on tags.

* **Parameters:**
  * **self** (*T*)
  * **tags** (*str*)
* **Return type:**
  *T*

#### slot(w: int | float, h: int | float, angle: int | float = 0, mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None) → T

Construct a slot-shaped face.

* **Parameters:**
  * **self** (*T*)
  * **w** (*int* *|* *float*)
  * **h** (*int* *|* *float*)
  * **angle** (*int* *|* *float*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### solve() → T

Solve current constraints and update edge positions.

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### sort(key: Callable[[[Shape](#cadquery.occ_impl.shapes.Shape) | [Location](#cadquery.Location)], Any]) → T

Sort items using a callable.

* **Parameters:**
  * **self** (*T*)
  * **key** (*Callable* *[* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Location*](#cadquery.Location) *]* *,* *Any* *]*) – Callable to be used for sorting.
* **Returns:**
  Sketch object with items sorted.
* **Return type:**
  *T*

#### spline(self: T, pts: Iterable[[cadquery.occ_impl.geom.Vector](#cadquery.Vector) | Tuple[int | float, int | float]], tangents: Iterable[[cadquery.occ_impl.geom.Vector](#cadquery.Vector) | Tuple[int | float, int | float]] | None, periodic: bool, tag: str | None = None, forConstruction: bool = False) → T

Construct a spline edge.

* **Parameters:**
  * **self** (*T*)
  * **pts** (*Iterable* *[*[*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]* *]*)
  * **tangents** (*Iterable* *[*[*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]* *]*  *|* *None*)
  * **periodic** (*bool*)
  * **tag** (*str* *|* *None*)
  * **forConstruction** (*bool*)
* **Return type:**
  *T*

#### subtract() → T

Subtract selection from the underlying faces.

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### tag(tag: str) → T

Tag current selection.

* **Parameters:**
  * **self** (*T*)
  * **tag** (*str*)
* **Return type:**
  *T*

#### trapezoid(w: int | float, h: int | float, a1: int | float, a2: float | None = None, angle: int | float = 0, mode: Literal['a', 's', 'i', 'c', 'r'] = 'a', tag: str | None = None) → T

Construct a trapezoidal face.

* **Parameters:**
  * **self** (*T*)
  * **w** (*int* *|* *float*)
  * **h** (*int* *|* *float*)
  * **a1** (*int* *|* *float*)
  * **a2** (*float* *|* *None*)
  * **angle** (*int* *|* *float*)
  * **mode** (*Literal* *[* *'a'* *,*  *'s'* *,*  *'i'* *,*  *'c'* *,*  *'r'* *]*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### val() → [Shape](#cadquery.occ_impl.shapes.Shape) | [Location](#cadquery.Location)

Return the first selected item, underlying compound or first edge.

* **Parameters:**
  **self** (*T*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape) | [*Location*](#cadquery.Location)

#### vals() → List[[Shape](#cadquery.occ_impl.shapes.Shape) | [Location](#cadquery.Location)]

Return all selected items, underlying compound or all edges.

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *List*[[*Shape*](#cadquery.occ_impl.shapes.Shape) | [*Location*](#cadquery.Location)]

#### vertices(s: str | [Selector](#cadquery.selectors.Selector) | None = None, tag: str | None = None) → T

Select vertices.

* **Parameters:**
  * **self** (*T*)
  * **s** (*str* *|* [*Selector*](#cadquery.selectors.Selector) *|* *None*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

#### wires(s: str | [Selector](#cadquery.selectors.Selector) | None = None, tag: str | None = None) → T

Select wires.

* **Parameters:**
  * **self** (*T*)
  * **s** (*str* *|* [*Selector*](#cadquery.selectors.Selector) *|* *None*)
  * **tag** (*str* *|* *None*)
* **Return type:**
  *T*

### *class* cadquery.Solid(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape), [`Mixin3D`](#cadquery.occ_impl.shapes.Mixin3D)

a single solid

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### *classmethod* extrudeLinear(cls, outerWire: [cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire), innerWires: List[[cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire)], vecNormal: ForwardRef('Vector') | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], taper: float | int = 0) → 'Solid'

Attempt to extrude the list of wires into a prismatic solid in the provided direction

* **Parameters:**
  * **outerWire** ([*Wire*](#cadquery.occ_impl.shapes.Wire)) – the outermost wire
  * **innerWires** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*) – a list of inner wires
  * **vecNormal** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – a vector along which to extrude the wires
  * **taper** (*float* *|* *int*) – taper angle, default=0
* **Returns:**
  a Solid object
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

The wires must not intersect

Extruding wires is very non-trivial.  Nested wires imply very different geometry, and
there are many geometries that are invalid. In general, the following conditions must be met:

* all wires must be closed
* there cannot be any intersecting or self-intersecting wires
* wires must be listed from outside in
* more than one levels of nesting is not supported reliably

This method will attempt to sort the wires, but there is much work remaining to make this method
reliable.

#### *classmethod* extrudeLinearWithRotation(outerWire: [Wire](#cadquery.occ_impl.shapes.Wire), innerWires: List[[Wire](#cadquery.occ_impl.shapes.Wire)], vecCenter: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], vecNormal: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], angleDegrees: float | int) → [Solid](#cadquery.occ_impl.shapes.Solid)

Creates a ‘twisted prism’ by extruding, while simultaneously rotating around the extrusion vector.

Though the signature may appear to be similar enough to extrudeLinear to merit combining them, the
construction methods used here are different enough that they should be separate.

At a high level, the steps followed are:

1. accept a set of wires
2. create another set of wires like this one, but which are transformed and rotated
3. create a ruledSurface between the sets of wires
4. create a shell and compute the resulting object

* **Parameters:**
  * **outerWire** ([*Wire*](#cadquery.occ_impl.shapes.Wire)) – the outermost wire
  * **innerWires** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*) – a list of inner wires
  * **vecCenter** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – the center point about which to rotate.  the axis of rotation is defined by
    vecNormal, located at vecCenter.
  * **vecNormal** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – a vector along which to extrude the wires
  * **angleDegrees** (*float* *|* *int*) – the angle to rotate through while extruding
* **Returns:**
  a Solid object
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### innerShells() → List[[Shell](#cadquery.occ_impl.shapes.Shell)]

Returns inner shells.

* **Return type:**
  *List*[[*Shell*](#cadquery.occ_impl.shapes.Shell)]

#### *classmethod* interpPlate(surf_edges, surf_pts, thickness, degree=3, nbPtsOnCur=15, nbIter=2, anisotropy=False, tol2d=1e-05, tol3d=0.0001, tolAng=0.01, tolCurv=0.1, maxDeg=8, maxSegments=9) → [Solid](#cadquery.occ_impl.shapes.Solid) | [Face](#cadquery.occ_impl.shapes.Face)

Returns a plate surface that is ‘thickness’ thick, enclosed by ‘surf_edge_pts’ points, and going through ‘surf_pts’ points.

* **Parameters:**
  * **surf_edges** – list of [x,y,z] float ordered coordinates
    or list of ordered or unordered wires
  * **surf_pts** – list of [x,y,z] float coordinates (uses only edges if [])
  * **thickness** – thickness may be negative or positive depending on direction, (returns 2D surface if 0)
  * **degree** – >=2
  * **nbPtsOnCur** – number of points on curve >= 15
  * **nbIter** – number of iterations >= 2
  * **anisotropy** – bool Anisotropy
  * **tol2d** – 2D tolerance >0
  * **tol3d** – 3D tolerance >0
  * **tolAng** – angular tolerance
  * **tolCurv** – tolerance for curvature >0
  * **maxDeg** – highest polynomial degree >= 2
  * **maxSegments** – greatest number of segments >= 2
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid) | [*Face*](#cadquery.occ_impl.shapes.Face)

#### *static* isSolid(obj: [Shape](#cadquery.occ_impl.shapes.Shape)) → bool

Returns true if the object is a solid, false otherwise

* **Parameters:**
  **obj** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  bool

#### *classmethod* makeBox(length,width,height,[pnt,dir]) -- Make a box located in pnt with the dimensions (length,width,height)

By default pnt=Vector(0,0,0) and dir=Vector(0,0,1)

* **Parameters:**
  * **length** (*float*)
  * **width** (*float*)
  * **height** (*float*)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### *classmethod* makeCone(radius1: float, radius2: float, height: float, pnt: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0), angleDegrees: float = 360) → [Solid](#cadquery.occ_impl.shapes.Solid)

Make a cone with given radii and height
By default pnt=Vector(0,0,0),
dir=Vector(0,0,1) and angle=360

* **Parameters:**
  * **radius1** (*float*)
  * **radius2** (*float*)
  * **height** (*float*)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **angleDegrees** (*float*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### *classmethod* makeCylinder(radius: float, height: float, pnt: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0), angleDegrees: float = 360) → [Solid](#cadquery.occ_impl.shapes.Solid)

makeCylinder(radius,height,[pnt,dir,angle]) –
Make a cylinder with a given radius and height
By default pnt=Vector(0,0,0),dir=Vector(0,0,1) and angle=360

* **Parameters:**
  * **radius** (*float*)
  * **height** (*float*)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **angleDegrees** (*float*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### *classmethod* makeLoft(listOfWire: List[[Wire](#cadquery.occ_impl.shapes.Wire)], ruled: bool = False) → [Solid](#cadquery.occ_impl.shapes.Solid)

makes a loft from a list of wires
The wires will be converted into faces when possible– it is presumed that nobody ever actually
wants to make an infinitely thin shell for a real FreeCADPart.

* **Parameters:**
  * **listOfWire** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*)
  * **ruled** (*bool*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### *classmethod* makeSolid(shell: [Shell](#cadquery.occ_impl.shapes.Shell)) → [Solid](#cadquery.occ_impl.shapes.Solid)

Makes a solid from a single shell.

* **Parameters:**
  **shell** ([*Shell*](#cadquery.occ_impl.shapes.Shell))
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### *classmethod* makeSphere(radius: float, pnt: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0), angleDegrees1: float = 0, angleDegrees2: float = 90, angleDegrees3: float = 360) → [Shape](#cadquery.occ_impl.shapes.Shape)

Make a sphere with a given radius
By default pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=0, angle2=90 and angle3=360

* **Parameters:**
  * **radius** (*float*)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **angleDegrees1** (*float*)
  * **angleDegrees2** (*float*)
  * **angleDegrees3** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### *classmethod* makeTorus(radius1: float, radius2: float, pnt: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0), angleDegrees1: float = 0, angleDegrees2: float = 360) → [Solid](#cadquery.occ_impl.shapes.Solid)

makeTorus(radius1,radius2,[pnt,dir,angle1,angle2,angle]) –
Make a torus with a given radii and angles
By default pnt=Vector(0,0,0),dir=Vector(0,0,1),angle1=0
,angle1=360 and angle=360

* **Parameters:**
  * **radius1** (*float*)
  * **radius2** (*float*)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **angleDegrees1** (*float*)
  * **angleDegrees2** (*float*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### *classmethod* makeWedge(dx: float, dy: float, dz: float, xmin: float, zmin: float, xmax: float, zmax: float, pnt: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0)) → [Solid](#cadquery.occ_impl.shapes.Solid)

Make a wedge located in pnt
By default pnt=Vector(0,0,0) and dir=Vector(0,0,1)

* **Parameters:**
  * **dx** (*float*)
  * **dy** (*float*)
  * **dz** (*float*)
  * **xmin** (*float*)
  * **zmin** (*float*)
  * **xmax** (*float*)
  * **zmax** (*float*)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### outerShell() → [Shell](#cadquery.occ_impl.shapes.Shell)

Returns outer shell.

* **Return type:**
  [*Shell*](#cadquery.occ_impl.shapes.Shell)

#### *classmethod* revolve(outerWire: [Wire](#cadquery.occ_impl.shapes.Wire), innerWires: List[[Wire](#cadquery.occ_impl.shapes.Wire)], angleDegrees: float | int, axisStart: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], axisEnd: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Solid](#cadquery.occ_impl.shapes.Solid)

Attempt to revolve the list of wires into a solid in the provided direction

* **Parameters:**
  * **outerWire** ([*Wire*](#cadquery.occ_impl.shapes.Wire)) – the outermost wire
  * **innerWires** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*) – a list of inner wires
  * **angleDegrees** (*float* *,* *anything less than 360 degrees will leave the shape open*) – the angle to revolve through.
  * **axisStart** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – the start point of the axis of rotation
  * **axisEnd** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – the end point of the axis of rotation
* **Returns:**
  a Solid object
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

The wires must not intersect

* all wires must be closed
* there cannot be any intersecting or self-intersecting wires
* wires must be listed from outside in
* more than one levels of nesting is not supported reliably
* the wire(s) that you’re revolving cannot be centered

This method will attempt to sort the wires, but there is much work remaining to make this method
reliable.

#### *classmethod* sweep(cls, outerWire: [cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire), innerWires: List[[cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire)], path: [cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire) | [cadquery.occ_impl.shapes.Edge](#cadquery.occ_impl.shapes.Edge), makeSolid: bool = True, isFrenet: bool = False, mode: [cadquery.occ_impl.geom.Vector](#cadquery.Vector) | [cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire) | [cadquery.occ_impl.shapes.Edge](#cadquery.occ_impl.shapes.Edge) | NoneType = None, transitionMode: Literal['transformed', 'round', 'right'] = 'transformed') → 'Shape'

Attempt to sweep the list of wires into a prismatic solid along the provided path

* **Parameters:**
  * **outerWire** ([*Wire*](#cadquery.occ_impl.shapes.Wire)) – the outermost wire
  * **innerWires** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*) – a list of inner wires
  * **path** ([*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Edge*](#cadquery.occ_impl.shapes.Edge)) – The wire to sweep the face resulting from the wires over
  * **makeSolid** (*bool*) – return Solid or Shell (default True)
  * **isFrenet** (*bool*) – Frenet mode (default False)
  * **mode** ([*Vector*](#cadquery.Vector) *|* [*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Edge*](#cadquery.occ_impl.shapes.Edge) *|* *None*) – additional sweep mode parameters
  * **transitionMode** (*Literal* *[* *'transformed'* *,*  *'round'* *,*  *'right'* *]*) – handling of profile orientation at C1 path discontinuities.
    Possible values are {‘transformed’,’round’, ‘right’} (default: ‘right’).
* **Returns:**
  a Solid object
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### *classmethod* sweep_multi(profiles: Iterable[[Wire](#cadquery.occ_impl.shapes.Wire) | [Face](#cadquery.occ_impl.shapes.Face)], path: [Wire](#cadquery.occ_impl.shapes.Wire) | [Edge](#cadquery.occ_impl.shapes.Edge), makeSolid: bool = True, isFrenet: bool = False, mode: [Vector](#cadquery.Vector) | [Wire](#cadquery.occ_impl.shapes.Wire) | [Edge](#cadquery.occ_impl.shapes.Edge) | None = None) → [Solid](#cadquery.occ_impl.shapes.Solid)

Multi section sweep. Only single outer profile per section is allowed.

* **Parameters:**
  * **profiles** (*Iterable* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Face*](#cadquery.occ_impl.shapes.Face) *]*) – list of profiles
  * **path** ([*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Edge*](#cadquery.occ_impl.shapes.Edge)) – The wire to sweep the face resulting from the wires over
  * **mode** ([*Vector*](#cadquery.Vector) *|* [*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Edge*](#cadquery.occ_impl.shapes.Edge) *|* *None*) – additional sweep mode parameters.
  * **makeSolid** (*bool*)
  * **isFrenet** (*bool*)
* **Returns:**
  a Solid object
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

### *class* cadquery.StringSyntaxSelector(selectorString)

Bases: [`Selector`](#cadquery.selectors.Selector)

Filter lists objects using a simple string syntax. All of the filters available in the string syntax
are also available ( usually with more functionality ) through the creation of full-fledged
selector objects. see [`Selector`](#cadquery.Selector) and its subclasses

Filtering works differently depending on the type of object list being filtered.

* **Parameters:**
  **selectorString** – A two-part selector string, [selector][axis]
* **Returns:**
  objects that match the specified selector

**\*Modifiers\*** are `('|','+','-','<','>','%')`

> * **|:**
>   parallel to ( same as [`ParallelDirSelector`](#cadquery.ParallelDirSelector) ). Can return multiple objects.
> * **#:**
>   perpendicular to (same as [`PerpendicularDirSelector`](#cadquery.PerpendicularDirSelector) )
> * **+:**
>   positive direction (same as [`DirectionSelector`](#cadquery.DirectionSelector) )
> * **-:**
>   negative direction (same as [`DirectionSelector`](#cadquery.DirectionSelector)  )
> * **>:**
>   maximize (same as [`DirectionMinMaxSelector`](#cadquery.DirectionMinMaxSelector) with directionMax=True)
> * **<:**
>   minimize (same as [`DirectionMinMaxSelector`](#cadquery.DirectionMinMaxSelector) with directionMax=False )
> * **%:**
>   curve/surface type (same as [`TypeSelector`](#cadquery.TypeSelector))

**\*axisStrings\*** are: `X,Y,Z,XY,YZ,XZ` or `(x,y,z)` which defines an arbitrary direction

It is possible to combine simple selectors together using logical operations.
The following operations are supported

> * **and:**
>   Logical AND, e.g. >X and >Y
> * **or:**
>   Logical OR, e.g. |X or |Y
> * **not:**
>   Logical NOT, e.g. not #XY
> * **exc(ept):**
>   Set difference (equivalent to AND NOT): |X exc >Z

Finally, it is also possible to use even more complex expressions with nesting
and arbitrary number of terms, e.g.

> (not >X[0] and #XY) or >XY[0]

Selectors are a complex topic: see [Selectors Reference](selectors.md#selector-reference) for more information

#### \_\_init_\_(selectorString)

Feed the input string through the parser and construct an relevant complex selector object

#### filter(objectList: Sequence[Shape])

Filter give object list through th already constructed complex selector object

* **Parameters:**
  **objectList** (*Sequence* *[**Shape* *]*)

### *class* cadquery.TypeSelector(typeString: str)

Bases: [`Selector`](#cadquery.selectors.Selector)

Selects objects having the prescribed geometry type.

Applicability:
: Faces: PLANE, CYLINDER, CONE, SPHERE, TORUS, BEZIER, BSPLINE, REVOLUTION, EXTRUSION, OFFSET, OTHER
  Edges: LINE, CIRCLE, ELLIPSE, HYPERBOLA, PARABOLA, BEZIER, BSPLINE, OFFSET, OTHER

You can use the string selector syntax. For example this:

```default
CQ(aCube).faces(TypeSelector("PLANE"))
```

will select 6 faces, and is equivalent to:

```default
CQ(aCube).faces("%PLANE")
```

* **Parameters:**
  **typeString** (*str*)

#### \_\_init_\_(typeString: str)

* **Parameters:**
  **typeString** (*str*)

#### filter(objectList: Sequence[Shape]) → List[Shape]

Filter the provided list.

The default implementation returns the original list unfiltered.

* **Parameters:**
  **objectList** (*list* *of* *OCCT primitives*) – list to filter
* **Returns:**
  filtered list
* **Return type:**
  *List*[*Shape*]

### *class* cadquery.Vector(x: float, y: float, z: float)

### *class* cadquery.Vector(x: float, y: float)

### *class* cadquery.Vector(v: [Vector](#cadquery.Vector))

### *class* cadquery.Vector(v: Sequence[float])

### *class* cadquery.Vector(v: gp_Vec | gp_Pnt | gp_Dir | gp_XYZ)

### *class* cadquery.Vector

Bases: `object`

Create a 3-dimensional vector

* **Parameters:**
  **args** – a 3D vector, with x-y-z parts.

you can either provide:
: * nothing (in which case the null vector is return)
  * a gp_Vec
  * a vector ( in which case it is copied )
  * a 3-tuple
  * a 2-tuple (z assumed to be 0)
  * three float values: x, y, and z
  * two float values: x,y

#### Center() → [Vector](#cadquery.Vector)

Return the vector itself

The center of myself is myself.
Provided so that vectors, vertices, and other shapes all support a
common interface, when Center() is requested for all objects on the
stack.

* **Return type:**
  [*Vector*](#cadquery.Vector)

#### \_\_eq_\_(other: [Vector](#cadquery.Vector)) → bool

Return self==value.

* **Parameters:**
  **other** ([*Vector*](#cadquery.Vector))
* **Return type:**
  bool

#### \_\_hash_\_ *= None*

#### \_\_init_\_(\*args)

#### \_\_repr_\_() → str

Return repr(self).

* **Return type:**
  str

#### \_\_str_\_() → str

Return str(self).

* **Return type:**
  str

#### \_\_weakref_\_

list of weak references to the object

#### multiply(scale: float) → [Vector](#cadquery.Vector)

Return a copy multiplied by the provided scalar

* **Parameters:**
  **scale** (*float*)
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### normalized() → [Vector](#cadquery.Vector)

Return a normalized version of this vector

* **Return type:**
  [*Vector*](#cadquery.Vector)

#### projectToLine(line: [Vector](#cadquery.Vector)) → [Vector](#cadquery.Vector)

Returns a new vector equal to the projection of this Vector onto the line
represented by Vector <line>

* **Parameters:**
  * **args** – Vector
  * **line** ([*Vector*](#cadquery.Vector))
* **Return type:**
  [*Vector*](#cadquery.Vector)

Returns the projected vector.

#### projectToPlane(plane: [Plane](#cadquery.Plane)) → [Vector](#cadquery.Vector)

Vector is projected onto the plane provided as input.

* **Parameters:**
  * **args** – Plane object
  * **plane** ([*Plane*](#cadquery.Plane))
* **Return type:**
  [*Vector*](#cadquery.Vector)

Returns the projected vector.

### *class* cadquery.Vertex(obj: TopoDS_Shape, forConstruction: bool = False)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape)

A Single Point in Space

* **Parameters:**
  * **obj** (*TopoDS_Shape*)
  * **forConstruction** (*bool*)

#### Center() → [Vector](#cadquery.Vector)

The center of a vertex is itself!

* **Return type:**
  [*Vector*](#cadquery.Vector)

#### \_\_init_\_(obj: TopoDS_Shape, forConstruction: bool = False)

Create a vertex

* **Parameters:**
  * **obj** (*TopoDS_Shape*)
  * **forConstruction** (*bool*)

### *class* cadquery.Wire(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape), [`Mixin1D`](#cadquery.occ_impl.shapes.Mixin1D)

A series of connected, ordered Edges, that typically bounds a Face

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### Vertices() → List[[Vertex](#cadquery.occ_impl.shapes.Vertex)]

Ordered list of vertices of the wire.

* **Return type:**
  *List*[[*Vertex*](#cadquery.occ_impl.shapes.Vertex)]

#### \_\_iter_\_() → Iterator[[Edge](#cadquery.occ_impl.shapes.Edge)]

Iterate over edges in an ordered way.

* **Return type:**
  *Iterator*[[*Edge*](#cadquery.occ_impl.shapes.Edge)]

#### *classmethod* assembleEdges(listOfEdges: Iterable[[Edge](#cadquery.occ_impl.shapes.Edge)]) → [Wire](#cadquery.occ_impl.shapes.Wire)

Attempts to build a wire that consists of the edges in the provided list

* **Parameters:**
  * **cls**
  * **listOfEdges** (*Iterable* *[*[*Edge*](#cadquery.occ_impl.shapes.Edge) *]*) – a list of Edge objects. The edges are not to be consecutive.
* **Returns:**
  a wire with the edges assembled
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

BRepBuilderAPI_MakeWire::Error() values:

* BRepBuilderAPI_WireDone = 0
* BRepBuilderAPI_EmptyWire = 1
* BRepBuilderAPI_DisconnectedWire = 2
* BRepBuilderAPI_NonManifoldWire = 3

#### chamfer2D(d: float, vertices: Iterable[[Vertex](#cadquery.occ_impl.shapes.Vertex)]) → [Wire](#cadquery.occ_impl.shapes.Wire)

Apply 2D chamfer to a wire

* **Parameters:**
  * **d** (*float*)
  * **vertices** (*Iterable* *[*[*Vertex*](#cadquery.occ_impl.shapes.Vertex) *]*)
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### close() → [Wire](#cadquery.occ_impl.shapes.Wire)

Close a Wire

* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### *classmethod* combine(listOfWires: Iterable[[Wire](#cadquery.occ_impl.shapes.Wire) | [Edge](#cadquery.occ_impl.shapes.Edge)], tol: float = 1e-09) → List[[Wire](#cadquery.occ_impl.shapes.Wire)]

Attempt to combine a list of wires and edges into a new wire.

* **Parameters:**
  * **cls**
  * **listOfWires** (*Iterable* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Edge*](#cadquery.occ_impl.shapes.Edge) *]*)
  * **tol** (*float*) – default 1e-9
* **Returns:**
  List[Wire]
* **Return type:**
  *List*[[*Wire*](#cadquery.occ_impl.shapes.Wire)]

#### fillet(radius: float, vertices: Iterable[[Vertex](#cadquery.occ_impl.shapes.Vertex)] | None = None) → [Wire](#cadquery.occ_impl.shapes.Wire)

Apply 2D or 3D fillet to a wire

* **Parameters:**
  * **radius** (*float*) – the radius of the fillet, must be > zero
  * **vertices** (*Iterable* *[*[*Vertex*](#cadquery.occ_impl.shapes.Vertex) *]*  *|* *None*) – the vertices to delete (where the fillet will be applied).  By default
    all vertices are deleted except ends of open wires.
* **Returns:**
  A wire with filleted corners
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### fillet2D(radius: float, vertices: Iterable[[Vertex](#cadquery.occ_impl.shapes.Vertex)]) → [Wire](#cadquery.occ_impl.shapes.Wire)

Apply 2D fillet to a wire

* **Parameters:**
  * **radius** (*float*)
  * **vertices** (*Iterable* *[*[*Vertex*](#cadquery.occ_impl.shapes.Vertex) *]*)
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### *classmethod* makeCircle(radius: float, center: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], normal: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Wire](#cadquery.occ_impl.shapes.Wire)

Makes a Circle centered at the provided point, having normal in the provided direction

* **Parameters:**
  * **radius** (*float*) – floating point radius of the circle, must be > 0
  * **center** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – vector representing the center of the circle
  * **normal** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – vector representing the direction of the plane the circle should lie in
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### *classmethod* makeEllipse(x_radius: float, y_radius: float, center: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], normal: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], xDir: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], angle1: float = 360.0, angle2: float = 360.0, rotation_angle: float = 0.0, closed: bool = True) → [Wire](#cadquery.occ_impl.shapes.Wire)

Makes an Ellipse centered at the provided point, having normal in the provided direction

* **Parameters:**
  * **x_radius** (*float*) – floating point major radius of the ellipse (x-axis), must be > 0
  * **y_radius** (*float*) – floating point minor radius of the ellipse (y-axis), must be > 0
  * **center** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – vector representing the center of the circle
  * **normal** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – vector representing the direction of the plane the circle should lie in
  * **angle1** (*float*) – start angle of arc
  * **angle2** (*float*) – end angle of arc
  * **rotation_angle** (*float*) – angle to rotate the created ellipse / arc
  * **xDir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **closed** (*bool*)
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### *classmethod* makeHelix(pitch: float, height: float, radius: float, center: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0), angle: float = 360.0, lefthand: bool = False) → [Wire](#cadquery.occ_impl.shapes.Wire)

Make a helix with a given pitch, height and radius
By default a cylindrical surface is used to create the helix. If
the fourth parameter is set (the apex given in degree) a conical surface is used instead’

* **Parameters:**
  * **pitch** (*float*)
  * **height** (*float*)
  * **radius** (*float*)
  * **center** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **angle** (*float*)
  * **lefthand** (*bool*)
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### *classmethod* makePolygon(listOfVertices: Iterable[[Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]], forConstruction: bool = False, close: bool = False) → [Wire](#cadquery.occ_impl.shapes.Wire)

Construct a polygonal wire from points.

* **Parameters:**
  * **listOfVertices** (*Iterable* *[*[*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]* *]*)
  * **forConstruction** (*bool*)
  * **close** (*bool*)
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### offset2D(d: float, kind: Literal['arc', 'intersection', 'tangent'] = 'arc') → List[[Wire](#cadquery.occ_impl.shapes.Wire)]

Offsets a planar wire

* **Parameters:**
  * **d** (*float*)
  * **kind** (*Literal* *[* *'arc'* *,*  *'intersection'* *,*  *'tangent'* *]*)
* **Return type:**
  *List*[[*Wire*](#cadquery.occ_impl.shapes.Wire)]

#### stitch(other: [Wire](#cadquery.occ_impl.shapes.Wire)) → [Wire](#cadquery.occ_impl.shapes.Wire)

Attempt to stitch wires

* **Parameters:**
  **other** ([*Wire*](#cadquery.occ_impl.shapes.Wire))
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

### *class* cadquery.Workplane(obj: [Vector](#cadquery.Vector) | [Location](#cadquery.Location) | [Shape](#cadquery.occ_impl.shapes.Shape) | [Sketch](#cadquery.Sketch))

### *class* cadquery.Workplane(inPlane: [Plane](#cadquery.Plane) | str = 'XY', origin: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector) = (0, 0, 0), obj: [Vector](#cadquery.Vector) | [Location](#cadquery.Location) | [Shape](#cadquery.occ_impl.shapes.Shape) | [Sketch](#cadquery.Sketch) | None = None)

Bases: `object`

Defines a coordinate system in space, in which 2D coordinates can be used.

* **Parameters:**
  * **plane** (*a Plane object* *, or* *a string in* *(**XY* *|**YZ* *|**XZ* *|**front* *|**back* *|**top* *|**bottom* *|**left* *|**right* *)*) – the plane in which the workplane will be done
  * **origin** (*a 3-tuple in global coordinates* *, or* *None to default to the origin*) – the desired origin of the new workplane
  * **obj** (*a CAD primitive* *, or* *None to use the centerpoint* *of* *the plane as the initial
    stack value.*) – an object to use initially for the stack
* **Raises:**
  ValueError if the provided plane is not a plane, a valid named workplane
* **Returns:**
  A Workplane object, with coordinate system matching the supplied plane.

The most common use is:

```default
s = Workplane("XY")
```

After creation, the stack contains a single point, the origin of the underlying plane,
and the *current point* is on the origin.

#### NOTE
You can also create workplanes on the surface of existing faces using
[`workplane()`](#cadquery.Workplane.workplane)

#### \_\_add_\_(other: [Workplane](#cadquery.Workplane) | [Solid](#cadquery.occ_impl.shapes.Solid) | [Compound](#cadquery.occ_impl.shapes.Compound)) → T

Syntactic sugar for union.

Notice that `r = a + b` is equivalent to `r = a.union(b)` and `r = a | b`.

* **Parameters:**
  * **self** (*T*)
  * **other** ([*Workplane*](#cadquery.Workplane) *|* [*Solid*](#cadquery.occ_impl.shapes.Solid) *|* [*Compound*](#cadquery.occ_impl.shapes.Compound))
* **Return type:**
  *T*

#### \_\_and_\_(other: [Workplane](#cadquery.Workplane) | [Solid](#cadquery.occ_impl.shapes.Solid) | [Compound](#cadquery.occ_impl.shapes.Compound)) → T

Syntactic sugar for intersect.

Notice that `r = a & b` is equivalent to `r = a.intersect(b)`.

Example:

```default
Box = Workplane("XY").box(1, 1, 1, centered=(False, False, False))
Sphere = Workplane("XY").sphere(1)
result = Box & Sphere
```

* **Parameters:**
  * **self** (*T*)
  * **other** ([*Workplane*](#cadquery.Workplane) *|* [*Solid*](#cadquery.occ_impl.shapes.Solid) *|* [*Compound*](#cadquery.occ_impl.shapes.Compound))
* **Return type:**
  *T*

#### \_\_init_\_(inPlane='XY', origin=(0, 0, 0), obj=None)

make a workplane from a particular plane

* **Parameters:**
  * **inPlane** (*a Plane object* *, or* *a string in* *(**XY* *|**YZ* *|**XZ* *|**front* *|**back* *|**top* *|**bottom* *|**left* *|**right* *)*) – the plane in which the workplane will be done
  * **origin** (*a 3-tuple in global coordinates* *, or* *None to default to the origin*) – the desired origin of the new workplane
  * **obj** (*a CAD primitive* *, or* *None to use the centerpoint* *of* *the plane as the initial
    stack value.*) – an object to use initially for the stack
* **Raises:**
  ValueError if the provided plane is not a plane, or one of XY|YZ|XZ
* **Returns:**
  A Workplane object, with coordinate system matching the supplied plane.

The most common use is:

```default
s = Workplane("XY")
```

After creation, the stack contains a single point, the origin of the underlying plane, and
the *current point* is on the origin.

#### \_\_iter_\_() → Iterator[[Shape](#cadquery.occ_impl.shapes.Shape)]

Special method for iterating over Shapes in objects

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *Iterator*[[*Shape*](#cadquery.occ_impl.shapes.Shape)]

#### \_\_mul_\_(other: [Workplane](#cadquery.Workplane) | [Solid](#cadquery.occ_impl.shapes.Solid) | [Compound](#cadquery.occ_impl.shapes.Compound)) → T

Syntactic sugar for intersect.

Notice that `r = a * b` is equivalent to `r = a.intersect(b)`.

Example:

```default
Box = Workplane("XY").box(1, 1, 1, centered=(False, False, False))
Sphere = Workplane("XY").sphere(1)
result = Box * Sphere
```

* **Parameters:**
  * **self** (*T*)
  * **other** ([*Workplane*](#cadquery.Workplane) *|* [*Solid*](#cadquery.occ_impl.shapes.Solid) *|* [*Compound*](#cadquery.occ_impl.shapes.Compound))
* **Return type:**
  *T*

#### \_\_or_\_(other: [Workplane](#cadquery.Workplane) | [Solid](#cadquery.occ_impl.shapes.Solid) | [Compound](#cadquery.occ_impl.shapes.Compound)) → T

Syntactic sugar for union.

Notice that `r = a | b` is equivalent to `r = a.union(b)` and `r = a + b`.

Example:

```default
Box = Workplane("XY").box(1, 1, 1, centered=(False, False, False))
Sphere = Workplane("XY").sphere(1)
result = Box | Sphere
```

* **Parameters:**
  * **self** (*T*)
  * **other** ([*Workplane*](#cadquery.Workplane) *|* [*Solid*](#cadquery.occ_impl.shapes.Solid) *|* [*Compound*](#cadquery.occ_impl.shapes.Compound))
* **Return type:**
  *T*

#### \_\_sub_\_(other: [Workplane](#cadquery.Workplane) | [Solid](#cadquery.occ_impl.shapes.Solid) | [Compound](#cadquery.occ_impl.shapes.Compound)) → T

Syntactic sugar for cut.

Notice that `r = a - b` is equivalent to `r = a.cut(b)`.

Example:

```default
Box = Workplane("XY").box(1, 1, 1, centered=(False, False, False))
Sphere = Workplane("XY").sphere(1)
result = Box - Sphere
```

* **Parameters:**
  * **self** (*T*)
  * **other** ([*Workplane*](#cadquery.Workplane) *|* [*Solid*](#cadquery.occ_impl.shapes.Solid) *|* [*Compound*](#cadquery.occ_impl.shapes.Compound))
* **Return type:**
  *T*

#### \_\_truediv_\_(other: [Workplane](#cadquery.Workplane) | [Solid](#cadquery.occ_impl.shapes.Solid) | [Compound](#cadquery.occ_impl.shapes.Compound)) → T

Syntactic sugar for intersect.

Notice that `r = a / b` is equivalent to `r = a.split(b)`.

Example:

```default
Box = Workplane("XY").box(1, 1, 1, centered=(False, False, False))
Sphere = Workplane("XY").sphere(1)
result = Box / Sphere
```

* **Parameters:**
  * **self** (*T*)
  * **other** ([*Workplane*](#cadquery.Workplane) *|* [*Solid*](#cadquery.occ_impl.shapes.Solid) *|* [*Compound*](#cadquery.occ_impl.shapes.Compound))
* **Return type:**
  *T*

#### \_\_weakref_\_

list of weak references to the object

#### add(obj)

Adds an object or a list of objects to the stack

* **Parameters:**
  **obj** (*a Workplane* *,* *CAD primitive* *, or* *list* *of* *CAD primitives*) – an object to add
* **Returns:**
  a Workplane with the requested operation performed

If a Workplane object, the values of that object’s stack are added. If
a list of cad primitives, they are all added. If a single CAD primitive
then it is added.

Used in rare cases when you need to combine the results of several CQ
results into a single Workplane object.

#### all() → List[T]

Return a list of all CQ objects on the stack.

useful when you need to operate on the elements
individually.

Contrast with vals, which returns the underlying
objects for all of the items on the stack

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *List*[*T*]

#### ancestors(kind: Literal['Vertex', 'Edge', 'Wire', 'Face', 'Shell', 'Solid', 'CompSolid', 'Compound'], tag: str | None = None) → T

Select topological ancestors.

* **Parameters:**
  * **self** (*T*)
  * **kind** (*Literal* *[* *'Vertex'* *,*  *'Edge'* *,*  *'Wire'* *,*  *'Face'* *,*  *'Shell'* *,*  *'Solid'* *,*  *'CompSolid'* *,*  *'Compound'* *]*) – kind of ancestor, e.g. “Face” or “Edge”
  * **tag** (*str* *|* *None*) – if set, search the tagged object instead of self
* **Returns:**
  a Workplane object whose stack contains selected ancestors.
* **Return type:**
  *T*

#### apply(f: Callable[[Iterable[[Vector](#cadquery.Vector) | [Location](#cadquery.Location) | [Shape](#cadquery.occ_impl.shapes.Shape) | [Sketch](#cadquery.Sketch)]], Iterable[[Vector](#cadquery.Vector) | [Location](#cadquery.Location) | [Shape](#cadquery.occ_impl.shapes.Shape) | [Sketch](#cadquery.Sketch)]]) → T

Apply a callable to all items at once.

* **Parameters:**
  * **self** (*T*)
  * **f** (*Callable* *[* *[**Iterable* *[*[*Vector*](#cadquery.Vector) *|* [*Location*](#cadquery.Location) *|* [*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Sketch*](#cadquery.Sketch) *]* *]* *,* *Iterable* *[*[*Vector*](#cadquery.Vector) *|* [*Location*](#cadquery.Location) *|* [*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Sketch*](#cadquery.Sketch) *]* *]*) – Callable to be applied.
* **Returns:**
  Workplane object with f applied to all items.
* **Return type:**
  *T*

#### bezier(listOfXYTuple: Iterable[Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector)], forConstruction: bool = False, includeCurrent: bool = False, makeWire: bool = False) → T

Make a cubic Bézier curve by the provided points (2D or 3D).

* **Parameters:**
  * **self** (*T*)
  * **listOfXYTuple** (*Iterable* *[**Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *]*) – Bezier control points and end point.
    All points except the last point are Bezier control points,
    and the last point is the end point
  * **includeCurrent** (*bool*) – Use the current point as a starting point of the curve
  * **makeWire** (*bool*) – convert the resulting bezier edge to a wire
  * **forConstruction** (*bool*)
* **Returns:**
  a Workplane object with the current point at the end of the bezier
* **Return type:**
  *T*

The Bézier Will begin at either current point or the first point
of listOfXYTuple, and end with the last point of listOfXYTuple

#### box(length: float, width: float, height: float, centered: bool | Tuple[bool, bool, bool] = True, combine: bool | Literal['cut', 'a', 's'] = True, clean: bool = True) → T

Return a 3d box with specified dimensions for each object on the stack.

* **Parameters:**
  * **self** (*T*)
  * **length** (*float*) – box size in X direction
  * **width** (*float*) – box size in Y direction
  * **height** (*float*) – box size in Z direction
  * **centered** (*bool* *|* *Tuple* *[**bool* *,* *bool* *,* *bool* *]*) – If True, the box will be centered around the reference point.
    If False, the corner of the box will be on the reference point and it will
    extend in the positive x, y and z directions. Can also use a 3-tuple to
    specify centering along each axis.
  * **combine** (*bool* *|* *Literal* *[* *'cut'* *,*  *'a'* *,*  *'s'* *]*) – should the results be combined with other solids on the stack
    (and each other)?
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
* **Return type:**
  *T*

One box is created for each item on the current stack. If no items are on the stack, one box
using the current workplane center is created.

If combine is true, the result will be a single object on the stack. If a solid was found
in the chain, the result is that solid with all boxes produced fused onto it otherwise, the
result is the combination of all the produced boxes.

If combine is false, the result will be a list of the boxes produced.

Most often boxes form the basis for a part:

```default
# make a single box with lower left corner at origin
s = Workplane().box(1, 2, 3, centered=False)
```

But sometimes it is useful to create an array of them:

```default
# create 4 small square bumps on a larger base plate:
s = (
    Workplane()
    .box(4, 4, 0.5)
    .faces(">Z")
    .workplane()
    .rect(3, 3, forConstruction=True)
    .vertices()
    .box(0.25, 0.25, 0.25, combine=True)
)
```

#### cboreHole(diameter: float, cboreDiameter: float, cboreDepth: float, depth: float | None = None, clean: bool = True) → T

Makes a counterbored hole for each item on the stack.

* **Parameters:**
  * **self** (*T*)
  * **diameter** (*float*) – the diameter of the hole
  * **cboreDiameter** (*float*) – the diameter of the cbore, must be greater than hole diameter
  * **cboreDepth** (*float > 0*) – depth of the counterbore
  * **depth** (*float > 0* *or* *None to drill thru the entire part*) – the depth of the hole
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
* **Return type:**
  *T*

The surface of the hole is at the current workplane plane.

One hole is created for each item on the stack.  A very common use case is to use a
construction rectangle to define the centers of a set of holes, like so:

```default
s = (
    Workplane()
    .box(2, 4, 0.5)
    .faces(">Z")
    .workplane()
    .rect(1.5, 3.5, forConstruction=True)
    .vertices()
    .cboreHole(0.125, 0.25, 0.125, depth=None)
)
```

This sample creates a plate with a set of holes at the corners.

**Plugin Note**: this is one example of the power of plugins. Counterbored holes are quite
time consuming to create, but are quite easily defined by users.

see [`cskHole()`](#cadquery.Workplane.cskHole) to make countersinks instead of counterbores

#### center(x: float, y: float) → T

Shift local coordinates to the specified location.

The location is specified in terms of local coordinates.

* **Parameters:**
  * **self** (*T*)
  * **x** (*float*) – the new x location
  * **y** (*float*) – the new y location
* **Returns:**
  the Workplane object, with the center adjusted.
* **Return type:**
  *T*

The current point is set to the new center.
This method is useful to adjust the center point after it has been created automatically on
a face, but not where you’d like it to be.

In this example, we adjust the workplane center to be at the corner of a cube, instead of
the center of a face, which is the default:

```default
# this workplane is centered at x=0.5,y=0.5, the center of the upper face
s = Workplane().box(1, 1, 1).faces(">Z").workplane()

s = s.center(-0.5, -0.5)  # move the center to the corner
t = s.circle(0.25).extrude(0.2)
assert t.faces().size() == 9  # a cube with a cylindrical nub at the top right corner
```

The result is a cube with a round boss on the corner

#### chamfer(length: float, length2: float | None = None) → T

Chamfers a solid on the selected edges.

The edges on the stack are chamfered. The solid to which the
edges belong must be in the parent chain of the selected
edges.

Optional parameter length2 can be supplied with a different
value than length for a chamfer that is shorter on one side
longer on the other side.

* **Parameters:**
  * **self** (*T*)
  * **length** (*float*) – the length of the chamfer, must be greater than zero
  * **length2** (*float* *|* *None*) – optional parameter for asymmetrical chamfer
* **Raises:**
  * **ValueError** – if at least one edge is not selected
  * **ValueError** – if the solid containing the edge is not in the chain
* **Returns:**
  CQ object with the resulting solid selected.
* **Return type:**
  *T*

This example will create a unit cube, with the top edges chamfered:

```default
s = Workplane("XY").box(1, 1, 1).faces("+Z").chamfer(0.1)
```

This example will create chamfers longer on the sides:

```default
s = Workplane("XY").box(1, 1, 1).faces("+Z").chamfer(0.2, 0.1)
```

#### circle(radius: float, forConstruction: bool = False) → T

Make a circle for each item on the stack.

* **Parameters:**
  * **self** (*T*)
  * **radius** (*float*) – radius of the circle
  * **forConstruction** (*true if the wires are for reference* *,* *false if they are creating
    part geometry*) – should the new wires be reference geometry only?
* **Returns:**
  a new CQ object with the created wires on the stack
* **Return type:**
  *T*

A common use case is to use a for-construction rectangle to define the centers of a
hole pattern:

```default
s = Workplane().rect(4.0, 4.0, forConstruction=True).vertices().circle(0.25)
```

Creates 4 circles at the corners of a square centered on the origin. Another common case is
to use successive circle() calls to create concentric circles.  This works because the
center of a circle is its reference point:

```default
s = Workplane().circle(2.0).circle(1.0)
```

Creates two concentric circles, which when extruded will form a ring.

Future Enhancements:
: better way to handle forConstruction
  project points not in the workplane plane onto the workplane plane

#### clean() → T

Cleans the current solid by removing unwanted edges from the
faces.

Normally you don’t have to call this function. It is
automatically called after each related operation. You can
disable this behavior with clean=False parameter if method
has any. In some cases this can improve performance
drastically but is generally dis-advised since it may break
some operations such as fillet.

Note that in some cases where lots of solid operations are
chained, clean() may actually improve performance since
the shape is ‘simplified’ at each step and thus next operation
is easier.

Also note that, due to limitation of the underlying engine,
clean may fail to produce a clean output in some cases such as
spherical faces.

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### close() → T

End construction, and attempt to build a closed wire.

* **Returns:**
  a CQ object with a completed wire on the stack, if possible.
* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

After 2D (or 3D) drafting with methods such as lineTo, threePointArc,
tangentArcPoint and polyline, it is necessary to convert the edges
produced by these into one or more wires.

When a set of edges is closed, CadQuery assumes it is safe to build
the group of edges into a wire. This example builds a simple triangular
prism:

```default
s = Workplane().lineTo(1, 0).lineTo(1, 1).close().extrude(0.2)
```

#### combine(clean: bool = True, glue: bool = False, tol: float | None = None) → T

Attempts to combine all of the items on the stack into a single item.

WARNING: all of the items must be of the same type!

* **Parameters:**
  * **self** (*T*)
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
  * **glue** (*bool*) – use a faster gluing mode for non-overlapping shapes (default False)
  * **tol** (*float* *|* *None*) – tolerance value for fuzzy bool operation mode (default None)
* **Raises:**
  ValueError if there are no items on the stack, or if they cannot be combined
* **Returns:**
  a CQ object with the resulting object selected
* **Return type:**
  *T*

#### combineSolids(otherCQToCombine: [Workplane](#cadquery.Workplane) | None = None) → [Workplane](#cadquery.Workplane)

!!!DEPRECATED!!! use union()
Combines all solids on the current stack, and any context object, together
into a single object.

After the operation, the returned solid is also the context solid.

* **Parameters:**
  **otherCQToCombine** ([*Workplane*](#cadquery.Workplane) *|* *None*) – another CadQuery to combine.
* **Returns:**
  a CQ object with the resulting combined solid on the stack.
* **Return type:**
  [*Workplane*](#cadquery.Workplane)

Most of the time, both objects will contain a single solid, which is
combined and returned on the stack of the new object.

#### compounds(selector: str | [Selector](#cadquery.selectors.Selector) | None = None, tag: str | None = None) → T

Select compounds on the stack, optionally filtering the selection. If there are multiple
objects on the stack, they are collected and a list of all the distinct compounds
is returned.

* **Parameters:**
  * **self** (*T*)
  * **selector** (*str* *|* [*Selector*](#cadquery.selectors.Selector) *|* *None*) – optional Selector object, or string selector expression
    (see [`StringSyntaxSelector`](#cadquery.StringSyntaxSelector))
  * **tag** (*str* *|* *None*) – if set, search the tagged object instead of self
* **Returns:**
  a CQ object whose stack contains all of the *distinct* compounds of *all* objects on
  the current stack, filtered by the provided selector.
* **Return type:**
  *T*

A compound contains multiple CAD primitives that resulted from a single operation, such as
a union, cut, split, or fillet.  Compounds can contain multiple edges, wires, or solids.

#### consolidateWires() → T

Attempt to consolidate wires on the stack into a single.
If possible, a new object with the results are returned.
if not possible, the wires remain separated

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### copyWorkplane(obj: T) → T

Copies the workplane from obj.

* **Parameters:**
  **obj** (*a CQ object*) – an object to copy the workplane from
* **Returns:**
  a CQ object with obj’s workplane
* **Return type:**
  *T*

#### cskHole(diameter: float, cskDiameter: float, cskAngle: float, depth: float | None = None, clean: bool = True) → T

Makes a countersunk hole for each item on the stack.

* **Parameters:**
  * **self** (*T*)
  * **diameter** (*float > 0*) – the diameter of the hole
  * **cskDiameter** (*float*) – the diameter of the countersink, must be greater than hole diameter
  * **cskAngle** (*float > 0*) – angle of the countersink, in degrees ( 82 is common )
  * **depth** (*float > 0* *or* *None to drill thru the entire part.*) – the depth of the hole
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
* **Return type:**
  *T*

The surface of the hole is at the current workplane.

One hole is created for each item on the stack.  A very common use case is to use a
construction rectangle to define the centers of a set of holes, like so:

```default
s = (
    Workplane()
    .box(2, 4, 0.5)
    .faces(">Z")
    .workplane()
    .rect(1.5, 3.5, forConstruction=True)
    .vertices()
    .cskHole(0.125, 0.25, 82, depth=None)
)
```

This sample creates a plate with a set of holes at the corners.

**Plugin Note**: this is one example of the power of plugins. CounterSunk holes are quite
time consuming to create, but are quite easily defined by users.

see [`cboreHole()`](#cadquery.Workplane.cboreHole) to make counterbores instead of countersinks

#### cut(toCut: [Workplane](#cadquery.Workplane) | [Solid](#cadquery.occ_impl.shapes.Solid) | [Compound](#cadquery.occ_impl.shapes.Compound), clean: bool = True, tol: float | None = None) → T

Cuts the provided solid from the current solid, IE, perform a solid subtraction.

* **Parameters:**
  * **self** (*T*)
  * **toCut** ([*Workplane*](#cadquery.Workplane) *|* [*Solid*](#cadquery.occ_impl.shapes.Solid) *|* [*Compound*](#cadquery.occ_impl.shapes.Compound)) – a solid object, or a Workplane object having a solid
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
  * **tol** (*float* *|* *None*) – tolerance value for fuzzy bool operation mode (default None)
* **Raises:**
  **ValueError** – if there is no solid to subtract from in the chain
* **Returns:**
  a Workplane object with the resulting object selected
* **Return type:**
  *T*

#### cutBlind(until: float | Literal['next', 'last'] | [Face](#cadquery.occ_impl.shapes.Face), clean: bool = True, both: bool = False, taper: float | None = None) → T

Use all un-extruded wires in the parent chain to create a prismatic cut from existing solid.

Specify either a distance value, or one of “next”, “last” to indicate a face to cut to.

Similar to extrude, except that a solid in the parent chain is required to remove material
from. cutBlind always removes material from a part.

* **Parameters:**
  * **self** (*T*)
  * **until** (*float* *|* *Literal* *[* *'next'* *,*  *'last'* *]*  *|*  *~cadquery.occ_impl.shapes.Face*) – The distance to cut to, normal to the workplane plane. When a negative float
    is passed the cut extends this far in the opposite direction to the normal of the plane
    (i.e in the solid). The string “next” cuts until the next face orthogonal to the wire
    normal.  “last” cuts to the last face. If an object of type Face is passed, then the cut
    will extend until this face.
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
  * **both** (*bool*) – cut in both directions symmetrically
  * **taper** (*float* *|* *None*) – angle for optional tapered extrusion
* **Raises:**
  **ValueError** – if there is no solid to subtract from in the chain
* **Returns:**
  a CQ object with the resulting object selected
* **Return type:**
  *T*

see [`cutThruAll()`](#cadquery.Workplane.cutThruAll) to cut material from the entire part

#### cutEach(fcn: Callable[[[Location](#cadquery.Location)], [Shape](#cadquery.occ_impl.shapes.Shape)], useLocalCoords: bool = False, clean: bool = True) → T

Evaluates the provided function at each point on the stack (ie, eachpoint)
and then cuts the result from the context solid.

* **Parameters:**
  * **self** (*T*)
  * **fcn** (*Callable* *[* *[*[*Location*](#cadquery.Location) *]* *,* [*Shape*](#cadquery.occ_impl.shapes.Shape) *]*) – a function suitable for use in the eachpoint method: ie, that accepts a vector
  * **useLocalCoords** (*bool*) – same as for [`eachpoint()`](#cadquery.Workplane.eachpoint)
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
* **Raises:**
  **ValueError** – if no solids or compounds are found in the stack or parent chain
* **Returns:**
  a CQ object that contains the resulting solid
* **Return type:**
  *T*

#### cutThruAll(clean: bool = True, taper: float = 0) → T

Use all un-extruded wires in the parent chain to create a prismatic cut from existing solid.
Cuts through all material in both normal directions of workplane.

Similar to extrude, except that a solid in the parent chain is required to remove material
from. cutThruAll always removes material from a part.

* **Parameters:**
  * **self** (*T*)
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
  * **taper** (*float*)
* **Raises:**
  * **ValueError** – if there is no solid to subtract from in the chain
  * **ValueError** – if there are no pending wires to cut with
* **Returns:**
  a CQ object with the resulting object selected
* **Return type:**
  *T*

see [`cutBlind()`](#cadquery.Workplane.cutBlind) to cut material to a limited depth

#### cylinder(height: float, radius: float, direct: ~typing.Tuple[float, float, float] | ~cadquery.occ_impl.geom.Vector = Vector: (0.0, 0.0, 1.0), angle: float = 360, centered: bool | ~typing.Tuple[bool, bool, bool] = True, combine: bool | ~typing.Literal['cut', 'a', 's'] = True, clean: bool = True) → T

Returns a cylinder with the specified radius and height for each point on the stack

* **Parameters:**
  * **self** (*T*)
  * **height** (*float*) – The height of the cylinder
  * **radius** (*float*) – The radius of the cylinder
  * **direct** (*A three-tuple*) – The direction axis for the creation of the cylinder
  * **angle** (*float > 0*) – The angle to sweep the cylinder arc through
  * **centered** (*bool* *|* *Tuple* *[**bool* *,* *bool* *,* *bool* *]*) – If True, the cylinder will be centered around the reference point. If False,
    the corner of a bounding box around the cylinder will be on the reference point and it
    will extend in the positive x, y and z directions. Can also use a 3-tuple to specify
    centering along each axis.
  * **combine** (*true to combine shapes* *,* *false otherwise*) – Whether the results should be combined with other solids on the stack
    (and each other)
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
* **Returns:**
  A cylinder object for each point on the stack
* **Return type:**
  *T*

One cylinder is created for each item on the current stack. If no items are on the stack, one
cylinder is created using the current workplane center.

If combine is true, the result will be a single object on the stack. If a solid was found
in the chain, the result is that solid with all cylinders produced fused onto it otherwise,
the result is the combination of all the produced cylinders.

If combine is false, the result will be a list of the cylinders produced.

#### each(callback: Callable[[[Vector](#cadquery.Vector) | [Location](#cadquery.Location) | [Shape](#cadquery.occ_impl.shapes.Shape) | [Sketch](#cadquery.Sketch)], [Shape](#cadquery.occ_impl.shapes.Shape)], useLocalCoordinates: bool = False, combine: bool | Literal['cut', 'a', 's'] = True, clean: bool = True) → T

Runs the provided function on each value in the stack, and collects the return values into
a new CQ object.

Special note: a newly created workplane always has its center point as its only stack item

* **Parameters:**
  * **self** (*T*)
  * **callBackFunction** – the function to call for each item on the current stack.
  * **useLocalCoordinates** (*bool*) – should  values be converted from local coordinates first?
  * **combine** (*bool* *|* *Literal* *[* *'cut'* *,*  *'a'* *,*  *'s'* *]*) – True or “a” to combine the resulting solid with parent solids if found,
    “cut” or “s” to remove the resulting solid from the parent solids if found.
    False to keep the resulting solid separated from the parent solids.
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
  * **callback** (*Callable* *[* *[*[*Vector*](#cadquery.Vector) *|* [*Location*](#cadquery.Location) *|* [*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Sketch*](#cadquery.Sketch) *]* *,* [*Shape*](#cadquery.occ_impl.shapes.Shape) *]*)
* **Return type:**
  *T*

The callback function must accept one argument, which is the item on the stack, and return
one object, which is collected. If the function returns None, nothing is added to the stack.
The object passed into the callBackFunction is potentially transformed to local coordinates,
if useLocalCoordinates is true

useLocalCoordinates is very useful for plugin developers.

If false, the callback function is assumed to be working in global coordinates.  Objects
created are added as-is, and objects passed into the function are sent in using global
coordinates

If true, the calling function is assumed to be  working in local coordinates.  Objects are
transformed to local coordinates before they are passed into the callback method, and result
objects are transformed to global coordinates after they are returned.

This allows plugin developers to create objects in local coordinates, without worrying
about the fact that the working plane is different than the global coordinate system.

TODO: wrapper object for Wire will clean up forConstruction flag everywhere

#### eachpoint(arg: [Shape](#cadquery.occ_impl.shapes.Shape) | [Workplane](#cadquery.Workplane) | Callable[[[Location](#cadquery.Location)], [Shape](#cadquery.occ_impl.shapes.Shape)], useLocalCoordinates: bool = False, combine: bool | Literal['cut', 'a', 's'] = False, clean: bool = True) → T

Same as each(), except arg is translated by the positions on the stack. If arg is a callback function, then the function is called for each point on the stack, and the resulting shape is used.
:return: CadQuery object which contains a list of  vectors (points ) on its stack.

* **Parameters:**
  * **self** (*T*)
  * **useLocalCoordinates** (*bool*) – should points be in local or global coordinates
  * **combine** (*bool* *|* *Literal* *[* *'cut'* *,*  *'a'* *,*  *'s'* *]*) – True or “a” to combine the resulting solid with parent solids if found,
    “cut” or “s” to remove the resulting solid from the parent solids if found.
    False to keep the resulting solid separated from the parent solids.
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
  * **arg** ([*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Workplane*](#cadquery.Workplane) *|* *Callable* *[* *[*[*Location*](#cadquery.Location) *]* *,* [*Shape*](#cadquery.occ_impl.shapes.Shape) *]*)
* **Return type:**
  *T*

The resulting object has a point on the stack for each object on the original stack.
Vertices and points remain a point.  Faces, Wires, Solids, Edges, and Shells are converted
to a point by using their center of mass.

If the stack has zero length, a single point is returned, which is the center of the current
workplane/coordinate system

#### edges(selector: str | [Selector](#cadquery.selectors.Selector) | None = None, tag: str | None = None) → T

Select the edges of objects on the stack, optionally filtering the selection. If there are
multiple objects on the stack, the edges of all objects are collected and a list of all the
distinct edges is returned.

* **Parameters:**
  * **self** (*T*)
  * **selector** (*str* *|* [*Selector*](#cadquery.selectors.Selector) *|* *None*) – optional Selector object, or string selector expression
    (see [`StringSyntaxSelector`](#cadquery.StringSyntaxSelector))
  * **tag** (*str* *|* *None*) – if set, search the tagged object instead of self
* **Returns:**
  a CQ object whose stack contains all of the *distinct* edges of *all* objects on
  the current stack, filtered by the provided selector.
* **Return type:**
  *T*

If there are no edges for any objects on the current stack, an empty CQ object is returned

The typical use is to select the edges of a single object on the stack. For example:

```default
Workplane().box(1, 1, 1).faces("+Z").edges().size()
```

returns 4, because the topmost face of a cube will contain four edges. Similarly:

```default
Workplane().box(1, 1, 1).edges().size()
```

returns 12, because a cube has a total of 12 edges, And:

```default
Workplane().box(1, 1, 1).edges("|Z").size()
```

returns 4, because a cube has 4 edges parallel to the z direction

#### ellipse(x_radius: float, y_radius: float, rotation_angle: float = 0.0, forConstruction: bool = False) → T

Make an ellipse for each item on the stack.

* **Parameters:**
  * **self** (*T*)
  * **x_radius** (*float*) – x radius of the ellipse (x-axis of plane the ellipse should lie in)
  * **y_radius** (*float*) – y radius of the ellipse (y-axis of plane the ellipse should lie in)
  * **rotation_angle** (*float*) – angle to rotate the ellipse
  * **forConstruction** (*true if the wires are for reference* *,* *false if they are creating
    part geometry*) – should the new wires be reference geometry only?
* **Returns:**
  a new CQ object with the created wires on the stack
* **Return type:**
  *T*

*NOTE* Due to a bug in opencascade ([https://tracker.dev.opencascade.org/view.php?id=31290](https://tracker.dev.opencascade.org/view.php?id=31290))
the center of mass (equals center for next shape) is shifted. To create concentric ellipses
use:

```default
Workplane("XY").center(10, 20).ellipse(100, 10).center(0, 0).ellipse(50, 5)
```

#### ellipseArc(x_radius: float, y_radius: float, angle1: float = 360, angle2: float = 360, rotation_angle: float = 0.0, sense: Literal[-1, 1] = 1, forConstruction: bool = False, startAtCurrent: bool = True, makeWire: bool = False) → T

Draw an elliptical arc with x and y radiuses either with start point at current point or
or current point being the center of the arc

* **Parameters:**
  * **self** (*T*)
  * **x_radius** (*float*) – x radius of the ellipse (along the x-axis of plane the ellipse should lie in)
  * **y_radius** (*float*) – y radius of the ellipse (along the y-axis of plane the ellipse should lie in)
  * **angle1** (*float*) – start angle of arc
  * **angle2** (*float*) – end angle of arc (angle2 == angle1 return closed ellipse = default)
  * **rotation_angle** (*float*) – angle to rotate the created ellipse / arc
  * **sense** (*Literal* *[* *-1* *,* *1* *]*) – clockwise (-1) or counter clockwise (1)
  * **startAtCurrent** (*bool*) – True: start point of arc is moved to current point; False: center of
    arc is on current point
  * **makeWire** (*bool*) – convert the resulting arc edge to a wire
  * **forConstruction** (*bool*)
* **Return type:**
  *T*

#### end(n: int = 1) → [Workplane](#cadquery.Workplane)

Return the nth parent of this CQ element

* **Parameters:**
  **n** (*int*) – number of ancestor to return (default: 1)
* **Return type:**
  a CQ object
* **Raises:**
  ValueError if there are no more parents in the chain.

For example:

```default
CQ(obj).faces("+Z").vertices().end()
```

will return the same as:

```default
CQ(obj).faces("+Z")
```

#### export(fname: str, tolerance: float = 0.1, angularTolerance: float = 0.1, opt: Dict[str, Any] | None = None) → T

Export Workplane to file.

* **Parameters:**
  * **self** (*T*)
  * **path** – Filename.
  * **tolerance** (*float*) – the deflection tolerance, in model units. Default 0.1.
  * **angularTolerance** (*float*) – the angular tolerance, in radians. Default 0.1.
  * **opt** (*Dict* *[**str* *,* *Any* *]*  *|* *None*) – additional options passed to the specific exporter. Default None.
  * **fname** (*str*)
* **Returns:**
  Self.
* **Return type:**
  *T*

#### exportSvg(fileName: str) → None

Exports the first item on the stack as an SVG file

For testing purposes mainly.

* **Parameters:**
  **fileName** (*str*) – the filename to export, absolute path to the file
* **Return type:**
  None

#### extrude(until: float | Literal['next', 'last'] | [Face](#cadquery.occ_impl.shapes.Face), combine: bool | Literal['cut', 'a', 's'] = True, clean: bool = True, both: bool = False, taper: float | None = None) → T

Use all un-extruded wires in the parent chain to create a prismatic solid.

* **Parameters:**
  * **self** (*T*)
  * **until** (*float* *|* *Literal* *[* *'next'* *,*  *'last'* *]*  *|*  *~cadquery.occ_impl.shapes.Face*) – The distance to extrude, normal to the workplane plane. When a float is
    passed, the extrusion extends this far and a negative value is in the opposite direction
    to the normal of the plane. The string “next” extrudes until the next face orthogonal to
    the wire normal. “last” extrudes to the last face. If a object of type Face is passed then
    the extrusion will extend until this face. **Note that the Workplane must contain a Solid for extruding to a given face.**
  * **combine** (*bool* *|* *Literal* *[* *'cut'* *,*  *'a'* *,*  *'s'* *]*) – True or “a” to combine the resulting solid with parent solids if found,
    “cut” or “s” to remove the resulting solid from the parent solids if found.
    False to keep the resulting solid separated from the parent solids.
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
  * **both** (*bool*) – extrude in both directions symmetrically
  * **taper** (*float* *|* *None*) – angle for optional tapered extrusion
* **Returns:**
  a CQ object with the resulting solid selected.
* **Return type:**
  *T*

The returned object is always a CQ object, and depends on whether combine is True, and
whether a context solid is already defined:

* if combine is False, the new value is pushed onto the stack. Note that when extruding
  : until a specified face, combine can not be False
* if combine is true, the value is combined with the context solid if it exists,
  : and the resulting solid becomes the new context solid.

#### faces(selector: str | [Selector](#cadquery.selectors.Selector) | None = None, tag: str | None = None) → T

Select the faces of objects on the stack, optionally filtering the selection. If there are
multiple objects on the stack, the faces of all objects are collected and a list of all the
distinct faces is returned.

* **Parameters:**
  * **self** (*T*)
  * **selector** (*str* *|* [*Selector*](#cadquery.selectors.Selector) *|* *None*) – optional Selector object, or string selector expression
    (see [`StringSyntaxSelector`](#cadquery.StringSyntaxSelector))
  * **tag** (*str* *|* *None*) – if set, search the tagged object instead of self
* **Returns:**
  a CQ object whose stack contains all of the *distinct* faces of *all* objects on
  the current stack, filtered by the provided selector.
* **Return type:**
  *T*

If there are no faces for any objects on the current stack, an empty CQ object
is returned.

The typical use is to select the faces of a single object on the stack. For example:

```default
Workplane().box(1, 1, 1).faces("+Z").size()
```

returns 1, because a cube has one face with a normal in the +Z direction. Similarly:

```default
Workplane().box(1, 1, 1).faces().size()
```

returns 6, because a cube has a total of 6 faces, And:

```default
Workplane().box(1, 1, 1).faces("|Z").size()
```

returns 2, because a cube has 2 faces having normals parallel to the z direction

#### fillet(radius: float) → T

Fillets a solid on the selected edges.

The edges on the stack are filleted. The solid to which the edges belong must be in the
parent chain of the selected edges.

* **Parameters:**
  * **self** (*T*)
  * **radius** (*float*) – the radius of the fillet, must be > zero
* **Raises:**
  * **ValueError** – if at least one edge is not selected
  * **ValueError** – if the solid containing the edge is not in the chain
* **Returns:**
  CQ object with the resulting solid selected.
* **Return type:**
  *T*

This example will create a unit cube, with the top edges filleted:

```default
s = Workplane().box(1, 1, 1).faces("+Z").edges().fillet(0.1)
```

#### filter(f: Callable[[[Vector](#cadquery.Vector) | [Location](#cadquery.Location) | [Shape](#cadquery.occ_impl.shapes.Shape) | [Sketch](#cadquery.Sketch)], bool]) → T

Filter items using a boolean predicate.

* **Parameters:**
  * **self** (*T*)
  * **f** (*Callable* *[* *[*[*Vector*](#cadquery.Vector) *|* [*Location*](#cadquery.Location) *|* [*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Sketch*](#cadquery.Sketch) *]* *,* *bool* *]*) – Callable to be used for filtering.
* **Returns:**
  Workplane object with filtered items.
* **Return type:**
  *T*

#### findFace(searchStack: bool = True, searchParents: bool = True) → [Face](#cadquery.occ_impl.shapes.Face)

Finds the first face object in the chain, searching from the current node
backwards through parents until one is found.

* **Parameters:**
  * **searchStack** (*bool*) – should objects on the stack be searched first.
  * **searchParents** (*bool*) – should parents be searched?
* **Returns:**
  A face or None if no face is found.
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### findSolid(searchStack: bool = True, searchParents: bool = True) → [Solid](#cadquery.occ_impl.shapes.Solid) | [Compound](#cadquery.occ_impl.shapes.Compound)

Finds the first solid object in the chain, searching from the current node
backwards through parents until one is found.

* **Parameters:**
  * **searchStack** (*bool*) – should objects on the stack be searched first?
  * **searchParents** (*bool*) – should parents be searched?
* **Raises:**
  **ValueError** – if no solid is found
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid) | [*Compound*](#cadquery.occ_impl.shapes.Compound)

This function is very important for chains that are modifying a single parent object,
most often a solid.

Most of the time, a chain defines or selects a solid, and then modifies it using workplanes
or other operations.

Plugin Developers should make use of this method to find the solid that should be modified,
if the plugin implements a unary operation, or if the operation will automatically merge its
results with an object already on the stack.

#### first() → T

Return the first item on the stack

* **Returns:**
  the first item on the stack.
* **Return type:**
  a CQ object
* **Parameters:**
  **self** (*T*)

#### hLine(distance: float, forConstruction: bool = False) → T

Make a horizontal line from the current point the provided distance

* **Parameters:**
  * **self** (*T*)
  * **distance** (*float*) – 
    1. distance from current point
  * **forConstruction** (*bool*)
* **Returns:**
  the Workplane object with the current point at the end of the new line
* **Return type:**
  *T*

#### hLineTo(xCoord: float, forConstruction: bool = False) → T

Make a horizontal line from the current point to the provided x coordinate.

Useful if it is more convenient to specify the end location rather than distance,
as in [`hLine()`](#cadquery.Workplane.hLine)

* **Parameters:**
  * **self** (*T*)
  * **xCoord** (*float*) – x coordinate for the end of the line
  * **forConstruction** (*bool*)
* **Returns:**
  the Workplane object with the current point at the end of the new line
* **Return type:**
  *T*

#### hole(diameter: float, depth: float | None = None, clean: bool = True) → T

Makes a hole for each item on the stack.

* **Parameters:**
  * **self** (*T*)
  * **diameter** (*float*) – the diameter of the hole
  * **depth** (*float > 0* *or* *None to drill thru the entire part.*) – the depth of the hole
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
* **Return type:**
  *T*

The surface of the hole is at the current workplane.

One hole is created for each item on the stack.  A very common use case is to use a
construction rectangle to define the centers of a set of holes, like so:

```default
s = (
    Workplane()
    .box(2, 4, 0.5)
    .faces(">Z")
    .workplane()
    .rect(1.5, 3.5, forConstruction=True)
    .vertices()
    .hole(0.125, 82)
)
```

This sample creates a plate with a set of holes at the corners.

**Plugin Note**: this is one example of the power of plugins. CounterSunk holes are quite
time consuming to create, but are quite easily defined by users.

see [`cboreHole()`](#cadquery.Workplane.cboreHole) and [`cskHole()`](#cadquery.Workplane.cskHole) to make counterbores or countersinks

#### interpPlate(surf_edges: Sequence[Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector)] | Sequence[[Edge](#cadquery.occ_impl.shapes.Edge) | [Wire](#cadquery.occ_impl.shapes.Wire)] | [Workplane](#cadquery.Workplane), surf_pts: Sequence[Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector)] = [], thickness: float = 0, combine: bool | Literal['cut', 'a', 's'] = False, clean: bool = True, degree: int = 3, nbPtsOnCur: int = 15, nbIter: int = 2, anisotropy: bool = False, tol2d: float = 1e-05, tol3d: float = 0.0001, tolAng: float = 0.01, tolCurv: float = 0.1, maxDeg: int = 8, maxSegments: int = 9) → T

Returns a plate surface that is ‘thickness’ thick, enclosed by ‘surf_edge_pts’ points, and going
through ‘surf_pts’ points.  Using pushPoints directly with interpPlate and combine=True, can be
very resource intensive depending on the complexity of the shape. In this case set combine=False.

* **Parameters:**
  * **self** (*T*)
  * **surf_edges** (*Sequence* *[**Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *]*  *|* *Sequence* *[*[*Edge*](#cadquery.occ_impl.shapes.Edge) *|* [*Wire*](#cadquery.occ_impl.shapes.Wire) *]*  *|* [*Workplane*](#cadquery.Workplane)) – list of [x,y,z] ordered coordinates or list of ordered or unordered edges, wires
  * **surf_pts** (*Sequence* *[**Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *]*) – list of points (uses only edges if [])
  * **thickness** (*float*) – value may be negative or positive depending on thickening direction (2D surface if 0)
  * **combine** (*bool* *|* *Literal* *[* *'cut'* *,*  *'a'* *,*  *'s'* *]*) – should the results be combined with other solids on the stack (and each other)?
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
  * **degree** (*int*) – >= 2
  * **nbPtsOnCur** (*int*) – number of points on curve >= 15
  * **nbIter** (*int*) – number of iterations >= 2
  * **anisotropy** (*bool*) – = bool Anisotropy
  * **tol2d** (*float*) – 2D tolerance
  * **tol3d** (*float*) – 3D tolerance
  * **tolAng** (*float*) – angular tolerance
  * **tolCurv** (*float*) – tolerance for curvature
  * **maxDeg** (*int*) – highest polynomial degree >= 2
  * **maxSegments** (*int*) – greatest number of segments >= 2
* **Return type:**
  *T*

#### intersect(toIntersect: [Workplane](#cadquery.Workplane) | [Solid](#cadquery.occ_impl.shapes.Solid) | [Compound](#cadquery.occ_impl.shapes.Compound), clean: bool = True, tol: float | None = None) → T

Intersects the provided solid from the current solid.

* **Parameters:**
  * **self** (*T*)
  * **toIntersect** ([*Workplane*](#cadquery.Workplane) *|* [*Solid*](#cadquery.occ_impl.shapes.Solid) *|* [*Compound*](#cadquery.occ_impl.shapes.Compound)) – a solid object, or a Workplane object having a solid
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
  * **tol** (*float* *|* *None*) – tolerance value for fuzzy bool operation mode (default None)
* **Raises:**
  **ValueError** – if there is no solid to intersect with in the chain
* **Returns:**
  a Workplane object with the resulting object selected
* **Return type:**
  *T*

#### invoke(f: Callable[[T], T] | Callable[[T], None] | Callable[[], None]) → T

Invoke a callable mapping Workplane to Workplane or None. Supports also
callables that take no arguments such as breakpoint. Returns self if callable
returns None.

* **Parameters:**
  * **self** (*T*)
  * **f** (*Callable* *[* *[**T* *]* *,* *T* *]*  *|* *Callable* *[* *[**T* *]* *,* *None* *]*  *|* *Callable* *[* *[* *]* *,* *None* *]*) – Callable to be invoked.
* **Returns:**
  Workplane object.
* **Return type:**
  *T*

#### item(i: int) → T

Return the ith item on the stack.

* **Return type:**
  a CQ object
* **Parameters:**
  * **self** (*T*)
  * **i** (*int*)

#### largestDimension() → float

Finds the largest dimension in the stack.

Used internally to create thru features, this is how you can compute
how long or wide a feature must be to make sure to cut through all of the material

* **Raises:**
  **ValueError** – if no solids or compounds are found
* **Returns:**
  A value representing the largest dimension of the first solid on the stack
* **Return type:**
  float

#### last() → T

Return the last item on the stack.

* **Return type:**
  a CQ object
* **Parameters:**
  **self** (*T*)

#### line(xDist: float, yDist: float, forConstruction: bool = False) → T

Make a line from the current point to the provided point, using
dimensions relative to the current point

* **Parameters:**
  * **self** (*T*)
  * **xDist** (*float*) – x distance from current point
  * **yDist** (*float*) – y distance from current point
  * **forConstruction** (*bool*)
* **Returns:**
  the workplane object with the current point at the end of the new line
* **Return type:**
  *T*

see [`lineTo()`](#cadquery.Workplane.lineTo) if you want to use absolute coordinates to make a line instead.

#### lineTo(x: float, y: float, forConstruction: bool = False) → T

Make a line from the current point to the provided point

* **Parameters:**
  * **self** (*T*)
  * **x** (*float*) – the x point, in workplane plane coordinates
  * **y** (*float*) – the y point, in workplane plane coordinates
  * **forConstruction** (*bool*)
* **Returns:**
  the Workplane object with the current point at the end of the new line
* **Return type:**
  *T*

See [`line()`](#cadquery.Workplane.line) if you want to use relative dimensions to make a line instead.

#### loft(ruled: bool = False, combine: bool | Literal['cut', 'a', 's'] = True, clean: bool = True) → T

Make a lofted solid, through the set of wires.

* **Parameters:**
  * **self** (*T*)
  * **ruled** (*bool*) – When set to True connects each section linearly and without continuity
  * **combine** (*bool* *|* *Literal* *[* *'cut'* *,*  *'a'* *,*  *'s'* *]*) – True or “a” to combine the resulting solid with parent solids if found,
    “cut” or “s” to remove the resulting solid from the parent solids if found.
    False to keep the resulting solid separated from the parent solids.
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
* **Returns:**
  a Workplane object containing the created loft
* **Return type:**
  *T*

#### map(f: Callable[[[Vector](#cadquery.Vector) | [Location](#cadquery.Location) | [Shape](#cadquery.occ_impl.shapes.Shape) | [Sketch](#cadquery.Sketch)], [Vector](#cadquery.Vector) | [Location](#cadquery.Location) | [Shape](#cadquery.occ_impl.shapes.Shape) | [Sketch](#cadquery.Sketch)]) → T

Apply a callable to every item separately.

* **Parameters:**
  * **self** (*T*)
  * **f** (*Callable* *[* *[*[*Vector*](#cadquery.Vector) *|* [*Location*](#cadquery.Location) *|* [*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Sketch*](#cadquery.Sketch) *]* *,* [*Vector*](#cadquery.Vector) *|* [*Location*](#cadquery.Location) *|* [*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Sketch*](#cadquery.Sketch) *]*) – Callable to be applied to every item separately.
* **Returns:**
  Workplane object with f applied to all items.
* **Return type:**
  *T*

#### mirror(mirrorPlane: Literal['XY', 'YX', 'XZ', 'ZX', 'YZ', 'ZY'] | Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector) | [Face](#cadquery.occ_impl.shapes.Face) | [Workplane](#cadquery.Workplane) = 'XY', basePointVector: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector) | None = None, union: bool = False) → T

Mirror a single CQ object.

* **Parameters:**
  * **self** (*T*)
  * **mirrorPlane** (*string* *,* *one* *of*  *"XY"* *,*  *"YX"* *,*  *"XZ"* *,*  *"ZX"* *,*  *"YZ"* *,*  *"ZY" the planes*
    *or* *the normal vector* *of* *the plane eg* *(**1* *,**0* *,**0* *) or* *a Face object*) – the plane to mirror about
  * **basePointVector** (*Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *|* *None*) – the base point to mirror about (this is overwritten if a Face is passed)
  * **union** (*bool*) – If true will perform a union operation on the mirrored object
* **Return type:**
  *T*

#### mirrorX() → T

Mirror entities around the x axis of the workplane plane.

* **Returns:**
  a new object with any free edges consolidated into as few wires as possible.
* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

All free edges are collected into a wire, and then the wire is mirrored,
and finally joined into a new wire

Typically used to make creating wires with symmetry easier.

#### mirrorY() → T

Mirror entities around the y axis of the workplane plane.

* **Returns:**
  a new object with any free edges consolidated into as few wires as possible.
* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

All free edges are collected into a wire, and then the wire is mirrored,
and finally joined into a new wire

Typically used to make creating wires with symmetry easier. This line of code:

```default
s = Workplane().lineTo(2, 2).threePointArc((3, 1), (2, 0)).mirrorX().extrude(0.25)
```

Produces a flat, heart shaped object

#### move(xDist: float = 0, yDist: float = 0) → T

Move the specified distance from the current point, without drawing.

* **Parameters:**
  * **self** (*T*)
  * **xDist** (*float* *, or* *none for zero*) – desired x distance, in local coordinates
  * **yDist** (*float* *, or* *none for zero.*) – desired y distance, in local coordinates
* **Return type:**
  *T*

Not to be confused with [`center()`](#cadquery.Workplane.center), which moves the center of the entire
workplane, this method only moves the current point ( and therefore does not affect objects
already drawn ).

See [`moveTo()`](#cadquery.Workplane.moveTo) to do the same thing but using absolute coordinates

#### moveTo(x: float = 0, y: float = 0) → T

Move to the specified point, without drawing.

* **Parameters:**
  * **self** (*T*)
  * **x** (*float* *, or* *none for zero*) – desired x location, in local coordinates
  * **y** (*float* *, or* *none for zero.*) – desired y location, in local coordinates
* **Return type:**
  *T*

Not to be confused with [`center()`](#cadquery.Workplane.center), which moves the center of the entire
workplane, this method only moves the current point ( and therefore does not affect objects
already drawn ).

See [`move()`](#cadquery.Workplane.move) to do the same thing but using relative dimensions

#### newObject(objlist: Iterable[[Vector](#cadquery.Vector) | [Location](#cadquery.Location) | [Shape](#cadquery.occ_impl.shapes.Shape) | [Sketch](#cadquery.Sketch)]) → T

Create a new workplane object from this one.

Overrides CQ.newObject, and should be used by extensions, plugins, and
subclasses to create new objects.

* **Parameters:**
  * **self** (*T*)
  * **objlist** (*a list* *of* *CAD primitives*) – new objects to put on the stack
* **Returns:**
  a new Workplane object with the current workplane as a parent.
* **Return type:**
  *T*

#### offset2D(d: float, kind: Literal['arc', 'intersection', 'tangent'] = 'arc', forConstruction: bool = False) → T

Creates a 2D offset wire.

* **Parameters:**
  * **self** (*T*)
  * **d** (*float*) – thickness. Negative thickness denotes offset to inside.
  * **kind** (*Literal* *[* *'arc'* *,*  *'intersection'* *,*  *'tangent'* *]*) – offset kind. Use “arc” for rounded and “intersection” for sharp edges (default: “arc”)
  * **forConstruction** (*bool*) – Should the result be added to pending wires?
* **Returns:**
  CQ object with resulting wire(s).
* **Return type:**
  *T*

#### parametricCurve(func: Callable[[float], Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector)], N: int = 400, start: float = 0, stop: float = 1, tol: float = 1e-06, minDeg: int = 1, maxDeg: int = 6, smoothing: Tuple[float, float, float] | None = (1, 1, 1), makeWire: bool = True) → T

Create a spline curve approximating the provided function.

* **Parameters:**
  * **self** (*T*)
  * **func** (*float -->* *(**float* *,**float* *,**float* *)*) – function f(t) that will generate (x,y,z) pairs
  * **N** (*int*) – number of points for discretization
  * **start** (*float*) – starting value of the parameter t
  * **stop** (*float*) – final value of the parameter t
  * **tol** (*float*) – tolerance of the algorithm (default: 1e-6)
  * **minDeg** (*int*) – minimum spline degree (default: 1)
  * **maxDeg** (*int*) – maximum spline degree (default: 6)
  * **smoothing** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* *None*) – optional parameters for the variational smoothing algorithm (default: (1,1,1))
  * **makeWire** (*bool*) – convert the resulting spline edge to a wire
* **Returns:**
  a Workplane object with the current point unchanged
* **Return type:**
  *T*

#### parametricSurface(func: Callable[[float, float], Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector)], N: int = 20, start: float = 0, stop: float = 1, tol: float = 0.01, minDeg: int = 1, maxDeg: int = 6, smoothing: Tuple[float, float, float] | None = (1, 1, 1)) → T

Create a spline surface approximating the provided function.

* **Parameters:**
  * **self** (*T*)
  * **func** ( *(**float* *,**float* *)*  *-->* *(**float* *,**float* *,**float* *)*) – function f(u,v) that will generate (x,y,z) pairs
  * **N** (*int*) – number of points for discretization in one direction
  * **start** (*float*) – starting value of the parameters u,v
  * **stop** (*float*) – final value of the parameters u,v
  * **tol** (*float*) – tolerance used by the approximation algorithm (default: 1e-3)
  * **minDeg** (*int*) – minimum spline degree (default: 1)
  * **maxDeg** (*int*) – maximum spline degree (default: 3)
  * **smoothing** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* *None*) – optional parameters for the variational smoothing algorithm (default: (1,1,1))
* **Returns:**
  a Workplane object with the current point unchanged
* **Return type:**
  *T*

This method might be unstable and may require tuning of the tol parameter.

#### placeSketch(\*sketches: [Sketch](#cadquery.Sketch)) → T

Place the provided sketch(es) based on the current items on the stack.

* **Returns:**
  Workplane object with the sketch added.
* **Parameters:**
  * **self** (*T*)
  * **sketches** ([*Sketch*](#cadquery.Sketch))
* **Return type:**
  *T*

#### polarArray(radius: float, startAngle: float, angle: float, count: int, fill: bool = True, rotate: bool = True) → T

Creates a polar array of points and pushes them onto the stack.
The zero degree reference angle is located along the local X-axis.

* **Parameters:**
  * **self** (*T*)
  * **radius** (*float*) – Radius of the array.
  * **startAngle** (*float*) – Starting angle (degrees) of array. Zero degrees is
    situated along the local X-axis.
  * **angle** (*float*) – The angle (degrees) to fill with elements. A positive
    value will fill in the counter-clockwise direction. If fill is
    False, angle is the angle between elements.
  * **count** (*int*) – Number of elements in array. (count >= 1)
  * **fill** (*bool*) – Interpret the angle as total if True (default: True).
  * **rotate** (*bool*) – Rotate every item (default: True).
* **Return type:**
  *T*

#### polarLine(distance: float, angle: float, forConstruction: bool = False) → T

Make a line of the given length, at the given angle from the current point

* **Parameters:**
  * **self** (*T*)
  * **distance** (*float*) – distance of the end of the line from the current point
  * **angle** (*float*) – angle of the vector to the end of the line with the x-axis
  * **forConstruction** (*bool*)
* **Returns:**
  the Workplane object with the current point at the end of the new line
* **Return type:**
  *T*

#### polarLineTo(distance: float, angle: float, forConstruction: bool = False) → T

Make a line from the current point to the given polar coordinates

Useful if it is more convenient to specify the end location rather than
the distance and angle from the current point

* **Parameters:**
  * **self** (*T*)
  * **distance** (*float*) – distance of the end of the line from the origin
  * **angle** (*float*) – angle of the vector to the end of the line with the x-axis
  * **forConstruction** (*bool*)
* **Returns:**
  the Workplane object with the current point at the end of the new line
* **Return type:**
  *T*

#### polygon(nSides: int, diameter: float, forConstruction: bool = False, circumscribed: bool = False) → T

Make a polygon for each item on the stack.

By default, each polygon is created by inscribing it in a circle of the
specified diameter, such that the first vertex is oriented in the x direction.
Alternatively, each polygon can be created by circumscribing it around
a circle of the specified diameter, such that the midpoint of the first edge
is oriented in the x direction. Circumscribed polygons are thus rotated by
pi/nSides radians relative to the inscribed polygon. This ensures the extent
of the polygon along the positive x-axis is always known.
This has the advantage of not requiring additional formulae for purposes such as
tiling on the x-axis (at least for even sided polygons).

* **Parameters:**
  * **self** (*T*)
  * **nSides** (*int*) – number of sides, must be >= 3
  * **diameter** (*float*) – the diameter of the circle for constructing the polygon
  * **circumscribed** (*true to create the polygon by circumscribing it about a circle* *,*
    *false to create the polygon by inscribing it in a circle*) – circumscribe the polygon about a circle
  * **forConstruction** (*bool*)
* **Returns:**
  a polygon wire
* **Return type:**
  *T*

#### polyline(listOfXYTuple: Sequence[Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector)], forConstruction: bool = False, includeCurrent: bool = False) → T

Create a polyline from a list of points

* **Parameters:**
  * **self** (*T*)
  * **listOfXYTuple** (*Sequence* *[**Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *]*) – a list of points in Workplane coordinates (2D or 3D)
  * **forConstruction** (*true if the edges are for reference* *,* *false if they are for creating geometry
    part geometry*) – whether or not the edges are used for reference
  * **includeCurrent** (*bool*) – use current point as a starting point of the polyline
* **Returns:**
  a new CQ object with a list of edges on the stack
* **Return type:**
  *T*

*NOTE* most commonly, the resulting wire should be closed.

#### pushPoints(pntList: Iterable[Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector) | [Location](#cadquery.Location)]) → T

Pushes a list of points onto the stack as vertices.
The points are in the 2D coordinate space of the workplane face

* **Parameters:**
  * **self** (*T*)
  * **pntList** (list of 2-tuples, in *local* coordinates) – a list of points to push onto the stack
* **Returns:**
  a new workplane with the desired points on the stack.
* **Return type:**
  *T*

A common use is to provide a list of points for a subsequent operation, such as creating
circles or holes. This example creates a cube, and then drills three holes through it,
based on three points:

```default
s = (
    Workplane()
    .box(1, 1, 1)
    .faces(">Z")
    .workplane()
    .pushPoints([(-0.3, 0.3), (0.3, 0.3), (0, 0)])
)
body = s.circle(0.05).cutThruAll()
```

Here the circle function operates on all three points, and is then extruded to create three
holes. See [`circle()`](#cadquery.Workplane.circle) for how it works.

#### radiusArc(endPoint: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector), radius: float, forConstruction: bool = False) → T

Draw an arc from the current point to endPoint with an arc defined by the radius.

* **Parameters:**
  * **self** (*T*)
  * **endPoint** (*2-tuple* *,* *in workplane coordinates*) – end point for the arc
  * **radius** (*float* *,* *the radius* *of* *the arc between start point and end point.*) – the radius of the arc
  * **forConstruction** (*bool*)
* **Returns:**
  a workplane with the current point at the end of the arc
* **Return type:**
  *T*

Given that a closed contour is drawn clockwise;
A positive radius means convex arc and negative radius means concave arc.

#### rarray(xSpacing: float, ySpacing: float, xCount: int, yCount: int, center: bool | Tuple[bool, bool] = True) → T

Creates an array of points and pushes them onto the stack.
If you want to position the array at another point, create another workplane
that is shifted to the position you would like to use as a reference

* **Parameters:**
  * **self** (*T*)
  * **xSpacing** (*float*) – spacing between points in the x direction ( must be >= 0)
  * **ySpacing** (*float*) – spacing between points in the y direction ( must be >= 0)
  * **xCount** (*int*) – number of points ( > 0 )
  * **yCount** (*int*) – number of points ( > 0 )
  * **center** (*bool* *|* *Tuple* *[**bool* *,* *bool* *]*) – If True, the array will be centered around the workplane center.
    If False, the lower corner will be on the reference point and the array will
    extend in the positive x and y directions. Can also use a 2-tuple to specify
    centering along each axis.
* **Return type:**
  *T*

#### rect(xLen: float, yLen: float, centered: bool | Tuple[bool, bool] = True, forConstruction: bool = False) → T

Make a rectangle for each item on the stack.

* **Parameters:**
  * **self** (*T*)
  * **xLen** (*float*) – length in the x direction (in workplane coordinates)
  * **yLen** (*float*) – length in the y direction (in workplane coordinates)
  * **centered** (*bool* *|* *Tuple* *[**bool* *,* *bool* *]*) – If True, the rectangle will be centered around the reference
    point. If False, the corner of the rectangle will be on the reference point and
    it will extend in the positive x and y directions. Can also use a 2-tuple to
    specify centering along each axis.
  * **forConstruction** (*true if the wires are for reference* *,* *false if they are creating part
    geometry*) – should the new wires be reference geometry only?
* **Returns:**
  a new CQ object with the created wires on the stack
* **Return type:**
  *T*

A common use case is to use a for-construction rectangle to define the centers of a hole
pattern:

```default
s = Workplane().rect(4.0, 4.0, forConstruction=True).vertices().circle(0.25)
```

Creates 4 circles at the corners of a square centered on the origin.

Negative values for xLen and yLen are permitted, although they only have an effect when
centered is False.

Future Enhancements:
: * project points not in the workplane plane onto the workplane plane

#### revolve(angleDegrees: float = 360.0, axisStart: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector) | None = None, axisEnd: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector) | None = None, combine: bool | Literal['cut', 'a', 's'] = True, clean: bool = True) → T

Use all un-revolved wires in the parent chain to create a solid.

* **Parameters:**
  * **self** (*T*)
  * **angleDegrees** (*float* *,* *anything less than 360 degrees will leave the shape open*) – the angle to revolve through.
  * **axisStart** (*Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *|* *None*) – the start point of the axis of rotation
  * **axisEnd** (*Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *|* *None*) – the end point of the axis of rotation
  * **combine** (*bool* *|* *Literal* *[* *'cut'* *,*  *'a'* *,*  *'s'* *]*) – True or “a” to combine the resulting solid with parent solids if found,
    “cut” or “s” to remove the resulting solid from the parent solids if found.
    False to keep the resulting solid separated from the parent solids.
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
* **Returns:**
  a CQ object with the resulting solid selected.
* **Return type:**
  *T*

The returned object is always a CQ object, and depends on whether combine is True, and
whether a context solid is already defined:

* if combine is False, the new value is pushed onto the stack.
* if combine is true, the value is combined with the context solid if it exists,
  and the resulting solid becomes the new context solid.

#### NOTE
Keep in mind that axisStart and axisEnd are defined relative to the current Workplane center position.
So if for example you want to revolve a circle centered at (10,0,0) around the Y axis, be sure to either [`move()`](#cadquery.Workplane.move) (or [`moveTo()`](#cadquery.Workplane.moveTo))
the current Workplane position or specify axisStart and axisEnd with the correct vector position.
In this example (0,0,0), (0,1,0) as axis coords would fail.

#### rotate(axisStartPoint: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector), axisEndPoint: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector), angleDegrees: float) → T

Returns a copy of all of the items on the stack rotated through and angle around the axis
of rotation.

* **Parameters:**
  * **self** (*T*)
  * **axisStartPoint** (*a 3-tuple* *of* *floats*) – The first point of the axis of rotation
  * **axisEndPoint** (*a 3-tuple* *of* *floats*) – The second point of the axis of rotation
  * **angleDegrees** (*float*) – the rotation angle, in degrees
* **Returns:**
  a CQ object
* **Return type:**
  *T*

#### rotateAboutCenter(axisEndPoint: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector), angleDegrees: float) → T

Rotates all items on the stack by the specified angle, about the specified axis

The center of rotation is a vector starting at the center of the object on the stack,
and ended at the specified point.

* **Parameters:**
  * **self** (*T*)
  * **axisEndPoint** (*a three-tuple in global coordinates*) – the second point of axis of rotation
  * **angleDegrees** (*float*) – the rotation angle, in degrees
* **Returns:**
  a CQ object, with all items rotated.
* **Return type:**
  *T*

WARNING: This version returns the same CQ object instead of a new one– the
old object is not accessible.

Future Enhancements:
: * A version of this method that returns a transformed copy, rather than modifying
    the originals
  * This method doesn’t expose a very good interface, because the axis of rotation
    could be inconsistent between multiple objects.  This is because the beginning
    of the axis is variable, while the end is fixed. This is fine when operating on
    one object, but is not cool for multiple.

#### sagittaArc(endPoint: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector), sag: float, forConstruction: bool = False) → T

Draw an arc from the current point to endPoint with an arc defined by the sag (sagitta).

* **Parameters:**
  * **self** (*T*)
  * **endPoint** (*2-tuple* *,* *in workplane coordinates*) – end point for the arc
  * **sag** (*float* *,* *perpendicular distance from arc center to arc baseline.*) – the sagitta of the arc
  * **forConstruction** (*bool*)
* **Returns:**
  a workplane with the current point at the end of the arc
* **Return type:**
  *T*

The sagitta is the distance from the center of the arc to the arc base.
Given that a closed contour is drawn clockwise;
A positive sagitta means convex arc and negative sagitta means concave arc.
See [https://en.wikipedia.org/wiki/Sagitta_(geometry)](https://en.wikipedia.org/wiki/Sagitta_(geometry)) for more information.

#### section(height: float = 0.0) → T

Slices current solid at the given height.

* **Parameters:**
  * **self** (*T*)
  * **height** (*float*) – height to slice at (default: 0)
* **Raises:**
  **ValueError** – if no solids or compounds are found
* **Returns:**
  a CQ object with the resulting face(s).
* **Return type:**
  *T*

#### shell(thickness: float, kind: Literal['arc', 'intersection'] = 'arc') → T

Remove the selected faces to create a shell of the specified thickness.

To shell, first create a solid, and *in the same chain* select the faces you wish to remove.

* **Parameters:**
  * **self** (*T*)
  * **thickness** (*float*) – thickness of the desired shell.
    Negative values shell inwards, positive values shell outwards.
  * **kind** (*Literal* *[* *'arc'* *,*  *'intersection'* *]*) – kind of join, arc or intersection (default: arc).
* **Raises:**
  **ValueError** – if the current stack contains objects that are not faces of a solid
  further up in the chain.
* **Returns:**
  a CQ object with the resulting shelled solid selected.
* **Return type:**
  *T*

This example will create a hollowed out unit cube, where the top most face is open,
and all other walls are 0.2 units thick:

```default
Workplane().box(1, 1, 1).faces("+Z").shell(0.2)
```

You can also select multiple faces at once. Here is an example that creates a three-walled
corner, by removing three faces of a cube:

```default
Workplane().box(10, 10, 10).faces(">Z or >X or <Y").shell(1)
```

**Note**:  When sharp edges are shelled inwards, they remain sharp corners, but **outward**
shells are automatically filleted (unless kind=”intersection”), because an outward offset
from a corner generates a radius.

#### shells(selector: str | [Selector](#cadquery.selectors.Selector) | None = None, tag: str | None = None) → T

Select the shells of objects on the stack, optionally filtering the selection. If there are
multiple objects on the stack, the shells of all objects are collected and a list of all the
distinct shells is returned.

* **Parameters:**
  * **self** (*T*)
  * **selector** (*str* *|* [*Selector*](#cadquery.selectors.Selector) *|* *None*) – optional Selector object, or string selector expression
    (see [`StringSyntaxSelector`](#cadquery.StringSyntaxSelector))
  * **tag** (*str* *|* *None*) – if set, search the tagged object instead of self
* **Returns:**
  a CQ object whose stack contains all of the *distinct* shells of *all* objects on
  the current stack, filtered by the provided selector.
* **Return type:**
  *T*

If there are no shells for any objects on the current stack, an empty CQ object is returned

Most solids will have a single shell, which represents the outer surface. A shell will
typically be composed of multiple faces.

#### siblings(kind: Literal['Vertex', 'Edge', 'Wire', 'Face', 'Shell', 'Solid', 'CompSolid', 'Compound'], level: int = 1, tag: str | None = None) → T

Select topological siblings.

* **Parameters:**
  * **self** (*T*)
  * **kind** (*Literal* *[* *'Vertex'* *,*  *'Edge'* *,*  *'Wire'* *,*  *'Face'* *,*  *'Shell'* *,*  *'Solid'* *,*  *'CompSolid'* *,*  *'Compound'* *]*) – kind of linking element, e.g. “Vertex” or “Edge”
  * **level** (*int*) – level of relation - how many elements of kind are in the link
  * **tag** (*str* *|* *None*) – if set, search the tagged object instead of self
* **Returns:**
  a Workplane object whose stack contains selected siblings.
* **Return type:**
  *T*

#### size() → int

Return the number of objects currently on the stack

* **Return type:**
  int

#### sketch() → [Sketch](#cadquery.Sketch)

Initialize and return a sketch

* **Returns:**
  Sketch object with the current workplane as a parent.
* **Parameters:**
  **self** (*T*)
* **Return type:**
  [*Sketch*](#cadquery.Sketch)

#### slot2D(length: float, diameter: float, angle: float = 0) → T

Creates a rounded slot for each point on the stack.

* **Parameters:**
  * **self** (*T*)
  * **diameter** (*float*) – desired diameter, or width, of slot
  * **length** (*float*) – desired end to end length of slot
  * **angle** (*float*) – angle of slot in degrees, with 0 being along x-axis
* **Returns:**
  a new CQ object with the created wires on the stack
* **Return type:**
  *T*

Can be used to create arrays of slots, such as in cooling applications:

```default
Workplane().box(10, 25, 1).rarray(1, 2, 1, 10).slot2D(8, 1, 0).cutThruAll()
```

#### solids(selector: str | [Selector](#cadquery.selectors.Selector) | None = None, tag: str | None = None) → T

Select the solids of objects on the stack, optionally filtering the selection. If there are
multiple objects on the stack, the solids of all objects are collected and a list of all the
distinct solids is returned.

* **Parameters:**
  * **self** (*T*)
  * **selector** (*str* *|* [*Selector*](#cadquery.selectors.Selector) *|* *None*) – optional Selector object, or string selector expression
    (see [`StringSyntaxSelector`](#cadquery.StringSyntaxSelector))
  * **tag** (*str* *|* *None*) – if set, search the tagged object instead of self
* **Returns:**
  a CQ object whose stack contains all of the *distinct* solids of *all* objects on
  the current stack, filtered by the provided selector.
* **Return type:**
  *T*

If there are no solids for any objects on the current stack, an empty CQ object is returned

The typical use is to select a single object on the stack. For example:

```default
Workplane().box(1, 1, 1).solids().size()
```

returns 1, because a cube consists of one solid.

It is possible for a single CQ object ( or even a single CAD primitive ) to contain
multiple solids.

#### sort(key: Callable[[[Vector](#cadquery.Vector) | [Location](#cadquery.Location) | [Shape](#cadquery.occ_impl.shapes.Shape) | [Sketch](#cadquery.Sketch)], Any]) → T

Sort items using a callable.

* **Parameters:**
  * **self** (*T*)
  * **key** (*Callable* *[* *[*[*Vector*](#cadquery.Vector) *|* [*Location*](#cadquery.Location) *|* [*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Sketch*](#cadquery.Sketch) *]* *,* *Any* *]*) – Callable to be used for sorting.
* **Returns:**
  Workplane object with items sorted.
* **Return type:**
  *T*

#### sphere(radius: float, direct: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector) = (0, 0, 1), angle1: float = -90, angle2: float = 90, angle3: float = 360, centered: bool | Tuple[bool, bool, bool] = True, combine: bool | Literal['cut', 'a', 's'] = True, clean: bool = True) → T

Returns a 3D sphere with the specified radius for each point on the stack.

* **Parameters:**
  * **self** (*T*)
  * **radius** (*float*) – The radius of the sphere
  * **direct** (*A three-tuple*) – The direction axis for the creation of the sphere
  * **angle1** (*float > 0*) – The first angle to sweep the sphere arc through
  * **angle2** (*float > 0*) – The second angle to sweep the sphere arc through
  * **angle3** (*float > 0*) – The third angle to sweep the sphere arc through
  * **centered** (*bool* *|* *Tuple* *[**bool* *,* *bool* *,* *bool* *]*) – If True, the sphere will be centered around the reference point. If False,
    the corner of a bounding box around the sphere will be on the reference point and it
    will extend in the positive x, y and z directions. Can also use a 3-tuple to specify
    centering along each axis.
  * **combine** (*true to combine shapes* *,* *false otherwise*) – Whether the results should be combined with other solids on the stack
    (and each other)
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
* **Returns:**
  A sphere object for each point on the stack
* **Return type:**
  *T*

One sphere is created for each item on the current stack. If no items are on the stack, one
box using the current workplane center is created.

If combine is true, the result will be a single object on the stack. If a solid was found
in the chain, the result is that solid with all spheres produced fused onto it otherwise,
the result is the combination of all the produced spheres.

If combine is false, the result will be a list of the spheres produced.

#### spline(listOfXYTuple: Iterable[Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector)], tangents: Sequence[Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector)] | None = None, periodic: bool = False, parameters: Sequence[float] | None = None, scale: bool = True, tol: float | None = None, forConstruction: bool = False, includeCurrent: bool = False, makeWire: bool = False) → T

Create a spline interpolated through the provided points (2D or 3D).

* **Parameters:**
  * **self** (*T*)
  * **listOfXYTuple** (*Iterable* *[**Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *]*) – points to interpolate through
  * **tangents** (*Sequence* *[**Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *]*  *|* *None*) – 

    vectors specifying the direction of the tangent to the
    curve at each of the specified interpolation points.

    If only 2 tangents are given, they will be used as the initial and
    final tangent.

    If some tangents are not specified (i.e., are None), no tangent
    constraint will be applied to the corresponding interpolation point.

    The spline will be C2 continuous at the interpolation points where
    no tangent constraint is specified, and C1 continuous at the points
    where a tangent constraint is specified.
  * **periodic** (*bool*) – creation of periodic curves
  * **parameters** (*Sequence* *[**float* *]*  *|* *None*) – 

    the value of the parameter at each interpolation point.
    (The interpolated curve is represented as a vector-valued function of a
    scalar parameter.)

    If periodic == True, then len(parameters) must be
    len(interpolation points) + 1, otherwise len(parameters) must be equal to
    len(interpolation points).
  * **scale** (*bool*) – 

    whether to scale the specified tangent vectors before
    interpolating.

    Each tangent is scaled, so it’s length is equal to the derivative of
    the Lagrange interpolated curve.

    I.e., set this to True, if you want to use only the direction of
    the tangent vectors specified by `tangents`, but not their magnitude.
  * **tol** (*float* *|* *None*) – 

    tolerance of the algorithm (consult OCC documentation)

    Used to check that the specified points are not too close to each
    other, and that tangent vectors are not too short. (In either case
    interpolation may fail.)

    Set to None to use the default tolerance.
  * **includeCurrent** (*bool*) – use current point as a starting point of the curve
  * **makeWire** (*bool*) – convert the resulting spline edge to a wire
  * **forConstruction** (*bool*)
* **Returns:**
  a Workplane object with the current point at the end of the spline
* **Return type:**
  *T*

The spline will begin at the current point, and end with the last point in the
XY tuple list.

This example creates a block with a spline for one side:

```default
s = Workplane(Plane.XY())
sPnts = [
    (2.75, 1.5),
    (2.5, 1.75),
    (2.0, 1.5),
    (1.5, 1.0),
    (1.0, 1.25),
    (0.5, 1.0),
    (0, 1.0),
]
r = s.lineTo(3.0, 0).lineTo(3.0, 1.0).spline(sPnts).close()
r = r.extrude(0.5)
```

*WARNING*  It is fairly easy to create a list of points
that cannot be correctly interpreted as a spline.

#### splineApprox(points: Iterable[Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector)], tol: float | None = 1e-06, minDeg: int = 1, maxDeg: int = 6, smoothing: Tuple[float, float, float] | None = (1, 1, 1), forConstruction: bool = False, includeCurrent: bool = False, makeWire: bool = False) → T

Create a spline interpolated through the provided points (2D or 3D).

* **Parameters:**
  * **self** (*T*)
  * **points** (*Iterable* *[**Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *]*) – points to interpolate through
  * **tol** (*float* *|* *None*) – tolerance of the algorithm (default: 1e-6)
  * **minDeg** (*int*) – minimum spline degree (default: 1)
  * **maxDeg** (*int*) – maximum spline degree (default: 6)
  * **smoothing** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* *None*) – optional parameters for the variational smoothing algorithm (default: (1,1,1))
  * **includeCurrent** (*bool*) – use current point as a starting point of the curve
  * **makeWire** (*bool*) – convert the resulting spline edge to a wire
  * **forConstruction** (*bool*)
* **Returns:**
  a Workplane object with the current point at the end of the spline
* **Return type:**
  *T*

*WARNING*  for advanced users.

#### split(\*args, \*\*kwargs) → T

Splits a solid on the stack into two parts, optionally keeping the separate parts.

* **Parameters:**
  * **self** (*T*)
  * **keepTop** (*bool*) – True to keep the top, False or None to discard it
  * **keepBottom** (*bool*) – True to keep the bottom, False or None to discard it
* **Raises:**
  * **ValueError** – if keepTop and keepBottom are both false.
  * **ValueError** – if there is no solid in the current stack or parent chain
* **Returns:**
  CQ object with the desired objects on the stack.
* **Return type:**
  *T*

The most common operation splits a solid and keeps one half. This sample creates
a split bushing:

```default
# drill a hole in the side
c = Workplane().box(1, 1, 1).faces(">Z").workplane().circle(0.25).cutThruAll()

# now cut it in half sideways
c = c.faces(">Y").workplane(-0.5).split(keepTop=True)
```

#### sweep(path: [Workplane](#cadquery.Workplane) | [Wire](#cadquery.occ_impl.shapes.Wire) | [Edge](#cadquery.occ_impl.shapes.Edge), multisection: bool = False, sweepAlongWires: bool | None = None, makeSolid: bool = True, isFrenet: bool = False, combine: bool | Literal['cut', 'a', 's'] = True, clean: bool = True, transition: Literal['right', 'round', 'transformed'] = 'right', normal: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector) | None = None, auxSpine: [Workplane](#cadquery.Workplane) | None = None) → T

Use all un-extruded wires in the parent chain to create a swept solid.

* **Parameters:**
  * **self** (*T*)
  * **path** ([*Workplane*](#cadquery.Workplane) *|* [*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Edge*](#cadquery.occ_impl.shapes.Edge)) – A wire along which the pending wires will be swept
  * **multiSection** – False to create multiple swept from wires on the chain along path.
    True to create only one solid swept along path with shape following the list of wires on the chain
  * **combine** (*bool* *|* *Literal* *[* *'cut'* *,*  *'a'* *,*  *'s'* *]*) – True or “a” to combine the resulting solid with parent solids if found,
    “cut” or “s” to remove the resulting solid from the parent solids if found.
    False to keep the resulting solid separated from the parent solids.
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
  * **transition** (*Literal* *[* *'right'* *,*  *'round'* *,*  *'transformed'* *]*) – handling of profile orientation at C1 path discontinuities. Possible values are {‘transformed’,’round’, ‘right’} (default: ‘right’).
  * **normal** (*Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *|* *None*) – optional fixed normal for extrusion
  * **auxSpine** ([*Workplane*](#cadquery.Workplane) *|* *None*) – a wire defining the binormal along the extrusion path
  * **multisection** (*bool*)
  * **sweepAlongWires** (*bool* *|* *None*)
  * **makeSolid** (*bool*)
  * **isFrenet** (*bool*)
* **Returns:**
  a CQ object with the resulting solid selected.
* **Return type:**
  *T*

#### tag(name: str) → T

Tags the current CQ object for later reference.

* **Parameters:**
  * **self** (*T*)
  * **name** (*str*) – the name to tag this object with
* **Returns:**
  self, a CQ object with tag applied
* **Return type:**
  *T*

#### tangentArcPoint(endpoint: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector), forConstruction: bool = False, relative: bool = True) → T

Draw an arc as a tangent from the end of the current edge to endpoint.

* **Parameters:**
  * **self** (*T*)
  * **endpoint** (*2-tuple* *,* *3-tuple* *or* [*Vector*](#cadquery.Vector)) – point for the arc to end at
  * **relative** (*bool*) – True if endpoint is specified relative to the current point, False if endpoint is in workplane coordinates
  * **forConstruction** (*bool*)
* **Returns:**
  a Workplane object with an arc on the stack
* **Return type:**
  *T*

Requires the the current first object on the stack is an Edge, as would
be the case after a lineTo operation or similar.

#### text(txt: str, fontsize: float, distance: float, cut: bool = True, combine: bool | Literal['cut', 'a', 's'] = False, clean: bool = True, font: str = 'Arial', fontPath: str | None = None, kind: Literal['regular', 'bold', 'italic'] = 'regular', halign: Literal['center', 'left', 'right'] = 'center', valign: Literal['center', 'top', 'bottom'] = 'center') → T

Returns a 3D text.

* **Parameters:**
  * **self** (*T*)
  * **txt** (*str*) – text to be rendered
  * **fontsize** (*float*) – size of the font in model units
  * **distance** (*float* *,* *negative means opposite the normal direction*) – the distance to extrude or cut, normal to the workplane plane
  * **cut** (*bool*) – True to cut the resulting solid from the parent solids if found
  * **combine** (*bool* *|* *Literal* *[* *'cut'* *,*  *'a'* *,*  *'s'* *]*) – True or “a” to combine the resulting solid with parent solids if found,
    “cut” or “s” to remove the resulting solid from the parent solids if found.
    False to keep the resulting solid separated from the parent solids.
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
  * **font** (*str*) – font name
  * **fontPath** (*str* *|* *None*) – path to font file
  * **kind** (*Literal* *[* *'regular'* *,*  *'bold'* *,*  *'italic'* *]*) – font type
  * **halign** (*Literal* *[* *'center'* *,*  *'left'* *,*  *'right'* *]*) – horizontal alignment
  * **valign** (*Literal* *[* *'center'* *,*  *'top'* *,*  *'bottom'* *]*) – vertical alignment
* **Returns:**
  a CQ object with the resulting solid selected
* **Return type:**
  *T*

The returned object is always a Workplane object, and depends on whether combine is True, and
whether a context solid is already defined:

* if combine is False, the new value is pushed onto the stack.
* if combine is true, the value is combined with the context solid if it exists,
  and the resulting solid becomes the new context solid.

Examples:

```default
cq.Workplane().text("CadQuery", 5, 1)
```

Specify the font (name), and kind to use an installed system font:

```default
cq.Workplane().text("CadQuery", 5, 1, font="Liberation Sans Narrow", kind="italic")
```

Specify fontPath to use a font from a given file:

```default
cq.Workplane().text("CadQuery", 5, 1, fontPath="/opt/fonts/texgyrecursor-bold.otf")
```

Cutting text into a solid:

```default
cq.Workplane().box(8, 8, 8).faces(">Z").workplane().text("Z", 5, -1.0)
```

#### threePointArc(point1: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector), point2: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector), forConstruction: bool = False) → T

Draw an arc from the current point, through point1, and ending at point2

* **Parameters:**
  * **self** (*T*)
  * **point1** (*2-tuple* *,* *in workplane coordinates*) – point to draw through
  * **point2** (*2-tuple* *,* *in workplane coordinates*) – end point for the arc
  * **forConstruction** (*bool*)
* **Returns:**
  a workplane with the current point at the end of the arc
* **Return type:**
  *T*

Future Enhancements:
: provide a version that allows an arc using relative measures
  provide a centerpoint arc
  provide tangent arcs

#### toOCC() → Any

Directly returns the wrapped OCCT object.

* **Returns:**
  The wrapped OCCT object
* **Return type:**
  TopoDS_Shape or a subclass

#### toPending() → T

Adds wires/edges to pendingWires/pendingEdges.

* **Returns:**
  same CQ object with updated context.
* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### toSvg(opts: Any = None) → str

Returns svg text that represents the first item on the stack.

for testing purposes.

* **Parameters:**
  **opts** (*dictionary* *,* *width and height*) – svg formatting options
* **Returns:**
  a string that contains SVG that represents this item.
* **Return type:**
  str

#### transformed(rotate: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector) = (0, 0, 0), offset: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector) = (0, 0, 0)) → T

Create a new workplane based on the current one.
The origin of the new plane is located at the existing origin+offset vector, where offset is
given in coordinates local to the current plane
The new plane is rotated through the angles specified by the components of the rotation
vector.

* **Parameters:**
  * **self** (*T*)
  * **rotate** (*Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector)) – 3-tuple of angles to rotate, in degrees relative to work plane coordinates
  * **offset** (*Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector)) – 3-tuple to offset the new plane, in local work plane coordinates
* **Returns:**
  a new work plane, transformed as requested
* **Return type:**
  *T*

#### translate(vec: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector)) → T

Returns a copy of all of the items on the stack moved by the specified translation vector.

* **Parameters:**
  * **self** (*T*)
  * **tupleDistance** (*a 3-tuple* *of* *float*) – distance to move, in global coordinates
  * **vec** (*Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector))
* **Returns:**
  a CQ object
* **Return type:**
  *T*

#### twistExtrude(distance: float, angleDegrees: float, combine: bool | Literal['cut', 'a', 's'] = True, clean: bool = True) → T

Extrudes a wire in the direction normal to the plane, but also twists by the specified
angle over the length of the extrusion.

The center point of the rotation will be the center of the workplane.

See extrude for more details, since this method is the same except for the the addition
of the angle. In fact, if angle=0, the result is the same as a linear extrude.

**NOTE**  This method can create complex calculations, so be careful using it with
complex geometries

* **Parameters:**
  * **self** (*T*)
  * **distance** (*float*) – the distance to extrude normal to the workplane
  * **angle** – angle (in degrees) to rotate through the extrusion
  * **combine** (*bool* *|* *Literal* *[* *'cut'* *,*  *'a'* *,*  *'s'* *]*) – True or “a” to combine the resulting solid with parent solids if found,
    “cut” or “s” to remove the resulting solid from the parent solids if found.
    False to keep the resulting solid separated from the parent solids.
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape
  * **angleDegrees** (*float*)
* **Returns:**
  a CQ object with the resulting solid selected.
* **Return type:**
  *T*

#### union(toUnion: [Workplane](#cadquery.Workplane) | [Solid](#cadquery.occ_impl.shapes.Solid) | [Compound](#cadquery.occ_impl.shapes.Compound) | None = None, clean: bool = True, glue: bool = False, tol: float | None = None) → T

Unions all of the items on the stack of toUnion with the current solid.
If there is no current solid, the items in toUnion are unioned together.

* **Parameters:**
  * **self** (*T*)
  * **toUnion** ([*Workplane*](#cadquery.Workplane) *|* [*Solid*](#cadquery.occ_impl.shapes.Solid) *|* [*Compound*](#cadquery.occ_impl.shapes.Compound) *|* *None*) – a solid object, or a Workplane object having a solid
  * **clean** (*bool*) – call [`clean()`](#cadquery.Workplane.clean) afterwards to have a clean shape (default True)
  * **glue** (*bool*) – use a faster gluing mode for non-overlapping shapes (default False)
  * **tol** (*float* *|* *None*) – tolerance value for fuzzy bool operation mode (default None)
* **Raises:**
  ValueError if there is no solid to add to in the chain
* **Returns:**
  a Workplane object with the resulting object selected
* **Return type:**
  *T*

#### vLine(distance: float, forConstruction: bool = False) → T

Make a vertical line from the current point the provided distance

* **Parameters:**
  * **self** (*T*)
  * **distance** (*float*) – 
    1. distance from current point
  * **forConstruction** (*bool*)
* **Returns:**
  the Workplane object with the current point at the end of the new line
* **Return type:**
  *T*

#### vLineTo(yCoord: float, forConstruction: bool = False) → T

Make a vertical line from the current point to the provided y coordinate.

Useful if it is more convenient to specify the end location rather than distance,
as in [`vLine()`](#cadquery.Workplane.vLine)

* **Parameters:**
  * **self** (*T*)
  * **yCoord** (*float*) – y coordinate for the end of the line
  * **forConstruction** (*bool*)
* **Returns:**
  the Workplane object with the current point at the end of the new line
* **Return type:**
  *T*

#### val() → [Vector](#cadquery.Vector) | [Location](#cadquery.Location) | [Shape](#cadquery.occ_impl.shapes.Shape) | [Sketch](#cadquery.Sketch)

Return the first value on the stack. If no value is present, current plane origin is returned.

* **Returns:**
  the first value on the stack.
* **Return type:**
  A CAD primitive

#### vals() → List[[Vector](#cadquery.Vector) | [Location](#cadquery.Location) | [Shape](#cadquery.occ_impl.shapes.Shape) | [Sketch](#cadquery.Sketch)]

get the values in the current list

* **Return type:**
  list of occ_impl objects
* **Returns:**
  the values of the objects on the stack.

Contrast with [`all()`](#cadquery.Workplane.all), which returns CQ objects for all of the items on the stack

#### vertices(selector: str | [Selector](#cadquery.selectors.Selector) | None = None, tag: str | None = None) → T

Select the vertices of objects on the stack, optionally filtering the selection. If there
are multiple objects on the stack, the vertices of all objects are collected and a list of
all the distinct vertices is returned.

* **Parameters:**
  * **self** (*T*)
  * **selector** (*str* *|* [*Selector*](#cadquery.selectors.Selector) *|* *None*) – optional Selector object, or string selector expression
    (see [`StringSyntaxSelector`](#cadquery.StringSyntaxSelector))
  * **tag** (*str* *|* *None*) – if set, search the tagged object instead of self
* **Returns:**
  a CQ object whose stack contains  the *distinct* vertices of *all* objects on the
  current stack, after being filtered by the selector, if provided
* **Return type:**
  *T*

If there are no vertices for any objects on the current stack, an empty CQ object
is returned

The typical use is to select the vertices of a single object on the stack. For example:

```default
Workplane().box(1, 1, 1).faces("+Z").vertices().size()
```

returns 4, because the topmost face of a cube will contain four vertices. While this:

```default
Workplane().box(1, 1, 1).faces().vertices().size()
```

returns 8, because a cube has a total of 8 vertices

**Note** Circles are peculiar, they have a single vertex at the center!

#### wedge(dx: float, dy: float, dz: float, xmin: float, zmin: float, xmax: float, zmax: float, pnt: ~typing.Tuple[float, float] | ~typing.Tuple[float, float, float] | ~cadquery.occ_impl.geom.Vector = Vector: (0.0, 0.0, 0.0), dir: ~typing.Tuple[float, float] | ~typing.Tuple[float, float, float] | ~cadquery.occ_impl.geom.Vector = Vector: (0.0, 0.0, 1.0), centered: bool | ~typing.Tuple[bool, bool, bool] = True, combine: bool | ~typing.Literal['cut', 'a', 's'] = True, clean: bool = True) → T

Returns a 3D wedge with the specified dimensions for each point on the stack.

* **Parameters:**
  * **self** (*T*)
  * **dx** (*float*) – Distance along the X axis
  * **dy** (*float*) – Distance along the Y axis
  * **dz** (*float*) – Distance along the Z axis
  * **xmin** (*float*) – The minimum X location
  * **zmin** (*float*) – The minimum Z location
  * **xmax** (*float*) – The maximum X location
  * **zmax** (*float*) – The maximum Z location
  * **pnt** (*Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector)) – A vector (or tuple) for the origin of the direction for the wedge
  * **dir** (*Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector)) – The direction vector (or tuple) for the major axis of the wedge
  * **centered** (*bool* *|* *Tuple* *[**bool* *,* *bool* *,* *bool* *]*) – If True, the wedge will be centered around the reference point.
    If False, the corner of the wedge will be on the reference point and it will
    extend in the positive x, y and z directions. Can also use a 3-tuple to
    specify centering along each axis.
  * **combine** (*bool* *|* *Literal* *[* *'cut'* *,*  *'a'* *,*  *'s'* *]*) – Whether the results should be combined with other solids on the stack
    (and each other)
  * **clean** (*bool*) – True to attempt to have the kernel clean up the geometry, False otherwise
* **Returns:**
  A wedge object for each point on the stack
* **Return type:**
  *T*

One wedge is created for each item on the current stack. If no items are on the stack, one
wedge using the current workplane center is created.

If combine is True, the result will be a single object on the stack. If a solid was found
in the chain, the result is that solid with all wedges produced fused onto it otherwise,
the result is the combination of all the produced wedges.

If combine is False, the result will be a list of the wedges produced.

#### wire(forConstruction: bool = False) → T

Returns a CQ object with all pending edges connected into a wire.

All edges on the stack that can be combined will be combined into a single wire object,
and other objects will remain on the stack unmodified. If there are no pending edges,
this method will just return self.

* **Parameters:**
  * **self** (*T*)
  * **forConstruction** (*bool*) – whether the wire should be used to make a solid, or if it is just
    for reference
* **Return type:**
  *T*

This method is primarily of use to plugin developers making utilities for 2D construction.
This method should be called when a user operation implies that 2D construction is
finished, and we are ready to begin working in 3d.

SEE ‘2D construction concepts’ for a more detailed explanation of how CadQuery handles
edges, wires, etc.

Any non edges will still remain.

#### wires(selector: str | [Selector](#cadquery.selectors.Selector) | None = None, tag: str | None = None) → T

Select the wires of objects on the stack, optionally filtering the selection. If there are
multiple objects on the stack, the wires of all objects are collected and a list of all the
distinct wires is returned.

* **Parameters:**
  * **self** (*T*)
  * **selector** (*str* *|* [*Selector*](#cadquery.selectors.Selector) *|* *None*) – optional Selector object, or string selector expression
    (see [`StringSyntaxSelector`](#cadquery.StringSyntaxSelector))
  * **tag** (*str* *|* *None*) – if set, search the tagged object instead of self
* **Returns:**
  a CQ object whose stack contains all of the *distinct* wires of *all* objects on
  the current stack, filtered by the provided selector.
* **Return type:**
  *T*

If there are no wires for any objects on the current stack, an empty CQ object is returned

The typical use is to select the wires of a single object on the stack. For example:

```default
Workplane().box(1, 1, 1).faces("+Z").wires().size()
```

returns 1, because a face typically only has one outer wire

#### workplane(offset: float = 0.0, invert: bool = False, centerOption: Literal['CenterOfMass', 'ProjectedOrigin', 'CenterOfBoundBox'] = 'ProjectedOrigin', origin: Tuple[float, float] | Tuple[float, float, float] | [Vector](#cadquery.Vector) | None = None) → T

Creates a new 2D workplane, located relative to the first face on the stack.

* **Parameters:**
  * **self** (*T*)
  * **offset** (*float*) – offset for the workplane in its normal direction . Default
  * **invert** (*bool*) – invert the normal direction from that of the face.
  * **centerOption** (*string* *or* *None='ProjectedOrigin'*) – how local origin of workplane is determined.
  * **origin** (*Tuple* *[**float* *,* *float* *]*  *|* *Tuple* *[**float* *,* *float* *,* *float* *]*  *|* [*Vector*](#cadquery.Vector) *|* *None*) – origin for plane center, requires ‘ProjectedOrigin’ centerOption.
* **Return type:**
  Workplane object

The first element on the stack must be a face, a set of
co-planar faces or a vertex.  If a vertex, then the parent
item on the chain immediately before the vertex must be a
face.

The result will be a 2D working plane
with a new coordinate system set up as follows:

> * The centerOption parameter sets how the center is defined.
>   Options are ‘CenterOfMass’, ‘CenterOfBoundBox’, or ‘ProjectedOrigin’.
>   ‘CenterOfMass’ and ‘CenterOfBoundBox’ are in relation to the selected
>   face(s) or vertex (vertices). ‘ProjectedOrigin’ uses by default the current origin
>   or the optional origin parameter (if specified) and projects it onto the plane
>   defined by the selected face(s).
> * The Z direction will be the normal of the face, computed
>   at the center point.
> * The X direction will be parallel to the x-y plane. If the workplane is  parallel to
>   the global x-y plane, the x direction of the workplane will co-incide with the
>   global x direction.

Most commonly, the selected face will be planar, and the workplane lies in the same plane
of the face ( IE, offset=0). Occasionally, it is useful to define a face offset from
an existing surface, and even more rarely to define a workplane based on a face that is
not planar.

#### workplaneFromTagged(name: str) → [Workplane](#cadquery.Workplane)

Copies the workplane from a tagged parent.

* **Parameters:**
  **name** (*str*) – tag to search for
* **Returns:**
  a CQ object with name’s workplane
* **Return type:**
  [*Workplane*](#cadquery.Workplane)

### cadquery.sortWiresByBuildOrder(wireList: List[[Wire](#cadquery.occ_impl.shapes.Wire)]) → List[List[[Wire](#cadquery.occ_impl.shapes.Wire)]]

Tries to determine how wires should be combined into faces.

Assume:
: The wires make up one or more faces, which could have ‘holes’
  Outer wires are listed ahead of inner wires
  there are no wires inside wires inside wires
  ( IE, islands – we can deal with that later on )
  none of the wires are construction wires

Compute:
: one or more sets of wires, with the outer wire listed first, and inner
  ones

Returns, list of lists.

* **Parameters:**
  **wireList** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*)
* **Return type:**
  *List*[*List*[[*Wire*](#cadquery.occ_impl.shapes.Wire)]]

<a id="module-cadquery.occ_impl.shapes"></a>

### *class* cadquery.occ_impl.shapes.CompSolid(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape), [`Mixin3D`](#cadquery.occ_impl.shapes.Mixin3D)

a single compsolid

* **Parameters:**
  **obj** (*TopoDS_Shape*)

### *class* cadquery.occ_impl.shapes.Compound(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape), [`Mixin3D`](#cadquery.occ_impl.shapes.Mixin3D)

a collection of disconnected solids

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### ancestors(shape: [Shape](#cadquery.occ_impl.shapes.Shape), kind: Literal['Vertex', 'Edge', 'Wire', 'Face', 'Shell', 'Solid', 'CompSolid', 'Compound']) → [Compound](#cadquery.occ_impl.shapes.Compound)

Iterate over ancestors, i.e. shapes of same kind within shape that contain elements of self.

* **Parameters:**
  * **shape** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **kind** (*Literal* *[* *'Vertex'* *,*  *'Edge'* *,*  *'Wire'* *,*  *'Face'* *,*  *'Shell'* *,*  *'Solid'* *,*  *'CompSolid'* *,*  *'Compound'* *]*)
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### cut(\*toCut: [Shape](#cadquery.occ_impl.shapes.Shape), tol: float | None = None) → [Compound](#cadquery.occ_impl.shapes.Compound)

Remove the positional arguments from this Shape.

* **Parameters:**
  * **tol** (*float* *|* *None*) – Fuzzy mode tolerance
  * **toCut** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### fuse(\*toFuse: [Shape](#cadquery.occ_impl.shapes.Shape), glue: bool = False, tol: float | None = None) → [Compound](#cadquery.occ_impl.shapes.Compound)

Fuse shapes together

* **Parameters:**
  * **toFuse** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **glue** (*bool*)
  * **tol** (*float* *|* *None*)
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### intersect(\*toIntersect: [Shape](#cadquery.occ_impl.shapes.Shape), tol: float | None = None) → [Compound](#cadquery.occ_impl.shapes.Compound)

Intersection of the positional arguments and this Shape.

* **Parameters:**
  * **tol** (*float* *|* *None*) – Fuzzy mode tolerance
  * **toIntersect** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### *classmethod* makeCompound(listOfShapes: Iterable[[Shape](#cadquery.occ_impl.shapes.Shape)]) → [Compound](#cadquery.occ_impl.shapes.Compound)

Create a compound out of a list of shapes

* **Parameters:**
  **listOfShapes** (*Iterable* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *]*)
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### *classmethod* makeText(text: str, size: float, height: float, font: str = 'Arial', fontPath: str | None = None, kind: Literal['regular', 'bold', 'italic'] = 'regular', halign: Literal['center', 'left', 'right'] = 'center', valign: Literal['center', 'top', 'bottom'] = 'center', position: [Plane](#cadquery.Plane) = Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))) → [Shape](#cadquery.occ_impl.shapes.Shape)

Create a 3D text

* **Parameters:**
  * **text** (*str*)
  * **size** (*float*)
  * **height** (*float*)
  * **font** (*str*)
  * **fontPath** (*str* *|* *None*)
  * **kind** (*Literal* *[* *'regular'* *,*  *'bold'* *,*  *'italic'* *]*)
  * **halign** (*Literal* *[* *'center'* *,*  *'left'* *,*  *'right'* *]*)
  * **valign** (*Literal* *[* *'center'* *,*  *'top'* *,*  *'bottom'* *]*)
  * **position** ([*Plane*](#cadquery.Plane))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### remove(shape: [Shape](#cadquery.occ_impl.shapes.Shape))

Remove the specified shape.

* **Parameters:**
  **shape** ([*Shape*](#cadquery.occ_impl.shapes.Shape))

#### siblings(shape: [Shape](#cadquery.occ_impl.shapes.Shape), kind: Literal['Vertex', 'Edge', 'Wire', 'Face', 'Shell', 'Solid', 'CompSolid', 'Compound'], level: int = 1) → [Compound](#cadquery.occ_impl.shapes.Compound)

Iterate over siblings, i.e. shapes within shape that share subshapes of kind with the elements of self.

* **Parameters:**
  * **shape** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **kind** (*Literal* *[* *'Vertex'* *,*  *'Edge'* *,*  *'Wire'* *,*  *'Face'* *,*  *'Shell'* *,*  *'Solid'* *,*  *'CompSolid'* *,*  *'Compound'* *]*)
  * **level** (*int*)
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

### *class* cadquery.occ_impl.shapes.Edge(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape), [`Mixin1D`](#cadquery.occ_impl.shapes.Mixin1D)

A trimmed curve that represents the border of a face

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### arcCenter() → [Vector](#cadquery.Vector)

Center of an underlying circle or ellipse geometry.

* **Return type:**
  [*Vector*](#cadquery.Vector)

#### close() → [Edge](#cadquery.occ_impl.shapes.Edge) | [Wire](#cadquery.occ_impl.shapes.Wire)

Close an Edge

* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge) | [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### *classmethod* makeBezier(points: List[[Vector](#cadquery.Vector)]) → [Edge](#cadquery.occ_impl.shapes.Edge)

Create a cubic Bézier Curve from the points.

* **Parameters:**
  **points** (*List* *[*[*Vector*](#cadquery.Vector) *]*) – a list of Vectors that represent the points.
  The edge will pass through the first and the last point,
  and the inner points are Bézier control points.
* **Returns:**
  An edge
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### *classmethod* makeEllipse(x_radius: float, y_radius: float, pnt: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0), xdir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (1.0, 0.0, 0.0), angle1: float = 360.0, angle2: float = 360.0, sense: ~typing.Literal[-1, 1] = 1) → [Edge](#cadquery.occ_impl.shapes.Edge)

Makes an Ellipse centered at the provided point, having normal in the provided direction.

* **Parameters:**
  * **cls**
  * **x_radius** (*float*) – x radius of the ellipse (along the x-axis of plane the ellipse should lie in)
  * **y_radius** (*float*) – y radius of the ellipse (along the y-axis of plane the ellipse should lie in)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – vector representing the center of the ellipse
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – vector representing the direction of the plane the ellipse should lie in
  * **angle1** (*float*) – start angle of arc
  * **angle2** (*float*) – end angle of arc (angle2 == angle1 return closed ellipse = default)
  * **sense** (*Literal* *[* *-1* *,* *1* *]*) – clockwise (-1) or counter clockwise (1)
  * **xdir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Returns:**
  an Edge
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### *classmethod* makeLine(v1: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], v2: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Edge](#cadquery.occ_impl.shapes.Edge)

Create a line between two points

* **Parameters:**
  * **v1** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – Vector that represents the first point
  * **v2** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – Vector that represents the second point
* **Returns:**
  A linear edge between the two provided points
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### *classmethod* makeSpline(listOfVector: List[[Vector](#cadquery.Vector)], tangents: Sequence[[Vector](#cadquery.Vector)] | None = None, periodic: bool = False, parameters: Sequence[float] | None = None, scale: bool = True, tol: float = 1e-06) → [Edge](#cadquery.occ_impl.shapes.Edge)

Interpolate a spline through the provided points.

* **Parameters:**
  * **listOfVector** (*List* *[*[*Vector*](#cadquery.Vector) *]*) – a list of Vectors that represent the points
  * **tangents** (*Sequence* *[*[*Vector*](#cadquery.Vector) *]*  *|* *None*) – tuple of Vectors specifying start and finish tangent
  * **periodic** (*bool*) – creation of periodic curves
  * **parameters** (*Sequence* *[**float* *]*  *|* *None*) – the value of the parameter at each interpolation point. (The interpolated
    curve is represented as a vector-valued function of a scalar parameter.) If periodic ==
    True, then len(parameters) must be len(intepolation points) + 1, otherwise len(parameters)
    must be equal to len(interpolation points).
  * **scale** (*bool*) – whether to scale the specified tangent vectors before interpolating. Each
    tangent is scaled, so it’s length is equal to the derivative of the Lagrange interpolated
    curve. I.e., set this to True, if you want to use only the direction of the tangent
    vectors specified by `tangents`, but not their magnitude.
  * **tol** (*float*) – tolerance of the algorithm (consult OCC documentation). Used to check that the
    specified points are not too close to each other, and that tangent vectors are not too
    short. (In either case interpolation may fail.)
* **Returns:**
  an Edge
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### *classmethod* makeSplineApprox(listOfVector: List[[Vector](#cadquery.Vector)], tol: float = 0.001, smoothing: Tuple[float, float, float] | None = None, minDeg: int = 1, maxDeg: int = 6) → [Edge](#cadquery.occ_impl.shapes.Edge)

Approximate a spline through the provided points.

* **Parameters:**
  * **listOfVector** (*List* *[*[*Vector*](#cadquery.Vector) *]*) – a list of Vectors that represent the points
  * **tol** (*float*) – tolerance of the algorithm (consult OCC documentation).
  * **smoothing** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* *None*) – optional tuple of 3 weights use for variational smoothing (default: None)
  * **minDeg** (*int*) – minimum spline degree. Enforced only when smothing is None (default: 1)
  * **maxDeg** (*int*) – maximum spline degree (default: 6)
* **Returns:**
  an Edge
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### *classmethod* makeTangentArc(v1: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], v2: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], v3: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Edge](#cadquery.occ_impl.shapes.Edge)

Makes a tangent arc from point v1, in the direction of v2 and ends at v3.

* **Parameters:**
  * **cls**
  * **v1** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – start vector
  * **v2** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – tangent vector
  * **v3** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – end vector
* **Returns:**
  an edge
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### *classmethod* makeThreePointArc(v1: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], v2: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], v3: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Edge](#cadquery.occ_impl.shapes.Edge)

Makes a three point arc through the provided points

* **Parameters:**
  * **cls**
  * **v1** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – start vector
  * **v2** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – middle vector
  * **v3** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – end vector
* **Returns:**
  an edge object through the three points
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### trim(u0: float | int, u1: float | int) → [Edge](#cadquery.occ_impl.shapes.Edge)

Trim the edge in the parametric space to (u0, u1).

NB: this operation is done on the base geometry.

* **Parameters:**
  * **u0** (*float* *|* *int*)
  * **u1** (*float* *|* *int*)
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

### *class* cadquery.occ_impl.shapes.Face(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape)

a bounded surface that represents part of the boundary of a solid

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### Center() → [Vector](#cadquery.Vector)

* **Returns:**
  The point of the center of mass of this Shape
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### chamfer2D(d: float, vertices: Iterable[[Vertex](#cadquery.occ_impl.shapes.Vertex)]) → [Face](#cadquery.occ_impl.shapes.Face)

Apply 2D chamfer to a face

* **Parameters:**
  * **d** (*float*)
  * **vertices** (*Iterable* *[*[*Vertex*](#cadquery.occ_impl.shapes.Vertex) *]*)
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### fillet2D(radius: float, vertices: Iterable[[Vertex](#cadquery.occ_impl.shapes.Vertex)]) → [Face](#cadquery.occ_impl.shapes.Face)

Apply 2D fillet to a face

* **Parameters:**
  * **radius** (*float*)
  * **vertices** (*Iterable* *[*[*Vertex*](#cadquery.occ_impl.shapes.Vertex) *]*)
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### isoline(param: float | int, direction: Literal['u', 'v'] = 'v') → [Edge](#cadquery.occ_impl.shapes.Edge)

Construct an isoline.

* **Parameters:**
  * **param** (*float* *|* *int*)
  * **direction** (*Literal* *[* *'u'* *,*  *'v'* *]*)
* **Return type:**
  [*Edge*](#cadquery.occ_impl.shapes.Edge)

#### isolines(params: Iterable[float | int], direction: Literal['u', 'v'] = 'v') → List[[Edge](#cadquery.occ_impl.shapes.Edge)]

Construct multiple isolines.

* **Parameters:**
  * **params** (*Iterable* *[**float* *|* *int* *]*)
  * **direction** (*Literal* *[* *'u'* *,*  *'v'* *]*)
* **Return type:**
  *List*[[*Edge*](#cadquery.occ_impl.shapes.Edge)]

#### *classmethod* makeFromWires(outerWire: [Wire](#cadquery.occ_impl.shapes.Wire), innerWires: List[[Wire](#cadquery.occ_impl.shapes.Wire)] = []) → [Face](#cadquery.occ_impl.shapes.Face)

Makes a planar face from one or more wires

* **Parameters:**
  * **outerWire** ([*Wire*](#cadquery.occ_impl.shapes.Wire))
  * **innerWires** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*)
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### *classmethod* makeNSidedSurface(edges: ~typing.Iterable[~cadquery.occ_impl.shapes.Edge | ~cadquery.occ_impl.shapes.Wire], constraints: ~typing.Iterable[~cadquery.occ_impl.shapes.Edge | ~cadquery.occ_impl.shapes.Wire | ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] | ~OCP.gp.gp_Pnt], continuity: ~OCP.GeomAbs.GeomAbs_Shape = <GeomAbs_Shape.GeomAbs_C0: 0>, degree: int = 3, nbPtsOnCur: int = 15, nbIter: int = 2, anisotropy: bool = False, tol2d: float = 1e-05, tol3d: float = 0.0001, tolAng: float = 0.01, tolCurv: float = 0.1, maxDeg: int = 8, maxSegments: int = 9) → [Face](#cadquery.occ_impl.shapes.Face)

Returns a surface enclosed by a closed polygon defined by ‘edges’ and ‘constraints’.

* **Parameters:**
  * **edges** (*list* *of* *edges* *or* *wires*) – edges
  * **constraints** (*list* *of* *points* *or* *edges*) – constraints
  * **continuity** (*GeomAbs_Shape*) – OCC.Core.GeomAbs continuity condition
  * **degree** (*int*) – >=2
  * **nbPtsOnCur** (*int*) – number of points on curve >= 15
  * **nbIter** (*int*) – number of iterations >= 2
  * **anisotropy** (*bool*) – bool Anisotropy
  * **tol2d** (*float*) – 2D tolerance >0
  * **tol3d** (*float*) – 3D tolerance >0
  * **tolAng** (*float*) – angular tolerance
  * **tolCurv** (*float*) – tolerance for curvature >0
  * **maxDeg** (*int*) – highest polynomial degree >= 2
  * **maxSegments** (*int*) – greatest number of segments >= 2
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### *classmethod* makeRuledSurface(edgeOrWire1: [Edge](#cadquery.occ_impl.shapes.Edge), edgeOrWire2: [Edge](#cadquery.occ_impl.shapes.Edge)) → [Face](#cadquery.occ_impl.shapes.Face)

#### *classmethod* makeRuledSurface(edgeOrWire1: [Wire](#cadquery.occ_impl.shapes.Wire), edgeOrWire2: [Wire](#cadquery.occ_impl.shapes.Wire)) → [Face](#cadquery.occ_impl.shapes.Face)

makeRuledSurface(Edge|Wire,Edge|Wire) – Make a ruled surface
Create a ruled surface out of two edges or wires. If wires are used then
these must have the same number of edges

#### *classmethod* makeSplineApprox(points: List[List[[Vector](#cadquery.Vector)]], tol: float = 0.01, smoothing: Tuple[float, float, float] | None = None, minDeg: int = 1, maxDeg: int = 3) → [Face](#cadquery.occ_impl.shapes.Face)

Approximate a spline surface through the provided points.

* **Parameters:**
  * **points** (*List* *[**List* *[*[*Vector*](#cadquery.Vector) *]* *]*) – a 2D list of Vectors that represent the points
  * **tol** (*float*) – tolerance of the algorithm (consult OCC documentation).
  * **smoothing** (*Tuple* *[**float* *,* *float* *,* *float* *]*  *|* *None*) – optional tuple of 3 weights use for variational smoothing (default: None)
  * **minDeg** (*int*) – minimum spline degree. Enforced only when smothing is None (default: 1)
  * **maxDeg** (*int*) – maximum spline degree (default: 6)
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### normalAt(self, locationVector: ForwardRef('Vector') | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float] | NoneType = None) → [cadquery.occ_impl.geom.Vector](#cadquery.Vector)

> Computes the normal vector at the desired location on the face.

> * **returns:**
>   a vector representing the direction
> * **param locationVector:**
>   the location to compute the normal at. If none, the center of the face is used.
> * **type locationVector:**
>   a vector that lies on the surface.

normalAt(self, u: Union[float, int], v: Union[float, int]) -> Tuple[cadquery.occ_impl.geom.Vector, cadquery.occ_impl.geom.Vector]

> Computes the normal vector at the desired location in the u,v parameter space.

> * **returns:**
>   a vector representing the normal direction and the position
> * **param u:**
>   the u parametric location to compute the normal at.
> * **param v:**
>   the v parametric location to compute the normal at.
* **Parameters:**
  **locationVector** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*  *|* *None*)
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### normals(us: Iterable[float | int], vs: Iterable[float | int]) → Tuple[List[[Vector](#cadquery.Vector)], List[[Vector](#cadquery.Vector)]]

Computes the normal vectors at the desired locations in the u,v parameter space.

* **Returns:**
  a tuple of list of vectors representing the normal directions and the positions
* **Parameters:**
  * **us** (*Iterable* *[**float* *|* *int* *]*) – the u parametric locations to compute the normal at.
  * **vs** (*Iterable* *[**float* *|* *int* *]*) – the v parametric locations to compute the normal at.
* **Return type:**
  *Tuple*[*List*[[*Vector*](#cadquery.Vector)], *List*[[*Vector*](#cadquery.Vector)]]

#### thicken(thickness: float) → [Solid](#cadquery.occ_impl.shapes.Solid)

Return a thickened face

* **Parameters:**
  **thickness** (*float*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### toArcs(tolerance: float = 0.001) → [Face](#cadquery.occ_impl.shapes.Face)

Approximate planar face with arcs and straight line segments.

* **Parameters:**
  **tolerance** (*float*) – Approximation tolerance.
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

#### toPln() → gp_Pln

Convert this face to a gp_Pln.

Note the Location of the resulting plane may not equal the center of this face,
however the resulting plane will still contain the center of this face.

* **Return type:**
  *gp_Pln*

#### trim(u0: float | int, u1: float | int, v0: float | int, v1: float | int, tol: float | int = 1e-06) → [Face](#cadquery.occ_impl.shapes.Face)

Trim the face in the parametric space to (u0, u1).

NB: this operation is done on the base geometry.

* **Parameters:**
  * **u0** (*float* *|* *int*)
  * **u1** (*float* *|* *int*)
  * **v0** (*float* *|* *int*)
  * **v1** (*float* *|* *int*)
  * **tol** (*float* *|* *int*)
* **Return type:**
  [*Face*](#cadquery.occ_impl.shapes.Face)

### *class* cadquery.occ_impl.shapes.Mixin1DProtocol(wrapped: TopoDS_Shape)

Bases: [`ShapeProtocol`](#cadquery.occ_impl.shapes.ShapeProtocol), `Protocol`

* **Parameters:**
  **wrapped** (*TopoDS_Shape*)

### *class* cadquery.occ_impl.shapes.Shape(obj: TopoDS_Shape)

Bases: `object`

Represents a shape in the system. Wraps TopoDS_Shape.

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### Area() → float

* **Returns:**
  The surface area of all faces in this Shape
* **Return type:**
  float

#### BoundingBox(tolerance: float | None = None) → [BoundBox](#cadquery.BoundBox)

Create a bounding box for this Shape.

* **Parameters:**
  **tolerance** (*float* *|* *None*) – Tolerance value passed to `BoundBox`
* **Returns:**
  A `BoundBox` object for this Shape
* **Return type:**
  [*BoundBox*](#cadquery.BoundBox)

#### Center() → [Vector](#cadquery.Vector)

* **Returns:**
  The point of the center of mass of this Shape
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### CenterOfBoundBox(tolerance: float | None = None) → [Vector](#cadquery.Vector)

* **Parameters:**
  **tolerance** (*float* *|* *None*) – Tolerance passed to the [`BoundingBox()`](#cadquery.occ_impl.shapes.Shape.BoundingBox) method
* **Returns:**
  Center of the bounding box of this shape
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### Closed() → bool

* **Returns:**
  The closedness flag
* **Return type:**
  bool

#### *static* CombinedCenter(objects: Iterable[[Shape](#cadquery.occ_impl.shapes.Shape)]) → [Vector](#cadquery.Vector)

Calculates the center of mass of multiple objects.

* **Parameters:**
  **objects** (*Iterable* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *]*) – A list of objects with mass
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### *static* CombinedCenterOfBoundBox(objects: List[[Shape](#cadquery.occ_impl.shapes.Shape)]) → [Vector](#cadquery.Vector)

Calculates the center of a bounding box of multiple objects.

* **Parameters:**
  **objects** (*List* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *]*) – A list of objects
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### CompSolids() → List[[CompSolid](#cadquery.occ_impl.shapes.CompSolid)]

* **Returns:**
  All the compsolids in this Shape
* **Return type:**
  *List*[[*CompSolid*](#cadquery.occ_impl.shapes.CompSolid)]

#### Compounds() → List[[Compound](#cadquery.occ_impl.shapes.Compound)]

* **Returns:**
  All the compounds in this Shape
* **Return type:**
  *List*[[*Compound*](#cadquery.occ_impl.shapes.Compound)]

#### Edges() → List[[Edge](#cadquery.occ_impl.shapes.Edge)]

* **Returns:**
  All the edges in this Shape
* **Return type:**
  *List*[[*Edge*](#cadquery.occ_impl.shapes.Edge)]

#### Faces() → List[[Face](#cadquery.occ_impl.shapes.Face)]

* **Returns:**
  All the faces in this Shape
* **Return type:**
  *List*[[*Face*](#cadquery.occ_impl.shapes.Face)]

#### Shells() → List[[Shell](#cadquery.occ_impl.shapes.Shell)]

* **Returns:**
  All the shells in this Shape
* **Return type:**
  *List*[[*Shell*](#cadquery.occ_impl.shapes.Shell)]

#### Solids() → List[[Solid](#cadquery.occ_impl.shapes.Solid)]

* **Returns:**
  All the solids in this Shape
* **Return type:**
  *List*[[*Solid*](#cadquery.occ_impl.shapes.Solid)]

#### Vertices() → List[[Vertex](#cadquery.occ_impl.shapes.Vertex)]

* **Returns:**
  All the vertices in this Shape
* **Return type:**
  *List*[[*Vertex*](#cadquery.occ_impl.shapes.Vertex)]

#### Volume() → float

* **Returns:**
  The volume of this Shape
* **Return type:**
  float

#### Wires() → List[[Wire](#cadquery.occ_impl.shapes.Wire)]

* **Returns:**
  All the wires in this Shape
* **Return type:**
  *List*[[*Wire*](#cadquery.occ_impl.shapes.Wire)]

#### ancestors(shape: [Shape](#cadquery.occ_impl.shapes.Shape), kind: Literal['Vertex', 'Edge', 'Wire', 'Face', 'Shell', 'Solid', 'CompSolid', 'Compound']) → [Compound](#cadquery.occ_impl.shapes.Compound)

Iterate over ancestors, i.e. shapes of same kind within shape that contain self.

* **Parameters:**
  * **shape** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **kind** (*Literal* *[* *'Vertex'* *,*  *'Edge'* *,*  *'Wire'* *,*  *'Face'* *,*  *'Shell'* *,*  *'Solid'* *,*  *'CompSolid'* *,*  *'Compound'* *]*)
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### *classmethod* cast(obj: TopoDS_Shape, forConstruction: bool = False) → [Shape](#cadquery.occ_impl.shapes.Shape)

Returns the right type of wrapper, given a OCCT object

* **Parameters:**
  * **obj** (*TopoDS_Shape*)
  * **forConstruction** (*bool*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### *static* centerOfMass(obj: [Shape](#cadquery.occ_impl.shapes.Shape)) → [Vector](#cadquery.Vector)

Calculates the center of ‘mass’ of an object.

* **Parameters:**
  **obj** ([*Shape*](#cadquery.occ_impl.shapes.Shape)) – Compute the center of mass of this object
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### clean() → T

Experimental clean using ShapeUpgrade

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### *static* computeMass(obj: [Shape](#cadquery.occ_impl.shapes.Shape)) → float

Calculates the ‘mass’ of an object.

* **Parameters:**
  **obj** ([*Shape*](#cadquery.occ_impl.shapes.Shape)) – Compute the mass of this object
* **Return type:**
  float

#### copy(mesh: bool = False) → T

Creates a new object that is a copy of this object.

* **Parameters:**
  * **self** (*T*)
  * **mesh** (*bool*) – should I copy the triangulation too (default: False)
* **Returns:**
  a copy of the object
* **Return type:**
  *T*

#### cut(\*toCut: [Shape](#cadquery.occ_impl.shapes.Shape), tol: float | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Remove the positional arguments from this Shape.

* **Parameters:**
  * **tol** (*float* *|* *None*) – Fuzzy mode tolerance
  * **toCut** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### distance(other: [Shape](#cadquery.occ_impl.shapes.Shape)) → float

Minimal distance between two shapes

* **Parameters:**
  **other** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  float

#### distances(\*others: [Shape](#cadquery.occ_impl.shapes.Shape)) → Iterator[float]

Minimal distances to between self and other shapes

* **Parameters:**
  **others** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  *Iterator*[float]

#### edges(selector: [Selector](#cadquery.selectors.Selector) | str | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Select edges.

* **Parameters:**
  **selector** ([*Selector*](#cadquery.selectors.Selector) *|* *str* *|* *None*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### export(fname: str, tolerance: float = 0.1, angularTolerance: float = 0.1, opt: Dict[str, Any] | None = None)

Export Shape to file.

* **Parameters:**
  * **self** (*T*)
  * **fname** (*str*)
  * **tolerance** (*float*)
  * **angularTolerance** (*float*)
  * **opt** (*Dict* *[**str* *,* *Any* *]*  *|* *None*)

#### exportBin(f: str | BytesIO) → bool

Export this shape to a binary BREP file.

* **Parameters:**
  **f** (*str* *|* *BytesIO*)
* **Return type:**
  bool

#### exportBrep(f: str | BytesIO) → bool

Export this shape to a BREP file

* **Parameters:**
  **f** (*str* *|* *BytesIO*)
* **Return type:**
  bool

#### exportStep(fileName: str, \*\*kwargs) → IFSelect_ReturnStatus

Export this shape to a STEP file.

kwargs is used to provide optional keyword arguments to configure the exporter.

* **Parameters:**
  * **fileName** (*str*) – Path and filename for writing.
  * **write_pcurves** (*bool*) – 

    Enable or disable writing parametric curves to the STEP file. Default True.

    If False, writes STEP file without pcurves. This decreases the size of the resulting STEP file.
  * **precision_mode** (*int*) – Controls the uncertainty value for STEP entities. Specify -1, 0, or 1. Default 0.
    See OCCT documentation.
* **Return type:**
  *IFSelect_ReturnStatus*

#### exportStl(fileName: str, tolerance: float = 0.001, angularTolerance: float = 0.1, ascii: bool = False, relative: bool = True, parallel: bool = True) → bool

Exports a shape to a specified STL file.

* **Parameters:**
  * **fileName** (*str*) – The path and file name to write the STL output to.
  * **tolerance** (*float*) – A linear deflection setting which limits the distance between a curve and its tessellation.
    Setting this value too low will result in large meshes that can consume computing resources.
    Setting the value too high can result in meshes with a level of detail that is too low.
    Default is 1e-3, which is a good starting point for a range of cases.
  * **angularTolerance** (*float*) – Angular deflection setting which limits the angle between subsequent segments in a polyline. Default is 0.1.
  * **ascii** (*bool*) – Export the file as ASCII (True) or binary (False) STL format.  Default is binary.
  * **relative** (*bool*) – If True, tolerance will be scaled by the size of the edge being meshed. Default is True.
    Setting this value to True may cause large features to become faceted, or small features dense.
  * **parallel** (*bool*) – If True, OCCT will use parallel processing to mesh the shape. Default is True.
* **Return type:**
  bool

#### faces(selector: [Selector](#cadquery.selectors.Selector) | str | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Select faces.

* **Parameters:**
  **selector** ([*Selector*](#cadquery.selectors.Selector) *|* *str* *|* *None*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### facesIntersectedByLine(point: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], axis: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], tol: float = 0.0001, direction: Literal['AlongAxis', 'Opposite'] | None = None)

Computes the intersections between the provided line and the faces of this Shape

* **Parameters:**
  * **point** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – Base point for defining a line
  * **axis** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – Axis on which the line rests
  * **tol** (*float*) – Intersection tolerance
  * **direction** (*Literal* *[* *'AlongAxis'* *,*  *'Opposite'* *]*  *|* *None*) – Valid values: “AlongAxis”, “Opposite”;
    If specified, will ignore all faces that are not in the specified direction
    including the face where the point lies if it is the case
* **Returns:**
  A list of intersected faces sorted by distance from point

#### fix() → T

Try to fix shape if not valid

* **Parameters:**
  **self** (*T*)
* **Return type:**
  *T*

#### fuse(\*toFuse: [Shape](#cadquery.occ_impl.shapes.Shape), glue: bool = False, tol: float | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Fuse the positional arguments with this Shape.

* **Parameters:**
  * **glue** (*bool*) – Sets the glue option for the algorithm, which allows
    increasing performance of the intersection of the input shapes
  * **tol** (*float* *|* *None*) – Fuzzy mode tolerance
  * **toFuse** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### geomType() → Literal['Vertex', 'Wire', 'Shell', 'Solid', 'Compound', 'PLANE', 'CYLINDER', 'CONE', 'SPHERE', 'TORUS', 'BEZIER', 'BSPLINE', 'REVOLUTION', 'EXTRUSION', 'OFFSET', 'OTHER', 'LINE', 'CIRCLE', 'ELLIPSE', 'HYPERBOLA', 'PARABOLA']

Gets the underlying geometry type.

Implementations can return any values desired, but the values the user
uses in type filters should correspond to these.

As an example, if a user does:

```default
CQ(object).faces("%mytype")
```

The expectation is that the geomType attribute will return ‘mytype’

The return values depend on the type of the shape:

Vertex:  always ‘Vertex’
<br/>
Edge:   LINE, CIRCLE, ELLIPSE, HYPERBOLA, PARABOLA, BEZIER,
<br/>
BSPLINE, OFFSET, OTHER
<br/>
Face:   PLANE, CYLINDER, CONE, SPHERE, TORUS, BEZIER, BSPLINE,
<br/>
REVOLUTION, EXTRUSION, OFFSET, OTHER
<br/>
Solid:  ‘Solid’
<br/>
Shell:  ‘Shell’
<br/>
Compound: ‘Compound’
<br/>
Wire:   ‘Wire’
<br/>
* **Returns:**
  A string according to the geometry type
* **Return type:**
  *Literal*[‘Vertex’, ‘Wire’, ‘Shell’, ‘Solid’, ‘Compound’, ‘PLANE’, ‘CYLINDER’, ‘CONE’, ‘SPHERE’, ‘TORUS’, ‘BEZIER’, ‘BSPLINE’, ‘REVOLUTION’, ‘EXTRUSION’, ‘OFFSET’, ‘OTHER’, ‘LINE’, ‘CIRCLE’, ‘ELLIPSE’, ‘HYPERBOLA’, ‘PARABOLA’]

#### hashCode() → int

Returns a hashed value denoting this shape. It is computed from the
TShape and the Location. The Orientation is not used.

* **Return type:**
  int

#### *classmethod* importBin(f: str | BytesIO) → [Shape](#cadquery.occ_impl.shapes.Shape)

Import shape from a binary BREP file.

* **Parameters:**
  **f** (*str* *|* *BytesIO*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### *classmethod* importBrep(f: str | BytesIO) → [Shape](#cadquery.occ_impl.shapes.Shape)

Import shape from a BREP file

* **Parameters:**
  **f** (*str* *|* *BytesIO*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### intersect(\*toIntersect: [Shape](#cadquery.occ_impl.shapes.Shape), tol: float | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Intersection of the positional arguments and this Shape.

* **Parameters:**
  * **tol** (*float* *|* *None*) – Fuzzy mode tolerance
  * **toIntersect** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### isEqual(other: [Shape](#cadquery.occ_impl.shapes.Shape)) → bool

Returns True if two shapes are equal, i.e. if they share the same
TShape with the same Locations and Orientations. Also see
[`isSame()`](#cadquery.occ_impl.shapes.Shape.isSame).

* **Parameters:**
  **other** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  bool

#### isNull() → bool

Returns true if this shape is null. In other words, it references no
underlying shape with the potential to be given a location and an
orientation.

* **Return type:**
  bool

#### isSame(other: [Shape](#cadquery.occ_impl.shapes.Shape)) → bool

Returns True if other and this shape are same, i.e. if they share the
same TShape with the same Locations. Orientations may differ. Also see
[`isEqual()`](#cadquery.occ_impl.shapes.Shape.isEqual)

* **Parameters:**
  **other** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  bool

#### isValid() → bool

Returns True if no defect is detected on the shape S or any of its
subshapes. See the OCCT docs on BRepCheck_Analyzer::IsValid for a full
description of what is checked.

* **Return type:**
  bool

#### locate(loc: [Location](#cadquery.Location)) → T

Apply a location in absolute sense to self.

* **Parameters:**
  * **self** (*T*)
  * **loc** ([*Location*](#cadquery.Location))
* **Return type:**
  *T*

#### located(loc: [Location](#cadquery.Location)) → T

Apply a location in absolute sense to a copy of self.

* **Parameters:**
  * **self** (*T*)
  * **loc** ([*Location*](#cadquery.Location))
* **Return type:**
  *T*

#### location() → [Location](#cadquery.Location)

Return the current location

* **Return type:**
  [*Location*](#cadquery.Location)

#### *static* matrixOfInertia(obj: [Shape](#cadquery.occ_impl.shapes.Shape)) → List[List[float]]

Calculates the matrix of inertia of an object.
Since the part’s density is unknown, this result is inertia/density with units of [1/length].
:param obj: Compute the matrix of inertia of this object

* **Parameters:**
  **obj** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  *List*[*List*[float]]

#### mesh(tolerance: float, angularTolerance: float = 0.1)

Generate triangulation if none exists.

* **Parameters:**
  * **tolerance** (*float*)
  * **angularTolerance** (*float*)

#### mirror(mirrorPlane: Literal['XY', 'YX', 'XZ', 'ZX', 'YZ', 'ZY'] | [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float] = 'XY', basePointVector: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float] = (0, 0, 0)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Applies a mirror transform to this Shape. Does not duplicate objects
about the plane.

* **Parameters:**
  * **mirrorPlane** (*Literal* *[* *'XY'* *,*  *'YX'* *,*  *'XZ'* *,*  *'ZX'* *,*  *'YZ'* *,*  *'ZY'* *]*  *|*  *~cadquery.occ_impl.geom.Vector* *|*  *~typing.Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|*  *~typing.Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – The direction of the plane to mirror about - one of
    ‘XY’, ‘XZ’ or ‘YZ’
  * **basePointVector** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – The origin of the plane to mirror about
* **Returns:**
  The mirrored shape
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### move(self: T, loc: [cadquery.occ_impl.geom.Location](#cadquery.Location)) → T

> Apply a location in relative sense (i.e. update current location) to self.

move(self: ~T, x: Union[float, int] = 0, y: Union[float, int] = 0, z: Union[float, int] = 0, rx: Union[float, int] = 0, ry: Union[float, int] = 0, rz: Union[float, int] = 0) -> ~T

> Apply translation and rotation in relative sense (i.e. update current location) to self.

move(self: ~T, loc: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]) -> ~T

> Apply a VectorLike in relative sense (i.e. update current location) to self.
* **Parameters:**
  * **self** (*T*)
  * **loc** ([*Location*](#cadquery.Location))
* **Return type:**
  *T*

#### moved(self: T, loc: [cadquery.occ_impl.geom.Location](#cadquery.Location)) → T

> Apply a location in relative sense (i.e. update current location) to a copy of self.

moved(self: ~T, loc1: cadquery.occ_impl.geom.Location, loc2: cadquery.occ_impl.geom.Location, 

```
*
```

locs: cadquery.occ_impl.geom.Location) -> ~T

> Apply multiple locations.

moved(self: ~T, locs: Sequence[cadquery.occ_impl.geom.Location]) -> ~T

> Apply multiple locations.

moved(self: ~T, x: Union[float, int] = 0, y: Union[float, int] = 0, z: Union[float, int] = 0, rx: Union[float, int] = 0, ry: Union[float, int] = 0, rz: Union[float, int] = 0) -> ~T

> Apply translation and rotation in relative sense to a copy of self.

moved(self: ~T, loc: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]) -> ~T

> Apply a VectorLike in relative sense to a copy of self.

moved(self: ~T, loc1: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]], loc2: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]], 

```
*
```

locs: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]) -> ~T

> Apply multiple VectorLikes in relative sense to a copy of self.

moved(self: ~T, loc: Sequence[Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]]) -> ~T

> Apply multiple VectorLikes in relative sense to a copy of self.
* **Parameters:**
  * **self** (*T*)
  * **loc** ([*Location*](#cadquery.Location))
* **Return type:**
  *T*

#### rotate(startVector: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], endVector: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], angleDegrees: float) → T

Rotates a shape around an axis.

* **Parameters:**
  * **self** (*T*)
  * **startVector** (*either a 3-tuple* *or* *a Vector*) – start point of rotation axis
  * **endVector** (*either a 3-tuple* *or* *a Vector*) – end point of rotation axis
  * **angleDegrees** (*float*) – angle to rotate, in degrees
* **Returns:**
  a copy of the shape, rotated
* **Return type:**
  *T*

#### scale(factor: float) → [Shape](#cadquery.occ_impl.shapes.Shape)

Scales this shape through a transformation.

* **Parameters:**
  **factor** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### shells(selector: [Selector](#cadquery.selectors.Selector) | str | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Select shells.

* **Parameters:**
  **selector** ([*Selector*](#cadquery.selectors.Selector) *|* *str* *|* *None*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### siblings(shape: [Shape](#cadquery.occ_impl.shapes.Shape), kind: Literal['Vertex', 'Edge', 'Wire', 'Face', 'Shell', 'Solid', 'CompSolid', 'Compound'], level: int = 1) → [Compound](#cadquery.occ_impl.shapes.Compound)

Iterate over siblings, i.e. shapes within shape that share subshapes of kind with self.

* **Parameters:**
  * **shape** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **kind** (*Literal* *[* *'Vertex'* *,*  *'Edge'* *,*  *'Wire'* *,*  *'Face'* *,*  *'Shell'* *,*  *'Solid'* *,*  *'CompSolid'* *,*  *'Compound'* *]*)
  * **level** (*int*)
* **Return type:**
  [*Compound*](#cadquery.occ_impl.shapes.Compound)

#### solids(selector: [Selector](#cadquery.selectors.Selector) | str | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Select solids.

* **Parameters:**
  **selector** ([*Selector*](#cadquery.selectors.Selector) *|* *str* *|* *None*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### split(\*splitters: [Shape](#cadquery.occ_impl.shapes.Shape)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Split this shape with the positional arguments.

* **Parameters:**
  **splitters** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### toSplines(degree: int = 3, tolerance: float = 0.001, nurbs: bool = False) → T

Approximate shape with b-splines of the specified degree.

* **Parameters:**
  * **self** (*T*)
  * **degree** (*int*) – Maximum degree.
  * **tolerance** (*float*) – Approximation tolerance.
  * **nurbs** (*bool*) – Use rational splines.
* **Return type:**
  *T*

#### toVtkPolyData(tolerance: float | None = None, angularTolerance: float | None = None, normals: bool = False) → vtkPolyData

Convert shape to vtkPolyData

* **Parameters:**
  * **tolerance** (*float* *|* *None*)
  * **angularTolerance** (*float* *|* *None*)
  * **normals** (*bool*)
* **Return type:**
  *vtkPolyData*

#### transformGeometry(tMatrix: [Matrix](#cadquery.Matrix)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Transforms this shape by tMatrix.

WARNING: transformGeometry will sometimes convert lines and circles to
splines, but it also has the ability to handle skew and stretching
transformations.

If your transformation is only translation and rotation, it is safer to
use [`transformShape()`](#cadquery.occ_impl.shapes.Shape.transformShape), which doesn’t change the underlying type
of the geometry, but cannot handle skew transformations.

* **Parameters:**
  **tMatrix** ([*Matrix*](#cadquery.Matrix)) – The transformation matrix
* **Returns:**
  a copy of the object, but with geometry transformed instead
  of just rotated.
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### transformShape(tMatrix: [Matrix](#cadquery.Matrix)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Transforms this Shape by tMatrix. Also see [`transformGeometry()`](#cadquery.occ_impl.shapes.Shape.transformGeometry).

* **Parameters:**
  **tMatrix** ([*Matrix*](#cadquery.Matrix)) – The transformation matrix
* **Returns:**
  a copy of the object, transformed by the provided matrix,
  with all objects keeping their type
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### translate(vector: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → T

Translates this shape through a transformation.

* **Parameters:**
  * **self** (*T*)
  * **vector** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Return type:**
  *T*

#### vertices(selector: [Selector](#cadquery.selectors.Selector) | str | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Select vertices.

* **Parameters:**
  **selector** ([*Selector*](#cadquery.selectors.Selector) *|* *str* *|* *None*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### wires(selector: [Selector](#cadquery.selectors.Selector) | str | None = None) → [Shape](#cadquery.occ_impl.shapes.Shape)

Select wires.

* **Parameters:**
  **selector** ([*Selector*](#cadquery.selectors.Selector) *|* *str* *|* *None*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### *class* cadquery.occ_impl.shapes.ShapeProtocol(wrapped: TopoDS_Shape)

Bases: `Protocol`

* **Parameters:**
  **wrapped** (*TopoDS_Shape*)

### *class* cadquery.occ_impl.shapes.Shell(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape)

the outer boundary of a surface

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### *classmethod* makeShell(listOfFaces: Iterable[[Face](#cadquery.occ_impl.shapes.Face)]) → [Shell](#cadquery.occ_impl.shapes.Shell)

Makes a shell from faces.

* **Parameters:**
  **listOfFaces** (*Iterable* *[*[*Face*](#cadquery.occ_impl.shapes.Face) *]*)
* **Return type:**
  [*Shell*](#cadquery.occ_impl.shapes.Shell)

### *class* cadquery.occ_impl.shapes.Solid(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape), [`Mixin3D`](#cadquery.occ_impl.shapes.Mixin3D)

a single solid

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### *classmethod* extrudeLinear(cls, outerWire: [cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire), innerWires: List[[cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire)], vecNormal: ForwardRef('Vector') | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], taper: float | int = 0) → 'Solid'

Attempt to extrude the list of wires into a prismatic solid in the provided direction

* **Parameters:**
  * **outerWire** ([*Wire*](#cadquery.occ_impl.shapes.Wire)) – the outermost wire
  * **innerWires** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*) – a list of inner wires
  * **vecNormal** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – a vector along which to extrude the wires
  * **taper** (*float* *|* *int*) – taper angle, default=0
* **Returns:**
  a Solid object
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

The wires must not intersect

Extruding wires is very non-trivial.  Nested wires imply very different geometry, and
there are many geometries that are invalid. In general, the following conditions must be met:

* all wires must be closed
* there cannot be any intersecting or self-intersecting wires
* wires must be listed from outside in
* more than one levels of nesting is not supported reliably

This method will attempt to sort the wires, but there is much work remaining to make this method
reliable.

#### *classmethod* extrudeLinearWithRotation(outerWire: [Wire](#cadquery.occ_impl.shapes.Wire), innerWires: List[[Wire](#cadquery.occ_impl.shapes.Wire)], vecCenter: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], vecNormal: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], angleDegrees: float | int) → [Solid](#cadquery.occ_impl.shapes.Solid)

Creates a ‘twisted prism’ by extruding, while simultaneously rotating around the extrusion vector.

Though the signature may appear to be similar enough to extrudeLinear to merit combining them, the
construction methods used here are different enough that they should be separate.

At a high level, the steps followed are:

1. accept a set of wires
2. create another set of wires like this one, but which are transformed and rotated
3. create a ruledSurface between the sets of wires
4. create a shell and compute the resulting object

* **Parameters:**
  * **outerWire** ([*Wire*](#cadquery.occ_impl.shapes.Wire)) – the outermost wire
  * **innerWires** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*) – a list of inner wires
  * **vecCenter** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – the center point about which to rotate.  the axis of rotation is defined by
    vecNormal, located at vecCenter.
  * **vecNormal** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – a vector along which to extrude the wires
  * **angleDegrees** (*float* *|* *int*) – the angle to rotate through while extruding
* **Returns:**
  a Solid object
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### innerShells() → List[[Shell](#cadquery.occ_impl.shapes.Shell)]

Returns inner shells.

* **Return type:**
  *List*[[*Shell*](#cadquery.occ_impl.shapes.Shell)]

#### *classmethod* interpPlate(surf_edges, surf_pts, thickness, degree=3, nbPtsOnCur=15, nbIter=2, anisotropy=False, tol2d=1e-05, tol3d=0.0001, tolAng=0.01, tolCurv=0.1, maxDeg=8, maxSegments=9) → [Solid](#cadquery.occ_impl.shapes.Solid) | [Face](#cadquery.occ_impl.shapes.Face)

Returns a plate surface that is ‘thickness’ thick, enclosed by ‘surf_edge_pts’ points, and going through ‘surf_pts’ points.

* **Parameters:**
  * **surf_edges** – list of [x,y,z] float ordered coordinates
    or list of ordered or unordered wires
  * **surf_pts** – list of [x,y,z] float coordinates (uses only edges if [])
  * **thickness** – thickness may be negative or positive depending on direction, (returns 2D surface if 0)
  * **degree** – >=2
  * **nbPtsOnCur** – number of points on curve >= 15
  * **nbIter** – number of iterations >= 2
  * **anisotropy** – bool Anisotropy
  * **tol2d** – 2D tolerance >0
  * **tol3d** – 3D tolerance >0
  * **tolAng** – angular tolerance
  * **tolCurv** – tolerance for curvature >0
  * **maxDeg** – highest polynomial degree >= 2
  * **maxSegments** – greatest number of segments >= 2
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid) | [*Face*](#cadquery.occ_impl.shapes.Face)

#### *static* isSolid(obj: [Shape](#cadquery.occ_impl.shapes.Shape)) → bool

Returns true if the object is a solid, false otherwise

* **Parameters:**
  **obj** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  bool

#### *classmethod* makeBox(length,width,height,[pnt,dir]) -- Make a box located in pnt with the dimensions (length,width,height)

By default pnt=Vector(0,0,0) and dir=Vector(0,0,1)

* **Parameters:**
  * **length** (*float*)
  * **width** (*float*)
  * **height** (*float*)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### *classmethod* makeCone(radius1: float, radius2: float, height: float, pnt: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0), angleDegrees: float = 360) → [Solid](#cadquery.occ_impl.shapes.Solid)

Make a cone with given radii and height
By default pnt=Vector(0,0,0),
dir=Vector(0,0,1) and angle=360

* **Parameters:**
  * **radius1** (*float*)
  * **radius2** (*float*)
  * **height** (*float*)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **angleDegrees** (*float*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### *classmethod* makeCylinder(radius: float, height: float, pnt: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0), angleDegrees: float = 360) → [Solid](#cadquery.occ_impl.shapes.Solid)

makeCylinder(radius,height,[pnt,dir,angle]) –
Make a cylinder with a given radius and height
By default pnt=Vector(0,0,0),dir=Vector(0,0,1) and angle=360

* **Parameters:**
  * **radius** (*float*)
  * **height** (*float*)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **angleDegrees** (*float*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### *classmethod* makeLoft(listOfWire: List[[Wire](#cadquery.occ_impl.shapes.Wire)], ruled: bool = False) → [Solid](#cadquery.occ_impl.shapes.Solid)

makes a loft from a list of wires
The wires will be converted into faces when possible– it is presumed that nobody ever actually
wants to make an infinitely thin shell for a real FreeCADPart.

* **Parameters:**
  * **listOfWire** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*)
  * **ruled** (*bool*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### *classmethod* makeSolid(shell: [Shell](#cadquery.occ_impl.shapes.Shell)) → [Solid](#cadquery.occ_impl.shapes.Solid)

Makes a solid from a single shell.

* **Parameters:**
  **shell** ([*Shell*](#cadquery.occ_impl.shapes.Shell))
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### *classmethod* makeSphere(radius: float, pnt: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0), angleDegrees1: float = 0, angleDegrees2: float = 90, angleDegrees3: float = 360) → [Shape](#cadquery.occ_impl.shapes.Shape)

Make a sphere with a given radius
By default pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=0, angle2=90 and angle3=360

* **Parameters:**
  * **radius** (*float*)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **angleDegrees1** (*float*)
  * **angleDegrees2** (*float*)
  * **angleDegrees3** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### *classmethod* makeTorus(radius1: float, radius2: float, pnt: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0), angleDegrees1: float = 0, angleDegrees2: float = 360) → [Solid](#cadquery.occ_impl.shapes.Solid)

makeTorus(radius1,radius2,[pnt,dir,angle1,angle2,angle]) –
Make a torus with a given radii and angles
By default pnt=Vector(0,0,0),dir=Vector(0,0,1),angle1=0
,angle1=360 and angle=360

* **Parameters:**
  * **radius1** (*float*)
  * **radius2** (*float*)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **angleDegrees1** (*float*)
  * **angleDegrees2** (*float*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### *classmethod* makeWedge(dx: float, dy: float, dz: float, xmin: float, zmin: float, xmax: float, zmax: float, pnt: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0)) → [Solid](#cadquery.occ_impl.shapes.Solid)

Make a wedge located in pnt
By default pnt=Vector(0,0,0) and dir=Vector(0,0,1)

* **Parameters:**
  * **dx** (*float*)
  * **dy** (*float*)
  * **dz** (*float*)
  * **xmin** (*float*)
  * **zmin** (*float*)
  * **xmax** (*float*)
  * **zmax** (*float*)
  * **pnt** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### outerShell() → [Shell](#cadquery.occ_impl.shapes.Shell)

Returns outer shell.

* **Return type:**
  [*Shell*](#cadquery.occ_impl.shapes.Shell)

#### *classmethod* revolve(outerWire: [Wire](#cadquery.occ_impl.shapes.Wire), innerWires: List[[Wire](#cadquery.occ_impl.shapes.Wire)], angleDegrees: float | int, axisStart: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], axisEnd: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Solid](#cadquery.occ_impl.shapes.Solid)

Attempt to revolve the list of wires into a solid in the provided direction

* **Parameters:**
  * **outerWire** ([*Wire*](#cadquery.occ_impl.shapes.Wire)) – the outermost wire
  * **innerWires** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*) – a list of inner wires
  * **angleDegrees** (*float* *,* *anything less than 360 degrees will leave the shape open*) – the angle to revolve through.
  * **axisStart** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – the start point of the axis of rotation
  * **axisEnd** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – the end point of the axis of rotation
* **Returns:**
  a Solid object
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

The wires must not intersect

* all wires must be closed
* there cannot be any intersecting or self-intersecting wires
* wires must be listed from outside in
* more than one levels of nesting is not supported reliably
* the wire(s) that you’re revolving cannot be centered

This method will attempt to sort the wires, but there is much work remaining to make this method
reliable.

#### *classmethod* sweep(cls, outerWire: [cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire), innerWires: List[[cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire)], path: [cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire) | [cadquery.occ_impl.shapes.Edge](#cadquery.occ_impl.shapes.Edge), makeSolid: bool = True, isFrenet: bool = False, mode: [cadquery.occ_impl.geom.Vector](#cadquery.Vector) | [cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire) | [cadquery.occ_impl.shapes.Edge](#cadquery.occ_impl.shapes.Edge) | NoneType = None, transitionMode: Literal['transformed', 'round', 'right'] = 'transformed') → 'Shape'

Attempt to sweep the list of wires into a prismatic solid along the provided path

* **Parameters:**
  * **outerWire** ([*Wire*](#cadquery.occ_impl.shapes.Wire)) – the outermost wire
  * **innerWires** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*) – a list of inner wires
  * **path** ([*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Edge*](#cadquery.occ_impl.shapes.Edge)) – The wire to sweep the face resulting from the wires over
  * **makeSolid** (*bool*) – return Solid or Shell (default True)
  * **isFrenet** (*bool*) – Frenet mode (default False)
  * **mode** ([*Vector*](#cadquery.Vector) *|* [*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Edge*](#cadquery.occ_impl.shapes.Edge) *|* *None*) – additional sweep mode parameters
  * **transitionMode** (*Literal* *[* *'transformed'* *,*  *'round'* *,*  *'right'* *]*) – handling of profile orientation at C1 path discontinuities.
    Possible values are {‘transformed’,’round’, ‘right’} (default: ‘right’).
* **Returns:**
  a Solid object
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

#### *classmethod* sweep_multi(profiles: Iterable[[Wire](#cadquery.occ_impl.shapes.Wire) | [Face](#cadquery.occ_impl.shapes.Face)], path: [Wire](#cadquery.occ_impl.shapes.Wire) | [Edge](#cadquery.occ_impl.shapes.Edge), makeSolid: bool = True, isFrenet: bool = False, mode: [Vector](#cadquery.Vector) | [Wire](#cadquery.occ_impl.shapes.Wire) | [Edge](#cadquery.occ_impl.shapes.Edge) | None = None) → [Solid](#cadquery.occ_impl.shapes.Solid)

Multi section sweep. Only single outer profile per section is allowed.

* **Parameters:**
  * **profiles** (*Iterable* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Face*](#cadquery.occ_impl.shapes.Face) *]*) – list of profiles
  * **path** ([*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Edge*](#cadquery.occ_impl.shapes.Edge)) – The wire to sweep the face resulting from the wires over
  * **mode** ([*Vector*](#cadquery.Vector) *|* [*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Edge*](#cadquery.occ_impl.shapes.Edge) *|* *None*) – additional sweep mode parameters.
  * **makeSolid** (*bool*)
  * **isFrenet** (*bool*)
* **Returns:**
  a Solid object
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

### *class* cadquery.occ_impl.shapes.Vertex(obj: TopoDS_Shape, forConstruction: bool = False)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape)

A Single Point in Space

* **Parameters:**
  * **obj** (*TopoDS_Shape*)
  * **forConstruction** (*bool*)

#### Center() → [Vector](#cadquery.Vector)

The center of a vertex is itself!

* **Return type:**
  [*Vector*](#cadquery.Vector)

### *class* cadquery.occ_impl.shapes.Wire(obj: TopoDS_Shape)

Bases: [`Shape`](#cadquery.occ_impl.shapes.Shape), [`Mixin1D`](#cadquery.occ_impl.shapes.Mixin1D)

A series of connected, ordered Edges, that typically bounds a Face

* **Parameters:**
  **obj** (*TopoDS_Shape*)

#### Vertices() → List[[Vertex](#cadquery.occ_impl.shapes.Vertex)]

Ordered list of vertices of the wire.

* **Return type:**
  *List*[[*Vertex*](#cadquery.occ_impl.shapes.Vertex)]

#### *classmethod* assembleEdges(listOfEdges: Iterable[[Edge](#cadquery.occ_impl.shapes.Edge)]) → [Wire](#cadquery.occ_impl.shapes.Wire)

Attempts to build a wire that consists of the edges in the provided list

* **Parameters:**
  * **cls**
  * **listOfEdges** (*Iterable* *[*[*Edge*](#cadquery.occ_impl.shapes.Edge) *]*) – a list of Edge objects. The edges are not to be consecutive.
* **Returns:**
  a wire with the edges assembled
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

BRepBuilderAPI_MakeWire::Error() values:

* BRepBuilderAPI_WireDone = 0
* BRepBuilderAPI_EmptyWire = 1
* BRepBuilderAPI_DisconnectedWire = 2
* BRepBuilderAPI_NonManifoldWire = 3

#### chamfer2D(d: float, vertices: Iterable[[Vertex](#cadquery.occ_impl.shapes.Vertex)]) → [Wire](#cadquery.occ_impl.shapes.Wire)

Apply 2D chamfer to a wire

* **Parameters:**
  * **d** (*float*)
  * **vertices** (*Iterable* *[*[*Vertex*](#cadquery.occ_impl.shapes.Vertex) *]*)
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### close() → [Wire](#cadquery.occ_impl.shapes.Wire)

Close a Wire

* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### *classmethod* combine(listOfWires: Iterable[[Wire](#cadquery.occ_impl.shapes.Wire) | [Edge](#cadquery.occ_impl.shapes.Edge)], tol: float = 1e-09) → List[[Wire](#cadquery.occ_impl.shapes.Wire)]

Attempt to combine a list of wires and edges into a new wire.

* **Parameters:**
  * **cls**
  * **listOfWires** (*Iterable* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *|* [*Edge*](#cadquery.occ_impl.shapes.Edge) *]*)
  * **tol** (*float*) – default 1e-9
* **Returns:**
  List[Wire]
* **Return type:**
  *List*[[*Wire*](#cadquery.occ_impl.shapes.Wire)]

#### fillet(radius: float, vertices: Iterable[[Vertex](#cadquery.occ_impl.shapes.Vertex)] | None = None) → [Wire](#cadquery.occ_impl.shapes.Wire)

Apply 2D or 3D fillet to a wire

* **Parameters:**
  * **radius** (*float*) – the radius of the fillet, must be > zero
  * **vertices** (*Iterable* *[*[*Vertex*](#cadquery.occ_impl.shapes.Vertex) *]*  *|* *None*) – the vertices to delete (where the fillet will be applied).  By default
    all vertices are deleted except ends of open wires.
* **Returns:**
  A wire with filleted corners
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### fillet2D(radius: float, vertices: Iterable[[Vertex](#cadquery.occ_impl.shapes.Vertex)]) → [Wire](#cadquery.occ_impl.shapes.Wire)

Apply 2D fillet to a wire

* **Parameters:**
  * **radius** (*float*)
  * **vertices** (*Iterable* *[*[*Vertex*](#cadquery.occ_impl.shapes.Vertex) *]*)
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### *classmethod* makeCircle(radius: float, center: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], normal: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Wire](#cadquery.occ_impl.shapes.Wire)

Makes a Circle centered at the provided point, having normal in the provided direction

* **Parameters:**
  * **radius** (*float*) – floating point radius of the circle, must be > 0
  * **center** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – vector representing the center of the circle
  * **normal** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – vector representing the direction of the plane the circle should lie in
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### *classmethod* makeEllipse(x_radius: float, y_radius: float, center: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], normal: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], xDir: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], angle1: float = 360.0, angle2: float = 360.0, rotation_angle: float = 0.0, closed: bool = True) → [Wire](#cadquery.occ_impl.shapes.Wire)

Makes an Ellipse centered at the provided point, having normal in the provided direction

* **Parameters:**
  * **x_radius** (*float*) – floating point major radius of the ellipse (x-axis), must be > 0
  * **y_radius** (*float*) – floating point minor radius of the ellipse (y-axis), must be > 0
  * **center** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – vector representing the center of the circle
  * **normal** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – vector representing the direction of the plane the circle should lie in
  * **angle1** (*float*) – start angle of arc
  * **angle2** (*float*) – end angle of arc
  * **rotation_angle** (*float*) – angle to rotate the created ellipse / arc
  * **xDir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **closed** (*bool*)
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### *classmethod* makeHelix(pitch: float, height: float, radius: float, center: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 0.0), dir: ~cadquery.occ_impl.geom.Vector | ~typing.Tuple[int | float, int | float] | ~typing.Tuple[int | float, int | float, int | float] = Vector: (0.0, 0.0, 1.0), angle: float = 360.0, lefthand: bool = False) → [Wire](#cadquery.occ_impl.shapes.Wire)

Make a helix with a given pitch, height and radius
By default a cylindrical surface is used to create the helix. If
the fourth parameter is set (the apex given in degree) a conical surface is used instead’

* **Parameters:**
  * **pitch** (*float*)
  * **height** (*float*)
  * **radius** (*float*)
  * **center** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **dir** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **angle** (*float*)
  * **lefthand** (*bool*)
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### *classmethod* makePolygon(listOfVertices: Iterable[[Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]], forConstruction: bool = False, close: bool = False) → [Wire](#cadquery.occ_impl.shapes.Wire)

Construct a polygonal wire from points.

* **Parameters:**
  * **listOfVertices** (*Iterable* *[*[*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]* *]*)
  * **forConstruction** (*bool*)
  * **close** (*bool*)
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

#### offset2D(d: float, kind: Literal['arc', 'intersection', 'tangent'] = 'arc') → List[[Wire](#cadquery.occ_impl.shapes.Wire)]

Offsets a planar wire

* **Parameters:**
  * **d** (*float*)
  * **kind** (*Literal* *[* *'arc'* *,*  *'intersection'* *,*  *'tangent'* *]*)
* **Return type:**
  *List*[[*Wire*](#cadquery.occ_impl.shapes.Wire)]

#### stitch(other: [Wire](#cadquery.occ_impl.shapes.Wire)) → [Wire](#cadquery.occ_impl.shapes.Wire)

Attempt to stitch wires

* **Parameters:**
  **other** ([*Wire*](#cadquery.occ_impl.shapes.Wire))
* **Return type:**
  [*Wire*](#cadquery.occ_impl.shapes.Wire)

### cadquery.occ_impl.shapes.box(w: float, l: float, h: float) → [Shape](#cadquery.occ_impl.shapes.Shape)

Construct a solid box.

* **Parameters:**
  * **w** (*float*)
  * **l** (*float*)
  * **h** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.cap(s: [Shape](#cadquery.occ_impl.shapes.Shape), ctx: [Shape](#cadquery.occ_impl.shapes.Shape), constraints: Sequence[[Shape](#cadquery.occ_impl.shapes.Shape) | [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]] = ()) → [Shape](#cadquery.occ_impl.shapes.Shape)

Fill edges/wire possibly obeying constraints and try to connect smoothly to the context shape.

* **Parameters:**
  * **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **ctx** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **constraints** (*Sequence* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]* *]*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.chamfer(s: [Shape](#cadquery.occ_impl.shapes.Shape), e: [Shape](#cadquery.occ_impl.shapes.Shape), d: float) → [Shape](#cadquery.occ_impl.shapes.Shape)

Chamfer selected edges in a given shell or solid.

* **Parameters:**
  * **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **e** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **d** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.check(s: [Shape](#cadquery.occ_impl.shapes.Shape), results: List[Tuple[List[[Shape](#cadquery.occ_impl.shapes.Shape)], Any]] | None = None) → bool

Check if a shape is valid.

* **Parameters:**
  * **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **results** (*List* *[**Tuple* *[**List* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *]* *,* *Any* *]* *]*  *|* *None*)
* **Return type:**
  bool

### cadquery.occ_impl.shapes.circle(r: float) → [Shape](#cadquery.occ_impl.shapes.Shape)

Construct a circle.

* **Parameters:**
  **r** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.clean(s: [Shape](#cadquery.occ_impl.shapes.Shape)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Clean superfluous edges and faces.

* **Parameters:**
  **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.compound(\*s: [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)) → [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)

> Build compound from shapes.

compound(s: Sequence[cadquery.occ_impl.shapes.Shape]) -> cadquery.occ_impl.shapes.Shape

> Build compound from a sequence of shapes.
* **Parameters:**
  **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.cone(d1: float | int, d2: float | int, h: float | int) → [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)

> Construct a partial solid cone.

cone(d: Union[float, int], h: Union[float, int]) -> cadquery.occ_impl.shapes.Shape

> Construct a full solid cone.
* **Parameters:**
  * **d1** (*float* *|* *int*)
  * **d2** (*float* *|* *int*)
  * **h** (*float* *|* *int*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.cut(s1: [Shape](#cadquery.occ_impl.shapes.Shape), s2: [Shape](#cadquery.occ_impl.shapes.Shape), tol: float = 0.0) → [Shape](#cadquery.occ_impl.shapes.Shape)

Subtract two shapes.

* **Parameters:**
  * **s1** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **s2** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **tol** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.cylinder(d: float, h: float) → [Shape](#cadquery.occ_impl.shapes.Shape)

Construct a solid cylinder.

* **Parameters:**
  * **d** (*float*)
  * **h** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.downcast(obj: TopoDS_Shape) → TopoDS_Shape

Downcasts a TopoDS object to suitable specialized type

* **Parameters:**
  **obj** (*TopoDS_Shape*)
* **Return type:**
  *TopoDS_Shape*

### cadquery.occ_impl.shapes.edgesToWires(edges: Iterable[[Edge](#cadquery.occ_impl.shapes.Edge)], tol: float = 1e-06) → List[[Wire](#cadquery.occ_impl.shapes.Wire)]

Convert edges to a list of wires.

* **Parameters:**
  * **edges** (*Iterable* *[*[*Edge*](#cadquery.occ_impl.shapes.Edge) *]*)
  * **tol** (*float*)
* **Return type:**
  *List*[[*Wire*](#cadquery.occ_impl.shapes.Wire)]

### cadquery.occ_impl.shapes.ellipse(r1: float, r2: float) → [Shape](#cadquery.occ_impl.shapes.Shape)

Construct an ellipse.

* **Parameters:**
  * **r1** (*float*)
  * **r2** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.extrude(s: [Shape](#cadquery.occ_impl.shapes.Shape), d: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Shape](#cadquery.occ_impl.shapes.Shape)

Extrude a shape.

* **Parameters:**
  * **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **d** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.face(\*s: [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)) → [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)

> Build face from edges or wires.

face(s: Sequence[cadquery.occ_impl.shapes.Shape]) -> cadquery.occ_impl.shapes.Shape

> Build face from a sequence of edges or wires.
* **Parameters:**
  **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.fill(s: [Shape](#cadquery.occ_impl.shapes.Shape), constraints: Sequence[[Shape](#cadquery.occ_impl.shapes.Shape) | [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]] = ()) → [Shape](#cadquery.occ_impl.shapes.Shape)

Fill edges/wire possibly obeying constraints.

* **Parameters:**
  * **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **constraints** (*Sequence* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *|* [*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]* *]*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.fillet(s: [Shape](#cadquery.occ_impl.shapes.Shape), e: [Shape](#cadquery.occ_impl.shapes.Shape), r: float) → [Shape](#cadquery.occ_impl.shapes.Shape)

Fillet selected edges in a given shell or solid.

* **Parameters:**
  * **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **e** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **r** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.fix(obj: TopoDS_Shape) → TopoDS_Shape

Fix a TopoDS object to suitable specialized type

* **Parameters:**
  **obj** (*TopoDS_Shape*)
* **Return type:**
  *TopoDS_Shape*

### cadquery.occ_impl.shapes.fuse(s1: [Shape](#cadquery.occ_impl.shapes.Shape), s2: [Shape](#cadquery.occ_impl.shapes.Shape), tol: float = 0.0) → [Shape](#cadquery.occ_impl.shapes.Shape)

Fuse two shapes.

* **Parameters:**
  * **s1** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **s2** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **tol** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.intersect(s1: [Shape](#cadquery.occ_impl.shapes.Shape), s2: [Shape](#cadquery.occ_impl.shapes.Shape), tol: float = 0.0) → [Shape](#cadquery.occ_impl.shapes.Shape)

Intersect two shapes.

* **Parameters:**
  * **s1** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **s2** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **tol** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.loft(s: Sequence[[cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)], cap: bool = False, ruled: bool = False, continuity: Literal['C1', 'C2', 'C3'] = 'C2', parametrization: Literal['uniform', 'chordal', 'centripetal'] = 'uniform', degree: int = 3, compat: bool = True, smoothing: bool = False, weights: Tuple[float, float, float] = (1, 1, 1)) → [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)

> Loft edges, wires or faces. For faces cap has no effect. Do not mix faces with other types.

loft(

```
*
```

s: cadquery.occ_impl.shapes.Shape, cap: bool = False, ruled: bool = False, continuity: Literal[‘C1’, ‘C2’, ‘C3’] = ‘C2’, parametrization: Literal[‘uniform’, ‘chordal’, ‘centripetal’] = ‘uniform’, degree: int = 3, compat: bool = True, smoothing: bool = False, weights: Tuple[float, float, float] = (1, 1, 1)) -> cadquery.occ_impl.shapes.Shape

> Variadic loft overload.
* **Parameters:**
  * **s** (*Sequence* *[*[*Shape*](#cadquery.occ_impl.shapes.Shape) *]*)
  * **cap** (*bool*)
  * **ruled** (*bool*)
  * **continuity** (*Literal* *[* *'C1'* *,*  *'C2'* *,*  *'C3'* *]*)
  * **parametrization** (*Literal* *[* *'uniform'* *,*  *'chordal'* *,*  *'centripetal'* *]*)
  * **degree** (*int*)
  * **compat** (*bool*)
  * **smoothing** (*bool*)
  * **weights** (*Tuple* *[**float* *,* *float* *,* *float* *]*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.offset(s: [Shape](#cadquery.occ_impl.shapes.Shape), t: float, cap=True, both: bool = False, tol: float = 1e-06) → [Shape](#cadquery.occ_impl.shapes.Shape)

Offset or thicken faces or shells.

* **Parameters:**
  * **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **t** (*float*)
  * **both** (*bool*)
  * **tol** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.plane(w: float | int, l: float | int) → [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)

> Construct a finite planar face.

plane() -> cadquery.occ_impl.shapes.Shape

> Construct an infinite planar face.

> This is a crude approximation. Truly infinite faces in OCCT do not work as
> expected in all contexts.
* **Parameters:**
  * **w** (*float* *|* *int*)
  * **l** (*float* *|* *int*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.polygon(\*pts: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Shape](#cadquery.occ_impl.shapes.Shape)

Construct a polygon (closed polyline) from points.

* **Parameters:**
  **pts** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.polyline(\*pts: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Shape](#cadquery.occ_impl.shapes.Shape)

Construct a polyline from points.

* **Parameters:**
  **pts** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.rect(w: float, h: float) → [Shape](#cadquery.occ_impl.shapes.Shape)

Construct a rectangle.

* **Parameters:**
  * **w** (*float*)
  * **h** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.revolve(s: [Shape](#cadquery.occ_impl.shapes.Shape), p: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], d: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], a: float = 360)

Revolve a shape.

* **Parameters:**
  * **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **p** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **d** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **a** (*float*)

### cadquery.occ_impl.shapes.segment(p1: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], p2: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float]) → [Shape](#cadquery.occ_impl.shapes.Shape)

Construct a segment from two points.

* **Parameters:**
  * **p1** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **p2** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.shell(\*s: [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape), tol: float = 1e-06) → [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)

> Build shell from faces.

shell(s: Sequence[cadquery.occ_impl.shapes.Shape], tol: float = 1e-06) -> cadquery.occ_impl.shapes.Shape

> Build shell from a sequence of faces.
* **Parameters:**
  * **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **tol** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.solid(s1: [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape), \*sn: [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape), tol: float = 1e-06) → [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)

> Build solid from faces or shells.

solid(s: Sequence[cadquery.occ_impl.shapes.Shape], inner: Optional[Sequence[cadquery.occ_impl.shapes.Shape]] = None, tol: float = 1e-06) -> cadquery.occ_impl.shapes.Shape

> Build solid from a sequence of faces.
* **Parameters:**
  * **s1** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **sn** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **tol** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.sortWiresByBuildOrder(wireList: List[[Wire](#cadquery.occ_impl.shapes.Wire)]) → List[List[[Wire](#cadquery.occ_impl.shapes.Wire)]]

Tries to determine how wires should be combined into faces.

Assume:
: The wires make up one or more faces, which could have ‘holes’
  Outer wires are listed ahead of inner wires
  there are no wires inside wires inside wires
  ( IE, islands – we can deal with that later on )
  none of the wires are construction wires

Compute:
: one or more sets of wires, with the outer wire listed first, and inner
  ones

Returns, list of lists.

* **Parameters:**
  **wireList** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*)
* **Return type:**
  *List*[*List*[[*Wire*](#cadquery.occ_impl.shapes.Wire)]]

### cadquery.occ_impl.shapes.sphere(d: float) → [Shape](#cadquery.occ_impl.shapes.Shape)

Construct a solid sphere.

* **Parameters:**
  **d** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.spline(\*pts: ForwardRef('Vector') | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], tol: float = 1e-06, periodic: bool = False) → [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)

> Construct a spline from points.

spline(pts: Sequence[Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]], tgts: Optional[Sequence[Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]]] = None, params: Optional[Sequence[float]] = None, tol: float = 1e-06, periodic: bool = False, scale: bool = True) -> cadquery.occ_impl.shapes.Shape

> Construct a spline from a sequence points.
* **Parameters:**
  * **pts** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **tol** (*float*)
  * **periodic** (*bool*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.split(s1: [Shape](#cadquery.occ_impl.shapes.Shape), s2: [Shape](#cadquery.occ_impl.shapes.Shape)) → [Shape](#cadquery.occ_impl.shapes.Shape)

Split one shape with another.

* **Parameters:**
  * **s1** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **s2** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.sweep(s: [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape), path: [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape), aux: [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape) | None = None, cap: bool = False) → [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)

> Sweep edge, wire or face along a path. For faces cap has no effect.
> Do not mix faces with other types.

sweep(s: Sequence[cadquery.occ_impl.shapes.Shape], path: cadquery.occ_impl.shapes.Shape, aux: Optional[cadquery.occ_impl.shapes.Shape] = None, cap: bool = False) -> cadquery.occ_impl.shapes.Shape

> Sweep edges, wires or faces along a path, multiple sections are supported.
> For faces cap has no effect. Do not mix faces with other types.
* **Parameters:**
  * **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **path** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
  * **aux** ([*Shape*](#cadquery.occ_impl.shapes.Shape) *|* *None*)
  * **cap** (*bool*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.text(txt: str, size: float | int, font: str = 'Arial', path: str | None = None, kind: Literal['regular', 'bold', 'italic'] = 'regular', halign: Literal['center', 'left', 'right'] = 'center', valign: Literal['center', 'top', 'bottom'] = 'center') → [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)

> Create a flat text.

text(txt: str, size: Union[float, int], spine: cadquery.occ_impl.shapes.Shape, planar: bool = False, font: str = ‘Arial’, path: Optional[str] = None, kind: Literal[‘regular’, ‘bold’, ‘italic’] = ‘regular’, halign: Literal[‘center’, ‘left’, ‘right’] = ‘center’, valign: Literal[‘center’, ‘top’, ‘bottom’] = ‘center’) -> cadquery.occ_impl.shapes.Shape

> Create a text on a spine.

text(txt: str, size: Union[float, int], spine: cadquery.occ_impl.shapes.Shape, base: cadquery.occ_impl.shapes.Shape, font: str = ‘Arial’, path: Optional[str] = None, kind: Literal[‘regular’, ‘bold’, ‘italic’] = ‘regular’, halign: Literal[‘center’, ‘left’, ‘right’] = ‘center’, valign: Literal[‘center’, ‘top’, ‘bottom’] = ‘center’) -> cadquery.occ_impl.shapes.Shape

> Create a text on a spine and a base surface.
* **Parameters:**
  * **txt** (*str*)
  * **size** (*float* *|* *int*)
  * **font** (*str*)
  * **path** (*str* *|* *None*)
  * **kind** (*Literal* *[* *'regular'* *,*  *'bold'* *,*  *'italic'* *]*)
  * **halign** (*Literal* *[* *'center'* *,*  *'left'* *,*  *'right'* *]*)
  * **valign** (*Literal* *[* *'center'* *,*  *'top'* *,*  *'bottom'* *]*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.torus(d1: float, d2: float) → [Shape](#cadquery.occ_impl.shapes.Shape)

Construct a solid torus.

* **Parameters:**
  * **d1** (*float*)
  * **d2** (*float*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.vertex(x: float | int, y: float | int, z: float | int) → [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)

> Construct a vertex from coordinates.

vertex(p: Union[ForwardRef(‘Vector’), Tuple[Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]])

> Construct a vertex from VectorLike.
* **Parameters:**
  * **x** (*float* *|* *int*)
  * **y** (*float* *|* *int*)
  * **z** (*float* *|* *int*)
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.wire(\*s: [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)) → [cadquery.occ_impl.shapes.Shape](#cadquery.occ_impl.shapes.Shape)

Build wire from edges.

* **Parameters:**
  **s** ([*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  [*Shape*](#cadquery.occ_impl.shapes.Shape)

### cadquery.occ_impl.shapes.wiresToFaces(wireList: List[[Wire](#cadquery.occ_impl.shapes.Wire)]) → List[[Face](#cadquery.occ_impl.shapes.Face)]

Convert wires to a list of faces.

* **Parameters:**
  **wireList** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*)
* **Return type:**
  *List*[[*Face*](#cadquery.occ_impl.shapes.Face)]

### *class* cadquery.occ_impl.shapes.Mixin1D

Bases: `object`

#### curvatureAt(d: float, mode: Literal['length', 'parameter'] = 'length', resolution: float = 1e-06) → float

Calculate mean curvature along the underlying curve.

* **Parameters:**
  * **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
  * **d** (*float*) – distance or parameter value
  * **mode** (*Literal* *[* *'length'* *,*  *'parameter'* *]*) – position calculation mode (default: length)
  * **resolution** (*float*) – resolution of the calculation (default: 1e-6)
* **Returns:**
  mean curvature value at the specified d value.
* **Return type:**
  float

#### curvatures(ds: Iterable[float], mode: Literal['length', 'parameter'] = 'length', resolution: float = 1e-06) → List[float]

Calculate mean curvatures along the underlying curve.

* **Parameters:**
  * **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
  * **d** – distance or parameter values
  * **mode** (*Literal* *[* *'length'* *,*  *'parameter'* *]*) – position calculation mode (default: length)
  * **resolution** (*float*) – resolution of the calculation (default: 1e-6)
  * **ds** (*Iterable* *[**float* *]*)
* **Returns:**
  mean curvature value at the specified d value.
* **Return type:**
  *List*[float]

#### endPoint() → [Vector](#cadquery.Vector)

* **Returns:**
  a vector representing the end point of this edge.
* **Parameters:**
  **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
* **Return type:**
  [*Vector*](#cadquery.Vector)

Note, circles may have the start and end points the same

#### locationAt(d: float, mode: Literal['length', 'parameter'] = 'length', frame: Literal['frenet', 'corrected'] = 'frenet', planar: bool = False) → [Location](#cadquery.Location)

Generate a location along the underlying curve.

* **Parameters:**
  * **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
  * **d** (*float*) – distance or parameter value
  * **mode** (*Literal* *[* *'length'* *,*  *'parameter'* *]*) – position calculation mode (default: length)
  * **frame** (*Literal* *[* *'frenet'* *,*  *'corrected'* *]*) – moving frame calculation method (default: frenet)
  * **planar** (*bool*) – planar mode
* **Returns:**
  A Location object representing local coordinate system at the specified distance.
* **Return type:**
  [*Location*](#cadquery.Location)

#### locations(ds: Iterable[float], mode: Literal['length', 'parameter'] = 'length', frame: Literal['frenet', 'corrected'] = 'frenet', planar: bool = False) → List[[Location](#cadquery.Location)]

Generate locations along the curve.

* **Parameters:**
  * **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
  * **ds** (*Iterable* *[**float* *]*) – distance or parameter values
  * **mode** (*Literal* *[* *'length'* *,*  *'parameter'* *]*) – position calculation mode (default: length)
  * **frame** (*Literal* *[* *'frenet'* *,*  *'corrected'* *]*) – moving frame calculation method (default: frenet)
  * **planar** (*bool*) – planar mode
* **Returns:**
  A list of Location objects representing local coordinate systems at the specified distances.
* **Return type:**
  *List*[[*Location*](#cadquery.Location)]

#### normal() → [Vector](#cadquery.Vector)

Calculate the normal Vector. Only possible for planar curves.

* **Returns:**
  normal vector
* **Parameters:**
  **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### paramAt(d: float | int | [Vector](#cadquery.Vector)) → float

Compute parameter value at the specified normalized distance or a point.

* **Parameters:**
  * **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
  * **d** (*float* *|* *int* *|* [*Vector*](#cadquery.Vector)) – normalized distance [0, 1] or a point
* **Returns:**
  parameter value
* **Return type:**
  float

#### positionAt(d: float, mode: Literal['length', 'parameter'] = 'length') → [Vector](#cadquery.Vector)

Generate a position along the underlying curve.

* **Parameters:**
  * **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
  * **d** (*float*) – distance or parameter value
  * **mode** (*Literal* *[* *'length'* *,*  *'parameter'* *]*) – position calculation mode (default: length)
* **Returns:**
  A Vector on the underlying curve located at the specified d value.
* **Return type:**
  [*Vector*](#cadquery.Vector)

#### positions(ds: Iterable[float], mode: Literal['length', 'parameter'] = 'length') → List[[Vector](#cadquery.Vector)]

Generate positions along the underlying curve.

* **Parameters:**
  * **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
  * **ds** (*Iterable* *[**float* *]*) – distance or parameter values
  * **mode** (*Literal* *[* *'length'* *,*  *'parameter'* *]*) – position calculation mode (default: length)
* **Returns:**
  A list of Vector objects.
* **Return type:**
  *List*[[*Vector*](#cadquery.Vector)]

#### project(face: [Face](#cadquery.occ_impl.shapes.Face), d: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], closest: bool = True) → T1D | List[T1D]

Project onto a face along the specified direction

* **Parameters:**
  * **self** (*T1D*)
  * **face** ([*Face*](#cadquery.occ_impl.shapes.Face))
  * **d** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*)
  * **closest** (*bool*)
* **Return type:**
  *T1D* | *List*[*T1D*]

#### radius() → float

Calculate the radius.

Note that when applied to a Wire, the radius is simply the radius of the first edge.

* **Returns:**
  radius
* **Raises:**
  **ValueError** – if kernel can not reduce the shape to a circular edge
* **Parameters:**
  **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
* **Return type:**
  float

#### sample(n: int | float) → Tuple[List[[Vector](#cadquery.Vector)], List[float]]

Sample a curve based on a number of points or deflection.

* **Parameters:**
  * **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
  * **n** (*int* *|* *float*) – Number of positions or deflection
* **Returns:**
  A list of Vectors and a list of parameters.
* **Return type:**
  *Tuple*[*List*[[*Vector*](#cadquery.Vector)], *List*[float]]

#### startPoint() → [Vector](#cadquery.Vector)

* **Returns:**
  a vector representing the start point of this edge
* **Parameters:**
  **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
* **Return type:**
  [*Vector*](#cadquery.Vector)

Note, circles may have the start and end points the same

#### tangentAt(locationParam: float = 0.5, mode: Literal['length', 'parameter'] = 'length') → [Vector](#cadquery.Vector)

Compute tangent vector at the specified location.

* **Parameters:**
  * **self** ([*Mixin1DProtocol*](#cadquery.occ_impl.shapes.Mixin1DProtocol))
  * **locationParam** (*float*) – distance or parameter value (default: 0.5)
  * **mode** (*Literal* *[* *'length'* *,*  *'parameter'* *]*) – position calculation mode (default: parameter)
* **Returns:**
  tangent vector
* **Return type:**
  [*Vector*](#cadquery.Vector)

### *class* cadquery.occ_impl.shapes.Mixin3D

Bases: `object`

#### chamfer(length: float, length2: float | None, edgeList: Iterable[[Edge](#cadquery.occ_impl.shapes.Edge)]) → Any

Chamfers the specified edges of this solid.

* **Parameters:**
  * **self** (*Any*)
  * **length** (*float*) – length > 0, the length (length) of the chamfer
  * **length2** (*float* *|* *None*) – length2 > 0, optional parameter for asymmetrical chamfer. Should be None if not required.
  * **edgeList** (*Iterable* *[*[*Edge*](#cadquery.occ_impl.shapes.Edge) *]*) – a list of Edge objects, which must belong to this solid
* **Returns:**
  Chamfered solid
* **Return type:**
  *Any*

#### dprism(self: TS, basis: [cadquery.occ_impl.shapes.Face](#cadquery.occ_impl.shapes.Face) | None, profiles: List[[cadquery.occ_impl.shapes.Wire](#cadquery.occ_impl.shapes.Wire)], depth: float | int | NoneType = None, taper: float | int = 0, upToFace: [cadquery.occ_impl.shapes.Face](#cadquery.occ_impl.shapes.Face) | None = None, thruAll: bool = True, additive: bool = True) → 'Solid'

Make a prismatic feature (additive or subtractive)

* **Parameters:**
  * **self** (*TS*)
  * **basis** ([*Face*](#cadquery.occ_impl.shapes.Face) *|* *None*) – face to perform the operation on
  * **profiles** (*List* *[*[*Wire*](#cadquery.occ_impl.shapes.Wire) *]*) – list of profiles
  * **depth** (*float* *|* *int* *|* *None*) – depth of the cut or extrusion
  * **upToFace** ([*Face*](#cadquery.occ_impl.shapes.Face) *|* *None*) – a face to extrude until
  * **thruAll** (*bool*) – cut thruAll
  * **taper** (*float* *|* *int*)
  * **additive** (*bool*)
* **Returns:**
  a Solid object
* **Return type:**
  [*Solid*](#cadquery.occ_impl.shapes.Solid)

#### fillet(radius: float, edgeList: Iterable[[Edge](#cadquery.occ_impl.shapes.Edge)]) → Any

Fillets the specified edges of this solid.

* **Parameters:**
  * **self** (*Any*)
  * **radius** (*float*) – float > 0, the radius of the fillet
  * **edgeList** (*Iterable* *[*[*Edge*](#cadquery.occ_impl.shapes.Edge) *]*) – a list of Edge objects, which must belong to this solid
* **Returns:**
  Filleted solid
* **Return type:**
  *Any*

#### isInside(point: [Vector](#cadquery.Vector) | Tuple[int | float, int | float] | Tuple[int | float, int | float, int | float], tolerance: float = 1e-06) → bool

Returns whether or not the point is inside a solid or compound
object within the specified tolerance.

* **Parameters:**
  * **self** ([*ShapeProtocol*](#cadquery.occ_impl.shapes.ShapeProtocol))
  * **point** ([*Vector*](#cadquery.Vector) *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *]*  *|* *Tuple* *[**int* *|* *float* *,* *int* *|* *float* *,* *int* *|* *float* *]*) – tuple or Vector representing 3D point to be tested
  * **tolerance** (*float*) – tolerance for inside determination, default=1.0e-6
* **Returns:**
  bool indicating whether or not point is within solid
* **Return type:**
  bool

#### shell(faceList: Iterable[[Face](#cadquery.occ_impl.shapes.Face)] | None, thickness: float, tolerance: float = 0.0001, kind: Literal['arc', 'intersection'] = 'arc') → Any

Make a shelled solid of self.

* **Parameters:**
  * **self** (*Any*)
  * **faceList** (*Iterable* *[*[*Face*](#cadquery.occ_impl.shapes.Face) *]*  *|* *None*) – List of faces to be removed, which must be part of the solid. Can
    be an empty list.
  * **thickness** (*float*) – Floating point thickness. Positive shells outwards, negative
    shells inwards.
  * **tolerance** (*float*) – Modelling tolerance of the method, default=0.0001.
  * **kind** (*Literal* *[* *'arc'* *,*  *'intersection'* *]*)
* **Returns:**
  A shelled solid.
* **Return type:**
  *Any*

<a id="module-cadquery.selectors"></a>

### *class* cadquery.selectors.AndSelector(left, right)

Bases: [`BinarySelector`](#cadquery.selectors.BinarySelector)

Intersection selector. Returns objects that is selected by both selectors.

### *class* cadquery.selectors.AreaNthSelector(n: int, directionMax: bool = True, tolerance: float = 0.0001)

Bases: `_NthSelector`

Selects the object(s) with Nth area

Applicability:
: - Faces, Shells, Solids - Shape.Area() is used to compute area
  - closed planar Wires - a temporary face is created to compute area

Will ignore non-planar or non-closed wires.

Among other things can be used to select one of
the nested coplanar wires or faces.

For example to create a fillet on a shank:

```default
result = (
    cq.Workplane("XY")
    .circle(5)
    .extrude(2)
    .circle(2)
    .extrude(10)
    .faces(">Z[-2]")
    .wires(AreaNthSelector(0))
    .fillet(2)
)
```

Or to create a lip on a case seam:

```default
result = (
    cq.Workplane("XY")
    .rect(20, 20)
    .extrude(10)
    .edges("|Z or <Z")
    .fillet(2)
    .faces(">Z")
    .shell(2)
    .faces(">Z")
    .wires(AreaNthSelector(-1))
    .toPending()
    .workplane()
    .offset2D(-1)
    .extrude(1)
    .faces(">Z[-2]")
    .wires(AreaNthSelector(0))
    .toPending()
    .workplane()
    .cutBlind(2)
)
```

* **Parameters:**
  * **n** (*int*)
  * **directionMax** (*bool*)
  * **tolerance** (*float*)

#### key(obj: Shape) → float

Return the key for ordering. Can raise a ValueError if obj can not be
used to create a key, which will result in obj being dropped by the
clustering method.

* **Parameters:**
  **obj** (*Shape*)
* **Return type:**
  float

### *class* cadquery.selectors.BaseDirSelector(vector: [Vector](#cadquery.Vector), tolerance: float = 0.0001)

Bases: [`Selector`](#cadquery.selectors.Selector)

A selector that handles selection on the basis of a single direction vector.

* **Parameters:**
  * **vector** ([*Vector*](#cadquery.Vector))
  * **tolerance** (*float*)

#### filter(objectList: Sequence[Shape]) → List[Shape]

There are lots of kinds of filters, but for planes they are always
based on the normal of the plane, and for edges on the tangent vector
along the edge

* **Parameters:**
  **objectList** (*Sequence* *[**Shape* *]*)
* **Return type:**
  *List*[*Shape*]

#### test(vec: [Vector](#cadquery.Vector)) → bool

Test a specified vector. Subclasses override to provide other implementations

* **Parameters:**
  **vec** ([*Vector*](#cadquery.Vector))
* **Return type:**
  bool

### *class* cadquery.selectors.BinarySelector(left, right)

Bases: [`Selector`](#cadquery.selectors.Selector)

Base class for selectors that operates with two other
selectors. Subclass must implement the :filterResults(): method.

#### filter(objectList: Sequence[Shape])

Filter the provided list.

The default implementation returns the original list unfiltered.

* **Parameters:**
  **objectList** (*list* *of* *OCCT primitives*) – list to filter
* **Returns:**
  filtered list

### *class* cadquery.selectors.BoxSelector(point0, point1, boundingbox=False)

Bases: [`Selector`](#cadquery.selectors.Selector)

Selects objects inside the 3D box defined by 2 points.

If boundingbox is True only the objects that have their bounding
box inside the given box is selected. Otherwise only center point
of the object is tested.

Applicability: all types of shapes

Example:

```default
CQ(aCube).edges(BoxSelector((0, 1, 0), (1, 2, 1)))
```

#### filter(objectList: Sequence[Shape])

Filter the provided list.

The default implementation returns the original list unfiltered.

* **Parameters:**
  **objectList** (*list* *of* *OCCT primitives*) – list to filter
* **Returns:**
  filtered list

### *class* cadquery.selectors.CenterNthSelector(vector: [Vector](#cadquery.Vector), n: int, directionMax: bool = True, tolerance: float = 0.0001)

Bases: `_NthSelector`

Sorts objects into a list with order determined by the distance of their center projected onto the specified direction.

Applicability:
: All Shapes.

* **Parameters:**
  * **vector** ([*Vector*](#cadquery.Vector))
  * **n** (*int*)
  * **directionMax** (*bool*)
  * **tolerance** (*float*)

#### key(obj: Shape) → float

Return the key for ordering. Can raise a ValueError if obj can not be
used to create a key, which will result in obj being dropped by the
clustering method.

* **Parameters:**
  **obj** (*Shape*)
* **Return type:**
  float

### *class* cadquery.selectors.DirectionMinMaxSelector(vector: [Vector](#cadquery.Vector), directionMax: bool = True, tolerance: float = 0.0001)

Bases: [`CenterNthSelector`](#cadquery.selectors.CenterNthSelector)

Selects objects closest or farthest in the specified direction.

Applicability:
: All object types. for a vertex, its point is used. for all other kinds
  of objects, the center of mass of the object is used.

You can use the string shortcuts >(X|Y|Z) or <(X|Y|Z) if you want to select
based on a cardinal direction.

For example this:

```default
CQ(aCube).faces(DirectionMinMaxSelector((0, 0, 1), True))
```

Means to select the face having the center of mass farthest in the positive
z direction, and is the same as:

```default
CQ(aCube).faces(">Z")
```

* **Parameters:**
  * **vector** ([*Vector*](#cadquery.Vector))
  * **directionMax** (*bool*)
  * **tolerance** (*float*)

### *class* cadquery.selectors.DirectionNthSelector(vector: [Vector](#cadquery.Vector), n: int, directionMax: bool = True, tolerance: float = 0.0001)

Bases: [`ParallelDirSelector`](#cadquery.selectors.ParallelDirSelector), [`CenterNthSelector`](#cadquery.selectors.CenterNthSelector)

Filters for objects parallel (or normal) to the specified direction then returns the Nth one.

Applicability:
: Linear Edges
  Planar Faces

* **Parameters:**
  * **vector** ([*Vector*](#cadquery.Vector))
  * **n** (*int*)
  * **directionMax** (*bool*)
  * **tolerance** (*float*)

#### filter(objectlist: Sequence[Shape]) → List[Shape]

There are lots of kinds of filters, but for planes they are always
based on the normal of the plane, and for edges on the tangent vector
along the edge

* **Parameters:**
  **objectlist** (*Sequence* *[**Shape* *]*)
* **Return type:**
  *List*[*Shape*]

### *class* cadquery.selectors.DirectionSelector(vector: [Vector](#cadquery.Vector), tolerance: float = 0.0001)

Bases: [`BaseDirSelector`](#cadquery.selectors.BaseDirSelector)

Selects objects aligned with the provided direction.

Applicability:
: Linear Edges
  Planar Faces

Use the string syntax shortcut +/-(X|Y|Z) if you want to select based on a cardinal direction.

Example:

```default
CQ(aCube).faces(DirectionSelector((0, 0, 1)))
```

selects faces with the normal in the z direction, and is equivalent to:

```default
CQ(aCube).faces("+Z")
```

* **Parameters:**
  * **vector** ([*Vector*](#cadquery.Vector))
  * **tolerance** (*float*)

#### test(vec: [Vector](#cadquery.Vector)) → bool

Test a specified vector. Subclasses override to provide other implementations

* **Parameters:**
  **vec** ([*Vector*](#cadquery.Vector))
* **Return type:**
  bool

### *class* cadquery.selectors.InverseSelector(selector)

Bases: [`Selector`](#cadquery.selectors.Selector)

Inverts the selection of given selector. In other words, selects
all objects that is not selected by given selector.

#### filter(objectList: Sequence[Shape])

Filter the provided list.

The default implementation returns the original list unfiltered.

* **Parameters:**
  **objectList** (*list* *of* *OCCT primitives*) – list to filter
* **Returns:**
  filtered list

### *class* cadquery.selectors.LengthNthSelector(n: int, directionMax: bool = True, tolerance: float = 0.0001)

Bases: `_NthSelector`

Select the object(s) with the Nth length

Applicability:
: All Edge and Wire objects

* **Parameters:**
  * **n** (*int*)
  * **directionMax** (*bool*)
  * **tolerance** (*float*)

#### key(obj: Shape) → float

Return the key for ordering. Can raise a ValueError if obj can not be
used to create a key, which will result in obj being dropped by the
clustering method.

* **Parameters:**
  **obj** (*Shape*)
* **Return type:**
  float

### *class* cadquery.selectors.NearestToPointSelector(pnt)

Bases: [`Selector`](#cadquery.selectors.Selector)

Selects object nearest the provided point.

If the object is a vertex or point, the distance
is used. For other kinds of shapes, the center of mass
is used to to compute which is closest.

Applicability: All Types of Shapes

Example:

```default
CQ(aCube).vertices(NearestToPointSelector((0, 1, 0)))
```

returns the vertex of the unit cube closest to the point x=0,y=1,z=0

#### filter(objectList: Sequence[Shape])

Filter the provided list.

The default implementation returns the original list unfiltered.

* **Parameters:**
  **objectList** (*list* *of* *OCCT primitives*) – list to filter
* **Returns:**
  filtered list

### *class* cadquery.selectors.ParallelDirSelector(vector: [Vector](#cadquery.Vector), tolerance: float = 0.0001)

Bases: [`BaseDirSelector`](#cadquery.selectors.BaseDirSelector)

Selects objects parallel with the provided direction.

Applicability:
: Linear Edges
  Planar Faces

Use the string syntax shortcut |(X|Y|Z) if you want to select based on a cardinal direction.

Example:

```default
CQ(aCube).faces(ParallelDirSelector((0, 0, 1)))
```

selects faces with the normal parallel to the z direction, and is equivalent to:

```default
CQ(aCube).faces("|Z")
```

* **Parameters:**
  * **vector** ([*Vector*](#cadquery.Vector))
  * **tolerance** (*float*)

#### test(vec: [Vector](#cadquery.Vector)) → bool

Test a specified vector. Subclasses override to provide other implementations

* **Parameters:**
  **vec** ([*Vector*](#cadquery.Vector))
* **Return type:**
  bool

### *class* cadquery.selectors.PerpendicularDirSelector(vector: [Vector](#cadquery.Vector), tolerance: float = 0.0001)

Bases: [`BaseDirSelector`](#cadquery.selectors.BaseDirSelector)

Selects objects perpendicular with the provided direction.

Applicability:
: Linear Edges
  Planar Faces

Use the string syntax shortcut #(X|Y|Z) if you want to select based on a
cardinal direction.

Example:

```default
CQ(aCube).faces(PerpendicularDirSelector((0, 0, 1)))
```

selects faces with the normal perpendicular to the z direction, and is equivalent to:

```default
CQ(aCube).faces("#Z")
```

* **Parameters:**
  * **vector** ([*Vector*](#cadquery.Vector))
  * **tolerance** (*float*)

#### test(vec: [Vector](#cadquery.Vector)) → bool

Test a specified vector. Subclasses override to provide other implementations

* **Parameters:**
  **vec** ([*Vector*](#cadquery.Vector))
* **Return type:**
  bool

### *class* cadquery.selectors.RadiusNthSelector(n: int, directionMax: bool = True, tolerance: float = 0.0001)

Bases: `_NthSelector`

Select the object with the Nth radius.

Applicability:
: All Edge and Wires.

Will ignore any shape that can not be represented as a circle or an arc of
a circle.

* **Parameters:**
  * **n** (*int*)
  * **directionMax** (*bool*)
  * **tolerance** (*float*)

#### key(obj: Shape) → float

Return the key for ordering. Can raise a ValueError if obj can not be
used to create a key, which will result in obj being dropped by the
clustering method.

* **Parameters:**
  **obj** (*Shape*)
* **Return type:**
  float

### *class* cadquery.selectors.Selector

Bases: `object`

Filters a list of objects.

Filters must provide a single method that filters objects.

#### filter(objectList: Sequence[Shape]) → List[Shape]

Filter the provided list.

The default implementation returns the original list unfiltered.

* **Parameters:**
  **objectList** (*list* *of* *OCCT primitives*) – list to filter
* **Returns:**
  filtered list
* **Return type:**
  *List*[*Shape*]

### *class* cadquery.selectors.StringSyntaxSelector(selectorString)

Bases: [`Selector`](#cadquery.selectors.Selector)

Filter lists objects using a simple string syntax. All of the filters available in the string syntax
are also available ( usually with more functionality ) through the creation of full-fledged
selector objects. see [`Selector`](#cadquery.selectors.Selector) and its subclasses

Filtering works differently depending on the type of object list being filtered.

* **Parameters:**
  **selectorString** – A two-part selector string, [selector][axis]
* **Returns:**
  objects that match the specified selector

**\*Modifiers\*** are `('|','+','-','<','>','%')`

> * **|:**
>   parallel to ( same as [`ParallelDirSelector`](#cadquery.selectors.ParallelDirSelector) ). Can return multiple objects.
> * **#:**
>   perpendicular to (same as [`PerpendicularDirSelector`](#cadquery.selectors.PerpendicularDirSelector) )
> * **+:**
>   positive direction (same as [`DirectionSelector`](#cadquery.selectors.DirectionSelector) )
> * **-:**
>   negative direction (same as [`DirectionSelector`](#cadquery.selectors.DirectionSelector)  )
> * **>:**
>   maximize (same as [`DirectionMinMaxSelector`](#cadquery.selectors.DirectionMinMaxSelector) with directionMax=True)
> * **<:**
>   minimize (same as [`DirectionMinMaxSelector`](#cadquery.selectors.DirectionMinMaxSelector) with directionMax=False )
> * **%:**
>   curve/surface type (same as [`TypeSelector`](#cadquery.selectors.TypeSelector))

**\*axisStrings\*** are: `X,Y,Z,XY,YZ,XZ` or `(x,y,z)` which defines an arbitrary direction

It is possible to combine simple selectors together using logical operations.
The following operations are supported

> * **and:**
>   Logical AND, e.g. >X and >Y
> * **or:**
>   Logical OR, e.g. |X or |Y
> * **not:**
>   Logical NOT, e.g. not #XY
> * **exc(ept):**
>   Set difference (equivalent to AND NOT): |X exc >Z

Finally, it is also possible to use even more complex expressions with nesting
and arbitrary number of terms, e.g.

> (not >X[0] and #XY) or >XY[0]

Selectors are a complex topic: see [Selectors Reference](selectors.md#selector-reference) for more information

#### filter(objectList: Sequence[Shape])

Filter give object list through th already constructed complex selector object

* **Parameters:**
  **objectList** (*Sequence* *[**Shape* *]*)

### *class* cadquery.selectors.SubtractSelector(left, right)

Bases: [`BinarySelector`](#cadquery.selectors.BinarySelector)

Difference selector. Subtract results of a selector from another
selectors results.

### *class* cadquery.selectors.SumSelector(left, right)

Bases: [`BinarySelector`](#cadquery.selectors.BinarySelector)

Union selector. Returns the sum of two selectors results.

### *class* cadquery.selectors.TypeSelector(typeString: str)

Bases: [`Selector`](#cadquery.selectors.Selector)

Selects objects having the prescribed geometry type.

Applicability:
: Faces: PLANE, CYLINDER, CONE, SPHERE, TORUS, BEZIER, BSPLINE, REVOLUTION, EXTRUSION, OFFSET, OTHER
  Edges: LINE, CIRCLE, ELLIPSE, HYPERBOLA, PARABOLA, BEZIER, BSPLINE, OFFSET, OTHER

You can use the string selector syntax. For example this:

```default
CQ(aCube).faces(TypeSelector("PLANE"))
```

will select 6 faces, and is equivalent to:

```default
CQ(aCube).faces("%PLANE")
```

* **Parameters:**
  **typeString** (*str*)

#### filter(objectList: Sequence[Shape]) → List[Shape]

Filter the provided list.

The default implementation returns the original list unfiltered.

* **Parameters:**
  **objectList** (*list* *of* *OCCT primitives*) – list to filter
* **Returns:**
  filtered list
* **Return type:**
  *List*[*Shape*]

<a id="module-cadquery.occ_impl.exporters.assembly"></a>

### cadquery.occ_impl.exporters.assembly.exportAssembly(assy: AssemblyProtocol, path: str, mode: Literal['default', 'fused'] = 'default', \*\*kwargs) → bool

Export an assembly to a STEP file.

kwargs is used to provide optional keyword arguments to configure the exporter.

* **Parameters:**
  * **assy** (*AssemblyProtocol*) – assembly
  * **path** (*str*) – Path and filename for writing
  * **mode** (*Literal* *[* *'default'* *,*  *'fused'* *]*) – STEP export mode. The options are “default”, and “fused” (a single fused compound).
    It is possible that fused mode may exhibit low performance.
  * **fuzzy_tol** (*float*) – OCCT fuse operation tolerance setting used only for fused assembly export.
  * **glue** (*bool*) – Enable gluing mode for improved performance during fused assembly export.
    This option should only be used for non-intersecting shapes or those that are only touching or partially overlapping.
    Note that when glue is enabled, the resulting fused shape may be invalid if shapes are intersecting in an incompatible way.
    Defaults to False.
  * **write_pcurves** (*bool*) – Enable or disable writing parametric curves to the STEP file. Default True.
    If False, writes STEP file without pcurves. This decreases the size of the resulting STEP file.
  * **precision_mode** (*int*) – Controls the uncertainty value for STEP entities. Specify -1, 0, or 1. Default 0.
    See OCCT documentation.
* **Return type:**
  bool

### cadquery.occ_impl.exporters.assembly.exportCAF(assy: AssemblyProtocol, path: str) → bool

Export an assembly to a OCAF xml file (internal OCCT format).

* **Parameters:**
  * **assy** (*AssemblyProtocol*)
  * **path** (*str*)
* **Return type:**
  bool

### cadquery.occ_impl.exporters.assembly.exportGLTF(assy: AssemblyProtocol, path: str, binary: bool | None = None, tolerance: float = 0.001, angularTolerance: float = 0.1)

Export an assembly to a gltf file.

* **Parameters:**
  * **assy** (*AssemblyProtocol*)
  * **path** (*str*)
  * **binary** (*bool* *|* *None*)
  * **tolerance** (*float*)
  * **angularTolerance** (*float*)

### cadquery.occ_impl.exporters.assembly.exportVRML(assy: AssemblyProtocol, path: str, tolerance: float = 0.001, angularTolerance: float = 0.1)

Export an assembly to a vrml file using vtk.

* **Parameters:**
  * **assy** (*AssemblyProtocol*)
  * **path** (*str*)
  * **tolerance** (*float*)
  * **angularTolerance** (*float*)

### cadquery.occ_impl.exporters.assembly.exportVTKJS(assy: AssemblyProtocol, path: str)

Export an assembly to a zipped vtkjs. NB: .zip extensions is added to path.

* **Parameters:**
  * **assy** (*AssemblyProtocol*)
  * **path** (*str*)

### cadquery.occ_impl.assembly.toJSON(assy: AssemblyProtocol, color: Tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0), tolerance: float = 0.001) → List[Dict[str, Any]]

Export an object to a structure suitable for converting to VTK.js JSON.

* **Parameters:**
  * **assy** (*AssemblyProtocol*)
  * **color** (*Tuple* *[**float* *,* *float* *,* *float* *,* *float* *]*)
  * **tolerance** (*float*)
* **Return type:**
  *List*[*Dict*[str, *Any*]]

### *class* cadquery.occ_impl.exporters.dxf.DxfDocument(dxfversion: str = 'AC1027', setup: bool | List[str] = False, doc_units: int = 4, , metadata: Dict[str, str] | None = None, approx: Literal['spline', 'arc'] | None = None, tolerance: float = 0.001)

Create DXF document from CadQuery objects.

A wrapper for [ezdxf](https://ezdxf.readthedocs.io/) providing methods for
converting [`cadquery.Workplane`](#cadquery.Workplane) objects to DXF entities.

The ezdxf document is available as the property `document`, allowing most
features of ezdxf to be utilised directly.

### Example usage

```python
rectangle = cq.Workplane().rect(10, 20)

dxf = DxfDocument()
dxf.add_shape(rectangle)
dxf.document.saveas("rectangle.dxf")
```

```python
rectangle = cq.Workplane().rect(10, 20)
circle = cq.Workplane().circle(3)

dxf = DxfDocument()
dxf = (
    dxf.add_layer("layer_1", color=2)
    .add_layer("layer_2", color=3)
    .add_shape(rectangle, "layer_1")
    .add_shape(circle, "layer_2")
)
dxf.document.saveas("rectangle-with-hole.dxf")
```

* **Parameters:**
  * **dxfversion** (*str*)
  * **setup** (*bool* *|* *List* *[**str* *]*)
  * **doc_units** (*int*)
  * **metadata** (*Dict* *[**str* *,* *str* *]*  *|* *None*)
  * **approx** (*Literal* *[* *'spline'* *,*  *'arc'* *]*  *|* *None*)
  * **tolerance** (*float*)

#### \_\_init_\_(dxfversion: str = 'AC1027', setup: bool | List[str] = False, doc_units: int = 4, , metadata: Dict[str, str] | None = None, approx: Literal['spline', 'arc'] | None = None, tolerance: float = 0.001)

Initialize DXF document.

* **Parameters:**
  * **dxfversion** (*str*) – [`DXF version specifier`](https://ezdxf.readthedocs.io/en/stable/drawing/drawing.html#ezdxf.document.Drawing.dxfversion)
    as string, default is “AC1027” respectively “R2013”
  * **setup** (*bool* *|* *List* *[**str* *]*) – setup default styles, `False` for no setup, `True` to set up
    everything or a list of topics as strings, e.g. `["linetypes", "styles"]`
    refer to [`ezdxf.new()`](https://ezdxf.readthedocs.io/en/stable/drawing/management.html#ezdxf.new).
  * **doc_units** (*int*) – ezdxf document/modelspace [units](https://ezdxf.readthedocs.io/en/stable/concepts/units.html)
  * **metadata** (*Dict* *[**str* *,* *str* *]*  *|* *None*) – document [metadata](https://ezdxf.readthedocs.io/en/stable/drawing/management.html#ezdxf-metadata) a dictionary of name value pairs
  * **approx** (*Literal* *[* *'spline'* *,*  *'arc'* *]*  *|* *None*) – 

    Approximation strategy for converting [`cadquery.Workplane`](#cadquery.Workplane) objects to DXF entities:

    `None`
    : no approximation applied

    `"spline"`
    : all splines approximated as cubic splines

    `"arc"`
    : all curves approximated as arcs and straight segments
  * **tolerance** (*float*) – Approximation tolerance for converting [`cadquery.Workplane`](#cadquery.Workplane) objects to DXF entities.

#### add_layer(name: str, , color: int = 7, linetype: str = 'CONTINUOUS') → Self

Create a layer definition

Refer to [ezdxf layers](https://ezdxf.readthedocs.io/en/stable/concepts/layers.html#layer-concept) and
[ezdxf layer tutorial](https://ezdxf.readthedocs.io/en/stable/tutorials/layers.html).

* **Parameters:**
  * **name** (*str*) – layer definition name
  * **color** (*int*) – color index. Standard colors include:
    1 red, 2 yellow, 3 green, 4 cyan, 5 blue, 6 magenta, 7 white/black
  * **linetype** (*str*) – ezdxf [line type](https://ezdxf.readthedocs.io/en/stable/concepts/linetypes.html)
* **Return type:**
  *Self*

#### add_shape(shape: WorkplaneLike | [Shape](#cadquery.occ_impl.shapes.Shape), layer: str = '') → Self

Add CadQuery shape to a DXF layer.

* **Parameters:**
  * **s** – CadQuery Workplane or Shape
  * **layer** (*str*) – layer definition name
  * **shape** (*WorkplaneLike* *|* [*Shape*](#cadquery.occ_impl.shapes.Shape))
* **Return type:**
  *Self*
