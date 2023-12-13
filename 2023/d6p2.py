#There's a simple formula at play here:
#Distance = time holding the button b * (time in the race t - time holding the button)
#Or d = -b^2+tb 
import numpy as np
import math

with open("Input/Day6Input.txt") as f:
    race = [int("".join(f.readline().split()[1:])), int("".join(f.readline().split()[1:]))]

roots = np.roots([-1, race[0], -race[1]])
print(math.ceil(roots[0])-math.floor(roots[1])-1)

