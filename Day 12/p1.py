from time import time
from more_itertools import distinct_permutations


def evaluate_record(record_list, groups_solution):
    i = 0
    current_group_count = groups_solution[i]
    damaged_count = 0
    group_start = False
    group_end = False
    for char in record_list:
        if char == '#':
            group_start = True
            damaged_count += 1
        if char == '.':
            if group_start is True:
                group_end = True
        if group_start is True and group_end is True:
            if damaged_count == current_group_count:
                i += 1
                if i >= len(groups_solution):
                    return True
                current_group_count = groups_solution[i]
                damaged_count = 0
                group_start = False
                group_end = False
                continue
            else:
                return False
        if damaged_count > current_group_count:
            return False

    if i == len(groups_solution) - 1 and damaged_count == current_group_count:
        return True


start_time = time()

input_list = open('input.txt', 'r').read().splitlines()
# input_list = open('test.txt', 'r').read().splitlines()

total = 0
for line in input_list:
    line_split = line.split()
    record = line_split[0]
    groups_solution = line_split[1].split(',')
    groups_solution = [int(number) for number in groups_solution]

    # remove leading or trailing '.' characters
    record = record.strip('.')

    # remove '.' characters beside each other
    while True:
        record_length = len(record)
        record = record.replace('..', '.')
        record_length_new = len(record)
        if record_length == record_length_new:
            break

    record_list = list(record)

    num_chars = len(record_list)
    required_damaged = sum(groups_solution)
    required_operational = num_chars - required_damaged
    known_damaged = record_list.count('#')
    known_operational = record_list.count('.')
    dummy_list = []
    for x in range(required_damaged - known_damaged):
        dummy_list.append('#')
    for x in range(required_operational - known_operational):
        dummy_list.append('.')
    unknowns_count = record_list.count('?')
    unknown_indices = [i for i, x in enumerate(record_list) if x == '?']

    perms = distinct_permutations(dummy_list)
    # for perm in distinct_permutations(required_dummy_str):
    #     print(perm)
    i = 0
    group = groups_solution[1]

    true_perms = []
    for perm in perms:
        perm_indices = zip(unknown_indices, perm)
        record_list_new = record_list.copy()
        for index, perm in perm_indices:
            record_list_new[index] = perm
        result = evaluate_record(record_list_new, groups_solution)
        if result is True:
            true_perms.append(record_list_new)
    print(f'{len(true_perms)}: {true_perms}')
    total += len(true_perms)


print(f'Total: {total}')
print('Process complete')
print(f"Process time: {round(time() - start_time, 2)} seconds.")