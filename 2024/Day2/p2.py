#The first time a "problem" level is found, take note of the levels to its left and right.
#A problematic level is either outside the tolerable range (i) or breaks the trend (i+1).
#If those surrounding levels are in a tolerable range, mark the report as dampened and continue.
#The second time this happens, or if this won't fix it, mark the report as unsafe and continue to the next.

# def dampenable(report, i, incdec):
#     if i == 0 or i == len(report)-1 or incdec == 0:
#         return True
#     before = report[i-1]
#     after = report[i+1]
#     diff = after - before
#     if incdec == 1:
#         if 1 <= diff <= 3:
#             return True
#         else:
#             return False
#     if incdec == -1:
#         if -1 >= diff >= -3:
#             return True
#         else:
#             return False

def safety_check(report):
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
        return True
    return False

reports = list()

with open('input.txt') as f:
    for line in f.readlines():
        reports.append([int(x) for x in line.split()])

safe = 0
for report in reports:
    #0=starting
    #1=increasing
    #-1=decreasing
    if safety_check(report):
        safe += 1
    else:
        for i in range(len(report)):
            dampened = report[:i] + report[i+1:]
            if safety_check(dampened):
                safe += 1
                break

print(safe)