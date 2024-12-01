list_a = list()
list_b = list()

with open('input.txt') as f:
    for line in f.readlines():
        line = line.split()
        list_a.append(int(line[0]))
        list_b.append(int(line[1]))

for 