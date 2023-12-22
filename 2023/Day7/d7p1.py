CARD_RANKS = "23456789TJQKA"
TYPE_RANKS = [[1,1,1,1,1],[1,1,1,2],[1,2,2],[1,1,3],[2,3],[1,4],[5]]

def better_hand(a, b):
    for i in range(len(a)):
        if CARD_RANKS.index(a[i]) > CARD_RANKS.index(b[i]):
            return 1
        elif CARD_RANKS.index(a[i]) < CARD_RANKS.index(b[i]):
            return 0

hand_ranks = list()

with open("Day7Input.txt") as f:
    for line in f.readlines():
        hand = (line.split()[0], int(line.split()[1]))
        card_counts = dict()
        for card in hand[0]:
            if card not in card_counts:
                card_counts[card] = 0
            card_counts[card] += 1
        type_rank = TYPE_RANKS.index(sorted(card_counts.values()))
        if hand_ranks:
            for index, ranked_hand in enumerate(hand_ranks):
                if type_rank > ranked_hand[0]:
                    continue
                elif ranked_hand[0] == type_rank:
                    if better_hand(hand[0], ranked_hand[1]):
                        continue
                    else:
                        hand_ranks.insert(index,(type_rank, hand[0], hand[1]))
                        break
                else:
                    hand_ranks.insert(index,(type_rank, hand[0], hand[1]))
                    break
            else:
                hand_ranks.append((type_rank, hand[0], hand[1]))
        else:
            hand_ranks.append((type_rank, hand[0], hand[1]))

print(sum([card[2]*(index+1) for index, card in enumerate(hand_ranks)]))
        

