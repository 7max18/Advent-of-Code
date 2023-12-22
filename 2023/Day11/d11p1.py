#Potential optimization: no need to expand the galaxy if each expansion just adds an additional step
from itertools import combinations

def manhattan(start, end):
    return sum(abs(value1 - value2) for value1, value2 in zip(start, end))

with open("Day11Input.txt") as f:
    universe = [line.strip() for line in f.readlines()]

empty_rows = list()
empty_columns = list()

for i, row in enumerate(universe):
    if "#" not in row:
        empty_rows.append(i)
for row in empty_rows[::-1]:
    universe.insert(row, "."*len(universe[0]))
for i in range(len(universe[0])):
    column = [row[i] for row in universe]
    if "#" not in column:
        empty_columns.append(i)
for column in empty_columns[::-1]:
    for row in range(len(universe)):
        universe[row] = universe[row][:column] + "." + universe[row][column:]
galaxies = set()
for row, row_str in enumerate(universe):
    for column, elem in enumerate(row_str):
        if elem == "#":
            galaxies.add((row,column))
galaxy_pairs = combinations(galaxies, 2)
paths = list()
for pair in galaxy_pairs:
    shortest_path = manhattan(pair[0],pair[1])
    paths.append(shortest_path)
print(sum(paths))
