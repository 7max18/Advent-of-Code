word_search = list()

with open('input.txt') as f:
    for line in f.readlines():
        word_search.append(list(line.strip()))

xmas_count = 0

search_vectors = {(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)}

for row, x in enumerate(word_search):
    for col, val in enumerate(x):
        if val == 'X':
            for vec in search_vectors:
                for i, v in enumerate(['M','A','S']):
                    if max(0, min(row+vec[0]*(i+1),len(word_search)-1)) != row+vec[0]*(i+1) or \
                    max(0, min(col+vec[1]*(i+1),len(word_search[0])-1)) != col+vec[1]*(i+1):
                        break
                    if word_search[row+vec[0]*(i+1)][col+vec[1]*(i+1)] != v:
                        break
                else:
                    xmas_count += 1

print(xmas_count)