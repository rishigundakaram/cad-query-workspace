<a id="selector-reference"></a>

# Selectors Reference

CadQuery selector strings allow filtering various types of object lists. Most commonly, Edges, Faces, and Vertices are
used, but all objects types can be filtered.

Object lists are created by using the following methods, which each collect a type of shape:

> * [`cadquery.Workplane.vertices()`](classreference.md#cadquery.Workplane.vertices)
> * [`cadquery.Workplane.edges()`](classreference.md#cadquery.Workplane.edges)
> * [`cadquery.Workplane.faces()`](classreference.md#cadquery.Workplane.faces)
> * [`cadquery.Workplane.shells()`](classreference.md#cadquery.Workplane.shells)
> * [`cadquery.Workplane.solids()`](classreference.md#cadquery.Workplane.solids)

Each of these methods accepts either a Selector object or a string. String selectors are simply
shortcuts for using the full object equivalents. If you pass one of the string patterns in,
CadQuery will automatically use the associated selector object.

#### NOTE
String selectors are simply shortcuts to concrete selector classes, which you can use or
extend. For a full description of how each selector class works, see [CadQuery Class Summary](classreference.md#classreference).

If you find that the built-in selectors are not sufficient, you can easily plug in your own.
See [Extending CadQuery](extending.md#extending) to see how.

## Combining Selectors

Selectors can be combined logically, currently defined operators include **and**, **or**, **not** and **exc[ept]** (set difference).  For example:

<div class="cq-vtk"
 style="text-align:left;float:left;border: 1px solid #ddd; width:100%; height:500px">
   <script>
   var parent_element = document.currentScript.parentNode;
   var data = [{"shape": "<?xml version=\\"1.0\\"?>\\n<VTKFile type=\\"PolyData\\" version=\\"0.1\\" byte_order=\\"LittleEndian\\" header_type=\\"UInt32\\" compressor=\\"vtkZLibDataCompressor\\">\\n  <PolyData>\\n    <Piece NumberOfPoints=\\"156\\"                  NumberOfVerts=\\"12\\"                   NumberOfLines=\\"54\\"                   NumberOfStrips=\\"0\\"                    NumberOfPolys=\\"20\\"                  >\\n      <PointData Normals=\\"Normals\\">\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0\\"                    RangeMax=\\"1.0000000672\\"         offset=\\"0\\"                   />\\n      </PointData>\\n      <CellData Normals=\\"Normals\\">\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"SUBSHAPE_IDS\\" format=\\"appended\\" RangeMin=\\"5\\"                    RangeMax=\\"49\\"                   offset=\\"104\\"                 />\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"MESH_TYPES\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"7\\"                    offset=\\"260\\"                 />\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0.99999998289\\"        RangeMax=\\"1\\"                    offset=\\"316\\"                 />\\n      </CellData>\\n      <Points>\\n        <DataArray type=\\"Float32\\" Name=\\"Points\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"1.6248076868\\"         RangeMax=\\"1.7320508076\\"         offset=\\"424\\"                 />\\n      </Points>\\n      <Verts>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"716\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"788\\"                 />\\n      </Verts>\\n      <Lines>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"860\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1136\\"                />\\n      </Lines>\\n      <Strips>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1312\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1328\\"                />\\n      </Strips>\\n      <Polys>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1344\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1508\\"                />\\n      </Polys>\\n    </Piece>\\n  </PolyData>\\n  <AppendedData encoding=\\"base64\\">\\n   \_AQAAAACAAABQBwAAOgAAAA==eJxjYBgFo2AUjIJRMDhBw37S2HAxe0rYX1hM9wMxWIwYNvluJVUPNjYp/iMtLED+Q/IvQTYAicI0pQ==AQAAAACAAACwAgAAYwAAAA==eJyV0DcOhAAQQ1EaRAaRgwhiQUQtgvtfjoLfj8bNa23bxhcHPQwwwQwLrLDDH664o4Uu+hhijCnmWGKNLfY44oQLbnjgH280BSOljeAgOCs9BS/BR1D7h7RXu0fq+wJ+PQmiAQAAAACAAACwAgAAFwAAAA==eJxjYoAAJhrRrKP0kKLZBzkNAP3XAbM=AQAAAACAAAAIBAAAPQAAAA==eJxjYGiwZ4CDUfYoe5QNZe9HYzcgYaLN+8xiuh+IwWLIbBx2MBCWw8YG24nmLqxuagDZj+QeOBsAF0lQBw==AQAAAACAAABQBwAAxwAAAA==eJzNU8ERgzAMy2ZeoEOxmRdod2rhoCcUKRjKo48cxrEdWZZbm/L1fERr03xyPYu9+hPPx7fdY05AjcB/iMcvvxnireA4jBGYu1zC3eVSL5iLuL4+7hHj8Q7q72I3DMiJsSUXAzuoDuNLiOs4FxyzHSbXaebWeR3U/4s5FjTWzfcAf2nurt8rPLu+VP6NenOzlbw5ff4w3xQ5iudTfbn6hf0aYnF7VNgXyYPjcKSHk7pFn9II45c8F7ThYsp6uDjfXY03Z+9WUw==AQAAAACAAABgAAAAJAAAAA==eJwtxbcBACAMAKBYY/n/XwdhIeIrrm7uHp5OL28fXz8JUABDAQAAAACAAABgAAAAJAAAAA==eJwtxbcBACAMACB7bP/f6yAs5PQVVzd3D4enl7ePrx8LwABPAQAAAACAAABgAwAAvAAAAA==eJwtxdciAgAAAEAfYMtKNqGMjGRlZc8ke2Wvssfve3D3csVF/0pc6jKXu8KVrnLA1a5xretc76AbHHKjm9zsFre6ze3ucKfD7nK3exxx1L3uc78HHPOghzzsEcc96oTHPO4JT3rKSU97xrOe87xTXvCil7zsFa96zeve8Ka3vO20d5zxrrPe874PfOgjH/vEpz7zuS+c86WvfO0b3/rO937wo5/87LwLfvGr3/zuD3/6y9/+8a//AEUOG6M=AQAAAACAAACwAQAAcAAAAA==eJwtxcEGwgAAANAkSZIkSZJkZpIkSZKZZCZJkiRJkiT9/7lD711ePvdXcNEll11x1TXX3XDTLbfdcdc99x04dOSBhx557ImnnnnuhZeOnXjltVNn3njrnfc++OiTz7746pvvfvjpl9/++OsfxooLmw==AAAAAACAAAAAAAAAAAAAAACAAAAAAAAAAQAAAACAAADgAQAAaQAAAA==eJxdzEkSgkAQRFGOzYwgo61MMgmXdcGvTfbmRf2MaN+7X4Qh+hjInmGCsXS7U+kPzKXbbf9V+MRCut0ldlhjI72V/YMvdNLfslsfsJfuZP/ihKN0u2dccMNdut0rXnjgT/op+x9eSyAjAQAAAACAAACgAAAAOQAAAA==eJwtxdEGgDAAAMARIyJixBgxRkTEiP3/d/XQ3ctN4Rc9e/Hqzcm7s4sPVzefvnz7cffr4Q+RAAJ3\\n  </AppendedData>\\n</VTKFile>\\n", "color": [1.0, 0.800000011920929, 0.0, 1.0], "position": [0.0, 0.0, 0.0], "orientation": [0.0, -0.0, 0.0]}];
   render(data, parent_element);
   </script>
</div>
<div style="clear:both;">
</div>
```default
result = cq.Workplane("XY").box(2, 2, 2).edges("|Z and >Y").chamfer(0.2)
```

Much more complex expressions are possible as well:

<div class="cq-vtk"
 style="text-align:left;float:left;border: 1px solid #ddd; width:100%; height:500px">
   <script>
   var parent_element = document.currentScript.parentNode;
   var data = [{"shape": "<?xml version=\\"1.0\\"?>\\n<VTKFile type=\\"PolyData\\" version=\\"0.1\\" byte_order=\\"LittleEndian\\" header_type=\\"UInt32\\" compressor=\\"vtkZLibDataCompressor\\">\\n  <PolyData>\\n    <Piece NumberOfPoints=\\"276\\"                  NumberOfVerts=\\"20\\"                   NumberOfLines=\\"96\\"                   NumberOfStrips=\\"0\\"                    NumberOfPolys=\\"36\\"                  >\\n      <PointData Normals=\\"Normals\\">\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0\\"                    RangeMax=\\"1.000000025\\"          offset=\\"0\\"                   />\\n      </PointData>\\n      <CellData Normals=\\"Normals\\">\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"SUBSHAPE_IDS\\" format=\\"appended\\" RangeMin=\\"5\\"                    RangeMax=\\"86\\"                   offset=\\"140\\"                 />\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"MESH_TYPES\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"7\\"                    offset=\\"380\\"                 />\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"1\\"                    RangeMax=\\"1.000000025\\"          offset=\\"440\\"                 />\\n      </CellData>\\n      <Points>\\n        <DataArray type=\\"Float32\\" Name=\\"Points\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"1.3856406667\\"         RangeMax=\\"1.7320508076\\"         offset=\\"596\\"                 />\\n      </Points>\\n      <Verts>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1040\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1128\\"                />\\n      </Verts>\\n      <Lines>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1220\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1696\\"                />\\n      </Lines>\\n      <Strips>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1976\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1992\\"                />\\n      </Strips>\\n      <Polys>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"2008\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"2260\\"                />\\n      </Polys>\\n    </Piece>\\n  </PolyData>\\n  <AppendedData encoding=\\"base64\\">\\n   \_AQAAAACAAADwDAAAVwAAAA==eJxjYBgFo2AUjIJRMApGwSgYBSMDNNjTgv2dxXQ/iPWBxZQoNogG8u1JZO8nlv0dyieWDfTDfiT/EMEmVh2MTWqYkqqHLPeTGs809i+pdhBvDwAmSV9BAQAAAACAAADABAAAogAAAA==eJyt0bkOAQEARVGN2Cd2E2ssYYRgCCPMhFhjiSXE/3+Kwq00r+A1p3836PsshBGMYQKTmMYsFrCENWxhH22c4BzXuMUjXjGAYYyigXFMYQZzmMcilrGKdWyihR3s4QCHOEYHZ+jiAle4wR0e8IQXvOED/T9qCivChrAt7ApHwqnQEy6Fe+FZeBc+hS/hv/urvqqf6qP+V/+q/77/eQM51hurAQAAAACAAADABAAAGgAAAA==eJxjYoAApkFKs47So/QIptlHabw0ADxqAwU=AQAAAACAAAAgBwAAYgAAAA==eJxjYGiwZ4CDUfYoe5Q9yh5l046NItaAQ20DEWx0sxtA7O8spvtBnA8spihskDyQb4+FzQBSh87+DuWjs4Fa9yPZvR/qpgYkPgMqG5dbcfkJr/m4woBEe3Hag6EPAGeskSk=AQAAAACAAADwDAAAOQEAAA==eJzdVcERgzAMY7Ms0DkyRzfzAu1OLVxy59iSnUD59JHDGDCOLCm11lJrlW177tdjtVhUXnr+u6Rde2zvi17v12Nfx/ctLi0WlZeeVzV1bWH/6/V7DXMv5pnUuf0WtPcFfGzfGVYON5IbegPYOpx1zyYvqo6dhaup96jnZeIz801nTN5luWgGEdZsVhnfBsx1XnMSvOO4yZbGkPB8iMH7Q61/5D/b1690wfAJ9ML6hDpiODN9Xezf9uB0yvpM9MvmfqeuGa9YnzO9onXJN4I67J9wf4n/oHN21ZdYfcjzEz4W+SE7R1Z9j/mn43nSt6t/N/dncERzJN853IJeIRcnzwvrXaK5etKvVv3zjB+6OoFvzMySzRbxYnYGjFfQNxJ/GPigtcz0vqrfRT2u6AtiH+gFauQDI0Q23A==AQAAAACAAACgAAAAMAAAAA==eJwtxUkCgBAAAECpiKLt/391MHOZEKbF0as3707OPlxcffpyc/ftx68//x4qMAC/AQAAAACAAACgAAAAMQAAAA==eJwtxbcBgCAAADDEgiBYkP9vdTBZMoVf9OzFqzcn784uPlzdfPry7cfdr4c/MMAA0w==AQAAAACAAAAABgAAUgEAAA==eJwtxddCCAAAAEAfkVFEZKeQssrKHqGiaZOKhqyUlbIyE4msSLKJKCOjZI/khzx093IBvXr0dh/3dT8HOsj9PcDBHuhBDvFgD3Goh3qYh3uER3qURzvMYxzuCI/1OI93pCc4ytGe6Eme7Cme6hjHepqne4ZnepbjPNtzPNfzPN8LvNCLvNhLHO+lXublTnCik7zCK53sFKc6zenO8Cqv9hqv9Tqv9wZv9CZnerOznO0cb/FW5zrP+S7wNhd6u3d4p3d5t4u8x8Uu8V7v834f8EGX+pDLXO7DPuKjPubjrvAJn/Qpn/YZn3Wlz7nK533B1b7oGl/yZdf6iq/6mq/7hut807dc79tu8B03+q7v+b4f+KEf+bGf+Kmb/MzP3ewXfukWt/qVX/uN37rN7/zeH/zR7e7wJ3f6s7/4q7/5u3/4p3/5t/+4y3/d7X/+D0wTVqE=AQAAAACAAAAAAwAAwAAAAA==eJwtxdFGAwAAAMAkSWaSTJJMJpMkmZlkMpNkkkySmUkySZJkkkySzCTJZJJMkkwyySTp03rY3ct1d3X0uNd97nfAQQ940EMOedgjHvWYwx53xBOOetJTnvaMZx1z3AnPed5JLzjltBe95GVnvOJVrznrdW940znnXfCWt73jone9530f+NBHPnbJJz71mcs+94UvfeWKq772jW9955rvXfeDH/3khp/94le/uel3f7jlT3+57W//+Nd//gcnKyRhAAAAAACAAAAAAAAAAAAAAACAAAAAAAAAAQAAAACAAABgAwAAqQAAAA==eJxdzEUCwzAQQ9GmzHj/WzVQZmZmWPTPosrmRZLtIPT7quhhgHXZXcm2+1iT+75kT3p7z+7Zew3ZXentfAdb2JTechsH2MOu9Jb7OMEhjqQfy77AKc6kn8u+wjUupd/IfsAt7qTfy37CI56lt3zBB97wKr3lO77wjU/pP7I7jv38CDv/veUIRjGOMekTsqcwiWnpLWewgFnMSZ+XvYJFLElvuYxfStxHhQ==AQAAAACAAAAgAQAAVgAAAA==eJwtxcEGgwAAANARI2LEiIgYETHGiIgYI0aMiBEjov8/d+i9ywtOh7NDR7449tWJU2fOfXPh0pXvfvjp2o1bd3757d4fD/569OSfZ/+9ePXmHRgtB88=\\n  </AppendedData>\\n</VTKFile>\\n", "color": [1.0, 0.800000011920929, 0.0, 1.0], "position": [0.0, 0.0, 0.0], "orientation": [0.0, -0.0, 0.0]}];
   render(data, parent_element);
   </script>
</div>
<div style="clear:both;">
</div>
```default
result = (
    cq.Workplane("XY")
    .box(2, 2, 2)
    .faces(">Z")
    .shell(-0.2)
    .faces(">Z")
    .edges("not(<X or >X or <Y or >Y)")
    .chamfer(0.1)
)
```

<a id="filteringfaces"></a>

## Filtering Faces

All types of string selectors work on faces.  In most cases, the selector refers to the direction
of the **normal vector** of the face.

#### WARNING
If a face is not planar, selectors are evaluated at the center of mass of the face. This can lead
to results that are quite unexpected.

The axis used in the listing below are for illustration: any axis would work similarly in each case.

| Selector   | Selects                                   | Selector Class                                                                             |
|------------|-------------------------------------------|--------------------------------------------------------------------------------------------|
| +Z         | Faces with normal in +z direction         | [`cadquery.DirectionSelector`](classreference.md#cadquery.DirectionSelector)               |
| |Z         | Faces with normal parallel to z dir       | [`cadquery.ParallelDirSelector`](classreference.md#cadquery.ParallelDirSelector)           |
| -X         | Faces with normal in neg x direction      | [`cadquery.DirectionSelector`](classreference.md#cadquery.DirectionSelector)               |
| #Z         | Faces with normal orthogonal to z dir     | [`cadquery.PerpendicularDirSelector`](classreference.md#cadquery.PerpendicularDirSelector) |
| %Plane     | Faces of type plane                       | [`cadquery.TypeSelector`](classreference.md#cadquery.TypeSelector)                         |
| >Y         | Face farthest in the positive y dir       | [`cadquery.DirectionMinMaxSelector`](classreference.md#cadquery.DirectionMinMaxSelector)   |
| <Y         | Face farthest in the negative y dir       | [`cadquery.DirectionMinMaxSelector`](classreference.md#cadquery.DirectionMinMaxSelector)   |
| >Y[-2]     | 2nd farthest Face **normal** to the y dir | `cadquery.DirectionNthSelector`                                                            |
| <Y[0]      | 1st closest Face **normal** to the y dir  | `cadquery.DirectionNthSelector`                                                            |
| >>Y[-2]    | 2nd farthest Face in the y dir            | `cadquery.CenterNthSelector`                                                               |
| <<Y[0]     | 1st closest Face in the y dir             | `cadquery.CenterNthSelector`                                                               |

<a id="filteringedges"></a>

## Filtering Edges

The selector usually refers to the **direction** of the edge.

#### WARNING
Non-linear edges are not selected for any string selectors except type (%) and center (>>).
Non-linear edges are never returned when these filters are applied.

The axis used in the listing below are for illustration: any axis would work similarly in each case.

| Selector   | Selects                                              | Selector Class                                                                             |
|------------|------------------------------------------------------|--------------------------------------------------------------------------------------------|
| +Z         | Edges aligned in the Z direction                     | [`cadquery.DirectionSelector`](classreference.md#cadquery.DirectionSelector)               |
| |Z         | Edges parallel to z direction                        | [`cadquery.ParallelDirSelector`](classreference.md#cadquery.ParallelDirSelector)           |
| -X         | Edges aligned in neg x direction                     | [`cadquery.DirectionSelector`](classreference.md#cadquery.DirectionSelector)               |
| #Z         | Edges perpendicular to z direction                   | [`cadquery.PerpendicularDirSelector`](classreference.md#cadquery.PerpendicularDirSelector) |
| %Line      | Edges of type line                                   | [`cadquery.TypeSelector`](classreference.md#cadquery.TypeSelector)                         |
| >Y         | Edges farthest in the positive y dir                 | [`cadquery.DirectionMinMaxSelector`](classreference.md#cadquery.DirectionMinMaxSelector)   |
| <Y         | Edges farthest in the negative y dir                 | [`cadquery.DirectionMinMaxSelector`](classreference.md#cadquery.DirectionMinMaxSelector)   |
| >Y[1]      | 2nd closest **parallel** edge in the positive y dir  | `cadquery.DirectionNthSelector`                                                            |
| <Y[-2]     | 2nd farthest **parallel** edge in the negative y dir | `cadquery.DirectionNthSelector`                                                            |
| >>Y[-2]    | 2nd farthest edge in the y dir                       | `cadquery.CenterNthSelector`                                                               |
| <<Y[0]     | 1st closest edge in the y dir                        | `cadquery.CenterNthSelector`                                                               |

<a id="filteringvertices"></a>

## Filtering Vertices

Only a few of the filter types apply to vertices. The location of the vertex is the subject of the filter.

| Selector   | Selects                                 | Selector Class                                                                           |
|------------|-----------------------------------------|------------------------------------------------------------------------------------------|
| >Y         | Vertices farthest in the positive y dir | [`cadquery.DirectionMinMaxSelector`](classreference.md#cadquery.DirectionMinMaxSelector) |
| <Y         | Vertices farthest in the negative y dir | [`cadquery.DirectionMinMaxSelector`](classreference.md#cadquery.DirectionMinMaxSelector) |
| >>Y[-2]    | 2nd farthest vertex in the y dir        | `cadquery.CenterNthSelector`                                                             |
| <<Y[0]     | 1st closest vertex in the y dir         | `cadquery.CenterNthSelector`                                                             |

## User-defined Directions

It is possible to use user defined vectors as a basis for the selectors. For example:

<div class="cq-vtk"
 style="text-align:left;float:left;border: 1px solid #ddd; width:100%; height:500px">
   <script>
   var parent_element = document.currentScript.parentNode;
   var data = [{"shape": "<?xml version=\\"1.0\\"?>\\n<VTKFile type=\\"PolyData\\" version=\\"0.1\\" byte_order=\\"LittleEndian\\" header_type=\\"UInt32\\" compressor=\\"vtkZLibDataCompressor\\">\\n  <PolyData>\\n    <Piece NumberOfPoints=\\"130\\"                  NumberOfVerts=\\"10\\"                   NumberOfLines=\\"45\\"                   NumberOfStrips=\\"0\\"                    NumberOfPolys=\\"16\\"                  >\\n      <PointData Normals=\\"Normals\\">\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0\\"                    RangeMax=\\"1.0000000672\\"         offset=\\"0\\"                   />\\n      </PointData>\\n      <CellData Normals=\\"Normals\\">\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"SUBSHAPE_IDS\\" format=\\"appended\\" RangeMin=\\"5\\"                    RangeMax=\\"42\\"                   offset=\\"92\\"                  />\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"MESH_TYPES\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"7\\"                    offset=\\"236\\"                 />\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0.99999998289\\"        RangeMax=\\"1\\"                    offset=\\"292\\"                 />\\n      </CellData>\\n      <Points>\\n        <DataArray type=\\"Float32\\" Name=\\"Points\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"8.1240384046\\"         RangeMax=\\"8.6602540378\\"         offset=\\"392\\"                 />\\n      </Points>\\n      <Verts>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"624\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"696\\"                 />\\n      </Verts>\\n      <Lines>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"768\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1008\\"                />\\n      </Lines>\\n      <Strips>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1164\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1180\\"                />\\n      </Strips>\\n      <Polys>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1196\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1340\\"                />\\n      </Polys>\\n    </Piece>\\n  </PolyData>\\n  <AppendedData encoding=\\"base64\\">\\n   \_AQAAAACAAAAYBgAAMQAAAA==eJxjYBgFo2AUjIKhAhr2k8aGi9mTyv7CYrofiMFixLDJdx+pemBsUvxEmv8BXhwnRw==AQAAAACAAAA4AgAAWAAAAA==eJyNz6cOgAAUQ1EMYUPYhBFGGIH//0AEV2H6ao5s6ztfAowwwQIrbHDABQ/0MMQYU8yxxBpb7HHEGVfc8cQbXWFmtBNOws3oJXyE1n9qv3Xfv/8F4fIG9A==AQAAAACAAAA4AgAAFgAAAA==eJxjYoAAJirRrKM0XWj2AaYBW88BZg==AQAAAACAAABUAwAANwAAAA==eJxjYGiwZ4CDUfYoe1Cw96OxG6AYWW0DNvZnFtP9QAw2C5mNw1wGwnIwNoZbG3C4vwEA+2ZAqA==AQAAAACAAAAYBgAAnAAAAA==eJy9UtsNwCAIZDRHYxRHYbSmiU1Q70D64QcJrSL3Eukmok2kv2WjRq/+3yj9zv1Mm0ttObPlnpFdYO+GDcxO+MCsot0L/o1XwtHv8nxhTzjTHmmY6cmwXtA5fP+y/mkGgC8hzkO/qCc/9GS80Hw1J+w+1Yd4kPoV4Sp4vM0vb7PcpvkkO2E2gBelzCAeEeYD71IfK75s3w88DrBQAQAAAACAAABQAAAAIgAAAA==eJwtxbcBACAIADAsiP7/sAPJkog2PL28nT4uXz9/BXgALg==AQAAAACAAABQAAAAIgAAAA==eJwtxbcBACAIADA76v8HM5As6a0MTy9vH4evn78TBzAAOA==AQAAAACAAADQAgAAoQAAAA==eJwtxcdCAQAAANDODamMSBpSWkJpGS1tIaGF1v//g0PvXd742L8JT3rKAU876BnPes4hhx1x1POOOe4FJ7zopJe87BWvOuU1p73uDWe86S1ve8e7znrPOedd8L4PXPShj3zsE5+65LIrrvrM577wpa9c87VvfOs73/vBj677yQ033fKz235xx133/Oo3v/vDn+574KG//O0f//rPI9gFEyo=AQAAAACAAABoAQAAYgAAAA==eJwtxdEGwgAAAMDJTCZJMkmSZJJkMplMksxkMplk//8hPXT3coPgL3TkoWOPPPbEU8+ceO6Fl1557Y23Tr3z3gcfnfnk3GcXvrj01Tff/XDl2k83frn1250//rr3D/cFCBc=AAAAAACAAAAAAAAAAAAAAACAAAAAAAAAAQAAAACAAACAAQAAWQAAAA==eJxdykcWg0AQA1EOO+RgcjbYN2dBaaPZ/DelDtH7UkwwYGx7gTlmWFnXXWm7+gcbrLG1rrsRO+ytD7YvOOGMm+3qq3XdnXjgjl/rurvxwp91/f/4AMA5FXU=AQAAAACAAACAAAAAMgAAAA==eJwtxdEGwCAAAMAYESMiImKMEbH//7oeunu5KxzRybezi6ubu4cfv/48vfx7A00AAZk=\\n  </AppendedData>\\n</VTKFile>\\n", "color": [1.0, 0.800000011920929, 0.0, 1.0], "position": [0.0, 0.0, 0.0], "orientation": [0.0, -0.0, 0.0]}];
   render(data, parent_element);
   </script>
</div>
<div style="clear:both;">
</div>
```default
result = cq.Workplane("XY").box(10, 10, 10)

# chamfer only one edge
result = result.edges(">(-1, 1, 0)").chamfer(1)
```

## Topological Selectors

Is is also possible to use topological relations to select objects. Currently
the following methods are supported:

> * [`cadquery.Workplane.ancestors()`](classreference.md#cadquery.Workplane.ancestors)
> * [`cadquery.Workplane.siblings()`](classreference.md#cadquery.Workplane.siblings)

Ancestors allows to select all objects containing currently selected object.

<div class="cq-vtk"
 style="text-align:left;float:left;border: 1px solid #ddd; width:100%; height:500px">
   <script>
   var parent_element = document.currentScript.parentNode;
   var data = [{"shape": "<?xml version=\\"1.0\\"?>\\n<VTKFile type=\\"PolyData\\" version=\\"0.1\\" byte_order=\\"LittleEndian\\" header_type=\\"UInt32\\" compressor=\\"vtkZLibDataCompressor\\">\\n  <PolyData>\\n    <Piece NumberOfPoints=\\"44\\"                   NumberOfVerts=\\"6\\"                    NumberOfLines=\\"15\\"                   NumberOfStrips=\\"0\\"                    NumberOfPolys=\\"4\\"                   >\\n      <PointData Normals=\\"Normals\\">\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0\\"                    RangeMax=\\"1\\"                    offset=\\"0\\"                   />\\n      </PointData>\\n      <CellData Normals=\\"Normals\\">\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"SUBSHAPE_IDS\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"18\\"                   offset=\\"56\\"                  />\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"MESH_TYPES\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"7\\"                    offset=\\"148\\"                 />\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"1\\"                    RangeMax=\\"1\\"                    offset=\\"212\\"                 />\\n      </CellData>\\n      <Points>\\n        <DataArray type=\\"Float32\\" Name=\\"Points\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"8.6602540378\\"         RangeMax=\\"8.6602540378\\"         offset=\\"272\\"                 />\\n      </Points>\\n      <Verts>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"372\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"428\\"                 />\\n      </Verts>\\n      <Lines>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"484\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"592\\"                 />\\n      </Lines>\\n      <Strips>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"680\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"696\\"                 />\\n      </Strips>\\n      <Polys>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"712\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"784\\"                 />\\n      </Polys>\\n    </Piece>\\n  </PolyData>\\n  <AppendedData encoding=\\"base64\\">\\n   \_AQAAAACAAAAQAgAAFwAAAA==eJxjYBgFQw807CeNDebbE8MGAKC3B/k=AQAAAACAAADIAAAAMQAAAA==eJyFyrkNACAQxECEeI5HwNF/sQQ4XyeTOIdfQcOOGx0TVmw4cOHBi1E4hep/XbAA4Q==AQAAAACAAADIAAAAHQAAAA==eJxjYoAAJiJpFjSaFYc4IZpYfTB17ARoACLoAGg=AQAAAACAAAAsAQAAGQAAAA==eJxjYGiwZ4CDkcYG8/djYTdg0wcAT7gUKA==AQAAAACAAAAQAgAAOAAAAA==eJxjYFjgwMCw4AAW7IBGo4uhY2x68ek/gGYWujgh89D14XLTUHcnPnuxuQOXemz2YNgLAC8llIE=AQAAAACAAAAwAAAAGAAAAA==eJxjYIAARijNBKWZoTQLlGaF0gABSAAQAQAAAACAAAAwAAAAGAAAAA==eJxjZIAAJijNDKVZoDQrlGaD0gAB8AAWAQAAAACAAADwAAAAPQAAAA==eJwtxbUBgwAAADAm3Iu7/P9jB5IlYfCJHDtx6sy5C5euXLtx65879x48evLsxas37z58+vLtx6//5JgCaA==AQAAAACAAAB4AAAALgAAAA==eJwtxUEGACEAAMAkycpaSVbS/5/ZoZnLxHAlZxc/rn79ubl7+Pf08vYBKvgA8Q==AAAAAACAAAAAAAAAAAAAAACAAAAAAAAAAQAAAACAAABgAAAAIwAAAA==eJxTZ4AAFSitCqXVobQamrw2lNaE0hpo4jC+FpQGAF6YAds=AQAAAACAAAAgAAAAEwAAAA==eJxjZoAANijNCaV5oDQAAgAAHw==\\n  </AppendedData>\\n</VTKFile>\\n", "color": [1.0, 0.800000011920929, 0.0, 1.0], "position": [0.0, 0.0, 0.0], "orientation": [0.0, -0.0, 0.0]}];
   render(data, parent_element);
   </script>
</div>
<div style="clear:both;">
</div>
```default
result = cq.Workplane("XY").box(10, 10, 10).faces(">Z").edges("<Y")

result = result.ancestors("Face")
```

Siblings allows to select all objects of the same type as selection that are connected
via the specfied kind of elements.

<div class="cq-vtk"
 style="text-align:left;float:left;border: 1px solid #ddd; width:100%; height:500px">
   <script>
   var parent_element = document.currentScript.parentNode;
   var data = [{"shape": "<?xml version=\\"1.0\\"?>\\n<VTKFile type=\\"PolyData\\" version=\\"0.1\\" byte_order=\\"LittleEndian\\" header_type=\\"UInt32\\" compressor=\\"vtkZLibDataCompressor\\">\\n  <PolyData>\\n    <Piece NumberOfPoints=\\"80\\"                   NumberOfVerts=\\"8\\"                    NumberOfLines=\\"28\\"                   NumberOfStrips=\\"0\\"                    NumberOfPolys=\\"8\\"                   >\\n      <PointData Normals=\\"Normals\\">\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0\\"                    RangeMax=\\"1\\"                    offset=\\"0\\"                   />\\n      </PointData>\\n      <CellData Normals=\\"Normals\\">\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"SUBSHAPE_IDS\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"29\\"                   offset=\\"60\\"                  />\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"MESH_TYPES\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"7\\"                    offset=\\"176\\"                 />\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"1\\"                    RangeMax=\\"1\\"                    offset=\\"240\\"                 />\\n      </CellData>\\n      <Points>\\n        <DataArray type=\\"Float32\\" Name=\\"Points\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"8.6602540378\\"         RangeMax=\\"8.6602540378\\"         offset=\\"316\\"                 />\\n      </Points>\\n      <Verts>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"468\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"532\\"                 />\\n      </Verts>\\n      <Lines>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"596\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"756\\"                 />\\n      </Lines>\\n      <Strips>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"868\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"884\\"                 />\\n      </Strips>\\n      <Polys>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"900\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"996\\"                 />\\n      </Polys>\\n    </Piece>\\n  </PolyData>\\n  <AppendedData encoding=\\"base64\\">\\n   \_AQAAAACAAADAAwAAGQAAAA==eJxjYBgFo2AkgwZ7Etn7SWPT1g4AtfsP8Q==AQAAAACAAABgAQAAQwAAAA==eJyFzckOQFAUREERMzE8QxD+/zct1P72pnZ9yuxfxYYdJ85M3FiwZsueIxeu3Hny4sOXeeAQeATegVEv+vsArf8Cpw==AQAAAACAAABgAQAAHgAAAA==eJxjYoAAJjJpVijNQiafEE0t88k1h51CGgB0gADFAQAAAACAAAAQAgAAJgAAAA==eJxjYGiwZ4CDUfYQZTcA0X4k8f0QMTCGqWtA08OARQ8DAP86JNU=AQAAAACAAADAAwAAXwAAAA==eJzdkbENwCAMBH80RmUUj5YiAkWvP9ykorIN0p85pDmkWXrr6r/zCHcVZs/w6mfeJxbx0z60GzG7rC7jL0e3+qE9T946bmI6nzyTh9M7aCYXHZ/+ifLJ+857AKk5DhA=AQAAAACAAABAAAAAHgAAAA==eJxjYIAARijNBKWZoTQLlGaF0mxQmh1KAwAC4AAdAQAAAACAAABAAAAAHgAAAA==eJxjZIAAJijNDKVZoDQrlGaD0uxQmgNKAwAEAAAlAQAAAACAAADAAQAAZQAAAA==eJwtxbUBwgAAADBG3J0Wp7i0uP//FQPJknTqL+Osc8674KJLLrviqmuuu+GmW2674657Dhy674GHHnnsiaeeOfLcCy+98tobb73z3gfHTnz0yWdffPXNdz/89Mtvf/z1DyNrB8U=AQAAAACAAADgAAAAQgAAAA==eJwtxUEKQEAAAEBJkiRJkrRJkiRJkv+/zMHMZeLolzh15tyFS1eu3bh1596Dg0dPnr149ebdh09fvv349Qf+oAMtAAAAAACAAAAAAAAAAAAAAACAAAAAAAAAAQAAAACAAADAAAAANgAAAA==eJxdybcVACAAQkFHM+ew/zYWfhto7gHOvFj06KQHTJgxyl7kH9iwyv57x4MTl+xb/guIfga1AQAAAACAAABAAAAAHgAAAA==eJxjZoAANijNCaV5oDQ/lBaC0qJQWgJKAwALgABt\\n  </AppendedData>\\n</VTKFile>\\n", "color": [1.0, 0.800000011920929, 0.0, 1.0], "position": [0.0, 0.0, 0.0], "orientation": [0.0, -0.0, 0.0]}];
   render(data, parent_element);
   </script>
</div>
<div style="clear:both;">
</div>
```default
result = cq.Workplane("XY").box(10, 10, 10).faces(">Z")

result = result.siblings("Edge")
```

## Using selectors with Shape and Sketch objects

It is possible to use selectors with [`cadquery.Shape`](classreference.md#cadquery.Shape) and [`cadquery.Sketch`](classreference.md#cadquery.Sketch)
objects. This includes chaining and combining.

<div class="cq-vtk"
 style="text-align:left;float:left;border: 1px solid #ddd; width:100%; height:500px">
   <script>
   var parent_element = document.currentScript.parentNode;
   var data = [{"shape": "<?xml version=\\"1.0\\"?>\\n<VTKFile type=\\"PolyData\\" version=\\"0.1\\" byte_order=\\"LittleEndian\\" header_type=\\"UInt32\\" compressor=\\"vtkZLibDataCompressor\\">\\n  <PolyData>\\n    <Piece NumberOfPoints=\\"24\\"                   NumberOfVerts=\\"8\\"                    NumberOfLines=\\"8\\"                    NumberOfStrips=\\"0\\"                    NumberOfPolys=\\"0\\"                   >\\n      <PointData Normals=\\"Normals\\">\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"1\\"                    RangeMax=\\"1\\"                    offset=\\"0\\"                   />\\n      </PointData>\\n      <CellData>\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"SUBSHAPE_IDS\\" format=\\"appended\\" RangeMin=\\"3\\"                    RangeMax=\\"19\\"                   offset=\\"48\\"                  />\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"MESH_TYPES\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"3\\"                    offset=\\"132\\"                 />\\n      </CellData>\\n      <Points>\\n        <DataArray type=\\"Float32\\" Name=\\"Points\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0\\"                    RangeMax=\\"3.7416573868\\"         offset=\\"180\\"                 />\\n      </Points>\\n      <Verts>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"288\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"352\\"                 />\\n      </Verts>\\n      <Lines>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"416\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"500\\"                 />\\n      </Lines>\\n      <Strips>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"564\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"580\\"                 />\\n      </Strips>\\n      <Polys>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"596\\"                 />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"612\\"                 />\\n      </Polys>\\n    </Piece>\\n  </PolyData>\\n  <AppendedData encoding=\\"base64\\">\\n   \_AQAAAACAAAAgAQAAEgAAAA==eJxjYICBBnuGUTYGGwDGnxHpAQAAAACAAACAAAAALQAAAA==eJwtxTkOgCAAADASQY6ACv7/rwy0S2M4krOrhx9/Xr58u7i5+/X07w0pAACxAQAAAACAAACAAAAAEQAAAA==eJxjYoAAJjJpZgppAAogACk=AQAAAACAAAAgAQAAPwAAAA==eJxjYAADByByYIADELvBHiEOZjMgqUFSCwMw9XA2GkDWi87GZReyOIbbGFDFEQow2bjchiyO4RcwAACoehH1AQAAAACAAABAAAAAHgAAAA==eJxjYIAARijNBKWZoTQLlGaF0mxQmh1KAwAC4AAdAQAAAACAAABAAAAAHgAAAA==eJxjZIAAJijNDKVZoDQrlGaD0uxQmgNKAwAEAAAlAQAAAACAAACAAAAALAAAAA==eJwtxbcBgCAAADBGQaoK/v8pA8mSKxzRybezi6ubu4cfv/48vfx7AzfAAPk=AQAAAACAAABAAAAAHgAAAA==eJxjYoAAFijNBqU5oDQXlOaB0nxQWgBKAwAHwABJAAAAAACAAAAAAAAAAAAAAACAAAAAAAAAAAAAAACAAAAAAAAAAAAAAACAAAAAAAAA\\n  </AppendedData>\\n</VTKFile>\\n", "color": [1.0, 0.800000011920929, 0.0, 1.0], "position": [0.0, 0.0, 0.0], "orientation": [0.0, -0.0, 0.0]}];
   render(data, parent_element);
   </script>
</div>
<div style="clear:both;">
</div>
```default
box = cq.Solid.makeBox(1,2,3)

# select top and bottom wires
result = box.faces(">Z or <Z").wires()
```

## Additional special methods

[`cadquery.Workplane`](classreference.md#cadquery.Workplane) and [`cadquery.Sketch`](classreference.md#cadquery.Sketch) provide the following special methods that can be used
for quick prototyping of selectors when implementing a complete selector via subclassing of
[`cadquery.Selector`](classreference.md#cadquery.Selector) is not desirable.

> * [`cadquery.Workplane.filter()`](classreference.md#cadquery.Workplane.filter)
> * [`cadquery.Workplane.sort()`](classreference.md#cadquery.Workplane.sort)
> * `cadquery.Workplane.__getitem__()`
> * [`cadquery.Sketch.filter()`](classreference.md#cadquery.Sketch.filter)
> * [`cadquery.Sketch.sort()`](classreference.md#cadquery.Sketch.sort)
> * `cadquery.Sketch.__getitem__()`

For example, one could use those methods for selecting objects within a certain range of volumes.

<div class="cq-vtk"
 style="text-align:left;float:left;border: 1px solid #ddd; width:100%; height:500px">
   <script>
   var parent_element = document.currentScript.parentNode;
   var data = [{"shape": "<?xml version=\\"1.0\\"?>\\n<VTKFile type=\\"PolyData\\" version=\\"0.1\\" byte_order=\\"LittleEndian\\" header_type=\\"UInt32\\" compressor=\\"vtkZLibDataCompressor\\">\\n  <PolyData>\\n    <Piece NumberOfPoints=\\"312\\"                  NumberOfVerts=\\"24\\"                   NumberOfLines=\\"108\\"                  NumberOfStrips=\\"0\\"                    NumberOfPolys=\\"36\\"                  >\\n      <PointData Normals=\\"Normals\\">\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0\\"                    RangeMax=\\"1\\"                    offset=\\"0\\"                   />\\n      </PointData>\\n      <CellData Normals=\\"Normals\\">\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"SUBSHAPE_IDS\\" format=\\"appended\\" RangeMin=\\"4\\"                    RangeMax=\\"102\\"                  offset=\\"92\\"                  />\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"MESH_TYPES\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"7\\"                    offset=\\"364\\"                 />\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"1\\"                    RangeMax=\\"1\\"                    offset=\\"428\\"                 />\\n      </CellData>\\n      <Points>\\n        <DataArray type=\\"Float32\\" Name=\\"Points\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0.70710678119\\"        RangeMax=\\"5.4313902456\\"         offset=\\"524\\"                 />\\n      </Points>\\n      <Verts>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1052\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1148\\"                />\\n      </Verts>\\n      <Lines>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1244\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1768\\"                />\\n      </Lines>\\n      <Strips>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"2076\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"2092\\"                />\\n      </Strips>\\n      <Polys>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"2108\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"2364\\"                />\\n      </Polys>\\n    </Piece>\\n  </PolyData>\\n  <AppendedData encoding=\\"base64\\">\\n   \_AQAAAACAAACgDgAAMwAAAA==eJxjYBgFo2AUjIJRMApGwSgYBaNgFBAPGvaTyLYnjT3U7RjKbqeHHUPZ7bS3AwCojke5AQAAAACAAABABQAAugAAAA==eJyF0jmPgQEAhGGFuIl7BeHLFuIm1h0EUQjrWHEtsr4g/v9PUOxbaWaap58Zu+U/DnShBwMYxDBGMYd5LGIZv7COTWzjHL9xiWvc4R6PeEIbOtGNXvRjCCP4gXFMYArTmMUClrCCNWxgCzvYwz4OcYQzXOAKf3CLB/zFM/7hFW94R6vQJ4wJk0JD+CnMCKvCrnAgHAsnwqlwI7wITeFD+BSqv6g/GG+qfdV+ah/Vv+rXfFP19QLnXSPvAQAAAACAAABABQAAHAAAAA==eJxjYoAApiFKs47So/QoTTOafZTGSwMAeUkDSQ==AQAAAACAAADgBwAANQAAAA==eJxjYGiwZ4CDUfYoe5Q9yh5lj7JxsvejsRsgGKv6Bhx6kNU1oOnBZw8Wd426B597AMFLjdk=AQAAAACAAACgDgAAeQEAAA==eJzdVsFtxDAM8yjdRBqlo3SEbOSOVtzBSVhSdBwU/eSAQw2CNRWKUq611tv7+xXtOL8/r78BeAw8gB/AD+DHyf/eOQnnHQ/AB/8jT/5x3vEAfPA/ByfzPB94AD74G/A34G/A34AvnpBX6I94xTh5i346b9FP9lZw6oXUjxysH7W4tupZQFd6yr1O32vBORutyABnI302BOcstd+6yMH6UUtqK54FdSWTlFXMJ2dVcMr26yMZpmxjnjnbgtMsYM2shfWjltRWPAvqPna+nO5s7pwPVI87i1cFvuzbTPeODxd9LP2v+mJ8e+r+cbrTveR84HrcOf0eu+vbVPeGD5d9TONzVX/h21P3s9Od7m3nA9XjzuxVha/6NtW94cNVH0v/i74435b29jiX75F+8d7pyhctvKfrPWUN1f38v93c080O73r/yl6SWR78cpabmev2P7/flt8LeA9rpd9LK3MnWaWcz/bGylz85ffb8t6jOS1nUObuB+Ogrkg=AQAAAACAAADAAAAANgAAAA==eJwtxUkCQCAAAMCSfQuF///UwcxlQvhFN05u3bn34NGTZy9evXl39uHTl4urbz9+/QFIoAEVAQAAAACAAADAAAAANgAAAA==eJwtxbcBgCAAADARe0MFy/+XOpgsCdWvdnTj1p17Dx49efbi1ZuTdx8+nV18+fbj1x9SAAEtAQAAAACAAADABgAAdwEAAA==eJwtxddCCAAAAECfYY/sTVkNe++EzJaMQtmyt2Rmlxmy98qe2XtERIiy1y94cPdypUv9V8ZlXc7lXcEVXcmVXcUBrupqru4arularu06rut6ru8GbuhGbuxAB7mJm7qZm7uFgx3iUIe5pVu5tdu4rdu5vTu4ozu5s7u4q7u5u3u4p3u5t8PdxxHu637u70gP8EAP8mAP8VBHOdoxjnWchznewz3CIz3KCU70aI/xWCc52eM83hM80ZM82VM81Sme5ume4Zme5dme47me5/le4IVe5MVO9RKneamXeblXeKVXOd2rvcZrvc7rvcEbneFMb/Jmb/FWb/N2Z3mHd3qXs73be7zX+7zfB3zQh3zYR3zUx3zcJ3zSp3zaOT7jsz7n877gi77ky77iq77m6871Dd/0Ld/2Hd/1Pd/3Az/0Iz/2Ez/1Mz93nl/4pfP9yq9d4Dd+60K/83t/cJE/+pOLXeLP/uKv/ubv/uGf/uXf/uO//gfGn271AQAAAACAAABgAwAA1QAAAA==eJwtxdFGAwAAAMAkSZJMkmQySZIkmSQzSTJJMpkkySRJJkmSJEkmk0mSJEkySZIkSWaSJEnS5/TQ3csVF/0rcanLXO4KV7rKAVe7xrWuc72DbnDIjW5ys1vc6ja3u8OdDrvL3e5xxFH3us/9HnDMgx7ysEcc96gTHvO4JzzpKSc97RnPes7zTnnBi17ysle86jWve8Ob3vK2095xxrvOes/7PvChj3zsE5/6zOe+cM6XvvK1b3zrO9/7wY9+8rPzLvjFr37zuz/86S9/+8e//gO3LC39AAAAAACAAAAAAAAAAAAAAACAAAAAAAAAAQAAAACAAABgAwAArAAAAA==eJxdyUViQlEQRFE+HtyCB/cETYD97wh3G+T2gHqT8+r22vX/NrjCNW7lvscdHqTbPuIVT3iWfpH7E+94k277gR6HDzrOe3fLPYA+9Eq37ccPDGFQeljuUYxgTLrtOKYxgUnpKbnn8BMz0m1nsYR5LEgvyr2KX1iWbruCdWxgTXpT7m1sYUe67S5+Yw/70gdyH+MQf6TbHuEvTnAqfSb3Jc7xT7rtBb4AVbYgjw==AQAAAACAAAAgAQAAVgAAAA==eJwtxcEGgwAAANARI2LEiIgYETHGiIgYI0aMiBEjov8/d+i9ywtOh7NDR7449tWJU2fOfXPh0pXvfvjp2o1bd3757d4fD/569OSfZ/+9ePXmHRgtB88=\\n  </AppendedData>\\n</VTKFile>\\n", "color": [1.0, 0.800000011920929, 0.0, 1.0], "position": [0.0, 0.0, 0.0], "orientation": [0.0, -0.0, 0.0]}];
   render(data, parent_element);
   </script>
</div>
<div style="clear:both;">
</div>
```default
from cadquery.occ_impl.shapes import box

result = (
    cq.Workplane()
    .add([box(1,1,i+1).moved(x=2*i) for i in range(5)])
)

# select boxes with volume <= 3
result = result.filter(lambda s: s.Volume() <= 3)
```

The same can be achieved using sorting.

<div class="cq-vtk"
 style="text-align:left;float:left;border: 1px solid #ddd; width:100%; height:500px">
   <script>
   var parent_element = document.currentScript.parentNode;
   var data = [{"shape": "<?xml version=\\"1.0\\"?>\\n<VTKFile type=\\"PolyData\\" version=\\"0.1\\" byte_order=\\"LittleEndian\\" header_type=\\"UInt32\\" compressor=\\"vtkZLibDataCompressor\\">\\n  <PolyData>\\n    <Piece NumberOfPoints=\\"312\\"                  NumberOfVerts=\\"24\\"                   NumberOfLines=\\"108\\"                  NumberOfStrips=\\"0\\"                    NumberOfPolys=\\"36\\"                  >\\n      <PointData Normals=\\"Normals\\">\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0\\"                    RangeMax=\\"1\\"                    offset=\\"0\\"                   />\\n      </PointData>\\n      <CellData Normals=\\"Normals\\">\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"SUBSHAPE_IDS\\" format=\\"appended\\" RangeMin=\\"4\\"                    RangeMax=\\"102\\"                  offset=\\"92\\"                  />\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"MESH_TYPES\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"7\\"                    offset=\\"364\\"                 />\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"1\\"                    RangeMax=\\"1\\"                    offset=\\"428\\"                 />\\n      </CellData>\\n      <Points>\\n        <DataArray type=\\"Float32\\" Name=\\"Points\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0.70710678119\\"        RangeMax=\\"5.4313902456\\"         offset=\\"524\\"                 />\\n      </Points>\\n      <Verts>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1052\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1148\\"                />\\n      </Verts>\\n      <Lines>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1244\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1768\\"                />\\n      </Lines>\\n      <Strips>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"2076\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"2092\\"                />\\n      </Strips>\\n      <Polys>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"2108\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"2364\\"                />\\n      </Polys>\\n    </Piece>\\n  </PolyData>\\n  <AppendedData encoding=\\"base64\\">\\n   \_AQAAAACAAACgDgAAMwAAAA==eJxjYBgFo2AUjIJRMApGwSgYBaNgFBAPGvaTyLYnjT3U7RjKbqeHHUPZ7bS3AwCojke5AQAAAACAAABABQAAugAAAA==eJyF0jmPgQEAhGGFuIl7BeHLFuIm1h0EUQjrWHEtsr4g/v9PUOxbaWaap58Zu+U/DnShBwMYxDBGMYd5LGIZv7COTWzjHL9xiWvc4R6PeEIbOtGNXvRjCCP4gXFMYArTmMUClrCCNWxgCzvYwz4OcYQzXOAKf3CLB/zFM/7hFW94R6vQJ4wJk0JD+CnMCKvCrnAgHAsnwqlwI7wITeFD+BSqv6g/GG+qfdV+ah/Vv+rXfFP19QLnXSPvAQAAAACAAABABQAAHAAAAA==eJxjYoAApiFKs47So/QoTTOafZTGSwMAeUkDSQ==AQAAAACAAADgBwAANQAAAA==eJxjYGiwZ4CDUfYoe5Q9yh5lj7JxsvejsRsgGKv6Bhx6kNU1oOnBZw8Wd426B597AMFLjdk=AQAAAACAAACgDgAAeQEAAA==eJzdVsFtxDAM8yjdRBqlo3SEbOSOVtzBSVhSdBwU/eSAQw2CNRWKUq611tv7+xXtOL8/r78BeAw8gB/AD+DHyf/eOQnnHQ/AB/8jT/5x3vEAfPA/ByfzPB94AD74G/A34G/A34AvnpBX6I94xTh5i346b9FP9lZw6oXUjxysH7W4tupZQFd6yr1O32vBORutyABnI302BOcstd+6yMH6UUtqK54FdSWTlFXMJ2dVcMr26yMZpmxjnjnbgtMsYM2shfWjltRWPAvqPna+nO5s7pwPVI87i1cFvuzbTPeODxd9LP2v+mJ8e+r+cbrTveR84HrcOf0eu+vbVPeGD5d9TONzVX/h21P3s9Od7m3nA9XjzuxVha/6NtW94cNVH0v/i74435b29jiX75F+8d7pyhctvKfrPWUN1f38v93c080O73r/yl6SWR78cpabmev2P7/flt8LeA9rpd9LK3MnWaWcz/bGylz85ffb8t6jOS1nUObuB+Ogrkg=AQAAAACAAADAAAAANgAAAA==eJwtxUkCQCAAAMCSfQuF///UwcxlQvhFN05u3bn34NGTZy9evXl39uHTl4urbz9+/QFIoAEVAQAAAACAAADAAAAANgAAAA==eJwtxbcBgCAAADARe0MFy/+XOpgsCdWvdnTj1p17Dx49efbi1ZuTdx8+nV18+fbj1x9SAAEtAQAAAACAAADABgAAdwEAAA==eJwtxddCCAAAAECfYY/sTVkNe++EzJaMQtmyt2Rmlxmy98qe2XtERIiy1y94cPdypUv9V8ZlXc7lXcEVXcmVXcUBrupqru4arularu06rut6ru8GbuhGbuxAB7mJm7qZm7uFgx3iUIe5pVu5tdu4rdu5vTu4ozu5s7u4q7u5u3u4p3u5t8PdxxHu637u70gP8EAP8mAP8VBHOdoxjnWchznewz3CIz3KCU70aI/xWCc52eM83hM80ZM82VM81Sme5ume4Zme5dme47me5/le4IVe5MVO9RKneamXeblXeKVXOd2rvcZrvc7rvcEbneFMb/Jmb/FWb/N2Z3mHd3qXs73be7zX+7zfB3zQh3zYR3zUx3zcJ3zSp3zaOT7jsz7n877gi77ky77iq77m6871Dd/0Ld/2Hd/1Pd/3Az/0Iz/2Ez/1Mz93nl/4pfP9yq9d4Dd+60K/83t/cJE/+pOLXeLP/uKv/ubv/uGf/uXf/uO//gfGn271AQAAAACAAABgAwAA1QAAAA==eJwtxdFGAwAAAMAkSZJMkmQySZIkmSQzSTJJMpkkySRJJkmSJEkmk0mSJEkySZIkSWaSJEnS5/TQ3csVF/0rcanLXO4KV7rKAVe7xrWuc72DbnDIjW5ys1vc6ja3u8OdDrvL3e5xxFH3us/9HnDMgx7ysEcc96gTHvO4JzzpKSc97RnPes7zTnnBi17ysle86jWve8Ob3vK2095xxrvOes/7PvChj3zsE5/6zOe+cM6XvvK1b3zrO9/7wY9+8rPzLvjFr37zuz/86S9/+8e//gO3LC39AAAAAACAAAAAAAAAAAAAAACAAAAAAAAAAQAAAACAAABgAwAArAAAAA==eJxdyUViQlEQRFE+HtyCB/cETYD97wh3G+T2gHqT8+r22vX/NrjCNW7lvscdHqTbPuIVT3iWfpH7E+94k277gR6HDzrOe3fLPYA+9Eq37ccPDGFQeljuUYxgTLrtOKYxgUnpKbnn8BMz0m1nsYR5LEgvyr2KX1iWbruCdWxgTXpT7m1sYUe67S5+Yw/70gdyH+MQf6TbHuEvTnAqfSb3Jc7xT7rtBb4AVbYgjw==AQAAAACAAAAgAQAAVgAAAA==eJwtxcEGgwAAANARI2LEiIgYETHGiIgYI0aMiBEjov8/d+i9ywtOh7NDR7449tWJU2fOfXPh0pXvfvjp2o1bd3757d4fD/569OSfZ/+9ePXmHRgtB88=\\n  </AppendedData>\\n</VTKFile>\\n", "color": [1.0, 0.800000011920929, 0.0, 1.0], "position": [0.0, 0.0, 0.0], "orientation": [0.0, -0.0, 0.0]}];
   render(data, parent_element);
   </script>
</div>
<div style="clear:both;">
</div>
```default
from cadquery.occ_impl.shapes import box

result = (
    cq.Workplane()
    .add([box(1,1,i+1).moved(x=2*i) for i in range(5)])
)

# select boxes with volume <= 3
result = result.sort(lambda s: s.Volume())[:3]
```
