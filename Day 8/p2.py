"""
Takes around 250 seconds
"""
from time import time

start_time = time()

input_list = open('input.txt', 'r').read().splitlines()

instructions = input_list.pop(0)
instructions = instructions.replace("L", "0")
instructions = instructions.replace("R", "1")
instructions = list(instructions)
instructions = [int(number) for number in instructions]

# duplicate instructions 1000 times
instructions_bigger = []
for k in range(1000):
    for n in instructions:
        instructions_bigger.append(n)

instructions = instructions_bigger.copy()

# remove empty line
input_list.pop(0)

# make dict of locations and destinations. values are tuples (L, R)
input_dict = {}
for line in input_list:
    line_split = line.split('=')
    tup = line_split[1].replace('(', '').replace(')', '').split(',')
    input_dict[line_split[0].strip()] = (tup[0].strip(), tup[1].strip())

# get start and end location for a complete set of instructions, and track any intermediate steps ending in 'Z'
instruction_set_dict = {}
for location, lr in input_dict.items():
    start_location = location
    z_indices = []
    for i, number in enumerate(instructions):
        location = input_dict[location][number]
        if location.endswith('Z'):
            z_indices.append(i)
    instruction_set_dict[start_location] = (location, z_indices)

# get list of all locations ending in 'A'
start_list = []
for location, lr in input_dict.items():
    if location.endswith('A'):
        start_list.append(location)

# iterate over each location in the starting list to find solution with all locations ending in 'Z'
end = False
location_list = start_list.copy()
steps = 0
while end is False:
    location_list_updated = []
    end = True
    intermediate_z_indices = []
    for location in location_list:
        location_updated = instruction_set_dict[location][0]
        z_indices = instruction_set_dict[location][1]
        intermediate_z_indices.append(z_indices)
        if not location_updated.endswith('Z'):
            end = False
        location_list_updated.append(location_updated)

    # break out if all locations end in 'Z'
    if end:
        steps += len(instructions)
        break

    # check if there is an intermediate step with all locations ending in z
    intermediate = False
    if len(intermediate_z_indices) == len(location_list):
        intermediate_z_indices_first_list = intermediate_z_indices.pop(0)
        for z in intermediate_z_indices_first_list:
            end = True
            intermediate = True
            for intermediate_z_indices_list in intermediate_z_indices:
                if z not in intermediate_z_indices_list:
                    end = False
                    intermediate = False
                    break
                z_steps = z + 1
            if end:
                steps += z_steps
                break

    # increment steps for next iteration and update location list
    if intermediate is False:
        steps += len(instructions)
    location_list = location_list_updated.copy()

    print(f'Steps so far: {steps}')

print(f'Total steps: {steps}')
print('Process complete')
print(f"Process time: {round(time() - start_time, 2)} seconds.")