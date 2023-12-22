#There's a simple formula at play here:
#Distance = time holding the button b * (time in the race t - time holding the button)
#Or d = -b^2+tb 
import numpy as np
import math

with open("Day6Input.txt") as f:
    race_data = list(zip([int(x) for x in f.readline().split()[1:]], [int(x) for x in f.readline().split()[1:]]))

wins = list()

for race in race_data:
    roots = np.roots([-1, race[0], -race[1]])
    wins.append(math.ceil(roots[0])-math.floor(roots[1])-1)

print(np.prod(wins))
