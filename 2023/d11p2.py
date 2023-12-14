#No need to expand the galaxy if each expansion just adds an additional step
from itertools import combinations
EXPANSION_RATE = 1000000
def manhattan(start, end, empty_rows, empty_columns):
    distance = 0
    empty = [empty_rows, empty_columns]
    paired_coords = zip(start, end, empty)
    for value1, value2, empty_values in paired_coords:
        distance += abs(value1 - value2)
        for empty_space in empty_values:
            if min(value1,value2) < empty_space < max(value1,value2):
                distance += EXPANSION_RATE-1
    return distance

with open("Input/Day11Input.txt") as f:
    universe = [line.strip() for line in f.readlines()]

empty_rows = list()
empty_columns = list()

for i, row in enumerate(universe):
    if "#" not in row:
        empty_rows.append(i)
for i in range(len(universe[0])):
    column = [row[i] for row in universe]
    if "#" not in column:
        empty_columns.append(i)
galaxies = set()
for row, row_str in enumerate(universe):
    for column, elem in enumerate(row_str):
        if elem == "#":
            galaxies.add((row,column))
galaxy_pairs = combinations(galaxies, 2)
paths = list()
for pair in galaxy_pairs:
    shortest_path = manhattan(pair[0],pair[1],empty_rows,empty_columns)
    paths.append(shortest_path)
print(sum(paths))
