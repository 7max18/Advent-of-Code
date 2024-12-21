#Exactly four valid configurations:
#M S M M S M S S
# A   A   A   A
#M S S S S M M M

word_search = list()

with open('input.txt') as f:
    for line in f.readlines():
        word_search.append(list(line.strip()))

x_mas_count = 0

for row in range(1, len(word_search) - 1):
    for col in range(1, len(word_search[0]) - 1):
        if word_search[row][col] == 'A':
            cross = ''.join([word_search[row-1][col-1],\
                            word_search[row-1][col+1],\
                            word_search[row+1][col-1],\
                            word_search[row+1][col+1]])
            if cross in ['MSMS','MMSS','SMSM','SSMM']:
                x_mas_count += 1

print(x_mas_count)