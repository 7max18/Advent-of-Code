from time import perf_counter

def beam(contraption, pos=[0,0], dir=[0,1]):
    while 0 <= pos[0] < len(contraption) and 0 <= pos[1] < len(contraption[0]):
        energized.add(tuple(pos))
        space = contraption[pos[0]][pos[1]]
        match space:
            case ".":
                pos = [pos[x] + dir[x] for x in range(2)]
            case "/":
                if (tuple(pos), tuple(dir)) in visited_nodes:
                    return
                visited_nodes.add((tuple(pos),tuple(dir)))
                match dir:
                    case [0,1]:
                        dir = [-1,0]
                    case [1,0]:
                        dir = [0,-1]
                    case [-1,0]:
                        dir = [0,1]
                    case [0,-1]:
                        dir = [1,0]
                pos = [pos[x] + dir[x] for x in range(2)]
            case "\\":
                if (tuple(pos), tuple(dir)) in visited_nodes:
                    return
                visited_nodes.add((tuple(pos),tuple(dir)))
                match dir:
                    case [0,1]:
                        dir = [1,0]
                    case [1,0]:
                        dir = [0,1]
                    case [-1,0]:
                        dir = [0,-1]
                    case [0,-1]:
                        dir = [-1,0]
                pos = [pos[x] + dir[x] for x in range(2)]
            case "-":
                if tuple(pos) in [value[0] for value in visited_nodes] and (dir == [1,0] or dir == [-1,0]):
                    return
                visited_nodes.add((tuple(pos),tuple(dir)))
                if dir == [1,0] or dir == [-1,0]:
                    beam(contraption, [pos[0],pos[1]+1], [0,1])
                    beam(contraption, [pos[0],pos[1]-1], [0,-1])
                else:
                    pos = [pos[x] + dir[x] for x in range(2)]
            case "|":
                if tuple(pos) in [value[0] for value in visited_nodes] and (dir == [0,1] or dir == [0,-1]):
                    return
                visited_nodes.add((tuple(pos),tuple(dir)))
                if dir == [0,1] or dir == [0,-1]:
                    beam(contraption, [pos[0]+1,pos[1]], [1,0])
                    beam(contraption, [pos[0]-1,pos[1]], [-1,0])
                else:
                    pos = [pos[x] + dir[x] for x in range(2)]
start_time = perf_counter()
with open("Input/Day16Input.txt") as f:
    contraption = [line.strip() for line in f.readlines()]
energized = set()
visited_nodes = set()
beam(contraption)
passed_time = perf_counter() - start_time
print(len(energized))
print(passed_time)