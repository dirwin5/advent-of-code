from time import time


class Tile:
    def __init__(self, tiles, x, y):
        self.x = x
        self.y = y
        self.name = tiles[self.y][self.x]
        self.north_tile_name = tiles[self.y - 1][self.x]
        self.east_tile_name = tiles[self.y][self.x + 1]
        self.south_tile_name = tiles[self.y + 1][self.x]
        self.west_tile_name = tiles[self.y][self.x - 1]
        self.north = False
        self.east = False
        self.south = False
        self.west = False
        self.start_tile = False
        if self.name == 'S':
            self.start_tile = True
        self.get_directions()

    def get_directions(self):
        if self.name == '|':
            self.north = True
            self.south = True
        if self.name == '-':
            self.east = True
            self.west = True
        if self.name == 'L':
            self.north = True
            self.east = True
        if self.name == 'J':
            self.north = True
            self.west = True
        if self.name == '7':
            self.south = True
            self.west = True
        if self.name == 'F':
            self.south = True
            self.east = True
        if self.name == 'S':
            if self.north_tile_name in ['|', '7', 'F']:
                self.north = True
            if self.east_tile_name in ['-', 'J', '7']:
                self.east = True
            if self.south_tile_name in ['|', 'L', 'J']:
                self.south = True
            if self. west_tile_name in ['-', 'L', 'F']:
                self.west = True


def trace(tiles, start_tile, from_direction=None):
    x = start_tile.x
    y = start_tile.y
    if start_tile.north and from_direction != 's':
        direction = 'n'
        y = y - 1
    elif start_tile.east and from_direction != 'w':
        direction = 'e'
        x = x + 1
    elif start_tile.south and from_direction != 'n':
        direction = 's'
        y = y + 1
    elif start_tile.west and from_direction != 'e':
        direction = 'w'
        x = x - 1

    next_tile = Tile(tiles, x, y)
    trace_end = False
    if next_tile.name == 'S':
        trace_end = True

    return trace_end, next_tile, direction


start_time = time()

input_list = open('input.txt', 'r').read().splitlines()
tiles = []
start_x = None
start_y = None
# make 2D list of tiles and find starting tile location
for y, line in enumerate(input_list):
    line_list = list(line)
    tiles.append(line_list)
    if 'S' in line_list:
        start_y = y
        start_x = line_list.index('S')

start_tile = Tile(tiles, start_x, start_y)

ret_tup = trace(tiles, start_tile)
next_tile = ret_tup[1]
direction = ret_tup[2]
steps = 1
while ret_tup[0] is False:
    ret_tup = trace(tiles, next_tile, direction)
    next_tile = ret_tup[1]
    direction = ret_tup[2]
    steps += 1

print(f'Steps: {steps}')
print(f'Steps to middle point: {int(steps/2)}')
print('Process complete')
print(f"Process time: {round(time() - start_time, 2)} seconds.")