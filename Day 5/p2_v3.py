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

# iterate over each seed and do all map conversions
# locations_list = []
lowest_location = None
for seed_pair in seeds_list:
    seed = seed_pair[0]
    print(f'Starting seed {seed}')
    while seed < seed_pair[1]:
        location = seed
        min_to_next_map = None
        for current_map in maps_list:
            no_map_min = None
            for i, line in enumerate(current_map):
                source_start = line[1]
                dest_start = line[0]
                range_length = line[2]
                source_end = source_start + range_length
                if location in range(source_start, source_end):
                    count_to_map_end = source_end - location
                    location = dest_start + location - source_start
                    if min_to_next_map is None or count_to_map_end < min_to_next_map:
                        min_to_next_map = count_to_map_end
                    break
                else:
                    if location < source_start:
                        gap_to_source_start = source_start - location
                        if no_map_min is None or gap_to_source_start < no_map_min:
                            no_map_min = gap_to_source_start
                if i == len(current_map) - 1:
                    if min_to_next_map is None or no_map_min < min_to_next_map:
                        min_to_next_map = no_map_min

        if lowest_location is None or location < lowest_location:
            lowest_location = location
        seed = seed + min_to_next_map

print(f'Lowest location: {lowest_location}')
print('Process complete')

