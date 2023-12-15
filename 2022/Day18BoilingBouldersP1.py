
import sys
import numpy as np
import matplotlib.pyplot as plt

file = sys.argv[1]

points = list()

with open(f"./{file}") as f:
    for line in f:
        points.append(eval(f"({line})"))

points.sort(key=lambda x: x[0])
points_set = set(points)

neighbors = [[False, False, False, False, False, False] for i in range(len(points))]
#points_np = np.array(points)
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.scatter(xs=points_np[:,0], ys=points_np[:,1], zs=points_np[:,2])
# plt.show()
# plt.savefig("obsidian.png")
            
surface_area = 6 * len(points)

for point in points:
    p_neighbors = [(point[0]+1, point[1], point[2]),
                   (point[0], point[1]+1, point[2]),
                   (point[0], point[1], point[2]+1),
                   (point[0], point[1], point[2]-1),
                   (point[0], point[1]-1, point[2]),
                   (point[0]-1, point[1], point[2])]
    neighbors_set = points_set.intersection(set(p_neighbors))
    for i, v in enumerate(p_neighbors):
        if v in neighbors_set:
            if not neighbors[points.index(v)][5-i]:
                neighbors[points.index(point)][i] = True
                neighbors[points.index(v)][5-i] = True
                surface_area -= 2

print(surface_area)
#Or maybe do x, y, z axis passes?