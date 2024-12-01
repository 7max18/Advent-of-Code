list_a = list()
list_b = list()

with open('input.txt') as f:
    for line in f.readlines():
        line = line.split()
        list_a.append(int(line[0]))
        list_b.append(int(line[1]))

list_a.sort()
list_b.sort()

sum = 0
for a,b in zip(list_a,list_b):
    sum += abs(a-b)

print(sum)