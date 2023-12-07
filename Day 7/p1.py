input_list = open('input.txt', 'r').read().splitlines()

card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

card_dict = {}
for i, card in enumerate(card_order):
    card_dict[card] = len(card_order) - i


def sort_tup_list(list, index_list):
    for index in index_list:
        list = sorted(list, key=lambda item: item[index])

    return list

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

    #rank each hand type
    if unique_chars == 5:
        highcard_list.append(line_tup)
    if unique_chars == 4:
        pair_list.append((line_tup))
    if unique_chars == 3:
        threeofakind = False
        for char in set(list(hand)):
            if hand.count(char) == 3:
                threeofakind = True
                threeofakind_list.append(line_tup)
                break
        if threeofakind is False:
            twopair_list.append(line_tup)
    if unique_chars == 2:
        fourofakind = False
        for char in set(list(hand)):
            if hand.count(char) == 4:
                fourofakind = True
                fourofakind_list.append(line_tup)
                break
        if fourofakind is False:
            fullhouse_list.append(line_tup)
    if unique_chars == 1:
        fiveofakind_list.append(line_tup)

# sort each list of hands and calculate scores
index_list = [6, 5, 4, 3, 2]
i = 1
total = 0
ranked_list = []
for list in [highcard_list,
             pair_list,
             twopair_list,
             threeofakind_list,
             fullhouse_list,
             fourofakind_list,
             fiveofakind_list]:
    list = sort_tup_list(list, index_list)
    for j, hand_tup in enumerate(list):
        ranked_list.append(((i + j), hand_tup[0], hand_tup[1]))
        total += (i + j) * hand_tup[1]
    i = i + j + 1

print(f'Total: {total}')
print('Process complete')