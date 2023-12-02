input_list = open('input.txt', 'r').read().splitlines()

colour_limits = {'red': 12,
                 'green': 13,
                 'blue': 14}

game_dict = {}
power_dict = {}
for input_line in input_list:
    game_no = int(input_line.split(':')[0].replace('Game ', ''))
    cube_sets = input_line.split(':')[1].split(';')
    set_dict_max = {'red': 0,
                    'green': 0,
                    'blue': 0}
    for i, cube_set in enumerate(cube_sets):
        cube_picks = cube_set.split(',')
        for cube_pick in cube_picks:
            cube_no = cube_pick.strip().split(' ')[0]
            cube_colour = cube_pick.strip().split(' ')[1]
            if int(cube_no) > set_dict_max[cube_colour]:
                set_dict_max[cube_colour] = int(cube_no)
    game_dict[game_no] = set_dict_max
    power = 1
    for colour, cube_no in set_dict_max.items():
        power = power * cube_no
    power_dict[game_no] = power

total = 0
for game_no, power in power_dict.items():
    total += power

print(f'Total: {total}')
print('Process complete')

