import re

input_list = open('input.txt', 'r').read().splitlines()

total = 0
for line_no, input_line in enumerate(input_list):
    numbers_list = list(filter(None, re.split(r'\D', input_line)))
    search_start_index = 0
    for number in numbers_list:
        part_number = False
        start_index = input_line.find(number, search_start_index)
        end_index = start_index + len(number)
        search_start_index = end_index + 1
        index_query_range = (max(start_index - 1, 0), end_index + 1)
        # get string to check for symbols from line above, below and current line
        for line in [line_no - 1, line_no, line_no + 1]:
            if line < 0:
                continue
            try:
                query_str = input_list[line][index_query_range[0]:index_query_range[1]]
            except IndexError:
                continue
            symbol_list = re.findall(r'[^\d.]', query_str)
            if len(symbol_list) > 0:
                part_number = True
                break
        if part_number is True:
            total += int(number)

print(f'Total: {total}')
print('Process complete')