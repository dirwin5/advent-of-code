from time import time


def create_col_list(input_list):
    cols_list = []
    for i in range(len(input_list[0])):
        col_str = ''
        for item in input_list:
            col_str += item[i]
        cols_list.append(col_str)
    return cols_list


def tilt(items_list):
    items_list_tilted = []
    for item in items_list:
        item = list(item)
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


start_time = time()

input_list = open('input.txt', 'r').read().splitlines()
# input_list = open('test.txt', 'r').read().splitlines()

cols_list = create_col_list(input_list)
cols_list_tilted = tilt(cols_list)
total = calculate_load(cols_list_tilted)


print(f'Total: {total}')
print('Process complete')
print(f"Process time: {round(time() - start_time, 2)} seconds.")