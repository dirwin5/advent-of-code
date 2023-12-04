input_list = open('input.txt', 'r').read().splitlines()

card_dict = {}

# populate dict with original cards
for input_line in input_list:
    card_no = int(input_line.split(':')[0].split()[1])
    card_dict[card_no] = 1

# iterate over each card to check for wins
for input_line in input_list:
    card_no = int(input_line.split(':')[0].split()[1])
    copies = card_dict[card_no]
    all_numbers = input_line.split(':')[1].strip()
    winning_numbers = all_numbers.split('|')[0].split()
    card_numbers = all_numbers.split('|')[1].split()

    matching_number_count = 0
    for winning_number in winning_numbers:
        if winning_number in card_numbers:
            matching_number_count += 1

    for copy in range(copies):
        for i in range(matching_number_count):
            card_dict[card_no + i + 1] += 1

# count total cards
total = 0
for card_no, copies in card_dict.items():
    total += copies


print(f'Total: {total}')
print('Process complete')