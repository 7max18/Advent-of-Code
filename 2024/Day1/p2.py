list_a = list()
list_b = list()

with open('input.txt') as f:
    for line in f.readlines():
        line = line.split()
        list_a.append(int(line[0]))
        list_b.append(int(line[1]))

occurrences = list()

for i, a in enumerate(list_a):
    if i > 0 and a in list_a[:i-1]:
        occurrences.append(occurrences[list_a.index(a)])
        continue
    total = 0
    for b in list_b:
        if a == b:
            total += 1
    occurrences.append(total)

final = sum([a*b for a,b in zip(list_a, occurrences)])

print(final)