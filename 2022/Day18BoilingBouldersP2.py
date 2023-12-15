import numpy as np
import matplotlib.pyplot as plt
import sys

def calc_surface_area(points):
    points_set = set(points)
    neighbors = [[False, False, False, False, False, False] for i in range(len(points))]
    surface_area = 6 * len(points)
    points_np = np.array(points)
    if points:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(xs=points_np[:,0], ys=points_np[:,1], zs=points_np[:,2])
        plt.show()
    for point in points:
        p_neighbors = [(point[0]+1, point[1], point[2]),
                       (point[0], point[1]+1, point[2]),
                       (point[0], point[1], point[2]+1),
                       (point[0], point[1], point[2]-1),
                       (point[0], point[1]-1, point[2]),
                       (point[0]-1, point[1], point[2])]
        neighbors_set = points_set & (set(p_neighbors))
        for i, v in enumerate(p_neighbors):
            if v in neighbors_set:
                if not neighbors[points.index(v)][5-i]:
                    neighbors[points.index(point)][i] = True
                    neighbors[points.index(v)][5-i] = True
                    surface_area -= 2
    return surface_area

def calc_negative_space(points):
    xy_cross_rows = set([(x[0], x[1]) for x in points])
    xz_cross_rows = set([(x[0], x[2]) for x in points])
    yz_cross_rows = set([(x[1], x[2]) for x in points])

    xy_holes = set()
    xz_holes = set()
    yz_holes = set()

    for row in xy_cross_rows:
        row_points = [x[2] for x in points if x[0] == row[0] and x[1] == row[1]]
        if row_points:
            z_min = min(row_points)
            z_max = max(row_points)
            xy_holes.update(set([(row[0], row[1], i) for i in set(range(z_min, z_max)) - set(row_points)]))
    for row in xz_cross_rows:
        row_points = [x[1] for x in points if x[0] == row[0] and x[2] == row[1]]
        if row_points:
            y_min = min(row_points)
            y_max = max(row_points)
            xz_holes.update(set([(row[0], i, row[1]) for i in set(range(y_min, y_max)) - set(row_points)]))
    for row in yz_cross_rows:
        row_points = [x[0] for x in points if x[1] == row[0] and x[2] == row[1]]
        if row_points:
            x_min = min(row_points)
            x_max = max(row_points)
            yz_holes.update(set([(i, row[0], row[1]) for i in set(range(x_min, x_max)) - set(row_points)]))
    
    all_holes = xy_holes & xz_holes & yz_holes
    all_open = (xy_holes | xz_holes | yz_holes) - all_holes
    all_holes = remove_open(all_holes, all_open, set(points))
    return list(all_holes)

#Flood fill algorithm
def remove_open(holes, open, points):
    visited = set()
    temp_holes = holes
    while visited & temp_holes != temp_holes:
        holes_list = list(holes - visited)
        fill = flood_fill(holes_list[0], points, open, set())
        if -1 in fill:
            holes = holes - fill
        visited = visited | fill - {-1}
    return holes

                                  
def flood_fill(point, rock, open, visited):
    if point in visited:
        return visited
    if point in rock:
        return visited - {point}
    visited = visited | {point}
    if point in open:
        return (visited | {-1}) - {point}
    p_neighbors = {(point[0]+1, point[1], point[2]),
                   (point[0], point[1]+1, point[2]),
                   (point[0], point[1], point[2]+1),
                   (point[0], point[1], point[2]-1),
                   (point[0], point[1]-1, point[2]),
                   (point[0]-1, point[1], point[2])}
    for neighbor in p_neighbors:
        visited = visited | flood_fill(neighbor, rock, open, visited)
    return visited
    
file = sys.argv[1]

points = list()

with open(f"./{file}") as f:
    for line in f:
        points.append(eval(f"({line})"))
            
surface_area = calc_surface_area(points) - calc_surface_area(calc_negative_space(points))

print(surface_area)