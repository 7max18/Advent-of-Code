def hash(step):
    code = 0
    for char in step:
        code += ord(char)
        code *= 17
        code %= 256
    return code

with open("Input/Day15Input.txt") as f:
    sequence = f.readline().strip().split(",")

boxes = [list() for i in range(256)]

for step in sequence:
    if step[-1].isdigit():
        label = step[:-2]
        operation = step[-2]
        focal_length = int(step[-1])
    else:
        label = step[:-1]
        operation = step[-1]
    index = hash(label)
    cur_lens = [lens for lens in boxes[index] if lens[0] == label]
    if operation == "-":
        if cur_lens:
            boxes[index].remove(cur_lens[0])
    elif operation == "=":
        if cur_lens:
            boxes[index] = [(label, focal_length) if lens[0] == label else lens for lens in boxes[index]]
        else:
            boxes[index].append((label, focal_length))

focusing_power = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        focusing_power += (i+1) * (j+1) * lens[1] 

print(focusing_power)