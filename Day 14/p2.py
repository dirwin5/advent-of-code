from time import time


def convert_row_col_list(input_list):
    output_list = []
    for i in range(len(input_list[0])):
        row_col_list = []
        for item in input_list:
            row_col_list.append(item[i])
        output_list.append(row_col_list)
    return output_list


def tilt(items_list, direction='N'):
    reverse = False
    if direction in ['S', 'E']:
        reverse = True
    items_list_tilted = []
    for item in items_list:
        if reverse:
            item.reverse()
        item_tilted = []
        move_to = 0
        for i, char in enumerate(item):
            if char == '.':
                item_tilted.append('.')
            if char == '#':
                item_tilted.append('#')
                move_to = i + 1
            if char == 'O':
                if move_to < i:
                    item_tilted[move_to] = 'O'
                    item_tilted.append('.')
                else:
                    item_tilted.append('O')
                move_to += 1
        if reverse:
            item_tilted.reverse()
        items_list_tilted.append(item_tilted)

    return items_list_tilted


def calculate_load(items_list_tilted):
    total = 0
    max_load = len(items_list_tilted[0])
    for item_list in items_list_tilted:
        for i, char in enumerate(item_list):
            if char == 'O':
                total += max_load - i

    return total


def cycle(rows_list):
    # north, west, south, east
    # north
    cols_list = convert_row_col_list(rows_list)
    cols_list_tilted = tilt(cols_list, 'N')
    # west
    rows_list = convert_row_col_list(cols_list_tilted)
    rows_list_tilted = tilt(rows_list, 'W')
    # south
    cols_list = convert_row_col_list(rows_list_tilted)
    cols_list_tilted = tilt(cols_list, 'S')
    # east
    rows_list = convert_row_col_list(cols_list_tilted)
    rows_list_tilted = tilt(rows_list, 'E')

    return rows_list_tilted


def print_dish(rows_list):
    for row in rows_list:
        row_str = ''.join(row)
        print(row_str)


start_time = time()

input_list = open('input.txt', 'r').read().splitlines()
# input_list = open('test.txt', 'r').read().splitlines()

# make rows list and convert strings to lists
rows_list = []
for input_str in input_list:
    rows_list.append(list(input_str))

# print_dish(rows_list)

load_list = []
previous_layouts = []
i = 0
# do cycle, then check if the layout is identical to one we've seen before
# if we find a layout we've seen before, we've found a repeating sequence
while True:
    rows_list_cycled = cycle(rows_list)
    if rows_list_cycled in previous_layouts:
        sequence_start_index = previous_layouts.index(rows_list_cycled)
        sequence = load_list[sequence_start_index:i]
        break
    else:
        previous_layouts.append(rows_list_cycled)
    print(f'\nAfter {i+1} cycles')
    cols_list_cycled = convert_row_col_list(rows_list_cycled)
    load = calculate_load(cols_list_cycled)
    print(f'Load: {load}')
    load_list.append(load)
    # print_dish(rows_list_cycled)
    rows_list = rows_list_cycled.copy()
    i += 1

# find 1000000000th load
# subtract number of items before repeating sequence, then get item number within sequence
sequence_item_no = (1000000000 - sequence_start_index) % len(sequence)
load = sequence[sequence_item_no - 1]


print(f'\n1000000000th Load: {load}')
print('Process complete')
print(f"Process time: {round(time() - start_time, 2)} seconds.")