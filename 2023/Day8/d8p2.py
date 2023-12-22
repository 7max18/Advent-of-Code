from math import gcd

with open("Day8Input.txt") as f:
    lines = f.readlines()
    instructions = lines[0]
    nodes = dict()
    for line in lines[2:]:
        nodes[line[:3]] = (line[7:10], line[12:15])

positions = [node for node in nodes if node[-1] == "A"]
steps = list()
for pos in positions:
    pointer = 0
    counter = 0
    cur = pos
    while cur[-1] != "Z":
        turn = instructions[pointer]
        if turn == "L":
            cur = nodes[cur][0]
        else:
            cur = nodes[cur][1]
        counter += 1
        pointer += 1
        if pointer == len(instructions)-1:
            pointer = 0
    steps.append(counter)

total = steps[0]
for path in steps[1:]:
    total = total * path // gcd(total, path)

print(total)
