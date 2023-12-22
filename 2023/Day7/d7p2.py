CARD_RANKS = "J23456789TQKA"
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
        card_counts_dict = dict()
        jokers = 0
        for card in hand[0]:
            if card == "J":
                jokers += 1
            elif card not in card_counts_dict:
                card_counts_dict[card] = 0
                card_counts_dict[card] += 1
            else:
                card_counts_dict[card] += 1
        card_counts = sorted(card_counts_dict.values())
        if card_counts:
            card_counts[-1] += jokers
        else:
            card_counts.append(jokers)
        type_rank = TYPE_RANKS.index(card_counts)
        
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
        

