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


def count_internal_tiles(tile_dict):
    total = 0
    for tile in tile_dict.values():
        if tile.name == 'I':
            total += 1

    return total


def print_dict(dict, max_x, max_y):
    print('\n\n')
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
ret_tup = (False, next_tile, direction)
while ret_tup[0] is False:
    ret_tup = trace(tile_dict, next_tile, direction)
    next_tile = ret_tup[1]
    direction = ret_tup[2]

# print_dict(tile_dict, max_x, max_y)

# change all tiles not on loop to '.'
for location, tile in tile_dict.items():
    if tile.on_trace is False:
        tile.name = '.'

print_dict(tile_dict, max_x, max_y)

# check if . characters are inside or outside loop
for y in range(max_y + 1):
    outside = True
    top_edge = False
    bottom_edge = False
    for x in range(max_x + 1):
        if tile_dict[(x, y)].name == '.':
            if outside:
                tile_dict[(x, y)].name = 'O'
            else:
                tile_dict[(x, y)].name = 'I'
        if tile_dict[(x, y)].name == '|':
            if outside:
                outside = False
            else:
                outside = True
        if tile_dict[(x, y)].name == 'F':
            top_edge = True
        if tile_dict[(x, y)].name == 'L':
            bottom_edge = True
        if tile_dict[(x, y)].name == '7':
            if top_edge:
                top_edge = False
            if bottom_edge:
                bottom_edge = False
                if outside:
                    outside = False
                else:
                    outside = True
        if tile_dict[(x, y)].name == 'J':
            if top_edge:
                top_edge = False
                if outside:
                    outside = False
                else:
                    outside = True
            if bottom_edge:
                bottom_edge = False

print_dict(tile_dict, max_x, max_y)

total = count_internal_tiles(tile_dict)


print(f'Total internal tiles: {total}')
print('Process complete')
print(f"Process time: {round(time() - start_time, 2)} seconds.")