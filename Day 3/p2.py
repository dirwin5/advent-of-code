import re

input_list = open('input.txt', 'r').read().splitlines()

total = 0
gears_dict = {}
for line_no, input_line in enumerate(input_list):
    numbers_list = list(filter(None, re.split(r'\D', input_line)))
    search_start_index = 0
    for number in numbers_list:
        start_index = input_line.find(number, search_start_index)
        end_index = start_index + len(number)
        search_start_index = end_index + 1
        index_query_range = (max(start_index - 1, 0), end_index + 1)
        # get string to check for symbols from line above, below and current line
        for line in [line_no - 1, line_no, line_no + 1]:
            if line < 0:
                continue
            if line >= len(input_list):
                continue
            query_str = input_list[line][index_query_range[0]:index_query_range[1]]
            gears_no = query_str.count('*')
            if gears_no > 0:
                for i, char in enumerate(query_str):
                    if char == '*':
                        gear_location = (line, i + index_query_range[0])
                        # gear_info is a list in format [no of adjacent numbers, [list of numbers]]
                        gear_info = gears_dict.get(gear_location)
                        if gear_info is None:
                            adjacent_no = 1
                            adjacent_number_list = [int(number)]
                            gears_dict[gear_location] = [adjacent_no, adjacent_number_list]
                        else:
                            gear_info[0] += 1
                            gear_info[1].append(int(number))

for gear, gear_info in gears_dict.items():
    if gear_info[0] == 2:
        gear_ratio = gear_info[1][0] * gear_info[1][1]
        total += gear_ratio

print(f'Total: {total}')
print('Process complete')