#With enough spin cycles, most (but not all) of the rocks will become stuck in loops.
#Even if the position of the rocks isn't periodic, the loads are!

with open("Day14Input.txt") as f:
    platform = [line.strip() for line in f.readlines()]

def spin_cycle(platform):
    #North
    for i in range(1, len(platform)):
        for j in range(i, 0, -1):
            for k in range(len(platform[0])):
                if platform[j][k] == "O":
                    if platform[j-1][k] == ".":
                        platform[j] = platform[j][:k]+"."+platform[j][k+1:]
                        platform[j-1] = platform[j-1][:k]+"O"+platform[j-1][k+1:]
    #West
    for i in range(1, len(platform[0])):
        for k in range(i, 0, -1):
            for j in range(len(platform)):
                if platform[j][k] == "O":
                    if platform[j][k-1] == ".":
                        platform[j] = platform[j][:k-1]+"O."+platform[j][k+1:]

    #South
    for i in range(len(platform)-1, 0, -1):
        for j in range(i):
            for k in range(len(platform[0])):
                if platform[j][k] == "O":
                    if platform[j+1][k] == ".":
                        platform[j] = platform[j][:k]+"."+platform[j][k+1:]
                        platform[j+1] = platform[j+1][:k]+"O"+platform[j+1][k+1:]
    #East
    for i in range(len(platform)-1, 0, -1):
        for k in range(i):
            for j in range(len(platform)):
                if platform[j][k] == "O":
                    if platform[j][k+1] == ".":
                        platform[j] = platform[j][:k]+".O"+platform[j][k+2:]
    return platform

def find_cycle(loads):
    for i in range(2, (len(loads)//2)+1):
        if loads[-2*i:-i] == loads[-i:]:
            return len(loads)-2*i, i
    return None

loads = list()

while not (cycle := find_cycle(loads)):    
    platform = spin_cycle(platform)
    load = 0
    for index, row in enumerate(platform[::-1]):
        load += (index+1) * row.count("O")
    loads.append(load)

final = (1000000000 - cycle[0] - 1) % cycle[1]
print(loads[cycle[0]+final])