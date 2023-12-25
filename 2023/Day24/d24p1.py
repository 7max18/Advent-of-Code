import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

MIN_COORD = 200000000000000
MAX_COORD = 400000000000000

def check_for_future(hailstone, intersection):
    if intersection[0] < hailstone[0][0] and intersection[1] < hailstone[0][1] \
        and hailstone[1][0] < 0 and hailstone[1][1] < 0:
        return True
    elif intersection[0] < hailstone[0][0] and intersection[1] > hailstone[0][1] \
        and hailstone[1][0] < 0 and hailstone[1][1] > 0:
        return True
    elif intersection[0] > hailstone[0][0] and intersection[1] < hailstone[0][1] \
        and hailstone[1][0] > 0 and hailstone[1][1] < 0:
        return True
    elif intersection[0] > hailstone[0][0] and intersection[1] > hailstone[0][1] \
        and hailstone[1][0] > 0 and hailstone[1][1] > 0:
        return True

            
hailstones = list()

with open("Day24Input.txt") as f:
    for line in f.readlines():
        line = line.split()
        position = [int(x) for x in "".join(line[:3]).split(",")]
        velocity = [int(x) for x in "".join(line[4:]).split(",")]
        x_coeff = velocity[1]
        y_coeff = -velocity[0]
        dependent = position[0]*velocity[1]-position[1]*velocity[0]
        hailstones.append([position, velocity, [[x_coeff, y_coeff], dependent]])

crossing_paths = 0
hailstone_pairs = combinations(hailstones, 2)
for pair in hailstone_pairs:
    A = [pair[0][2][0], pair[1][2][0]]
    B = [pair[0][2][1], pair[1][2][1]]
    if np.linalg.det(A) != 0:
        intersection = np.linalg.solve(A, B)
        if MIN_COORD <= intersection[0] <= MAX_COORD and MIN_COORD <= intersection[1] <= MAX_COORD \
            and check_for_future(pair[0], intersection) and check_for_future(pair[1], intersection):
            crossing_paths += 1

print(crossing_paths)


    
