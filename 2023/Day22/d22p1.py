#A brick can be disintegrated if any brick it supports is supported by at least one other brick.
#This can be determined by creating a two-way directed graph of which bricks are supported by other bricks.
#A brick is at rest if its lowest point's Z coordinate is 1, or if its Z-coordinate is one greater than a brick at rest.
#AND its X, Y coordinates overlap with said brick.

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D

def gen_voxels(bricks, volume):
    voxel_coords = np.zeros(volume, dtype=bool)
    for brick in bricks:
        start, end, dummy = brick
        voxel_coords[start[0]:end[0]+1, start[1]:end[1]+1, start[2]:end[2]+1] = True
    return voxel_coords

with open("Day22Input.txt") as f:
    bricks = [[eval("["+p+"]")for p in line.split("~")] + [False] for line in f.readlines()]
#Row, column indicates row supports column
brick_supports = [[False for x in range(len(bricks))] for y in range(len(bricks))]

while not all([b[2] for b in bricks]):
    #See if a brick has landed
    for i, brick in enumerate(bricks):
        if brick[2]:
            continue
        if brick[0][2] == 1:
            brick[2] = True
        else:
            for j, resting in [x for x in enumerate(bricks) if x[1][2]]:
                if brick[0][0] > resting[1][0] or resting[0][0] > brick[1][0]:
                    continue
                if brick[0][1] > resting[1][1] or resting[0][1] > brick[1][1]:
                    continue
                if brick[0][2] != resting[1][2] + 1:
                    continue
                brick[2] = True
                print(j, resting, i, brick)
                brick_supports[j][i] = True
    #Make bricks fall
    for i, brick in [x for x in enumerate(bricks) if not x[1][2]]:
        bricks[i][0][2] -= 1
        bricks[i][1][2] -= 1
print(bricks)
can_disintegrate = list()
# [print(line) for line in brick_supports]
for row_num, supporter in enumerate(brick_supports):
    for col_num, supporting in enumerate(supporter):
        if supporting:
            if not any([row[col_num] for index, row in enumerate(brick_supports) if index != row_num]):
                break
    else:
        can_disintegrate.append(row_num)

print(can_disintegrate)

voxel_bricks = list()
all_edge_points = [j for i in [b[:2] for b in bricks] for j in i]
x_size = max([p[0] for p in all_edge_points])+1
y_size = max([p[1] for p in all_edge_points])+1
z_size = max([p[2] for p in all_edge_points])+1
volume = (x_size, y_size, z_size)

voxel_bricks = gen_voxels(bricks, volume)
fig = plt.figure()
b = fig.add_subplot(projection='3d')
ax = fig.gca()
b.set_xticks(range(x_size+1))
b.set_yticks(range(y_size+1))
b.voxels(voxel_bricks)
plt.show()