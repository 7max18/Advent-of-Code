#0, 1, 2, 3 = up, right, down, left
import turtle

PIXEL_SIZE = 5

with open("Day10Input.txt") as f:
    pipes = [line.strip() for line in f.readlines()]

WIDTH, HEIGHT = len(pipes[0]), len(pipes)
turtle.setup((WIDTH + 3) * PIXEL_SIZE, (HEIGHT + 3) * PIXEL_SIZE)
turtle.tracer(False)
turt = turtle.Turtle()
turt.hideturtle()
turt.shape("circle")
turt.shapesize(PIXEL_SIZE/20)
turt.color("black")
turt.penup()
for y, row in enumerate(pipes):
    for x, column in enumerate(row):
        if column == "S":
            pos = [y,x]
            break
turt.setposition(-WIDTH/2 * PIXEL_SIZE+pos[1]*PIXEL_SIZE, HEIGHT/2 * PIXEL_SIZE-pos[0]*PIXEL_SIZE)
turt.stamp()
turt.pendown()
if pipes[pos[0]-1][pos[1]] in "|7F":
    pos[0] -= 1
    prev = 2
elif pipes[pos[0]][pos[1]+1] in "-7J":
    pos[1] += 1
    prev = 3
elif pipes[pos[0]+1][pos[1]] in "|JL":
    pos[0] += 1
    prev = 0
elif pipes[pos[0]][pos[1]-1] in "-LF":
    pos[1] -= 1
    prev = 1
cur = pipes[pos[0]][pos[1]]
steps = 1
turt.setposition(-WIDTH/2 * PIXEL_SIZE+pos[1]*PIXEL_SIZE, HEIGHT/2 * PIXEL_SIZE-pos[0]*PIXEL_SIZE)
while cur != "S":
    match cur:
        case "|":
            if prev == 0:
                pos[0] += 1
            else:
                pos[0] -= 1
        case "-":
            if prev == 3:
                pos[1] += 1
            else:
                pos[1] -= 1
        case "L":
            if prev == 0:
                pos[1] += 1
                prev = 3
            else:
                pos[0] -= 1
                prev = 2
        case "J":
            if prev == 0:
                pos[1] -= 1
                prev = 1
            else:
                pos[0] -= 1
                prev = 2
        case "7":
            if prev == 2:
                pos[1] -= 1
                prev = 1
            else:
                pos[0] += 1
                prev = 0
        case "F":
            if prev == 2:
                pos[1] += 1
                prev = 3
            else:
                pos[0] += 1
                prev = 0
    cur = pipes[pos[0]][pos[1]]
    steps += 1
    turt.setposition(-WIDTH/2 * PIXEL_SIZE+pos[1]*PIXEL_SIZE, HEIGHT/2 * PIXEL_SIZE-pos[0]*PIXEL_SIZE)
print(steps//2)
turtle.tracer(True)
turtle.done()
