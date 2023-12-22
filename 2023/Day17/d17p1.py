import heapq, time
#Compare direction and steps
def dijkstra(map, start, end):
    visited  = distances = [[[[False for w in range(3)] for x in range(4)] for y in range(len(map[0]))] for z in range(len(map))]
    distances = [[[[10e7 for w in range(3)] for x in range(4)] for y in range(len(map[0]))] for z in range(len(map))]
    distances[start[1]][start[0]] = [[0,0,0] for x in range(4)]
    pq = list()
    #Distance, coords, steps, direction
    all_adjacent = [[list() for x in range(len(map[0]))] for y in range(len(map))]
    heapq.heappush(pq, (0, 0, tuple(start), -1))
    for y in range(len(map)):
        for x in range(len(map[0])):
            if y > 0:
                all_adjacent[y][x].append(([x, y-1], 0))
            if x < len(map[0]) - 1:
                all_adjacent[y][x].append(([x+1, y], 1))
            if y < len(map) - 1:
                all_adjacent[y][x].append(([x, y+1], 2))
            if x > 0:
                all_adjacent[y][x].append(([x-1, y], 3))
    while pq:
        cur = heapq.heappop(pq)
        cur_dist = cur[0]
        cur_steps = cur[1]
        cur_coords = cur[2]
        cur_dir = cur[3]
        if visited[cur_coords[1]][cur_coords[0]][cur_dir][cur_steps-1]:
            continue
        adjacent = all_adjacent[cur_coords[1]][cur_coords[0]]
        cur_adjacent = list()
        visited[cur_coords[1]][cur_coords[0]][cur_dir][cur_steps-1] = True
        if cur_coords[1] > 0 and cur_dir != 2 and not (cur_dir == 0 and cur_steps >= 3):
            cur_adjacent += [x for x in adjacent if x[1] == 0]
        if cur_coords[0] < len(map[0]) - 1 and cur_dir != 3 and not (cur_dir == 1 and cur_steps >= 3):
            cur_adjacent += [x for x in adjacent if x[1] == 1]
        if cur_coords[1] < len(map) - 1 and cur_dir != 0 and not (cur_dir == 2 and cur_steps >= 3):
            cur_adjacent += [x for x in adjacent if x[1] == 2]
        if cur_coords[0] > 0 and cur_dir != 1 and not (cur_dir == 3 and cur_steps >= 3):
            cur_adjacent += [x for x in adjacent if x[1] == 3]
        for node in cur_adjacent:
            adj_coords = node[0]
            adj_dir = node[1]
            if adj_dir == cur_dir:
                adj_steps = cur_steps + 1
            else:
                adj_steps = 1
            if cur_dist + map[adj_coords[1]][adj_coords[0]] < distances[adj_coords[1]][adj_coords[0]][adj_dir][adj_steps-1]:
                if adj_dir == cur_dir:
                    distances[adj_coords[1]][adj_coords[0]][adj_dir][adj_steps-1] = cur_dist + map[adj_coords[1]][adj_coords[0]]
                else:
                    distances[adj_coords[1]][adj_coords[0]][adj_dir][adj_steps-1] = cur_dist + map[adj_coords[1]][adj_coords[0]]
                if adj_dir == cur_dir:
                    new = (cur_dist + map[adj_coords[1]][adj_coords[0]], cur_steps+1, tuple(adj_coords), adj_dir)
                else:
                    new = (cur_dist + map[adj_coords[1]][adj_coords[0]], 1, tuple(adj_coords), adj_dir)
                heapq.heappush(pq, new)
                
    distances = [[min([min(x) for x in dirs]) for dirs in y] for y in distances]
    return distances[end[1]][end[0]]
with open("Day17Input.txt") as f:
    map = [[int(x) for x in line.strip()] for line in f.readlines()]
start = [0,0]
end = [len(map[0])-1, len(map)-1]
#[print(line) for line in map]
#[print(line) for line in dijkstra(map, start, end)]
print(dijkstra(map, start, end))


