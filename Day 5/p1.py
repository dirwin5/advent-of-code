input_str = open('input.txt', 'r').read()

input_list = input_str.split('\n\n')

# get seeds list and convert all to int
seeds_input = input_list.pop(0)
seeds_list = seeds_input.split(':')[1].split()
seeds_list = [int(seed) for seed in seeds_list]

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

# iterate over each seed and do all map conversions
locations_list = []
for seed in seeds_list:
    for current_map in maps_list:
        for line in current_map:
            if seed in range(line[1], line[1] + line[2]):
                seed = line[0] + seed - line[1]
                break
    locations_list.append(seed)

lowest_location = min(locations_list)

print(f'Lowest location: {lowest_location}')
print('Process complete')

