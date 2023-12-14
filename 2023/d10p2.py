# 0, 1, 2, 3 = up, right, down, left
#From discord: Shoelace formula + Pick's theorem

with open("Input/Day10Input.txt") as f:
    pipes = [line.strip() for line in f.readlines()]

for y, row in enumerate(pipes):
    for x, column in enumerate(row):
        if column == "S":
            pos = [y,x]
            break
prev = pos.copy()
if pipes[pos[0]-1][pos[1]] in "|7F":
    pos[0] -= 1
    dir = 0
elif pipes[pos[0]][pos[1]+1] in "-7J":
    pos[1] += 1
    dir = 1
elif pipes[pos[0]+1][pos[1]] in "|JL":
    pos[0] += 1
    dir = 2
elif pipes[pos[0]][pos[1]-1] in "-LF":
    pos[1] -= 1
    dir = 3
cur = pipes[pos[0]][pos[1]]
shoelace = 0
steps = 1
while cur != "S":
    shoelace += prev[0]*pos[1]-pos[0]*prev[1]
    prev = pos.copy()
    match cur:
        case "|":
            if dir == 2:
                pos[0] += 1
            else:
                pos[0] -= 1
        case "-":
            if dir == 1:
                pos[1] += 1
            else:
                pos[1] -= 1
        case "L":
            if dir == 2:
                pos[1] += 1
                dir = 1
            else:
                pos[0] -= 1
                dir = 0
        case "J":
            if dir == 2:
                pos[1] -= 1
                dir = 3
            else:
                pos[0] -= 1
                dir = 0
        case "7":
            if dir == 0:
                pos[1] -= 1
                dir = 3
            else:
                pos[0] += 1
                dir = 2
        case "F":
            if dir == 0:
                pos[1] += 1
                dir = 1
            else:
                pos[0] += 1
                dir = 2
    cur = pipes[pos[0]][pos[1]]
    steps += 1
shoelace += prev[0]*pos[1]-pos[0]*prev[1]
area = abs(shoelace//2)
interior = area + 1 - steps//2
print(interior)
