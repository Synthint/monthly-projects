
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
        return f"{self.x}, {self.y}, {self.z}"

class triangle():
    a: point
    b: point
    c: point
    def __init__(self, points: tuple) -> None:
        if len(points) != 3 :
            raise Exception("triangles requires exactly 3 sides")
        self.a = points[0]
        self.b = points[1]
        self.c = points[2]

    def compute_normal(self) -> tuple:
        Nx = (self.a.y * self.b.z) - (self.a.z * self.b.y)
        Ny = (self.a.z * self.b.x) - (self.a.x * self.b.z)
        Nz = (self.a.x * self.b.y) - (self.a.y * self.b.x)
        return (Nx,Ny,Nz)

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
        point((0,0,0)),
        point((0,10,0)),
        point((10,10,10))
    ))
    ])

my_obj.save_ascii(solidname="hello", filename="./my_obj.stl")