import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt
from sympy import solve, symbols

hailstones = list()
x, y, z, v, u, w, q, r, s = symbols("x, y, z, v, u, w, q, r, s")

with open("Day24Input.txt") as f:
    for line in f.readlines():
        line = line.split()
        position = [int(x) for x in "".join(line[:3]).split(",")]
        velocity = [int(x) for x in "".join(line[4:]).split(",")]
        hailstones.append([position, velocity])

solutions = set()
hailstone_trios = combinations(hailstones, 3)
for trio in hailstone_trios:
    x1 = trio[0][0][0]
    vx1 = trio[0][1][0]
    y1 = trio[0][0][1]
    vy1 = trio[0][1][1]
    z1 = trio[0][0][2]
    vz1 = trio[0][1][2]
    x2 = trio[0][0][0]
    vx2 = trio[0][1][0]
    y2 = trio[0][0][1]
    vy2 = trio[0][1][1]
    z2 = trio[0][0][2]
    vz2 = trio[0][1][2]
    x3 = trio[0][0][0]
    vx3 = trio[0][1][0]
    y3 = trio[0][0][1]
    vy3 = trio[0][1][1]
    z3 = trio[0][0][2]
    vz3 = trio[0][1][2]

    system = [x+q*(v-trio[0][1][0])-trio[0][0][0],
              y+q*(u-trio[0][1][1])-trio[0][0][1],
              z+q*(w-trio[0][1][2])-trio[0][0][2],
              x+r*(v-trio[1][1][0])-trio[1][0][0],
              y+r*(u-trio[1][1][1])-trio[1][0][1],
              z+r*(w-trio[1][1][2])-trio[1][0][2],
              x+s*(v-trio[2][1][0])-trio[2][0][0],
              y+s*(u-trio[2][1][1])-trio[2][0][1],
              z+s*(w-trio[2][1][2])-trio[2][0][2]]
    solution = solve(system, x, y, z, v, u, w, q, r, s, dict=True)[0]
    print(solution[x]+solution[y]+solution[z])
    break
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# for point_on_line, vector in hailstones:
#     points = np.zeros((3, 0))
#     for i in np.arange(0, 15, 1):
#         points = np.concatenate((points, point_on_line + i * vector), axis=1)
#     ax.scatter(*point_on_line, "r")
#     ax.scatter(points[0, :].ravel(), points[1, :].ravel(),points[2, :].ravel(),s=1)
    
# plt.show()

        

