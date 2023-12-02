input_list = open('input.txt', 'r').read().splitlines()

colour_limits = {'red': 12,
                 'green': 13,
                 'blue': 14}

game_dict = {}
for input_line in input_list:
    game_no = int(input_line.split(':')[0].replace('Game ', ''))
    cube_sets = input_line.split(':')[1].split(';')
    set_dict = {}
    for i, cube_set in enumerate(cube_sets):
        cube_picks = cube_set.split(',')
        pick_dict = {}
        for cube_pick in cube_picks:
            cube_no = cube_pick.strip().split(' ')[0]
            cube_colour = cube_pick.strip().split(' ')[1]
            pick_dict[cube_colour] = cube_no
        set_dict[i+1] = pick_dict
    game_dict[game_no] = set_dict

possible_dict = {}
for game_no, set_dict in game_dict.items():
    possible = True
    for pick_no, pick_dict in set_dict.items():
        if possible is False:
            break
        for cube_colour, cube_no in pick_dict.items():
            if colour_limits[cube_colour] < int(cube_no):
                possible = False
                possible_dict[game_no] = False
                break
    if possible is True:
        possible_dict[game_no] = True

total = 0
for game_no, possible in possible_dict.items():
    if possible is True:
        total += game_no

print(f'Total: {total}')
print('Process complete')

