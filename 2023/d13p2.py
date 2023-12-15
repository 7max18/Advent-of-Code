#1. Scan the rows and columns for pairs that are one character off.
#2. Propagate inward and outward; if there are no other differences, the smudge has been found.
#3. Extract checksum using the new line of reflection.

patterns = list()

with open("Input/Day13Input.txt") as f:
    pattern = list()
    for line in f.readlines():
        row = line.strip()
        if row:
            pattern.append(row)
        else:
            patterns.append(pattern)
            pattern = list()
    patterns.append(pattern)

total = 0

for pattern in patterns:
    checksum = 0
    for i in range(len(pattern[0])-1):
        for j in range(i+1, len(pattern[0]), 2):
            left, right = "".join([row[i] for row in pattern]), "".join([row[j] for row in pattern])
            diff = [True if left[i] != right[i] else False for i in range(len(left))]
            if diff.count(True)==1:
                for k in range(1, min(i+1, len(pattern[0])-j)):
                    if "".join([row[i-k] for row in pattern]) != "".join([row[j+k] for row in pattern]):
                        break
                else:
                    for l in range(1, (j-i)//2+1):
                        if "".join([row[i+l] for row in pattern]) != "".join([row[j-l] for row in pattern]):
                            break
                    else:
                        checksum = (i+j)//2+1
            if checksum:
                break
        if checksum:
            break
    if checksum:
        total += checksum
        continue
    for i in range(len(pattern)-1):
        for j in range(i+1, len(pattern), 2):
            top, bottom = pattern[i], pattern[j]
            diff = [True if top[i] != bottom[i] else False for i in range(len(top))]
            if diff.count(True)==1:
                for k in range(1, min(i+1, len(pattern)-j)):
                    if pattern[i-k] != pattern[j+k]:
                        break
                else:
                    for l in range(1, (j-i)//2+1):
                        if pattern[i+l] != pattern[j-l]:
                            break
                    else:
                        checksum = 100*((i+j)//2+1)
            if checksum:
                break
        if checksum:
            break
    total += checksum
    
print(total)
