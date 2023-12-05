"""
Still pretty slow, but much faster than first attempt.
"""

input_str = open('input.txt', 'r').read()

input_list = input_str.split('\n\n')

# get seeds list and convert all to int
seeds_input = input_list.pop(0)
seeds_list_raw = seeds_input.split(':')[1].split()
seeds_list_raw = [int(seed) for seed in seeds_list_raw]
seeds_list = []
for i, number in enumerate(seeds_list_raw):
    # even indices
    if i % 2 == 0:
        start_seed = number
    # odd indices
    else:
        end_seed = start_seed + number
        seeds_list.append((start_seed, end_seed))


# get numbers in each map and convert values to int
maps_list = []
for map_input in input_list:
    all_lines = map_input.split('\n')
    all_lines.pop(0)
    current_map = []
    for line in all_lines:
        line_numbers = line.split()
        line_numbers = [int(number) for number in line_numbers]
        current_map.append(line_numbers)
    maps_list.append(current_map)

# Start with location 0 and increment upwards until we find a seed number in our input list
lowest_location = None
location = 0
while lowest_location is None:
    seed = location
    for current_map in reversed(maps_list):
        for line in current_map:
            if seed in range(line[0], line[0] + line[2]):
                seed = line[1] + seed - line[0]
                break
    if location % 100000 == 0:
        print(f'Location {location} has seed number {seed}')
    for seed_list in seeds_list:
        if seed in range(seed_list[0], seed_list[1]):
            lowest_location = location
    if lowest_location is None:
        location += 1

print(f'Lowest location: {lowest_location}')
print('Process complete')

