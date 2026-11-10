
"""Generate a thin 3D diamond-shaped flat-plate wing as an ASCII STL."""

import math
from pathlib import Path

# Original square plate dimensions (metres)
SIDE = 0.99
THICKNESS = 0.010

# Diagonal length of the square, used as the wing chord and span
D = SIDE * math.sqrt(2.0)

# Diamond planform vertices: leading edge, upper tip,
# trailing edge, lower tip
LE = (0.0, 0.0)
UPPER = (D / 2.0, D / 2.0)
TE = (D, 0.0)
LOWER = (D / 2.0, -D / 2.0)

CENTER = (D / 2.0, 0.0)
Z0 = -THICKNESS / 2.0
Z1 = THICKNESS / 2.0

def normal(a, b, c):
    """Calculate a unit normal for one triangle."""
    u = [b[i] - a[i] for i in range(3)]
    v = [c[i] - a[i] for i in range(3)]
    n = (
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    )
    length = math.sqrt(sum(value * value for value in n))
    if length == 0:
        return (0.0, 0.0, 0.0)
    return tuple(value / length for value in n)

def write_triangle(file, a, b, c):
    n = normal(a, b, c)
    file.write(f"  facet normal {n[0]} {n[1]} {n[2]}\n")
    file.write("    outer loop\n")
    for p in (a, b, c):
        file.write(f"      vertex {p[0]} {p[1]} {p[2]}\n")
    file.write("    endloop\n")
    file.write("  endfacet\n")

def main():
    vertices = [LE, UPPER, TE, LOWER]
    center = CENTER
    triangles = []

    # Top and bottom surfaces
    for i in range(4):
        a = vertices[i]
        b = vertices[(i + 1) % 4]
        triangles.append((
            (center[0], center[1], Z1),
            (a[0], a[1], Z1),
            (b[0], b[1], Z1),
        ))
        triangles.append((
            (center[0], center[1], Z0),
            (b[0], b[1], Z0),
            (a[0], a[1], Z0),
        ))

    # Four side walls
    for i in range(4):
        a = vertices[i]
        b = vertices[(i + 1) % 4]
        a0 = (a[0], a[1], Z0)
        b0 = (b[0], b[1], Z0)
        a1 = (a[0], a[1], Z1)
        b1 = (b[0], b[1], Z1)
        triangles.append((a0, b0, b1))
        triangles.append((a0, b1, a1))

    output = Path(__file__).resolve().parent / "diamond_wing.stl"

    with output.open("w") as file:
        file.write("solid diamond_wing\n")
        for triangle in triangles:
            write_triangle(file, *triangle)
        file.write("endsolid diamond_wing\n")

    print(f"Created: {output}")
    print(f"Diagonal chord/span: {D:.4f} m")
    print(f"Plate thickness: {THICKNESS:.4f} m")
    print(f"Triangles: {len(triangles)}")

if __name__ == "__main__":
    main()
