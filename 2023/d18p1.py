import turtle

PIXEL_SIZE = 2

directions = list()

with open("Input/Day18Input.txt") as f:
    for line in f.readlines():
        direction = line.split()
        directions.append([direction[0], int(direction[1]), direction[2][1:8]])

turtle.tracer(False)
turt = turtle.Turtle()
turt.hideturtle
turt.shape("square")
turt.shapesize(PIXEL_SIZE/20)
turt.penup()
border_points = 0
shoelace = 0
vertices = [[0,0]]
boundary_points = set()
cw_orientation = True
for index, direction in enumerate(directions):
    turt.color(direction[2])
    cur = vertices[-1].copy()
    for i in range(direction[1]):
        match direction[0]:
            case "U":
                turt.setheading(90)
                cur[1] += 1
            case "R":
                turt.setheading(0)
                cur[0] += 1
            case "D":
                turt.setheading(-90)
                cur[1] -= 1
            case "L":
                turt.setheading(180)
                cur[0] -= 1
        turt.forward(PIXEL_SIZE)
        turt.stamp()
        border_points += 1
    vertices.append(cur)
shoelace = 0
for i in range(len(vertices)-1):
    prev, next = vertices[i], vertices[i+1]
    shoelace += prev[0]*next[1]-next[0]*prev[1]
interior_area = abs(shoelace)//2
interior_points = abs(shoelace//2) + 1 - (border_points//2)
print(interior_points + border_points)
turtle.tracer(True)
turtle.done()