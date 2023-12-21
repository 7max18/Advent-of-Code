from math import trunc

TOTAL_STEPS = 5000

def wrapped_pos(position, grid):
    return grid[position[0]-len(grid)*trunc(position[0]/len(grid))][position[1]-len(grid[0])*trunc(position[1]/len(grid[0]))]

def get_steps(current, even_parity):
    visited_orders = [current.copy()]
    print(visited_orders)
    for i in range(7):
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
            if 0 <= north_two[0] < len(gardens) and 0 <= north_two[1] < len(gardens[0]) and \
                gardens[north_two[0]][north_two[1]] == "." and gardens[north_one[0]][north_one[1]] == ".":
                next_steps.add(north_two)
            if 0 <= south_two[0] < len(gardens) and 0 <= south_two[1] < len(gardens[0]) and \
                gardens[south_two[0]][south_two[1]] == "." and gardens[south_one[0]][south_one[1]] == ".":
                next_steps.add(south_two)
            if 0 <= west_two[0] < len(gardens) and 0 <= west_two[1] < len(gardens[0]) and \
                gardens[west_two[0]][west_two[1]] == "." and gardens[west_one[0]][west_one[1]] == ".":
                next_steps.add(west_two)
            if 0 <= east_two[0] < len(gardens) and 0 <= east_two[1] < len(gardens[0]) and \
                gardens[east_two[0]][east_two[1]] == "." and gardens[east_one[0]][east_one[1]] == ".":
                next_steps.add(east_two)
            if 0 <= northwest[0] < len(gardens) and 0 <= northwest[1] < len(gardens[0]) and \
                gardens[northwest[0]][northwest[1]] == "." and (gardens[west_one[0]][west_one[1]] == "." or gardens[north_one[0]][north_one[1]] == "."):
                next_steps.add(northwest)
            if 0 <= northeast[0] < len(gardens) and 0 <= northeast[1] < len(gardens[0]) and \
                gardens[northeast[0]][northeast[1]] == "." and (gardens[east_one[0]][east_one[1]] == "." or gardens[north_one[0]][north_one[1]] == "."):
                next_steps.add(northeast)
            if 0 <= southwest[0] < len(gardens) and 0 <= southwest[1] < len(gardens[0]) and \
                gardens[southwest[0]][southwest[1]] == "." and (gardens[west_one[0]][west_one[1]] == "." or gardens[south_one[0]][south_one[1]] == "."):
                next_steps.add(southwest)
            if 0 <= southeast[0] < len(gardens) and 0 <= southeast[1] < len(gardens[0]) and \
                gardens[southeast[0]][southeast[1]] == "." and (gardens[east_one[0]][east_one[1]] == "." or gardens[south_one[0]][south_one[1]] == "."):
                next_steps.add(southeast)
            # if wrapped_pos(north_two, gardens) != "#" and wrapped_pos(north_one, gardens) != "#":
            #     next_steps.add(north_two)
            # if wrapped_pos(south_two, gardens) != "#" and wrapped_pos(south_one, gardens) != "#":
            #     next_steps.add(south_two)
            # if wrapped_pos(west_two, gardens) != "#" and wrapped_pos(west_one, gardens) != "#":
            #     next_steps.add(west_two)
            # if wrapped_pos(east_two, gardens) != "#" and wrapped_pos(east_one, gardens) != "#":
            #     next_steps.add(east_two)
            # if wrapped_pos(northwest, gardens) != "#" and (wrapped_pos(west_one, gardens) != "#" or wrapped_pos(north_one, gardens) != "#"):
            #     next_steps.add(northwest)
            # if wrapped_pos(northeast, gardens) != "#" and (wrapped_pos(east_one, gardens) != "#" or wrapped_pos(north_one, gardens) != "#"):
            #     next_steps.add(northeast)
            # if wrapped_pos(southwest, gardens) != "#" and (wrapped_pos(west_one, gardens) != "#" or wrapped_pos(south_one, gardens) != "#"):
            #     next_steps.add(southwest)
            # if wrapped_pos(southeast, gardens) != "#" and (wrapped_pos(east_one, gardens) != "#" or wrapped_pos(south_one, gardens) != "#"):
            #     next_steps.add(southeast)
        if next_steps == visited_orders[-1]:
            break
        visited_orders.append(next_steps)
        current = next_steps
    if even_parity:
        return (len(visited_orders)-1)*2, set.union(*visited_orders)
    else:
        return len(visited_orders)*2+1, set.union(*visited_orders)
with open("Input/Day21Input.txt") as f:
    gardens = [line.strip()*5 for line in f.readlines()]*5
    #gardens = [line.strip() for line in f.readlines()]
print(len(gardens))
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

even_start = {(27, 27)}
even_steps, even_plots = get_steps(even_start, True)
odd_steps, odd_plots = get_steps(odd_start, False)
print(even_steps, len(even_plots))
print(odd_steps, len(odd_plots))
step_count = even_steps
iter_count = 0
even_sum = 1
odd_sum = 0
cur_sum = even_sum
while step_count * cur_sum < TOTAL_STEPS:
    if iter_count % 2 == 0:
        even_sum += 4*iter_count
        cur_sum = even_sum
    else:
        odd_sum += 4*iter_count
        cur_sum = odd_sum
    print(iter_count, cur_sum, step_count*cur_sum)
    iter_count += 1
    
count = 0
for row_num, row in enumerate(gardens):
    for col_num, col in enumerate(row):
        if col == "S":
            gardens[row_num] = gardens[row_num][:col_num]+"."+gardens[row_num][col_num+1:]
        if (row_num, col_num) in even_plots:
            gardens[row_num] = gardens[row_num][:col_num]+"O"+gardens[row_num][col_num+1:]
            count += 1
# [print(line[:11]) for line in gardens[:11]]
# print()
# [print(line[11:22]) for line in gardens[:11]]
# print()
# [print(line[22:]) for line in gardens[:11]]
[print(line[11:22]) for line in gardens[11:22]]
[print(line) for line in gardens]
print(count)
