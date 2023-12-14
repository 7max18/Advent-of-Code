# 0, 1, 2, 3 = up, right, down, left
#From discord: Shoelace formula + Pick's theorem

import turtle
    
PIXEL_SIZE = 15

with open("Input/Day10Input.txt") as f:
    pipes = [line.strip() for line in f.readlines()]

WIDTH, HEIGHT = len(pipes[0]), len(pipes)
turtle.setup((WIDTH + 3) * PIXEL_SIZE, (HEIGHT + 3) * PIXEL_SIZE)
turtle.tracer(False)
turt = turtle.Turtle()
turt.hideturtle()
#turt.shape("circle")
turt.shapesize(PIXEL_SIZE/20)
turt.color("black")
turt.penup()

for y, row in enumerate(pipes):
    for x, column in enumerate(row):
        if column == "S":
            pos = [y,x]
            break
turt.setposition(-WIDTH/2 * PIXEL_SIZE+pos[1]*PIXEL_SIZE, HEIGHT/2 * PIXEL_SIZE-pos[0]*PIXEL_SIZE)
turt.pendown()
prev = pos.copy()
if pipes[pos[0]-1][pos[1]] in "|7F":
    pos[0] -= 1
    dir = 0
    turt.left(90)
elif pipes[pos[0]][pos[1]+1] in "-7J":
    pos[1] += 1
    dir = 1
elif pipes[pos[0]+1][pos[1]] in "|JL":
    pos[0] += 1
    dir = 2
    turt.right(90)
elif pipes[pos[0]][pos[1]-1] in "-LF":
    pos[1] -= 1
    dir = 3
    turt.right(180)
cur = pipes[pos[0]][pos[1]]
# path[prev_pos[0]][prev_pos[1]] = [dir, dir]
turt.setposition(-WIDTH/2 * PIXEL_SIZE+pos[1]*PIXEL_SIZE, HEIGHT/2 * PIXEL_SIZE-pos[0]*PIXEL_SIZE)
turt.stamp()
shoelace = 0
steps = 1
while cur != "S":
    # prev = dir
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
                turt.left(90)
            else:
                pos[0] -= 1
                dir = 0
                turt.right(90)
        case "J":
            if dir == 2:
                pos[1] -= 1
                dir = 3
                turt.right(90)
            else:
                pos[0] -= 1
                dir = 0
                turt.left(90)
        case "7":
            if dir == 0:
                pos[1] -= 1
                dir = 3
                turt.left(90)
            else:
                pos[0] += 1
                dir = 2
                turt.right(90)
        case "F":
            if dir == 0:
                pos[1] += 1
                dir = 1
                turt.right(90)
            else:
                pos[0] += 1
                dir = 2
                turt.left(90)
    cur = pipes[pos[0]][pos[1]]
    steps += 1
    # path[prev_pos[0]][prev_pos[1]] = [prev, dir]
    turt.setposition(-WIDTH/2 * PIXEL_SIZE+pos[1]*PIXEL_SIZE, HEIGHT/2 * PIXEL_SIZE-pos[0]*PIXEL_SIZE)
    turt.stamp()
shoelace += prev[0]*pos[1]-pos[0]*prev[1]
# path[pos[0]][pos[1]][0] = prev
# [print("".join(["A>V<."[x[1]] for x in line])) for line in path]
# print()
# [print("".join(["A>V<."[x[0]] for x in line])) for line in path]
area = abs(shoelace//2)
print(area)
interior = area + 1 - steps//2
print(interior)
turtle.tracer(True)
turtle.done()
