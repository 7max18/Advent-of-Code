reports = list()

with open('input.txt') as f:
    for line in f.readlines():
        reports.append([int(x) for x in line.split()])

safe = 0
for report in reports:
    #0=starting
    #1=increasing
    #-1=decreasing
    incdec = 0
    for i in range(len(report)-1):
        diff = report[i+1] - report[i]
        if incdec == 0:
            if diff > 0:
                incdec = 1
            elif diff < 0:
                incdec = -1
            else:
                break
        if incdec == 1:
            if 1 <= diff <= 3:
                continue
            else:
                break
        if incdec == -1:
            if -1 >= diff >= -3:
                continue
            else:
                break
    else:
        safe += 1

print(safe)