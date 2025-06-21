# Workplane

Most CAD programs use the concept of Workplanes. If you have experience with other CAD programs you will probably
feel comfortable with CadQuery’s Workplanes, but if you don’t have experience then they are an essential concept to
understand.

Workplanes represent a plane in space, from which other features can be located. They have a center point and a local
coordinate system. Most methods that create an object do so relative to the current workplane.

Usually the first workplane created is the “XY” plane, also known as the “front” plane. Once a solid is defined the most
common way to create a workplane is to select a face on the solid that you intend to modify and create a new workplane
relative to it. You can also create new workplanes anywhere in the world coordinate system, or relative to other planes
using offsets or rotations.

The most powerful feature of workplanes is that they allow you to work in 2D space in the coordinate system of the
workplane, and then CadQuery will transform these points from the workplane coordinate system to the world coordinate
system so your 3D features are located where you intended. This makes scripts much easier to create and maintain.

See [`cadquery.Workplane`](classreference.md#cadquery.Workplane) to learn more.

## 2D Construction

Once you create a workplane, you can work in 2D, and then later use the features you create to make 3D objects.
You’ll find all of the 2D constructs you expect – circles, lines, arcs, mirroring, points, etc.

See [2D Operations](apireference.md#doperations) to learn more.

## 3D Construction

You can construct 3D primitives such as boxes, wedges, cylinders and spheres directly. You can also sweep, extrude,
and loft 2D geometry to form 3D features.  Of course the basic primitive operations are also available.

See [3D Operations](apireference.md#id1) to learn more.

## Selectors

Selectors allow you to select one or more features, in order to define new features.  As an example, you might
extrude a box, and then select the top face as the location for a new feature.  Or, you might extrude a box, and
then select all of the vertical edges so that you can apply a fillet to them.

You can select Vertices, Edges, Faces, Solids, and Wires using selectors.

Think of selectors as the equivalent of your hand and mouse, if you were to build an object using a conventional CAD system.

See [Selectors](apireference.md#selectors) to learn more.

## Construction Geometry

Construction geometry are features that are not part of the object, but are only defined to aid in building the object.
A common example might be to define a rectangle, and then use the corners to define the location of a set of holes.

Most CadQuery construction methods provide a `forConstruction` keyword, which creates a feature that will only be used
to locate other features.

## The Stack

As you work in CadQuery, each operation returns a new Workplane object with the result of that
operation. Each Workplane object has a list of objects, and a reference to its parent.

You can always go backwards to older operations by removing the current object from the stack.  For example:

```default
Workplane(someObject).faces(">Z").first().vertices()
```

returns a CadQuery object that contains all of the vertices on the highest face of someObject. But you can always move
backwards in the stack to get the face as well:

```default
Workplane(someObject).faces(">Z").first().vertices().end()
```

You can browse stack access methods here: [Stack and Selector Methods](apireference.md#stackmethods).

<a id="chaining"></a>

## Chaining

All Workplane methods return another Workplane object, so that you can chain the methods together
fluently. Use the core Workplane methods to get at the objects that were created.

Each time a new Workplane object is produced during these chained calls, it has a
`parent` attribute that points to the Workplane object that created it.
Several CadQuery methods search this parent chain, for example when searching for the context solid.
You can also give a Workplane object a tag, and further down your chain of calls you can refer back
to this particular object using its tag.

## The Context Solid

Most of the time, you are building a single object, and adding features to that single object.  CadQuery watches
your operations, and defines the first solid object created as the ‘context solid’.  After that, any features
you create are automatically combined (unless you specify otherwise) with that solid.  This happens even if the
solid was created a long way up in the stack.  For example:

```default
Workplane("XY").box(1, 2, 3).faces(">Z").circle(0.25).extrude(1)
```

Will create a 1x2x3 box, with a cylindrical boss extending from the top face.  It was not necessary to manually
combine the cylinder created by extruding the circle with the box, because the default behavior for extrude is
to combine the result with the context solid. The [`hole()`](classreference.md#cadquery.Workplane.hole) method works similarly – CadQuery presumes that you want
to subtract the hole from the context solid.

If you want to avoid this, you can specify `combine=False`, and CadQuery will create the solid separately.

## Iteration

CAD models often have repeated geometry, and it’s really annoying to resort to for loops to construct features.
Many CadQuery methods operate automatically on each element on the stack, so that you don’t have to write loops.
For example, this:

```default
Workplane("XY").box(1, 2, 3).faces(">Z").vertices().circle(0.5)
```

Will actually create 4 circles, because `vertices()` selects 4 vertices of a rectangular face, and the `circle()` method
iterates on each member of the stack.

This is really useful to remember when you author your own plugins. [`cadquery.Workplane.each()`](classreference.md#cadquery.Workplane.each) is useful for this purpose.

## An Introspective Example

#### NOTE
If you are just beginning with CadQuery then you can leave this example for later.  If you have
some experience with creating CadQuery models and now you want to read the CadQuery source to
better understand what your code does, then it is recommended you read this example first.

To demonstrate the above concepts, we can define a more detailed string representations for the
[`Workplane`](classreference.md#cadquery.Workplane), [`Plane`](classreference.md#cadquery.Plane) and `CQContext` classes and
patch them in:

```default
import cadquery as cq


def tidy_repr(obj):
    """Shortens a default repr string"""
    return repr(obj).split(".")[-1].rstrip(">")


def _ctx_str(self):
    return (
        tidy_repr(self)
        + ":\n"
        + f"    pendingWires: {self.pendingWires}\n"
        + f"    pendingEdges: {self.pendingEdges}\n"
        + f"    tags: {self.tags}"
    )


cq.cq.CQContext.__str__ = _ctx_str


def _plane_str(self):
    return (
        tidy_repr(self)
        + ":\n"
        + f"    origin: {self.origin.toTuple()}\n"
        + f"    z direction: {self.zDir.toTuple()}"
    )


cq.occ_impl.geom.Plane.__str__ = _plane_str


def _wp_str(self):
    out = tidy_repr(self) + ":\n"
    out += f"  parent: {tidy_repr(self.parent)}\n" if self.parent else "  no parent\n"
    out += f"  plane: {self.plane}\n"
    out += f"  objects: {self.objects}\n"
    out += f"  modelling context: {self.ctx}"
    return out


cq.Workplane.__str__ = _wp_str
```

Now we can make a simple part and examine the [`Workplane`](classreference.md#cadquery.Workplane) and
`CQContext` objects at each step. The final part looks like:

<div class="cq-vtk"
 style="text-align:left;float:left;border: 1px solid #ddd; width:100%; height:500px">
   <script>
   var parent_element = document.currentScript.parentNode;
   var data = [{"shape": "<?xml version=\\"1.0\\"?>\\n<VTKFile type=\\"PolyData\\" version=\\"0.1\\" byte_order=\\"LittleEndian\\" header_type=\\"UInt32\\" compressor=\\"vtkZLibDataCompressor\\">\\n  <PolyData>\\n    <Piece NumberOfPoints=\\"1448\\"                 NumberOfVerts=\\"14\\"                   NumberOfLines=\\"819\\"                  NumberOfStrips=\\"0\\"                    NumberOfPolys=\\"524\\"                 >\\n      <PointData Normals=\\"Normals\\">\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0\\"                    RangeMax=\\"1.0000000513\\"         offset=\\"0\\"                   />\\n      </PointData>\\n      <CellData Normals=\\"Normals\\">\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"SUBSHAPE_IDS\\" format=\\"appended\\" RangeMin=\\"5\\"                    RangeMax=\\"65\\"                   offset=\\"2072\\"                />\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"MESH_TYPES\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"8\\"                    offset=\\"2320\\"                />\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0.99999996487\\"        RangeMax=\\"1.0000000239\\"         offset=\\"2428\\"                />\\n      </CellData>\\n      <Points>\\n        <DataArray type=\\"Float32\\" Name=\\"Points\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0.53851647781\\"        RangeMax=\\"1.7233688106\\"         offset=\\"3700\\"                />\\n      </Points>\\n      <Verts>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"5496\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"5572\\"                />\\n      </Verts>\\n      <Lines>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"5648\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"7764\\"                />\\n      </Lines>\\n      <Strips>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"9412\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"9428\\"                />\\n      </Strips>\\n      <Polys>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"9444\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"12216\\"               />\\n      </Polys>\\n    </Piece>\\n  </PolyData>\\n  <AppendedData encoding=\\"base64\\">\\n   \_AQAAAACAAADgQwAA/gUAAA==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AQAAAACAAABoKgAApgAAAA==eJzt2MdqQgEQRmE3YuxY0RixYMGChQSFJFje/6VceLYyG+WC98zme4X5z0fmfnksYhnr2MQu9nCIU1ziFv/wjDksYAkrWMMGtrCDn/iFAxzhBGe4wBVucIffeMBfVU2NJ7yoamrMBlYD24H9wHHgPHAduA/8CTyqquK/qqqqvr1XVU2NUf+I+kbUL6I+YX9Q1Ucm/Q+pqqrq8016/6jq67wBGis1AA==AQAAAACAAABoKgAAPQAAAA==eJztziEKACAQAEE5EO//LzbYjAp6YbZM3WireGQnySJmkQ+SJMlq5ubvH5IkSZLnDpIkSZIkyUsncCoeeQ==AQAAAACAAACcPwAApwMAAA==eJzt101IVUEUAOALUQuFciP0Y0igQS0Kg2hh7w70QxJGi4h+IBKUKCoxC7EwvYsgKiIIKwqSfggJyxaRgfnuZIt4YEQ/tMn+iArUNpGrFtl5950ZjnPueymRJh1B/DzMnXfv3DNnzvO8QHn2RywWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovF4qnnR93NOv33UqovQQ1jNBmfdoC/0TWZMaMcZPscGKPaUn1J1zGfQa+LmY9fk54vrfSc1NnnkPgExqe6gyluL/N/7DNKfGLi2caIJ8Wed3WoRbUmnqx0/bCiRd3Pv5hwXTOtWXW2/2TeVtSkip6X+a4/th5W+95UM5+qbVAXOk4y7+yoV+0F15m7N9SqWTMfMNdv3aPKW18wX3tarRpaB5j77+5QwyMjzN/zt6jKT3nKdWn/RrWqrpB5zsIKlXe5mLnrm1JLaxYxz1i9Qt3Sy5ifFS9R626WM/eeLlGN89Ywvz87Vw0VVDL3Li9QVcc2Maeapqu1B7Yzd70d9he8rGIeLn3nD9zYxTzy4bH/+vNe5rL5d/x7Z+qY1eB5f/eVQ8w/bjf5BwsbmV99We+f+3qEeX/bbH96yVHm44N9ic3Y41CnFlcmTnS2MHtZahKMSZoxME+SzBMbh3sIzT3AfYbkPmPj8IwheV5rWJOQrI81rGFI1tMa1jwk628N7ygk78sa3mlI3q815IAm+WANOaNJ/lhDjmmSb9aQk5rkpzXksCb5bA05r0n+W8Me0WaPwD7SZB/FxmEParIfrWHParNnYV9rsq9j41ATNKkP1lBDNKkn1lBzNKk/1lCjNKlX1lDTNKlv1lADNamH1lAztamZUFc1qas2DnVYkzpsx9A41HBN6rlxgO5xjdcmHZv5ozixuZ8wHafGZ2HGZ2fGtXJt1jaKU+O7cG3eXRSnxnft2uSDTsepMZeYMfdcm/yM4tSY267NXoji1Lh3mHGvMePeZMa9zIx7nxlrBTPWFmasRa5N7Yri1FjrXJvaGMWpsX4yY+1lxvrsGn/od/TMd2Q8C5jx7GDGs4YZzyZmPMuY8eyLjOdjzjierZHx/M0Zx7ObGc96ZuwNmLGXyMQz/UbOOPYqzNjbMGMvxIy9EzP2WszYmzFjLxe6xt6PGXtFZuwtmbEXZcbeNTL2tznj2BszYy+ddI29NzP26j2jHfudPYjre8bpP5kn+Mtx8djX/3908I/aE0+6vd84GKezXTuW+dmYX9aCrd0=AQAAAACAAADgQwAAMQUAAA==eJztmkuIXEUUhhsVn5CFC2WCiJMxEkFECY4y6Vs9jEbjZFwoiBsDGnTh0ihxIS40LnzrIgEVQSGtSFAwBEnUrppfs3DQuHTlEwlCVtn4WMbq8p7ks+d2zwyEIDNncZmf5t5bdc75b331mFarNd9qtTr1NV9fne+OHUv9q9VS0W+/Ndbpa9xz+t7Bv/177dm+xrODF9/ROdP2XGi1Hpr4t23Tje2N7POI/nfs/hFxNcXW1O7gvY0xDcsP+zmYt6Ycss8DuWU7jVfD/U19b9JNf0fpkfUd1lfUuvPey3Phq/sn2n29dWF7WBjfX/Ste2bDDzf9UfQdcVuYuW9D1devP3Vn+Pra2aJfPHR76O5+vOg/d02Hx658pejjh9vhgfXvFn34+dvCeUcOFr3+x83hjeNHi77gyxvDrr3fF/3p5PXhkd7vRR+anghP3/t30d/8dlXY1z0/9PXF41eE7txlRR85tS5c+s7lRT+656Iw/tpY0e8/fKp65upriv5r7GR1ctt1RY9N/Vy9eskNofZi9dGDNxe96afPqxNhsui9uz+sNn08VfRCd1/1ZjcUPf/Ec9XBDTNF7/hlR9XeuLXoC2cnq3sO3FX0gel11ewndxf9wmfftk/csr3ojb8+2d48NVf00Z37tzzbO62/MJ3v6dk9+dmePZvfGe2dua1obeU+ROtD7lu0vuU+R+tzjiVaLDnGaDHm2KPFnnMSLSc5V9FylXMYLYc5t8lym3OeLOe5FslqkWuUrEa5dslql2uarKa51slqnT2QzAPZG8m8kT2TzDPZS8m8lD2WzGPZe8m8lz2ZzJPZq8m8mj2czMPZ28m8nT2fXqpmPsDvPdzfw3t6eH9EuxH9iehnRP8j4oqINyIPEfmJyFtEPhPynJD/hLok1Cuhjgn1Tah7gh8SfJLgnwRfJfgtwYcJ/kzwbYKfE3xueovp+ruwZ9v2bP0dWVuVtVV/d9a3yvpWf6cWS2Wx1N+1xV5Z7PU4YLmqLFf1uGG5DZbbepyxWgSrRT0uJYxXVtNgNa3HN/NAMA/U46F5Jphn6vHTPBbMY/V4GzEOR4zP5uFgHq7H897gON/M+v/qMywQWCCwQGCBwAKBBQILBBYILBBYILBAYIHAAoEFAgsEFggsEFggsEBggcACgQUCCwQWCCwQWCCwQGCBwAKBBQILBBYILBBYILBAYIHAAoEFAgsEFggsEFggsEBggcACgQUCCwQWCCwQWCCwQGCBwAKBBQILBBYILBBYILBAYIHAAoEFAgsEFggsEFggsEBggcACgQUCCwQWCCwQWCCwQGCBwAKBBQILBBYILBBYILBAYIHAAoEFAgsEFggsEFggsEBggcACgQUCCwQWCCwQWCCwQGCBwAKBBQILBBYILBBYILBAYIHAAoEFAgsEFggsEFggsEBggcACgQUCCwQWCCwQWCCwQGCBwIL/zfpu1NrmnK77VhrvOVg/NuZzxHvO5npzVD2a3reS9elS8a6k7mfDO6P6tCifS+yxLPLbMvvblIvl5tPX775+9/W7r999/b7m1+/L+d0Z4YxwRjgjnBGrmxG+l+t7ub6X63u5vpe7dvZyfcz3Md/HfB/zfcxfO2N+89nCCv6PdDnnP4vOH4adqQ1rd8S5SeMZyBLnZU3nOMPOTIaduyx19rLc3DTGMOzMqOE9g8/6+Y7v3VnsvnfX8r0737vzvTtfx/k6ztdxvo7zddyqXcf5PN/n+T7P93m+z/NX9Tzf5/Y+t/e5vc/tfW6/muf2/wDqhUZ6AQAAAACAAABwAAAAJgAAAA==eJwtxacBACAAACD39v93DUIhhC86Obu4url7eHp5+/j6AQ6oAFw=AQAAAACAAABwAAAAJwAAAA==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AQAAAACAAACYGQAAwAQAAA==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AQAAAACAAABgEAAASwMAAA==eJw111PDEAYAQNFs27Zt17K1bNu2sey2bC/btm3b9h6+s/tyfsMNGiigEAzNcIzIKIzOWIzLBEzMZEzJNEzPTMzKHMzNfCzIIvyDJVmG5VmJVfkna7EuG7Axm7El27A9O7Ere7A3+3Egh3A4R3EMx3MSp3IG/+EczuciLuUKruZabuBmbuNO7uF+HuJRnuBpnuNFXuF13uJdPuBjPuNLvuF7fuJX/uBvBgkcYHCGYlhGYGRGY0zGYXwmYlKmYGqmY0ZmYXbmYl4WYGEWYwmWZjlWZBVWZ03WYX02YlO2YGu2Y0d2YXf2Yl8O4GAO40j+xXGcyCmczr85m/O4kEu4nKv4L9dzE7dyB3dzHw/yCI/zFM/yAi/zGm/yDu/zEZ/yBV/zHT/yC7/zFwMHCTAYQzIMwzMSozIGYzMeEzIJkzMV0zIDMzMbczIP87MQi7I4S7EsK7Ayq7EGa7MeG7IJm7MV27IDO7Mbe7IP+3MQh3IER3MsJ3Ayp3EmZ3EuF3Axl3El13AdN3ILt3MX9/IAD/MYT/IMz/MSr/IGb/MeH/IJn/MV3/IDP/MbfzJQUDAEQzMcIzIKozMW4zIBEzMZUzIN0zMTszIHczMfC7II/2BJlmF5VmJV/slarMsGbMxmbMk2bM9O7Moe7M1+HMghHM5RHMPxnMSpnMF/OIfzuYhLuYKruZYbuJnbuJN7uJ+HeJQneJrneJFXeJ23eJcP+JjP+JJv+J6f+JU/+JtBggUYnKEYlhEYmdEYk3EYn4mYlCmYmumYkVmYnbmYlwVYmMVYgqVZjhVZhdVZk3VYn43YlC3Ymu3YkV3Ynb3YlwM4mMM4kn9xHCdyCqfzb87mPC7kEi7nKv7L9dzErdzB3dzHgzzC4zzFs7zAy7zGm7zD+3zEp3zB13zHj/zC7/zFwMEDDMaQDMPwjMSojMHYjMeETMLkTMW0zMDMzMaczMP8LMSiLM5SLMsKrMxqrMHarMeGbMLmbMW27MDO7Mae7MP+HMShHMHRHMsJnMxpnMlZnMsFXMxlXMk1XMeN3MLt3MW9PMDDPMaTPMPzvMSrvMHbvMeHfMLnfMW3/MDP/Maf/H/4gzIEQzMcIzIKozMW4zIBEzMZ/wPjFwVG\\n  </AppendedData>\\n</VTKFile>\\n", "color": [1.0, 0.800000011920929, 0.0, 1.0], "position": [0.0, 0.0, 0.0], "orientation": [0.0, -0.0, 0.0]}];
   render(data, parent_element);
   </script>
</div>
<div style="clear:both;">
</div>
```default
part = (
    cq.Workplane()
    .box(1, 1, 1)
    .tag("base")
    .wires(">Z")
    .toPending()
    .translate((0.1, 0.1, 1.0))
    .toPending()
    .loft()
    .faces(">>X", tag="base")
    .workplane(centerOption="CenterOfMass")
    .circle(0.2)
    .extrude(1)
)
```

#### NOTE
Some of the modelling process for this part is a bit contrived and not a great example of fluent
CadQuery techniques.

The start of our chain of calls is:

```default
part = cq.Workplane()
print(part)
```

Which produces the output:

```none
Workplane object at 0x2760:
  no parent
  plane: Plane object at 0x2850:
    origin: (0.0, 0.0, 0.0)
    z direction: (0.0, 0.0, 1.0)
  objects: []
  modelling context: CQContext object at 0x2730:
    pendingWires: []
    pendingEdges: []
    tags: {}
```

This is simply an empty [`Workplane`](classreference.md#cadquery.Workplane). Being the first [`Workplane`](classreference.md#cadquery.Workplane)
in the chain, it does not have a parent. The `plane` attribute contains a
[`Plane`](classreference.md#cadquery.Plane) object that describes the XY plane.

Now we create a simple box. To keep things short, the `print(part)` line will not be shown for the
rest of these code blocks:

```default
part = part.box(1, 1, 1)
```

Which produces the output:

```none
Workplane object at 0xaa90:
  parent: Workplane object at 0x2760
  plane: Plane object at 0x3850:
    origin: (0.0, 0.0, 0.0)
    z direction: (0.0, 0.0, 1.0)
  objects: [<cadquery.occ_impl.shapes.Solid object at 0xbbe0>]
  modelling context: CQContext object at 0x2730:
    pendingWires: []
    pendingEdges: []
    tags: {}
```

The first thing to note is that this is a different [`Workplane`](classreference.md#cadquery.Workplane) object to the
previous one, and in the `parent` attribute of this
[`Workplane`](classreference.md#cadquery.Workplane) is our previous [`Workplane`](classreference.md#cadquery.Workplane). Returning a new instance
of [`Workplane`](classreference.md#cadquery.Workplane) is the normal behaviour of most [`Workplane`](classreference.md#cadquery.Workplane) methods
(with some exceptions, as will be shown below) and this is how the [chaining]() concept is
implemented.

Secondly, the modelling context object is the same as the one in the previous
[`Workplane`](classreference.md#cadquery.Workplane), and this one modelling context at `0x2730` will be shared between
every `Workplane` object in this chain. If we instantiate a new [`Workplane`](classreference.md#cadquery.Workplane)
with `part2 = cq.Workplane()`, then this `part2` would have a different instance of the
`CQContext` attached to it.

Thirdly, in our objects list is a single [`Solid`](classreference.md#cadquery.Solid) object, which is the box we just
created.

Often when creating models you will find yourself wanting to refer back to a specific
[`Workplane`](classreference.md#cadquery.Workplane) object, perhaps because it is easier to select the feature you want in this
earlier state, or because you want to reuse a plane. Tags offer a way to refer back to a previous
[`Workplane`](classreference.md#cadquery.Workplane). We can tag the [`Workplane`](classreference.md#cadquery.Workplane) that contains this basic box now:

```default
part = part.tag("base")
```

The string representation of `part` is now:

```none
Workplane object at 0xaa90:
  parent: Workplane object at 0x2760
  plane: Plane object at 0x3850:
    origin: (0.0, 0.0, 0.0)
    z direction: (0.0, 0.0, 1.0)
  objects: [<cadquery.occ_impl.shapes.Solid object at 0xbbe0>]
  modelling context: CQContext object at 0x2730:
    pendingWires: []
    pendingEdges: []
    tags: {'base': <cadquery.cq.Workplane object at 0xaa90>}
```

The `tags` attribute of the modelling context is simply a dict
associating the string name given by the [`tag()`](classreference.md#cadquery.Workplane.tag) method to the
[`Workplane`](classreference.md#cadquery.Workplane). Methods such as [`workplaneFromTagged()`](classreference.md#cadquery.Workplane.workplaneFromTagged) and
selection methods like [`edges()`](classreference.md#cadquery.Workplane.edges) can operate on a tagged
[`Workplane`](classreference.md#cadquery.Workplane). Note that unlike the `part = part.box(1, 1, 1)` step where we went
from `Workplane object at 0x2760` to `Workplane object at 0xaa90`, the
[`tag()`](classreference.md#cadquery.Workplane.tag) method has returned the same object at `0xaa90`. This is unusual
for a [`Workplane`](classreference.md#cadquery.Workplane) method.

The next step is:

```default
part = part.faces(">>Z")
```

The output is:

```none
Workplane object at 0x8c40:
  parent: Workplane object at 0xaa90
  plane: Plane object at 0xac40:
    origin: (0.0, 0.0, 0.0)
    z direction: (0.0, 0.0, 1.0)
  objects: [<cadquery.occ_impl.shapes.Face object at 0x3c10>]
  modelling context: CQContext object at 0x2730:
    pendingWires: []
    pendingEdges: []
    tags: {'base': <cadquery.cq.Workplane object at 0xaa90>}
```

Our selection method has taken the [`Solid`](classreference.md#cadquery.Solid) from the
`objects` list of the previous [`Workplane`](classreference.md#cadquery.Workplane), found the
face with its center furthest in the Z direction, and placed that face into the
`objects` attribute. The [`Solid`](classreference.md#cadquery.Solid) representing the box we
are modelling is gone, and when a [`Workplane`](classreference.md#cadquery.Workplane) method needs to access that solid it
searches through the parent chain for the nearest solid. This action can also be done by a user
through the [`findSolid()`](classreference.md#cadquery.Workplane.findSolid) method.

Now we want to select the boundary of this [`Face`](classreference.md#cadquery.Face) (a [`Wire`](classreference.md#cadquery.Wire)), so
we use:

```default
part = part.wires()
```

The output is now:

```none
Workplane object at 0x6880:
  parent: Workplane object at 0x8c40
  plane: Plane object at 0x38b0:
    origin: (0.0, 0.0, 0.0)
    z direction: (0.0, 0.0, 1.0)
  objects: [<cadquery.occ_impl.shapes.Wire object at 0xaca0>]
  modelling context: CQContext object at 0x2730:
    pendingWires: []
    pendingEdges: []
    tags: {'base': <cadquery.cq.Workplane object at 0xaa90>}
```

Modelling operations take their wires and edges from the modelling context’s pending lists. In order
to use the [`loft()`](classreference.md#cadquery.Workplane.loft) command further down the chain, we need to push this wire
to the modelling context with:

```default
part = part.toPending()
```

Now we have:

```none
Workplane object at 0x6880:
  parent: Workplane object at 0x8c40
  plane: Plane object at 0x38b0:
    origin: (0.0, 0.0, 0.0)
    z direction: (0.0, 0.0, 1.0)
  objects: [<cadquery.occ_impl.shapes.Wire object at 0xaca0>]
  modelling context: CQContext object at 0x2730:
    pendingWires: [<cadquery.occ_impl.shapes.Wire object at 0xaca0>]
    pendingEdges: []
    tags: {'base': <cadquery.cq.Workplane object at 0xaa90>}
```

The [`Wire`](classreference.md#cadquery.Wire) object that was only in the `objects`
attribute before is now also in the modelling context’s `pendingWires`.
The [`toPending()`](classreference.md#cadquery.Workplane.toPending) method is also another of the unusual methods that return
the same [`Workplane`](classreference.md#cadquery.Workplane) object instead of a new one.

To set up the other side of the [`loft()`](classreference.md#cadquery.Workplane.loft) command further down the chain, we
translate the wire in `objects` by calling:

```default
part = part.translate((0.1, 0.1, 1.0))
```

Now the string representation of `part` looks like:

```none
Workplane object at 0x3a00:
  parent: Workplane object at 0x6880
  plane: Plane object at 0xac70:
    origin: (0.0, 0.0, 0.0)
    z direction: (0.0, 0.0, 1.0)
  objects: [<cadquery.occ_impl.shapes.Wire object at 0x35e0>]
  modelling context: CQContext object at 0x2730:
    pendingWires: [<cadquery.occ_impl.shapes.Wire object at 0xaca0>]
    pendingEdges: []
    tags: {'base': <cadquery.cq.Workplane object at 0xaa90>}
```

It may look similar to the previous step, but the [`Wire`](classreference.md#cadquery.Wire) object in
`objects` is different. To get this wire into the pending wires list,
again we use:

```default
part = part.toPending()
```

The result:

```none
Workplane object at 0x3a00:
  parent: Workplane object at 0x6880
  plane: Plane object at 0xac70:
    origin: (0.0, 0.0, 0.0)
    z direction: (0.0, 0.0, 1.0)
  objects: [<cadquery.occ_impl.shapes.Wire object at 0x35e0>]
  modelling context: CQContext object at 0x2730:
    pendingWires: [<cadquery.occ_impl.shapes.Wire object at 0xaca0>, <cadquery.occ_impl.shapes.Wire object at 0x7f5c7f5c35e0>]
    pendingEdges: []
    tags: {'base': <cadquery.cq.Workplane object at 0xaa90>}
```

The modelling context’s `pendingWires` attribute now contains the two
wires we want to loft between, and we simply call:

```default
part = part.loft()
```

After the loft operation, our Workplane looks quite different:

```none
Workplane object at 0x32b0:
  parent: Workplane object at 0x3a00
  plane: Plane object at 0x3d60:
    origin: (0.0, 0.0, 0.0)
    z direction: (0.0, 0.0, 1.0)
  objects: [<cadquery.occ_impl.shapes.Compound object at 0xad30>]
  modelling context: CQContext object at 0x2730:
    pendingWires: []
    pendingEdges: []
    tags: {'base': <cadquery.cq.Workplane object at 0xaa90>}
```

In the `cq.Workplane.objects` attribute we now have one [`Compound`](classreference.md#cadquery.Compound) object and the modelling
context’s `pendingWires` has been cleared by
[`loft()`](classreference.md#cadquery.Workplane.loft).

#### NOTE
To inspect the [`Compound`](classreference.md#cadquery.Compound) object further you can use
[`val()`](classreference.md#cadquery.Workplane.val) or [`findSolid()`](classreference.md#cadquery.Workplane.findSolid) to get at the
[`Compound`](classreference.md#cadquery.Compound) object, then use [`cadquery.Shape.Solids()`](classreference.md#cadquery.Shape.Solids) to return a list
of the [`Solid`](classreference.md#cadquery.Solid) objects contained in the [`Compound`](classreference.md#cadquery.Compound), which in
this example will be a single [`Solid`](classreference.md#cadquery.Solid) object. For example:

```pycon
>>> a_compound = part.findSolid()
>>> a_list_of_solids = a_compound.Solids()
>>> len(a_list_of_solids)
1
```

Now we will create a small cylinder protruding from a face on the original box. We need to set up a
workplane to draw a circle on, so firstly we will select the correct face:

```default
part = part.faces(">>X", tag="base")
```

Which results in:

```none
Workplane object at 0x3f10:
  parent: Workplane object at 0x32b0
  plane: Plane object at 0xefa0:
    origin: (0.0, 0.0, 0.0)
    z direction: (0.0, 0.0, 1.0)
  objects: [<cadquery.occ_impl.shapes.Face object at 0x3af0>]
  modelling context: CQContext object at 0x2730:
    pendingWires: []
    pendingEdges: []
    tags: {'base': <cadquery.cq.Workplane object at 0xaa90>}
```

We have the desired [`Face`](classreference.md#cadquery.Face) in the `objects` attribute,
but the `plane` has not changed yet. To create the new plane we use the
`Workplane.workplane()` method:

```default
part = part.workplane()
```

Now:

```none
Workplane object at 0xe700:
  parent: Workplane object at 0x3f10
  plane: Plane object at 0xe730:
    origin: (0.5, 0.0, 0.0)
    z direction: (1.0, 0.0, 0.0)
  objects: []
  modelling context: CQContext object at 0x2730:
    pendingWires: []
    pendingEdges: []
    tags: {'base': <cadquery.cq.Workplane object at 0xaa90>}
```

The `objects` list has been cleared and the [`Plane`](classreference.md#cadquery.Plane)
object has a local Z direction in the global X direction. Since the base of the plane is the side of
the box, the origin is offset in the X direction.

Onto this plane we can draw a circle:

```default
part = part.circle(0.2)
```

Now:

```none
Workplane object at 0xe790:
  parent: Workplane object at 0xe700
  plane: Plane object at 0xaf40:
    origin: (0.5, 0.0, 0.0)
    z direction: (1.0, 0.0, 0.0)
  objects: [<cadquery.occ_impl.shapes.Wire object at 0xe610>]
  modelling context: CQContext object at 0x2730:
    pendingWires: [<cadquery.occ_impl.shapes.Wire object at 0xe610>]
    pendingEdges: []
    tags: {'base': <cadquery.cq.Workplane object at 0xaa90>}
```

The [`circle()`](classreference.md#cadquery.Workplane.circle) method - like all 2D drawing methods - has placed the circle
into both the `objects` attribute (where it will be cleared during the
next modelling step), and the modelling context’s pending wires (where it will persist until used by
another [`Workplane`](classreference.md#cadquery.Workplane) method).

The next step is to extrude this circle and create a cylindrical protrusion:

```default
part = part.extrude(1, clean=False)
```

Now:

```none
Workplane object at 0xafd0:
  parent: Workplane object at 0xe790
  plane: Plane object at 0x3e80:
    origin: (0.5, 0.0, 0.0)
    z direction: (1.0, 0.0, 0.0)
  objects: [<cadquery.occ_impl.shapes.Compound object at 0xaaf0>]
  modelling context: CQContext object at 0x2730:
    pendingWires: []
    pendingEdges: []
    tags: {'base': <cadquery.cq.Workplane object at 0xaa90>}
```

The [`extrude()`](classreference.md#cadquery.Workplane.extrude) method has cleared all the pending wires and edges. The
`objects` attribute contains the final [`Compound`](classreference.md#cadquery.Compound) object
that is shown in the 3D view above.

#### NOTE
The [`extrude()`](classreference.md#cadquery.Workplane.extrude) has an argument for `clean` which defaults to `True`.
This extrudes the pending wires (creating a new [`Workplane`](classreference.md#cadquery.Workplane) object), then runs
the [`clean()`](classreference.md#cadquery.Workplane.clean) method to refine the result, creating another
[`Workplane`](classreference.md#cadquery.Workplane). If you were to run the example with the default
`clean=True` then you would see an intermediate
[`Workplane`](classreference.md#cadquery.Workplane) object in `parent`
rather than the object from the previous step.
