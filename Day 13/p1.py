from time import time


def create_row_list(pattern):
    rows_list = []
    pattern_list = pattern.split('\n')
    for i, item in enumerate(pattern_list):
        rows_list.append(item)
    return rows_list


def create_col_list(pattern):
    cols_list = []
    pattern_list = pattern.split('\n')
    for i in range(len(pattern_list[0])):
        col_str = ''
        for item in pattern_list:
            col_str += item[i]
        cols_list.append(col_str)
    return cols_list


def check_mirror(items_list):
    i = 0
    while i < len(items_list) - 1:
        index1 = i
        index2 = i + 1
        prev_item = items_list[index1]
        next_item = items_list[index2]
        if prev_item == next_item:
            mirror = True
            index1 -= 1
            index2 += 1
            # check next rows either side too
            while index1 >= 0 and index2 < len(items_list):
                prev_item = items_list[index1]
                next_item = items_list[index2]
                if prev_item != next_item:
                    mirror = False
                    break
                index1 -= 1
                index2 += 1
            if mirror is True:
                return True, i + 1
        i += 1

    return False, None


start_time = time()

input_str = open('input.txt', 'r').read()
# input_str = open('test.txt', 'r').read()

input_list = input_str.split('\n\n')

total = 0
for pattern in input_list:
    rows_list = create_row_list(pattern)
    row_result = check_mirror(rows_list)
    if row_result[0] is True:
        total += row_result[1] * 100
        continue
    cols_list = create_col_list(pattern)
    col_result = check_mirror(cols_list)
    if col_result[0] is True:
        total += col_result[1]
    else:
        print('Did not find mirror line')


print(f'Total: {total}')
print('Process complete')
print(f"Process time: {round(time() - start_time, 2)} seconds.")