# Any obstruction to the loop would have to exist somewhere along the path.
# No need to brute force every step, just the ones with an obstacle somewhere due right.
# Plan B: rather than go step by step, add the whole line segment at once.
# Or stop it from recalcuating the main path over and over.
# And don't forget to make sure it searches from the back for vecs 2 and 3.
# Or that the obstacle itself could affect the path.
# Or that they can't be placed outside the grid.
# Filtering out already visited obstacles is a bad idea.

def loop_check(lab, pos, vec, visited_obstacles):
    while True:
        match vec:
            case 0:
                ray = list(enumerate([row[pos[1]] for row in lab]))[pos[0]::-1]
                if '#' in [r[1] for r in ray]:
                    obstacle = [ray[[r[1] for r in ray].index('#')][0]+1, pos[1]]
                else:
                    return False
            case 1:
                ray = list(enumerate(lab[pos[0]][pos[1]:], pos[1]))
                if '#' in [r[1] for r in ray]:
                    obstacle = [pos[0], ray[[r[1] for r in ray].index('#')][0]-1]
                else:
                    return False
            case 2:
                ray = list(enumerate([row[pos[1]] for row in lab]))[pos[0]:]
                if '#' in [r[1] for r in ray]:
                    obstacle = [ray[[r[1] for r in ray].index('#')][0]-1, pos[1]]
                else:
                    return False
            case 3:
                ray = list(enumerate(lab[pos[0]][:pos[1]]))[::-1]
                if '#' in [r[1] for r in ray]:
                    obstacle = [pos[0], ray[[r[1] for r in ray].index('#')][0]+1]
                else:
                    return False 
        print(ray,vec,pos)
        pos = obstacle
        #lab[pos[0]] = lab[pos[0]][:pos[1]] + '^>v<'[vec] + lab[pos[0]][pos[1]+1:]
        if [pos,vec] in visited_obstacles:
            #print(visited_obstacles)
            #[print(line, i) for i, line in enumerate(lab)]
            return True
        visited_obstacles.append([pos,vec])
        vec = (vec+1)%4


with open('input.txt') as f:
    lab = [line.strip() for line in f.readlines()]

for r, row in enumerate(lab):
    for c, col in enumerate(row):
        if col == '^':
            start = [r,c]

rots = [(-1,0),(0,1),(1,0),(0,-1)]
pos = start.copy()
path = list()
vec = 0 
while True:
    try:
        pos = [pos[0]+rots[vec][0],pos[1]+rots[vec][1]]
        path.append([pos,vec])
        lab[pos[0]] = lab[pos[0]][:pos[1]] + '^>v<'[vec] + lab[pos[0]][pos[1]+1:]
        while lab[pos[0]+rots[vec][0]][pos[1]+rots[vec][1]] == '#':
            vec = (vec + 1) % 4
            path.append([pos,vec])
    except IndexError:
        lab[pos[0]] = lab[pos[0]][:pos[1]] + '^>v<'[vec] + lab[pos[0]][pos[1]+1:]
        break

obstructions = set()

for pos,vec in path:
    obstacle = None
    match vec:
        case 0:
            if pos[0] > 0:
                ray = list(enumerate(lab[pos[0]][pos[1]:], pos[1]))
                if '#' in [r[1] for r in ray]:
                    obstacle = [pos[0], ray[[r[1] for r in ray].index('#')][0]]
        case 1:
            if pos[1] < len(lab[0]) - 1:
                ray = list(enumerate([row[pos[1]] for row in lab]))[pos[0]:]
                if '#' in [r[1] for r in ray]:
                    obstacle = [ray[[r[1] for r in ray].index('#')][0], pos[1]]
        case 2:
            if pos[0] < len(lab) - 1:
                ray = list(enumerate(lab[pos[0]][:pos[1]]))[::-1]
                if '#' in [r[1] for r in ray]:
                    obstacle = [pos[0], ray[[r[1] for r in ray].index('#')][0]]
        case 3:
            if pos[1] > 0:
                ray = list(enumerate([row[pos[1]] for row in lab]))[pos[0]::-1]
                if '#' in [r[1] for r in ray]:
                    obstacle = [ray[[r[1] for r in ray].index('#')][0], pos[1]]
    if obstacle and lab[pos[0]+rots[vec][0]][pos[1]+rots[vec][1]] != '#':
        #print(pos,vec)
        altered_lab = lab.copy()
        obstruction = [pos[0]+rots[vec][0],pos[1]+rots[vec][1]]
        altered_lab[obstruction[0]] = altered_lab[obstruction[0]][:obstruction[1]]+'#'+altered_lab[obstruction[0]][obstruction[1]+1:]
        if loop_check(altered_lab, pos, vec, path.copy()[:path.index([pos,vec])]):
            obstructions.add(tuple(obstruction))

for row, col in obstructions:
    lab[row] = lab[row][:col]+'X'+lab[row][col+1:]

[print(line) for line in lab]
print(len(obstructions))