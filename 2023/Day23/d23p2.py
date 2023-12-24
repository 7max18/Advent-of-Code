#Since each node/junction can still only be visited once,
#you just need the longest Hamiltonian path from start to end.

def traverse(pos, direction):
    vertices.append(tuple(pos))
    if pos[0] == 0:
        count_steps(pos.copy(), direction, pos)
    else:
        if trail_map[pos[0]+1][pos[1]] in "^v" and direction != 0:
            count_steps([pos[0]+1, pos[1]], 2, pos)
        if trail_map[pos[0]][pos[1]+1] in "><" and direction != 3:
            count_steps([pos[0], pos[1]+1], 1, pos)
        if trail_map[pos[0]-1][pos[1]] in "^v" and direction != 2: 
            count_steps([pos[0]-1, pos[1]], 0, pos)
        if trail_map[pos[0]][pos[1]-1] in "><" and direction != 1:
            count_steps([pos[0], pos[1]-1], 3, pos)
    return

def count_steps(pos, direction, start):
    at_junction = False
    if pos[0] == 0:
        path_len = 0
    else:
        path_len = 1
    while not (at_junction or pos[0] == len(trail_map) - 1 or (pos[0] == 0 and direction == 0)):
        path_len += 1
        if trail_map[pos[0]+1][pos[1]] == "." and direction != 0:
            pos[0] += 1
            direction = 2
        elif trail_map[pos[0]+1][pos[1]] in "^v" and direction != 0:
            pos[0] += 2
            path_len += 1
            direction = 2
            at_junction = True               
        elif trail_map[pos[0]][pos[1]+1] == "." and direction != 3:
            pos[1] += 1
            direction = 1
        elif trail_map[pos[0]][pos[1]+1] in "><" and direction != 3:
            pos[1] += 2
            path_len += 1
            direction = 1
            at_junction = True   
        elif trail_map[pos[0]-1][pos[1]] == "." and direction != 2:
            pos[0] -= 1
            direction = 0
        elif trail_map[pos[0]-1][pos[1]] in "^v" and direction != 2:
            pos[0] -= 2
            path_len += 1
            direction = 0
            at_junction = True   
        elif trail_map[pos[0]][pos[1]-1] == "." and direction != 1:
            pos[1] -= 1
            direction = 3
        elif trail_map[pos[0]][pos[1]-1] in "><" and direction != 1:
            pos[1] -= 2
            path_len += 1
            direction = 3
            at_junction = True
    if not frozenset({tuple(start), tuple(pos)}) in edges:
        edges[frozenset([tuple(start), tuple(pos)])] = path_len
        if tuple(start) not in adj_list:
            adj_list[tuple(start)] = dict()
        adj_list[tuple(start)][tuple(pos)] = path_len
        if tuple(pos) not in adj_list:
            adj_list[tuple(pos)] = dict()
        adj_list[tuple(pos)][tuple(start)] = path_len
        if tuple(pos) not in vertices:
            if pos[0] == len(trail_map) - 1:
                vertices.append(tuple(pos))
            else:
                traverse(pos.copy(), direction)
    return

def longest_path(cur_vert, cur_path=list()):
    used[cur_vert] = True
    for i, v in enumerate(vertices):
        if not used[i]:
            edge = frozenset({vertices[cur_vert], v})
            if edge in edges:
                cur_path.append(edge)
                if i == len(vertices) - 1:
                    paths.append(sum([edges[y] for y in cur_path]))
                else:
                    longest_path(i)
                cur_path.remove(edge)
    used[cur_vert] = False

with open("Day23Input.txt") as f:
    trail_map = [line.strip() for line in f.readlines()]

pos = [0,0]
while trail_map[0][pos[1]] != ".":
    pos[1] += 1

vertices = list()
edges = dict()
adj_list = dict()
traverse(pos.copy(), 2)
vertices.sort()

adj_matrix = [[0 for x in range(len(vertices))] for y in range(len(vertices))]
for i, row in enumerate(adj_matrix):
    for j, col in enumerate(row):
        if frozenset({vertices[i], vertices[j]}) in edges:
            adj_matrix[i][j] = 1
visited_nodes = [False for i in range(len(vertices))]
paths = list()
used = [False for n in range(len(vertices))]
longest_path(0)
print(max(paths))

