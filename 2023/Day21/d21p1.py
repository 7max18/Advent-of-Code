with open("Day21Input.txt") as f:
    gardens = [line.strip() for line in f.readlines()]

visited = set()

for row_num, row in enumerate(gardens):
    for col_num, col in enumerate(row):
        if col == "S":
            current = {(row_num, col_num)}
            break
visited = current.copy()
for i in range(32):
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
        if gardens[north_two[0]][north_two[1]] == "." and gardens[north_one[0]][north_one[1]] == ".":
            next_steps.add(north_two)
        if gardens[south_two[0]][south_two[1]] == "." and gardens[south_one[0]][south_one[1]] == ".":
            next_steps.add(south_two)
        if gardens[west_two[0]][west_two[1]] == "." and gardens[west_one[0]][west_one[1]] == ".":
            next_steps.add(west_two)
        if gardens[east_two[0]][east_two[1]] == "." and gardens[east_one[0]][east_one[1]] == ".":
            next_steps.add(east_two)
        if gardens[northwest[0]][northwest[1]] == "." and (gardens[west_one[0]][west_one[1]] == "." or gardens[north_one[0]][north_one[1]] == "."):
            next_steps.add(northwest)
        if gardens[northeast[0]][northeast[1]] == "." and (gardens[east_one[0]][east_one[1]] == "." or gardens[north_one[0]][north_one[1]] == "."):
            next_steps.add(northeast)
        if gardens[southwest[0]][southwest[1]] == "." and (gardens[west_one[0]][west_one[1]] == "." or gardens[south_one[0]][south_one[1]] == "."):
            next_steps.add(southwest)
        if gardens[southeast[0]][southeast[1]] == "." and (gardens[east_one[0]][east_one[1]] == "." or gardens[south_one[0]][south_one[1]] == "."):
            next_steps.add(southeast)
    visited.update(next_steps)
    current = next_steps

# for row_num, row in enumerate(gardens):
#     for col_num, col in enumerate(row):
#         if (row_num, col_num) in visited:
#             gardens[row_num] = gardens[row_num][:col_num]+"O"+gardens[row_num][col_num+1:]
# [print(line) for line in gardens]

print(len(visited))