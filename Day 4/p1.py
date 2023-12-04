input_list = open('input.txt', 'r').read().splitlines()

total = 0

for input_line in input_list:
    card_no = input_line.split(':')[0]
    all_numbers = input_line.split(':')[1].strip()
    winning_numbers = all_numbers.split('|')[0].split()
    card_numbers = all_numbers.split('|')[1].split()

    matching_number_count = 0
    for winning_number in winning_numbers:
        if winning_number in card_numbers:
            matching_number_count += 1

    if matching_number_count == 0:
        card_value = 0
    else:
        card_value = 2 ** (matching_number_count - 1)
    total += card_value

print(f'Total: {total}')
print('Process complete')