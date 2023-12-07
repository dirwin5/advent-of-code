input_list = open('input.txt', 'r').read().splitlines()

card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

card_dict = {}
for i, card in enumerate(card_order):
    card_dict[card] = len(card_order) - i


def sort_tup_list(l, index_list):
    for index in index_list:
        l = sorted(l, key=lambda item: item[index])

    return l

highcard_list = []
pair_list = []
twopair_list = []
threeofakind_list = []
fullhouse_list = []
fourofakind_list = []
fiveofakind_list = []

# iterate over each line and extract hand, bid and rank of each card
for line in input_list:
    hand = line.split()[0]
    bid = int(line.split()[1])
    line_tup = (hand,
                bid,
                card_dict[line[0]],
                card_dict[line[1]],
                card_dict[line[2]],
                card_dict[line[3]],
                card_dict[line[4]])

    # count unique characters
    unique_chars = len(set(list(hand)))

    # count number of jokers
    jokers = hand.count('J')

    #rank each hand type
    if unique_chars == 5:
        if jokers == 1:
            pair_list.append(line_tup)
        else:
            highcard_list.append(line_tup)

    if unique_chars == 4:
        # one or two jokers will always be used to make three of a kind here
        if jokers > 0:
            threeofakind_list.append(line_tup)
        else:
            pair_list.append(line_tup)

    if unique_chars == 3:
        # if 2 or 3 jokers, will always become 4 of a kind
        if jokers >= 2:
            fourofakind_list.append(line_tup)
            continue
        # test if three of a kind or two pair
        threeofakind = False
        for char in set(list(hand)):
            if hand.count(char) == 3:
                threeofakind = True
                break
        # if 1 joker, 3 of a kind becomes 4 of a kind and two pair becomes full house
        if jokers == 1:
            if threeofakind:
                fourofakind_list.append(line_tup)
            else:
                fullhouse_list.append(line_tup)
            continue
        # if no jokers
        if threeofakind:
            threeofakind_list.append(line_tup)
        else:
            twopair_list.append(line_tup)

    if unique_chars == 2:
        # any jokers will always make 5 of a kind
        if jokers > 0:
            fiveofakind_list.append(line_tup)
            continue
        # if no jokers
        # test if 4 of a kind or full house
        fourofakind = False
        for char in set(list(hand)):
            if hand.count(char) == 4:
                fourofakind = True
                break
        if fourofakind:
            fourofakind_list.append(line_tup)
        else:
            fullhouse_list.append(line_tup)

    if unique_chars == 1:
        fiveofakind_list.append(line_tup)

# sort each list of hands and calculate scores
index_list = [6, 5, 4, 3, 2]
i = 1
total = 0
ranked_list = []
for l in [highcard_list,
             pair_list,
             twopair_list,
             threeofakind_list,
             fullhouse_list,
             fourofakind_list,
             fiveofakind_list]:
    l = sort_tup_list(l, index_list)
    for j, hand_tup in enumerate(l):
        ranked_list.append(((i + j), hand_tup[0], hand_tup[1]))
        total += (i + j) * hand_tup[1]
    i = i + j + 1

print(f'Total: {total}')
print('Process complete')