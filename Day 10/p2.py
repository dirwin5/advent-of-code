from time import time


class Tile:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        self.name = name
        self.north_tile = None
        self.east_tile = None
        self.south_tile = None
        self.west_tile = None
        self.on_trace = False
        self.trace_north = False
        self.trace_east = False
        self.trace_south = False
        self.trace_west = False
        self.channel_entry = False
        self.outside_loop = False
        self.start_tile = False
        if self.name == 'S':
            self.start_tile = True
            self.on_trace = True
        self.get_directions()

    def get_directions(self):
        if self.name == '|':
            self.trace_north = True
            self.trace_south = True
        if self.name == '-':
            self.trace_east = True
            self.trace_west = True
        if self.name == 'L':
            self.trace_north = True
            self.trace_east = True
        if self.name == 'J':
            self.trace_north = True
            self.trace_west = True
        if self.name == '7':
            self.trace_south = True
            self.trace_west = True
        if self.name == 'F':
            self.trace_south = True
            self.trace_east = True

    def get_starting_directions(self):
        if self.name == 'S':
            if self.north_tile.name in ['|', '7', 'F']:
                self.trace_north = True
            if self.east_tile.name in ['-', 'J', '7']:
                self.trace_east = True
            if self.south_tile.name in ['|', 'L', 'J']:
                self.trace_south = True
            if self. west_tile.name in ['-', 'L', 'F']:
                self.trace_west = True


def trace(tile_dict, start_tile, from_direction=None):
    x = start_tile.x
    y = start_tile.y
    direction = None
    if start_tile.trace_north and from_direction != 's':
        direction = 'n'
        y = y - 1
    elif start_tile.trace_east and from_direction != 'w':
        direction = 'e'
        x = x + 1
    elif start_tile.trace_south and from_direction != 'n':
        direction = 's'
        y = y + 1
    elif start_tile.trace_west and from_direction != 'e':
        direction = 'w'
        x = x - 1

    next_tile = tile_dict[x, y]
    next_tile.on_trace = True
    trace_end = False
    if next_tile.name == 'S':
        trace_end = True

    return trace_end, next_tile, direction

def check_for_channels(tile_dict):
    channels_no = 0
    for location, tile in tile_dict.items():
        try:
            if tile.name == '7':
                if tile.east_tile.name in ['F', '|']:
                    tile.channel_entry = True
                    tile.east_tile.channel_entry = True
                    channels_no += 1
                if tile.north_tile.name in ['J', '-']:
                    tile.channel_entry = True
                    tile.north_tile.channel_entry = True
                    channels_no += 1
            if tile.name == 'J':
                if tile.east_tile.name in ['L', '|']:
                    tile.channel_entry = True
                    tile.east_tile.channel_entry = True
                    channels_no += 1
                if tile.south_tile.name in ['7', '-']:
                    tile.channel_entry = True
                    tile.south_tile.channel_entry = True
                    channels_no += 1
            if tile.name == 'L':
                if tile.west_tile.name in ['J', '|']:
                    tile.channel_entry = True
                    tile.west_tile.channel_entry = True
                    channels_no += 1
                if tile.south_tile.name in ['F', '-']:
                    tile.channel_entry = True
                    tile.south_tile.channel_entry = True
                    channels_no += 1
            if tile.name == 'F':
                if tile.west_tile.name in ['7', '|']:
                    tile.channel_entry = True
                    tile.west_tile.channel_entry = True
                    channels_no += 1
                if tile.north_tile.name in ['L', '-']:
                    tile.channel_entry = True
                    tile.north_tile.channel_entry = True
                    channels_no += 1
        except AttributeError as e:
            print(e)

    print(f'Channels: {channels_no}')

def print_dict(dict, max_x, max_y):     # for debugging
    for y in range(max_y):
        line = ''
        for x in range(max_x):
            line += dict[(x, y)].name
        print(line)


start_time = time()

input_list = open('input.txt', 'r').read().splitlines()
max_y = len(input_list) - 1
max_x = len(input_list[0]) - 1

tile_dict = {}
start_x = None
start_y = None
# populate tile_dict
for y, line in enumerate(input_list):
    line_list = list(line)
    for x, char in enumerate(line_list):
        tile_dict[(x, y)] = Tile(char, x, y)
    if 'S' in line_list:
        start_y = y
        start_x = line_list.index('S')

# populate adjacent tiles
for location, tile in tile_dict.items():
    tile.north_tile = tile_dict.get((tile.x, tile.y - 1), None)
    tile.east_tile = tile_dict.get((tile.x + 1, tile.y), None)
    tile.south_tile = tile_dict.get((tile.x, tile.y + 1), None)
    tile.west_tile = tile_dict.get((tile.x - 1, tile.y), None)

# start_tile = Tile(tiles, start_x, start_y)
start_tile = tile_dict[(start_x, start_y)]
start_tile.get_starting_directions()

# iterate through loop from starting tile
next_tile = start_tile
direction = None
# steps = 0
ret_tup = (False, next_tile, direction)
while ret_tup[0] is False:
    ret_tup = trace(tile_dict, next_tile, direction)
    next_tile = ret_tup[1]
    direction = ret_tup[2]
    # steps += 1

# print_dict(tile_dict, max_x, max_y)

# change all tiles not on loop to '.'
for location, tile in tile_dict.items():
    if tile.on_trace is False:
        tile.name = '.'

print_dict(tile_dict, max_x, max_y)

# search for channels between pipes
check_for_channels(tile_dict)

# change tiles outside loop to 0
x = 0
y = 0
current_tile = tile_dict[(x, y)]
if current_tile.name != '.':
    print("Starting point for changing tiles to 0 isn't '.'. Pick a different starting location.")

to_be_tested = [(x, y)]
tiles_tested = []
while len(to_be_tested) > 0:
    current_location = to_be_tested.pop()
    tiles_tested.append(current_location)
    current_tile = tile_dict[current_location]
    current_tile.outside_loop = True
    try:
        if current_tile.north_tile.name == '.':
            current_tile.north_tile.outside_loop = True
            current_tile.north_tile.name = '0'
            to_be_tested.append((current_tile.north_tile.location))
    except AttributeError:
        pass
    try:
        if current_tile.east_tile.name == '.':
            current_tile.east_tile.outside_loop = True
            current_tile.east_tile.name = '0'
            to_be_tested.append((current_tile.east_tile.location))
    except AttributeError:
        pass
    try:
        if current_tile.south_tile.name == '.':
            current_tile.south_tile.outside_loop = True
            current_tile.south_tile.name = '0'
            to_be_tested.append((current_tile.south_tile.location))
    except AttributeError:
        pass
    try:
        if current_tile.west_tile.name == '.':
            current_tile.west_tile.outside_loop = True
            current_tile.west_tile.name = '0'
            to_be_tested.append((current_tile.west_tile.location))
    except AttributeError:
        pass

print_dict(tile_dict, max_x, max_y)


# print(f'Steps: {steps}')
# print(f'Steps to middle point: {int(steps/2)}')
print('Process complete')
print(f"Process time: {round(time() - start_time, 2)} seconds.")