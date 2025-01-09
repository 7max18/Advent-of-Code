with open('input.txt') as f:
    lab = [line.strip() for line in f.readlines()]

for r, row in enumerate(lab):
    for c, col in enumerate(row):
        if col == '^':
            pos = [r,c]

rots = [(-1,0),(0,1),(1,0),(0,-1)]
vec = 0
visited = [pos]

while True:
    if pos not in visited:
        visited.append(pos)
    try:
        if lab[pos[0]+rots[vec][0]][pos[1]+rots[vec][1]] == '#':
            vec = (vec + 1) % 4
        lab[pos[0]] = lab[pos[0]][:pos[1]] + '^>v<'[vec] + lab[pos[0]][pos[1]+1:]
        pos = [pos[0]+rots[vec][0],pos[1]+rots[vec][1]]

    except IndexError:
        if pos not in visited:
            visited.append(pos)
        break

#[print(line, i) for i, line in enumerate(lab)]
print(len(visited))