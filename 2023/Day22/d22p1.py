#A brick can be disintegrated if any brick it supports is supported by at least one other brick.
#This can be determined by creating a directed graph of which bricks are supported by other bricks.
#A brick is at rest if its lowest point's Z coordinate is 1, or if its Z-coordinate is one greater than a brick at rest.
#AND its X, Y coordinates overlap with said brick.
#The bricks need to be sorted from lowest to highest somehow.

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
from random import random

def gen_voxels(bricks, volume):
    fig = plt.figure()
    b = fig.add_subplot(projection='3d')
    ax = fig.gca()
    b.set_xticks(range(volume[0]+1))
    b.set_yticks(range(volume[1]+1))
    for brick in bricks:
        start, end, dummy = brick
        voxel_coords = np.zeros(volume, dtype=bool)
        color = colors.to_rgba((random(), random(), random()))
        voxel_coords[start[0]:end[0]+1, start[1]:end[1]+1, start[2]:end[2]+1] = True
        b.voxels(voxel_coords, facecolors=color)
    plt.show()

with open("Day22Input.txt") as f:
    bricks = [[eval("["+p+"]")for p in line.split("~")] + [False] for line in f.readlines()]
bricks.sort(key=lambda x: x[0][2])
#Adjacency matrix: (row, column) indicates if row supports column
brick_supports = [[False for x in range(len(bricks))] for y in range(len(bricks))]

all_edge_points = [j for i in [b[:2] for b in bricks] for j in i]
x_size = max([p[0] for p in all_edge_points])+1
y_size = max([p[1] for p in all_edge_points])+1
z_size = max([p[2] for p in all_edge_points])+1
volume = (x_size, y_size, z_size)
counter = 0
while not all([b[2] for b in bricks]):
    #See if a brick has landed
    for i, brick in [x for x in enumerate(bricks) if not x[1][2]]:
        if brick[0][2] == 1:
            brick[2] = True
    for i, brick in [x for x in enumerate(bricks) if not x[1][2]]:       
        for j, resting in [x for x in enumerate(bricks) if x[1][2]]:
            if not (brick[0][0] > resting[1][0] or resting[0][0] > brick[1][0]) and \
                not (brick[0][1] > resting[1][1] or resting[0][1] > brick[1][1]) and \
                brick[0][2] == resting[1][2] + 1:
                brick[2] = True
                brick_supports[j][i] = True
                #print(i, brick, j, resting)
    for i, brick in [x for x in enumerate(bricks) if not x[1][2]]:
        bricks[i][0][2] -= 1
        bricks[i][1][2] -= 1
    counter += 1
#[print(index, brick) for index, brick in enumerate(bricks)]
#Use adjacency matrix to identify which bricks support other bricks once all have fallen
#[print(row) for row in brick_supports]
can_disintegrate = list()
for row_num, supporter in enumerate(brick_supports):
    for col_num, supporting in enumerate(supporter):
        if supporting:
            if not any([row[col_num] for index, row in enumerate(brick_supports) if index != row_num]):
                break
    else:
        can_disintegrate.append(row_num)

print(len(can_disintegrate))

#Bonus visulalization in matplotlib
#gen_voxels(bricks, volume)
