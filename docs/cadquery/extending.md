<a id="extending"></a>

# Extending CadQuery

If you find that CadQuery does not suit your needs, you can easily extend it.  CadQuery provides several extension
methods:

> * You can load plugins others have developed. This is by far the easiest way to access other code
> * You can define your own plugins.
> * You can use OCP scripting directly

## Using OpenCascade methods

The easiest way to extend CadQuery is to simply use OpenCascade/OCP scripting inside of your build method.  Just about
any valid OCP script will execute just fine. For example, this simple CadQuery script:

```default
return cq.Workplane("XY").box(1.0, 2.0, 3.0).val()
```

is actually equivalent to:

```default
return cq.Shape.cast(
    BRepPrimAPI_MakeBox(
        gp_Ax2(Vector(-0.1, -1.0, -1.5), Vector(0, 0, 1)), 1.0, 2.0, 3.0
    ).Shape()
)
```

As long as you return a valid OCP Shape, you can use any OCP methods you like. You can even mix and match the
two. For example, consider this script, which creates a OCP box, but then uses CadQuery to select its faces:

```default
box = cq.Shape.cast(
    BRepPrimAPI_MakeBox(
        gp_Ax2(Vector(-0.1, -1.0, -1.5), Vector(0, 0, 1)), 1.0, 2.0, 3.0
    ).Shape()
)
cq = Workplane(box).faces(">Z").size()  # returns 6
```

## Extending CadQuery: Plugins

Though you can get a lot done with OpenCascade, the code gets pretty nasty in a hurry. CadQuery shields you from
a lot of the complexity of the OpenCascade API.

You can get the best of both worlds by wrapping your OCP script into a CadQuery plugin.

A CadQuery plugin is simply a function that is attached to the CadQuery [`cadquery.CQ()`](classreference.md#cadquery.CQ) or [`cadquery.Workplane()`](classreference.md#cadquery.Workplane) class.
When connected, your plugin can be used in the chain just like the built-in functions.

There are a few key concepts important to understand when building a plugin

## The Stack

Every CadQuery object has a local stack, which contains a list of items.  The items on the stack will be
one of these types:

> * **A CadQuery SolidReference object**, which holds a reference to a OCP solid
> * **A OCP object**, a Vertex, Edge, Wire, Face, Shell, Solid, or Compound

The stack is available by using self.objects, and will always contain at least one object.

#### NOTE
Objects and points on the stack are **always** in global coordinates.  Similarly, any objects you
create must be created in terms of global coordinates as well!

## Preserving the Chain

CadQuery’s fluent API relies on the ability to chain calls together one after another. For this to work,
you must return a valid CadQuery object as a return value.  If you choose not to return a CadQuery object,
then your plugin will end the chain. Sometimes this is desired for example [`cadquery.Workplane.size()`](classreference.md#cadquery.Workplane.size)

There are two ways you can safely continue the chain:

> 1. **return self**  If you simply wish to modify the stack contents, you can simply return a reference to
>    self.  This approach is destructive, because the contents of the stack are modified, but it is also the
>    simplest.
> 2. [`cadquery.Workplane.newObject()`](classreference.md#cadquery.Workplane.newObject)  Most of the time, you will want to return a new object.  Using newObject will
>    return a new CQ or Workplane object having the stack you specify, and will link this object to the
>    previous one.  This preserves the original object and its stack.

## Helper Methods

When you implement a CadQuery plugin, you are extending CadQuery’s base objects.  As a result, you can call any
CadQuery or Workplane methods from inside of your extension.  You can also call a number of internal methods that
are designed to aid in plugin creation:

> * `cadquery.Workplane._makeWireAtPoints()` will invoke a factory function you supply for all points on the stack,
>   and return a properly constructed cadquery object. This function takes care of registering wires for you
>   and everything like that
> * [`cadquery.Workplane.newObject()`](classreference.md#cadquery.Workplane.newObject) returns a new Workplane object with the provided stack, and with its parent set
>   to the current object. The preferred way to continue the chain
> * [`cadquery.Workplane.findSolid()`](classreference.md#cadquery.Workplane.findSolid) returns the first Solid found in the chain, working from the current object upwards
>   in the chain. commonly used when your plugin will modify an existing solid, or needs to create objects and
>   then combine them onto the ‘main’ part that is in progress
> * `cadquery.Workplane._addPendingWire()` must be called if you add a wire.  This allows the base class to track all the wires
>   that are created, so that they can be managed when extrusion occurs.
> * [`cadquery.Workplane.wire()`](classreference.md#cadquery.Workplane.wire) gathers up all of the edges that have been drawn ( eg, by line, vline, etc ), and
>   attempts to combine them into a single wire, which is returned. This should be used when your plugin creates
>   2D edges, and you know it is time to collect them into a single wire.
> * `cadquery.Workplane.plane()` provides a reference to the workplane, which allows you to convert between workplane
>   coordinates and global coordinates:
>   \* `cadquery.occ_impl.geom.Plane.toWorldCoords()` will convert local coordinates to global ones
>   \* `cadquery.occ_impl.geom.Plane.toLocalCoords()` will convert from global coordinates to local coordinates

## Coordinate Systems

Keep in mind that the user may be using a work plane that has created a local coordinate system. Consequently,
the orientation of shapes that you create are often implicitly defined by the user’s workplane.

Any objects that you create must be fully defined in *global coordinates*, even though some or all of the users’
inputs may be defined in terms of local coordinates.

## Linking in your plugin

Your plugin is a single method, which is attached to the main Workplane or CadQuery object.

Your plugin method’s first parameter should be ‘self’, which will provide a reference to base class functionality.
You can also accept other arguments.

To install it, simply attach it to the CadQuery or Workplane object, like this:

```default
def _yourFunction(self, arg1, arg):
    # do stuff
    return whatever_you_want


cq.Workplane.yourPlugin = _yourFunction
```

That’s it!

## CadQueryExample Plugins

Some core cadquery code is intentionally written exactly like a plugin.
If you are writing your own plugins, have a look at these methods for inspiration:

> * [`cadquery.Workplane.polygon()`](classreference.md#cadquery.Workplane.polygon)
> * [`cadquery.Workplane.cboreHole()`](classreference.md#cadquery.Workplane.cboreHole)

## Plugin Example

This ultra simple plugin makes cubes of the specified size for each stack point.

(The cubes are off-center because the boxes have their lower left corner at the reference points.)

<div class="cq-vtk"
 style="text-align:left;float:left;border: 1px solid #ddd; width:100%; height:500px">
   <script>
   var parent_element = document.currentScript.parentNode;
   var data = [{"shape": "<?xml version=\\"1.0\\"?>\\n<VTKFile type=\\"PolyData\\" version=\\"0.1\\" byte_order=\\"LittleEndian\\" header_type=\\"UInt32\\" compressor=\\"vtkZLibDataCompressor\\">\\n  <PolyData>\\n    <Piece NumberOfPoints=\\"520\\"                  NumberOfVerts=\\"40\\"                   NumberOfLines=\\"180\\"                  NumberOfStrips=\\"0\\"                    NumberOfPolys=\\"76\\"                  >\\n      <PointData Normals=\\"Normals\\">\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0\\"                    RangeMax=\\"1\\"                    offset=\\"0\\"                   />\\n      </PointData>\\n      <CellData Normals=\\"Normals\\">\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"SUBSHAPE_IDS\\" format=\\"appended\\" RangeMin=\\"5\\"                    RangeMax=\\"159\\"                  offset=\\"120\\"                 />\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"MESH_TYPES\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"7\\"                    offset=\\"524\\"                 />\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"1\\"                    RangeMax=\\"1\\"                    offset=\\"596\\"                 />\\n      </CellData>\\n      <Points>\\n        <DataArray type=\\"Float32\\" Name=\\"Points\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"2.1360009363\\"         RangeMax=\\"5.0062460986\\"         offset=\\"744\\"                 />\\n      </Points>\\n      <Verts>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1612\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1740\\"                />\\n      </Verts>\\n      <Lines>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1872\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"2712\\"                />\\n      </Lines>\\n      <Strips>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"3176\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"3192\\"                />\\n      </Strips>\\n      <Polys>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"3208\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"3700\\"                />\\n      </Polys>\\n    </Piece>\\n  </PolyData>\\n  <AppendedData encoding=\\"base64\\">\\n   \_AQAAAACAAABgGAAARgAAAA==eJzt0cEJACAMBDA3czU3czXBCWxFKJi8zkfhbFsDAAAAgMrGjOX0TP8nR+f2+3Cn4U6P75v6a2SX+ut/0T87UyMvthhviQ==AQAAAACAAABACQAAHQEAAA==eJzN01crKAAAhmE3wrFyjJB9smXLpoNIZkZGZGZkRGZGRnQ4Rw4ZkeSvuvDev1fiu3n+wPcGB3wsBEMxHH9iDCZgMqZgGmZgFmZjLuZjERZjKZZjFVZjLdZjE3ZiN/bjME7iNM7jMm7iNu7jMV7gX/yP9xiEPzAMIzAKozEW4zERkzAV0/EXZmIO5mEBFmIJlmEFVmIN1mED/sZmbMUO7MIe7MMBHMIRHMMJnMIZnMMFXMIVXMMN3MId3MMDPMITPMM/eIn/8Bpv8A4f8AkDxUgx7pvbKLaIbWK72CsOiqPiuDgrLoqr4rq4Kx6Kp+K5eCXeio/is/givopvovX61f19ds/Wq/VovVlP1ov1YH+3P9tf7Y/2t3c8XF6LAQAAAACAAABACQAAIwAAAA==eJxjYoAAplGaLJp1lB6lR+lRepQelDT7KD1K05AGAIi5Bek=AQAAAACAAADgDQAAXAAAAA==eJxjYGiwZ4CDUfYoe5Q9yh5lj7JH2aPsUfYom2T2fjR2AxRjk2NAksNndgMRbFL1Qu3GYFNqJrX0NhA2E5cZYD5aWOO0g8T4wmUOLveMmo/ffJxpgCriABFk+tk=AQAAAACAAABgGAAAdwIAAA==eJztVsFtwzAM1CiZJOJoHSWT2B6tTWBJ5xOPsuICbYE+AhAMRcri3ZEp2ZbSx/N3T81edtvAb7vfIMbgrLX425dvW5t922OePrRLzJaPdom52dE+5MRaGXKCXWJeOcEuMa+cYJeY+i1Lu/8jt+965PYtxa7+DP7c/OVbil39+/2L/fyv5sxQyyBnhloGOTPU2v1dT7nX96DX7GdsLOT3sME4wbrs5/fnGMJYxcZJvHnYw7OMyRp/Ep8eVvEsY7hi7ySePWzjWcZ8jT+Jf48LePbAEdaEyL47eCB+Ye8qFxzeca+Zj9hrzsOcdfmLGFj7uorviI1IBxhLrA+IJc7DGuLqCWLM+rpKfxB7kS4xVlmvEKuchzXN1TfE8NrXVXqI2I50krnA+olc4DyssZ7eIkfQz7X+pD6/c0/Wc5WfbcQY6MO/zv9ynY/6PotbVWtz/LM4F3j7qfl1FeejeafuqfLMzsdp3ok8as7KuU/8fXf+XtWB0bxW91R5Zuf7tC6JPGpPkHsL6du7+8NVnRztG+qeKs/sfjKt2yKP2nPUu33X/nN1jnh1PT/fU+WZ3a9m59rsnqbebaTznn56uqp0e6Rjnj54uqF0acRTD/8eLxTvRjj0+uv1XeEq3EttsG+YOGtpvN9amtpXed7xLBhp9SFnhlpCT5hrIy6UGLl38bd778lnNycP+/kNl/g9mWvRHoXvLPm19vHITbWfqD2n43vue438jfYQ7Lvkr/XxyH0139We0OkJ4Y21IprjiEOpD2sfj9qi5qOas51eEf5Zi6I5iLxQ+hPNr2i+qDnV6aGD+WiOqHmh5oLSf7n/OG+odfsTuJN3bA==AQAAAACAAABAAQAATgAAAA==eJwtxUkCgQAAAMBICtFqqUgb/v/DDmYuEwR/G28deufIe8dOfPDRJ6c+++LMuQuXrlz76pvvfrhx685Pv9z77cGjJ89e/PHXP69ObwMNAQAAAACAAABAAQAATwAAAA==eJwtxUkCgQAAAEAkhWi1VKQN/f+FDmYus179bRx469A7R46998FHJz757NSZcxcuXfniq2++u3bj1g8/3fnl3oNHT5799sdfL/4BaA8DNQ==AQAAAACAAABACwAAYwIAAA==eJwtxVeACAQAANCLUhmViIhkhjMOZ595hxvcGXfOdnfucPYeZ53tzh5NZVRWoZ1RlFEosveIIsosm8iH935e6YDHyrisA13O5V3BFR3kSq7sKg52VVdzdddwTddybYe4juu6nuu7gRs61GFu5MZu4nBHONJRbupmjnaMm7uFW7qVYx3n1o53G7d1O7d3B3d0J3d2ghOd5C5Odoq7upu7O9U93NO93Nt93Nf93N8DPNCDPNhDPNTDPNxpHuGRHuXRHuN0j/U4j/cET/QkT/YUZzjTUz3N0z3DMz3Lsz3Hcz3Pb/hNv+W3/Y7f9Xy/5/e9wAu9yIv9gT/0R17ipV7m5V7hj/2JV3qVV/tTf+bP/YW/9Ff+2t94jdd6ndf7W3/nDd7o7/2DN3mzt3irf/RP3ubt3uGf/Yt3epd/9W7v8V7v834f8EEf8mEf8VEf83Gf8Emf8m8+7TP+3X/4rM/5T5/3Bf/lv33Rl3zZV3zV1/yP//V13/BN3/Jt3/Fd3/N9/+cHfuj/HfCEnMVZ/aSfcjY/7Wf8rLM7h3M6l5/z837Buf2i8zivX3I+5/fLLuCCfsWFXNivuohfc1EXc3GXcEmX8usu7TIu60CXc3lXcEUHuZIru4qDXdXVXN01XNO1XNshruO6ruf6buCGDnWYG7mxmzjcEY50lJu6maMd4+Zu4ZZu5VjHubXj3cZt3c7t3cEd3cmdneBEJ7mLk53iru7m7k51D/d0L/d2H/d1P/f3AA/0IA/2EA/1MA93mkd4pEd5tMc43WM9zuM9wRM9yZM9xRnO9FRP83TP8Ew/AsczpT0=AQAAAACAAACgBQAASAEAAA==eJwtxVFEHAAAANCWJEnOSZKTnJPkJEmSJElOzjknyTlJkiRJMplkJklmZmZmZmaSJJlJkkmSZGZmZiZJkiRJJsnM9NF7Py87616Oc53nfBe40AEHXeRil7jUIZe53GFHXOFKVznqate41nWud4Mb3eRmt7jVbW53zB2OO+GkU+50l7uddsY97nWf+z3gQQ952CMe9ZjH/dATfuRJT/mxn3jaM571nJ/6mZ/7hV/6lV/7jd/6nd/7g+e94EUvedkr/uhPXvWa173hz970lre9413v+Yu/+pu/+4d/+pd/e98HPvSRj33iU5/53Be+9JX/+No3vvVf//N/Zz24L9s5znWe813gQgccdJGLXeJSh1zmcocdcYUrXeWoq13jWte53g1udJOb3eJWt7ndMXc47oSTTrnTXe522hn3uNd97veAB30Hy99Keg==AAAAAACAAAAAAAAAAAAAAACAAAAAAAAAAQAAAACAAAAgBwAAXwEAAA==eJxd0ldTFGEYRGFYQP8+SUmyZHYBlZyjiIASDGAgSlZQcgZBq/S8F569eaq7Z+abmtq8zIy/v3zMxTws0F6EhfhI/WPtFfgEi7FcOfZK9aXqK7TXaI/rqzCp+6qU476U3iupvlZ7tc6Pc0t0fZ36yPWY1jlJ9Um9d5Nytfq09gadl1Kf0n0Net+4r0x7o/pGvUeZnuPn+n9Qohzfr1TPa1IfOb5DMz7Dp+ojP8d2bMFW9W3aO7EDu9RH7sZe7MMe9f3ah3EAB9UPaX+BIziqPvJLnMBXOKY+8ji+xjc4qX5K+1ucxhn1s9rf4zv8oD7yHH7GjzivPvInXMBF/KJ+SftXXMYV9ava13ENN9RH3sRvuI1b6iPv4C7u4Xf1P7Qf4k/cV3+g/RiP8ER95FO8xHM8Ux/5Am/xGq/UR77B33iHv9RHvsesxD8zMSPxfx85gQ8xB7PVR36AfwCUq6InAQAAAACAAABgAgAApAAAAA==eJwtxdFmAgAAAMARI2JExIgRESMixhgxRsQYI2JEREREjDHGGBFjjIiIiBERMSJGjBERI6IP6aG7lwscHRw76JBPHHbEUZ865jPHnXDS50457YwvfOkrZ33tG+ec963vfO+Ci35wyWVXXHXNdTfc9KOf/OwXv/rNLbf97g9/uuOue+574KG/PPLYE0/97Znn/vHCv/7z0iuv/e+Nt955D+AVIks=\\n  </AppendedData>\\n</VTKFile>\\n", "color": [1.0, 0.800000011920929, 0.0, 1.0], "position": [0.0, 0.0, 0.0], "orientation": [0.0, -0.0, 0.0]}];
   render(data, parent_element);
   </script>
</div>
<div style="clear:both;">
</div>
```default
from cadquery.occ_impl.shapes import box

def makeCubes(self, length):
    # self refers to the CQ or Workplane object

    # inner method that creates a cube
    def _singleCube(loc):
        # loc is a location in local coordinates
        # since we're using eachpoint with useLocalCoordinates=True
        return box(length, length, length).locate(loc)

    # use CQ utility method to iterate over the stack, call our
    # method, and convert to/from local coordinates.
    return self.eachpoint(_singleCube, True)


# link the plugin into CadQuery
cq.Workplane.makeCubes = makeCubes

# use the plugin
result = (
    cq.Workplane("XY")
    .box(6.0, 8.0, 0.5)
    .faces(">Z")
    .rect(4.0, 4.0, forConstruction=True)
    .vertices()
    .makeCubes(1.0)
    .combineSolids()
)
```

## Extending CadQuery: Special Methods

The above-mentioned approach has one drawback, it requires monkey-patching or subclassing. To avoid this
one can also use the following special methods of [`cadquery.Workplane`](classreference.md#cadquery.Workplane) and [`cadquery.Sketch`](classreference.md#cadquery.Sketch)
and write plugins in a more functional style.

> * [`cadquery.Workplane.map()`](classreference.md#cadquery.Workplane.map)
> * [`cadquery.Workplane.apply()`](classreference.md#cadquery.Workplane.apply)
> * [`cadquery.Workplane.invoke()`](classreference.md#cadquery.Workplane.invoke)
> * [`cadquery.Sketch.map()`](classreference.md#cadquery.Sketch.map)
> * [`cadquery.Sketch.apply()`](classreference.md#cadquery.Sketch.apply)
> * [`cadquery.Sketch.invoke()`](classreference.md#cadquery.Sketch.invoke)

Here is the same plugin rewritten using one of those methods.

<div class="cq-vtk"
 style="text-align:left;float:left;border: 1px solid #ddd; width:100%; height:500px">
   <script>
   var parent_element = document.currentScript.parentNode;
   var data = [{"shape": "<?xml version=\\"1.0\\"?>\\n<VTKFile type=\\"PolyData\\" version=\\"0.1\\" byte_order=\\"LittleEndian\\" header_type=\\"UInt32\\" compressor=\\"vtkZLibDataCompressor\\">\\n  <PolyData>\\n    <Piece NumberOfPoints=\\"520\\"                  NumberOfVerts=\\"40\\"                   NumberOfLines=\\"180\\"                  NumberOfStrips=\\"0\\"                    NumberOfPolys=\\"76\\"                  >\\n      <PointData Normals=\\"Normals\\">\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"0\\"                    RangeMax=\\"1\\"                    offset=\\"0\\"                   />\\n      </PointData>\\n      <CellData Normals=\\"Normals\\">\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"SUBSHAPE_IDS\\" format=\\"appended\\" RangeMin=\\"5\\"                    RangeMax=\\"159\\"                  offset=\\"120\\"                 />\\n        <DataArray type=\\"Int64\\" IdType=\\"1\\" Name=\\"MESH_TYPES\\" format=\\"appended\\" RangeMin=\\"2\\"                    RangeMax=\\"7\\"                    offset=\\"524\\"                 />\\n        <DataArray type=\\"Float32\\" Name=\\"Normals\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"1\\"                    RangeMax=\\"1\\"                    offset=\\"596\\"                 />\\n      </CellData>\\n      <Points>\\n        <DataArray type=\\"Float32\\" Name=\\"Points\\" NumberOfComponents=\\"3\\" format=\\"appended\\" RangeMin=\\"2.1360009363\\"         RangeMax=\\"5.0062460986\\"         offset=\\"744\\"                 />\\n      </Points>\\n      <Verts>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1612\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1740\\"                />\\n      </Verts>\\n      <Lines>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"1872\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"2712\\"                />\\n      </Lines>\\n      <Strips>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"3176\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"3192\\"                />\\n      </Strips>\\n      <Polys>\\n        <DataArray type=\\"Int64\\" Name=\\"connectivity\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"3208\\"                />\\n        <DataArray type=\\"Int64\\" Name=\\"offsets\\" format=\\"appended\\" RangeMin=\\"\\"                     RangeMax=\\"\\"                     offset=\\"3700\\"                />\\n      </Polys>\\n    </Piece>\\n  </PolyData>\\n  <AppendedData encoding=\\"base64\\">\\n   \_AQAAAACAAABgGAAARgAAAA==eJzt0cEJACAMBDA3czU3czXBCWxFKJi8zkfhbFsDAAAAgMrGjOX0TP8nR+f2+3Cn4U6P75v6a2SX+ut/0T87UyMvthhviQ==AQAAAACAAABACQAAHQEAAA==eJzN01crKAAAhmE3wrFyjJB9smXLpoNIZkZGZGZkRGZGRnQ4Rw4ZkeSvuvDev1fiu3n+wPcGB3wsBEMxHH9iDCZgMqZgGmZgFmZjLuZjERZjKZZjFVZjLdZjE3ZiN/bjME7iNM7jMm7iNu7jMV7gX/yP9xiEPzAMIzAKozEW4zERkzAV0/EXZmIO5mEBFmIJlmEFVmIN1mED/sZmbMUO7MIe7MMBHMIRHMMJnMIZnMMFXMIVXMMN3MId3MMDPMITPMM/eIn/8Bpv8A4f8AkDxUgx7pvbKLaIbWK72CsOiqPiuDgrLoqr4rq4Kx6Kp+K5eCXeio/is/givopvovX61f19ds/Wq/VovVlP1ov1YH+3P9tf7Y/2t3c8XF6LAQAAAACAAABACQAAIwAAAA==eJxjYoAAplGaLJp1lB6lR+lRepQelDT7KD1K05AGAIi5Bek=AQAAAACAAADgDQAAXAAAAA==eJxjYGiwZ4CDUfYoe5Q9yh5lj7JH2aPsUfYom2T2fjR2AxRjk2NAksNndgMRbFL1Qu3GYFNqJrX0NhA2E5cZYD5aWOO0g8T4wmUOLveMmo/ffJxpgCriABFk+tk=AQAAAACAAABgGAAAdwIAAA==eJztVsFtwzAM1CiZJOJoHSWT2B6tTWBJ5xOPsuICbYE+AhAMRcri3ZEp2ZbSx/N3T81edtvAb7vfIMbgrLX425dvW5t922OePrRLzJaPdom52dE+5MRaGXKCXWJeOcEuMa+cYJeY+i1Lu/8jt+965PYtxa7+DP7c/OVbil39+/2L/fyv5sxQyyBnhloGOTPU2v1dT7nX96DX7GdsLOT3sME4wbrs5/fnGMJYxcZJvHnYw7OMyRp/Ep8eVvEsY7hi7ySePWzjWcZ8jT+Jf48LePbAEdaEyL47eCB+Ye8qFxzeca+Zj9hrzsOcdfmLGFj7uorviI1IBxhLrA+IJc7DGuLqCWLM+rpKfxB7kS4xVlmvEKuchzXN1TfE8NrXVXqI2I50krnA+olc4DyssZ7eIkfQz7X+pD6/c0/Wc5WfbcQY6MO/zv9ynY/6PotbVWtz/LM4F3j7qfl1FeejeafuqfLMzsdp3ok8as7KuU/8fXf+XtWB0bxW91R5Zuf7tC6JPGpPkHsL6du7+8NVnRztG+qeKs/sfjKt2yKP2nPUu33X/nN1jnh1PT/fU+WZ3a9m59rsnqbebaTznn56uqp0e6Rjnj54uqF0acRTD/8eLxTvRjj0+uv1XeEq3EttsG+YOGtpvN9amtpXed7xLBhp9SFnhlpCT5hrIy6UGLl38bd778lnNycP+/kNl/g9mWvRHoXvLPm19vHITbWfqD2n43vue438jfYQ7Lvkr/XxyH0139We0OkJ4Y21IprjiEOpD2sfj9qi5qOas51eEf5Zi6I5iLxQ+hPNr2i+qDnV6aGD+WiOqHmh5oLSf7n/OG+odfsTuJN3bA==AQAAAACAAABAAQAATgAAAA==eJwtxUkCgQAAAMBICtFqqUgb/v/DDmYuEwR/G28deufIe8dOfPDRJ6c+++LMuQuXrlz76pvvfrhx685Pv9z77cGjJ89e/PHXP69ObwMNAQAAAACAAABAAQAATwAAAA==eJwtxUkCgQAAAEAkhWi1VKQN/f+FDmYus179bRx469A7R46998FHJz757NSZcxcuXfniq2++u3bj1g8/3fnl3oNHT5799sdfL/4BaA8DNQ==AQAAAACAAABACwAAYwIAAA==eJwtxVeACAQAANCLUhmViIhkhjMOZ595hxvcGXfOdnfucPYeZ53tzh5NZVRWoZ1RlFEosveIIsosm8iH935e6YDHyrisA13O5V3BFR3kSq7sKg52VVdzdddwTddybYe4juu6nuu7gRs61GFu5MZu4nBHONJRbupmjnaMm7uFW7qVYx3n1o53G7d1O7d3B3d0J3d2ghOd5C5Odoq7upu7O9U93NO93Nt93Nf93N8DPNCDPNhDPNTDPNxpHuGRHuXRHuN0j/U4j/cET/QkT/YUZzjTUz3N0z3DMz3Lsz3Hcz3Pb/hNv+W3/Y7f9Xy/5/e9wAu9yIv9gT/0R17ipV7m5V7hj/2JV3qVV/tTf+bP/YW/9Ff+2t94jdd6ndf7W3/nDd7o7/2DN3mzt3irf/RP3ubt3uGf/Yt3epd/9W7v8V7v834f8EEf8mEf8VEf83Gf8Emf8m8+7TP+3X/4rM/5T5/3Bf/lv33Rl3zZV3zV1/yP//V13/BN3/Jt3/Fd3/N9/+cHfuj/HfCEnMVZ/aSfcjY/7Wf8rLM7h3M6l5/z837Buf2i8zivX3I+5/fLLuCCfsWFXNivuohfc1EXc3GXcEmX8usu7TIu60CXc3lXcEUHuZIru4qDXdXVXN01XNO1XNshruO6ruf6buCGDnWYG7mxmzjcEY50lJu6maMd4+Zu4ZZu5VjHubXj3cZt3c7t3cEd3cmdneBEJ7mLk53iru7m7k51D/d0L/d2H/d1P/f3AA/0IA/2EA/1MA93mkd4pEd5tMc43WM9zuM9wRM9yZM9xRnO9FRP83TP8Ew/AsczpT0=AQAAAACAAACgBQAASAEAAA==eJwtxVFEHAAAANCWJEnOSZKTnJPkJEmSJElOzjknyTlJkiRJMplkJklmZmZmZmaSJJlJkkmSZGZmZiZJkiRJJsnM9NF7Py87616Oc53nfBe40AEHXeRil7jUIZe53GFHXOFKVznqate41nWud4Mb3eRmt7jVbW53zB2OO+GkU+50l7uddsY97nWf+z3gQQ952CMe9ZjH/dATfuRJT/mxn3jaM571nJ/6mZ/7hV/6lV/7jd/6nd/7g+e94EUvedkr/uhPXvWa173hz970lre9413v+Yu/+pu/+4d/+pd/e98HPvSRj33iU5/53Be+9JX/+No3vvVf//N/Zz24L9s5znWe813gQgccdJGLXeJSh1zmcocdcYUrXeWoq13jWte53g1udJOb3eJWt7ndMXc47oSTTrnTXe522hn3uNd97veAB30Hy99Keg==AAAAAACAAAAAAAAAAAAAAACAAAAAAAAAAQAAAACAAAAgBwAAXwEAAA==eJxd0ldTFGEYRGFYQP8+SUmyZHYBlZyjiIASDGAgSlZQcgZBq/S8F569eaq7Z+abmtq8zIy/v3zMxTws0F6EhfhI/WPtFfgEi7FcOfZK9aXqK7TXaI/rqzCp+6qU476U3iupvlZ7tc6Pc0t0fZ36yPWY1jlJ9Um9d5Nytfq09gadl1Kf0n0Net+4r0x7o/pGvUeZnuPn+n9Qohzfr1TPa1IfOb5DMz7Dp+ojP8d2bMFW9W3aO7EDu9RH7sZe7MMe9f3ah3EAB9UPaX+BIziqPvJLnMBXOKY+8ji+xjc4qX5K+1ucxhn1s9rf4zv8oD7yHH7GjzivPvInXMBF/KJ+SftXXMYV9ava13ENN9RH3sRvuI1b6iPv4C7u4Xf1P7Qf4k/cV3+g/RiP8ER95FO8xHM8Ux/5Am/xGq/UR77B33iHv9RHvsesxD8zMSPxfx85gQ8xB7PVR36AfwCUq6InAQAAAACAAABgAgAApAAAAA==eJwtxdFmAgAAAMARI2JExIgRESMixhgxRsQYI2JEREREjDHGGBFjjIiIiBERMSJGjBERI6IP6aG7lwscHRw76JBPHHbEUZ865jPHnXDS50457YwvfOkrZ33tG+ec963vfO+Ci35wyWVXXHXNdTfc9KOf/OwXv/rNLbf97g9/uuOue+574KG/PPLYE0/97Znn/vHCv/7z0iuv/e+Nt955D+AVIks=\\n  </AppendedData>\\n</VTKFile>\\n", "color": [1.0, 0.800000011920929, 0.0, 1.0], "position": [0.0, 0.0, 0.0], "orientation": [0.0, -0.0, 0.0]}];
   render(data, parent_element);
   </script>
</div>
<div style="clear:both;">
</div>
```default
from cadquery.occ_impl.shapes import box

def makeCubes(length):

    # inner method that creates the cubes
    def callback(wp):

        return wp.eachpoint(box(length, length, length), True)

    return callback

# use the plugin
result = (
    cq.Workplane("XY")
    .box(6.0, 8.0, 0.5)
    .faces(">Z")
    .rect(4.0, 4.0, forConstruction=True)
    .vertices()
    .invoke(makeCubes(1.0))
    .combineSolids()
)
```

Such an approach is more friendly for auto-completion and static analysis tools.
