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
    for j in range(len(pattern)-1):
        top, bottom = j, j+1
        if pattern[top] == pattern[bottom]:
            for i in range(min(top+1, len(pattern)-bottom)):
                if pattern[top-i] != pattern[bottom+i]:
                    break
            else:
                checksum += 100 * bottom
                break
    if checksum:
        total += checksum
        continue
    for j in range(len(pattern[0])-1):
        left, right = j, j + 1
        if "".join([row[left] for row in pattern]) == "".join([row[right] for row in pattern]):
            for i in range(min(left+1, len(pattern[0])-right)):
                if "".join([row[left-i] for row in pattern]) != "".join([row[right+i] for row in pattern]):
                    break
            else:
                checksum += right
                break
    total += checksum
    
print(total)
