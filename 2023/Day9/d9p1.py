histories = list()

with open("Day9Input.txt") as f:
    for line in f.readlines():
        histories.append([int(x) for x in line.split()])

nexts = list()
for history in histories:
    diffs = history
    ends = [history[-1]]
    while any(diffs):
        diffs = [v - diffs[i] for i,v in enumerate(diffs[1:])]
        ends.append(diffs[-1])
    nexts.append(sum(ends))

print(sum(nexts))