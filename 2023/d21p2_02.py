from math import trunc, isclose
from numpy import polyfit, poly1d

TOTAL_STEPS = 26501365

def wrapped_pos(position, grid):
    return grid[position[0]-len(grid)*trunc(position[0]/len(grid))][position[1]-len(grid[0])*trunc(position[1]/len(grid[0]))]

def get_steps(current: set, even_parity, step_range):
    visited = current.copy()
    results = list()
    for i in range(step_range):
        if even_parity:
            results.append((i*2, len(visited)))
        else:
            results.append(((i*2)+1, len(visited)))
        next_steps = set()
        for point in current:
            north_two = (point[0]-2, point[1])
            south_two = (point[0]+2, point[1])
            west_two = (point[0], point[1]-2)
            east_two = (point[0], point[1]+2)
            northwest = (point[0]-1, point[1]-1)
            northeast = (point[0]-1, point[1]+1)
            southwest = (point[0]+1, point[1]-1)
            southeast = (point[0]+1, point[1]+1)
            north_one = (point[0]-1, point[1])
            south_one = (point[0]+1, point[1])
            west_one = (point[0], point[1]-1)
            east_one = (point[0], point[1]+1)
            north_one_wrapped = wrapped_pos(north_one, gardens)
            south_one_wrapped = wrapped_pos(south_one, gardens)
            west_one_wrapped = wrapped_pos(west_one, gardens)
            east_one_wrapped = wrapped_pos(east_one, gardens)
            if wrapped_pos(north_two, gardens) != "#" and north_one_wrapped != "#":
                next_steps.add(north_two)
            if wrapped_pos(south_two, gardens) != "#" and south_one_wrapped != "#":
                next_steps.add(south_two)
            if wrapped_pos(west_two, gardens) != "#" and west_one_wrapped != "#":
                next_steps.add(west_two)
            if wrapped_pos(east_two, gardens) != "#" and east_one_wrapped != "#":
                next_steps.add(east_two)
            if wrapped_pos(northwest, gardens) != "#" and (west_one_wrapped != "#" or north_one_wrapped != "#"):
                next_steps.add(northwest)
            if wrapped_pos(northeast, gardens) != "#" and (east_one_wrapped != "#" or north_one_wrapped != "#"):
                next_steps.add(northeast)
            if wrapped_pos(southwest, gardens) != "#" and (west_one_wrapped != "#" or south_one_wrapped != "#"):
                next_steps.add(southwest)
            if wrapped_pos(southeast, gardens) != "#" and (east_one_wrapped != "#" or south_one_wrapped != "#"):
                next_steps.add(southeast)
        visited.update(next_steps)
        current = next_steps
    return results

with open("Input/Day21Input.txt") as f:
    gardens = [line.strip() for line in f.readlines()]

for row_num, row in enumerate(gardens):
    for col_num, col in enumerate(row):
        if col == "S":
            even_start = {(row_num, col_num)}
            odd_start = set()
            odd_points = [(row_num-1, col_num),(row_num+1, col_num),(row_num, col_num-1),(row_num, col_num+1)]
            for point in odd_points:
                if gardens[point[0]][point[1]] != "#":
                    odd_start.add(point)
            break

even_steps = get_steps(even_start, True, 200)
odd_steps = get_steps(odd_start, False, 200)

xp = [p[0] for p in [val for pair in zip(even_steps, odd_steps) for val in pair]]
fp = [p[1] for p in [val for pair in zip(even_steps, odd_steps) for val in pair]]

quadratics = list()
for i in range(len(xp)-len(gardens)):
    curve = polyfit(xp[i::len(gardens)], fp[i::len(gardens)], 2)
    p = poly1d(curve)
    quadratics.append(p)
    if len(quadratics) >= len(gardens)+1:
        if all([isclose(x, y, rel_tol=1e-5) for x, y in zip(list(quadratics[-1].coeffs), list(quadratics[-len(gardens)-1].coeffs))]):
            offset = len(quadratics) - len(gardens)
            break
print(round(quadratics[(TOTAL_STEPS-offset)%len(gardens)+offset](TOTAL_STEPS)))

