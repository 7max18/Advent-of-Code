with open("Input/Day5Input.txt") as f:
    lines = f.readlines()
    seed_pairs = lines[0].split()[1:]
    seed_maps = [[int(x), int(seed_pairs[i+1])] for i, x in list(enumerate(seed_pairs))[::2]]
    other_maps = list()
    at_next = False
    for line in lines[1:]:
        if at_next:
            at_next = False
            continue
        if line.strip():
            other_maps[-1].append([int(x) for x in line.split()])
        else:
            at_next = True
            other_maps.append(list())

locations = list()
#If a source range intersects a map range, create a subrange one level up. Repeat.
#Don't forget to split previous subrange to get leftovers.
for seed_map in seed_maps:
    cur_subranges = [seed_map]
    for map_section in other_maps:
        next_subranges = list()
        overlaps = list()
        for map in map_section:
            for subrange in cur_subranges:
                overlap = [max(subrange[0], map[1]), min(subrange[0]+subrange[1]-1, map[1]+map[2]-1)]
                if overlap[0] < overlap[1]:
                    next_subranges.append([overlap[0] - map[1] + map[0], overlap[1]-overlap[0]])
                    overlaps.append(overlap)
        for overlap in overlaps:
            for subrange in cur_subranges:
                if subrange[0] <= overlap[0] < subrange[0] + subrange[1]:
                    cur_subranges.remove(subrange)
                    #If a non-mapped range is a one-to-one correspondence, and we're looking for minimae, there's no need to save the higher partition.
                    if overlap[0]-subrange[0] > 0:
                        cur_subranges.append([subrange[0], overlap[0]-subrange[0]])
                    break
        cur_subranges += next_subranges
        cur_subranges.sort()
    locations.append(cur_subranges[0][0])

print(min(locations))
                                  

