#If I'm correct, the trails can be expressed as a DAG; hence, the longest path can be found in linear time.
#1. Generate the graph.
#2. Find a topological ordering using depth-first search.
#3. For each vertex V, in topological order:
#       For every adjacent vertex U:
#           if dist[U] < dist[V] + edge weight from U to V:
#               dist[U] = dist[V] + edge weight from U to V
#4. Start at the vertex v with the largest recorded value, 
#   then repeatedly step backwards to its incoming neighbor with the largest recorded value.

def traverse(pos, direction):
    if pos in topo_ordering:
        return
    if pos in temp:
        print("Sorry, this isn't a DAG.")
        return
    temp.append(pos)
    if pos[0] == len(trail_map) - 1:
        topo_ordering.insert(0, pos)
        dag[tuple(pos)] = dict()
    elif pos[0] == 0:
        edge_weight, next_node, direction = count_steps(pos.copy(), direction)
        temp.remove(pos)
        topo_ordering.insert(0, pos)
        dag[tuple(pos)] = dict()
        dag[tuple(pos)][tuple(next_node)] = -edge_weight + 1
    else:
        if trail_map[pos[0]+1][pos[1]] == "v":
            edge_weight, next_node, direction = count_steps([pos[0]+1, pos[1]], 2)
            if not tuple(pos) in dag:
                dag[tuple(pos)] = dict()
            dag[tuple(pos)][tuple(next_node)] = -edge_weight
        if trail_map[pos[0]][pos[1]+1] == ">":
            edge_weight, next_node, direction = count_steps([pos[0], pos[1]+1], 1)
            if not tuple(pos) in dag:
                dag[tuple(pos)] = dict()
            dag[tuple(pos)][tuple(next_node)] = -edge_weight
        if trail_map[pos[0]-1][pos[1]] == "^":
            edge_weight, next_node, direction = count_steps([pos[0]-1, pos[1]], 0)
            if not tuple(pos) in dag:
                dag[tuple(pos)] = dict()
            dag[tuple(pos)][tuple(next_node)] = -edge_weight
        if trail_map[pos[0]][pos[1]-1] == "<":
            edge_weight, next_node, direction = count_steps([pos[0], pos[1]-1], 3)
            if not tuple(pos) in dag:
                dag[tuple(pos)] = dict()
            dag[tuple(pos)][tuple(next_node)] = -edge_weight
        temp.remove(pos)
        topo_ordering.insert(0, pos)
    return

def count_steps(pos, direction):
    at_junction = False
    path_len = 1
    while not (at_junction or pos[0] == len(trail_map) - 1):
        path_len += 1
        if trail_map[pos[0]+1][pos[1]] == "." and direction != 0:
            pos[0] += 1
            direction = 2
        elif trail_map[pos[0]+1][pos[1]] == "v":
            pos[0] += 2
            path_len += 1
            at_junction = True               
        elif trail_map[pos[0]][pos[1]+1] == "." and direction != 3:
            pos[1] += 1
            direction = 1
        elif trail_map[pos[0]][pos[1]+1] == ">":
            pos[1] += 2
            path_len += 1
            at_junction = True   
        elif trail_map[pos[0]-1][pos[1]] == "." and direction != 2:
            pos[0] -= 1
            direction = 0
        elif trail_map[pos[0]-1][pos[1]] == "^":
            pos[0] -= 2
            path_len += 1
            at_junction = True   
        elif trail_map[pos[0]][pos[1]-1] == "." and direction != 1:
            pos[1] -= 1
            direction = 3
        elif trail_map[pos[0]][pos[1]-1] == "<":
            pos[1] -= 2
            path_len += 1
            at_junction = True
    traverse(pos.copy(), direction)
    return path_len, pos, direction

def longest_path(dag, start, end):
    visited = {node: False for node in dag.keys()}
    dist = {node: 10e7 for node in dag.keys()}
    prev = {node: None for node in dag.keys()}
    pq = list()
    dist[tuple(start)] = 0
    pq.append(tuple(start))
    while pq:
        u = pq.pop(0)
        if visited[u]:
            continue
        visited[u] = True
        for v in dag[u]:
            alt = dist[u] + dag[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                pq.append(tuple(v))
    return -dist[tuple(end)]
        
with open("Day23Input.txt") as f:
    trail_map = [line.strip() for line in f.readlines()]

pos = [0,0]
while trail_map[0][pos[1]] != ".":
    pos[1] += 1

dag = dict()
temp = list()
topo_ordering = list()

traverse(pos.copy(), 2)
print(sorted(dag.items()))
print(topo_ordering)
print(longest_path(dag, topo_ordering[0], topo_ordering[-1]))
