import numpy as np
class point():
    x = 0
    y = 0
    z = 0
    def __init__(self, coords: tuple) -> None:
        if len(coords) != 3 :
            raise Exception("point construction requires 3 coordinates (X,Y,Z)")
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.z}"
    
    def to_np_array(self):
        return np.array([self.x, self.y, self.z])

class triangle():
    a: point
    b: point
    c: point
    def __init__(self, points: tuple) -> None:
        if len(points) != 3 :
            raise Exception("triangles requires exactly 3 sides")
        self.a: point = points[0]
        self.b: point = points[1]
        self.c: point = points[2]
    
        x = np.array([
            [self.a.x, self.a.y, self.a.z],
            [self.b.x, self.b.y, self.b.z],
            [self.c.x, self.c.y, self.c.z]
        ])
        if np.linalg.det(x) < 0: # if 0 might be bad??
            temp: point = self.b
            self.b = self.c
            self.c = temp

        # norm = point(self.compute_normal()).to_np_array()

        # # if the dot product is positive it is clockwise
        # # the order should be counter-clockwise, though
        # # since its viewed from 0,0,0 inside the model
        # # all orderings should be made to be clockwise
        # dot = norm.dot(self.a.to_np_array() - point((0,0,0)).to_np_array()) 
        # print(dot)
        # if dot < 0:
        #     temp: point = self.b
        #     self.b = self.c
        #     self.c = temp

    def compute_normal(self) -> tuple:
        N = np.cross(
            self.b.to_np_array() - self.a.to_np_array(),
            self.c.to_np_array() - self.a.to_np_array()
        )
        return N / N.sum()

class solid():
    triangles: list[triangle] = []
    def __init__(self, triangles: list[triangle]) -> None:
        self.triangles = triangles

    def save_ascii(self, solidname: str, filename: str):
        with open(filename, "w") as f:
            f.write(f"solid {solidname}\n")
            for tri in self.triangles:
                normals = tri.compute_normal()
                f.write(f"\tfacet normal {normals[0]} {normals[1]} {normals[2]}\n")
                f.write("\touter loop\n")
                f.write(f"\t\tvertex {str(tri.a)}\n")
                f.write(f"\t\tvertex {str(tri.b)}\n")
                f.write(f"\t\tvertex {str(tri.c)}\n")
                f.write("\tendloop\n")
            f.write(f"endsolid {solidname}\n")


my_obj: solid = solid([
    triangle((
        point((-5,-5,-5)),
        point((-5,-5,25)),
        point((-5,25,25))
    )),
    triangle((
        point((-5,-5,-5)),
        point((-5,25,-5)),
        point((-5,25,25))
    )),
    triangle((
        point((-5,25,-5)),
        point((-5,25,25)),
        point((25,25,25))
    )),
    triangle((
        point((-5,25,-5)),
        point((25,25,-5)),
        point((25,25,25))
    )),
    triangle((
        point((-5,-5,-5)),
        point((-5,25,-5)),
        point((25,25,-5))
    )),
    triangle((
        point((-5,-5,-5)),
        point((25,-5,-5)),
        point((25,25,-5))
    )),
    triangle((
        point((-5,-5,-5)),
        point((25,-5,-5)),
        point((25,-5,25))
    )),
    triangle((
        point((-5,-5,-5)),
        point((-5,-5,25)),
        point((25,-5,25))
    )),
    triangle((
        point((25,25,-5)),
        point((25,-5,-5)),
        point((25,-5,25))
    )),
    triangle((
        point((25,-5,25)),
        point((25,25,-5)),
        point((25,25,25))
    )),
    triangle((
        point((-5,-5,25)),
        point((25,-5,25)),
        point((-5,25,25))
    )),
    triangle((
        point((25,-5,25)),
        point((-5,25,25)),
        point((25,25,25))
    ))
])

my_obj.save_ascii(solidname="test_cube", filename="./my_obj.stl")