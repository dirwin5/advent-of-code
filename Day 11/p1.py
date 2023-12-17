from time import time
from bisect import bisect_left

class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def print_map(galaxy_dict, len_x, len_y):
    for y in range(len_y):
        line = ''
        for x in range(len_x):
            if galaxy_dict.get((x, y)) is None:
                line += '.'
            else:
                line += '#'
        print(repr(line))


start_time = time()

input_list = open('input.txt', 'r').read().splitlines()

len_y = len(input_list)
len_x = len(input_list[0])

# make and populate dict of galaxies
galaxy_dict = {}
x_list = []
y_list = []
for y, line in enumerate(input_list):
    line_list = list(line)
    for x, char in enumerate(line_list):
        if char == '#':
            galaxy_dict[(x, y)] = Galaxy(x, y)
            x_list.append(x)
            y_list.append(y)

# remove duplicate x and y values
x_set = set(x_list)
y_set = set(y_list)

# find rows and columns with no galaxies
x_empty_list = []
y_empty_list = []

for x in range(len_x):
    if x not in x_set:
        x_empty_list.append(x)

for y in range(len_y):
    if y not in y_set:
        y_empty_list.append(y)

# print_map(galaxy_dict, len_x, len_y)

# expand
galaxy_dict_expanded = {}
for location, galaxy in galaxy_dict.items():
    x_expansion = bisect_left(x_empty_list, galaxy.x)
    galaxy.x = galaxy.x + x_expansion
    y_expansion = bisect_left(y_empty_list, galaxy.y)
    galaxy.y = galaxy.y + y_expansion
    galaxy_dict_expanded[(galaxy.x, galaxy.y)] = galaxy

galaxy_dict = galaxy_dict_expanded.copy()
# print('\n\n')
# print_map(galaxy_dict, len_x + len(x_empty_list), len_y + len(y_empty_list))

# calculate dist between each galaxy
galaxy_list = list(galaxy_dict.values())
total = 0
current_galaxy = galaxy_list.pop()
while len(galaxy_list) > 0:
    for galaxy in galaxy_list:
        x_diff = abs(current_galaxy.x - galaxy.x)
        y_diff = abs(current_galaxy.y - galaxy.y)
        dist = x_diff + y_diff
        total += dist
    current_galaxy = galaxy_list.pop()

print(f'Total: {total}')
print('Process complete')
print(f"Process time: {round(time() - start_time, 2)} seconds.")