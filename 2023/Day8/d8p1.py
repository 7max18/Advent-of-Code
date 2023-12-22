with open("Day8Input.txt") as f:
    lines = f.readlines()
    instructions = lines[0]
    nodes = dict()
    for line in lines[2:]:
        nodes[line[:3]] = (line[7:10], line[12:15])

cur = "AAA"
pointer = 0
counter = 0
while cur != "ZZZ":
    turn = instructions[pointer]
    if turn == "L":
        cur = nodes[cur][0]
    else:
        cur = nodes[cur][1]
    counter += 1
    pointer += 1
    if pointer == len(instructions)-1:
        pointer = 0

print(counter)