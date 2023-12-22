import turtle

PIXEL_SIZE = 2

directions = list()

with open("Day18Input.txt") as f:
    for line in f.readlines():
        direction = line.split()
        directions.append([int(direction[2][7]), int(direction[2][2:7], 16)])

turtle.tracer(False)
turt = turtle.Turtle()
turt.hideturtle
turt.shapesize(PIXEL_SIZE/20)

border_points = 0
shoelace = 0
vertices = [[0,0]]
boundary_points = set()
for index, direction in enumerate(directions):
    cur = vertices[-1].copy()
    match direction[0]:
        case 3:
            turt.setheading(90)
            cur[1] += direction[1]
        case 0:
            turt.setheading(0)
            cur[0] += direction[1]
        case 1:
            turt.setheading(-90)
            cur[1] -= direction[1]
        case 2:
            turt.setheading(180)
            cur[0] -= direction[1]
    border_points += direction[1]
    turt.forward(direction[1]/40000)
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