with open("Day5Input.txt") as f:
    lines = f.readlines()
    seeds = [int(x) for x in lines[0].split()[1:]]
    maps = list()
    at_next = False
    for line in lines[1:]:
        if at_next:
            at_next = False
            continue
        if line.strip():
            maps[-1].append([int(x) for x in line.split()])
        else:
            at_next = True
            maps.append(list())

locations = list()

for seed in seeds:
    cur_num = seed
    for map_section in maps:
        for map in map_section:
            if map[1] <= cur_num < map[1] + map[2]:
                cur_num = cur_num - map[1] + map[0]
                break
        else:
            continue
    locations.append(cur_num)

print(min(locations))
