from time import time

TILE_DICT = {}

# nested rules dict for beams.
# first key is tuple direction. Second key is tile_data. Value is list of directions for each outgoing tile
TRANSFORM_DIRECTION_DICT = {
    'r': {'.': ['r'],
          '\\': ['d'],
          '/': ['u'],
          '|': ['u', 'd'],
          '-': ['r']
          },
    'l': {'.': ['l'],
          '\\': ['u'],
          '/': ['d'],
          '|': ['u', 'd'],
          '-': ['l']
          },
    'd': {'.': ['d'],
          '\\': ['r'],
          '/': ['l'],
          '|': ['d'],
          '-': ['r', 'l']
          },
    'u': {'.': ['u'],
          '\\': ['l'],
          '/': ['r'],
          '|': ['u'],
          '-': ['r', 'l']
          }
}

# rules for xy modifications based on outgoing direction
TRANSFORM_XY_DICT = {
    'r': (1, 0),
    'l': (-1, 0),
    'd': (0, 1),
    'u': (0, -1)
}

class Tile:
    def __init__(self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
        self.energised = False
        self.input_directions = []


def calc_next_tiles(current_tile, direction, max_x, max_y):
    current_tile.energised = True
    next_tiles = []
    # check if we've entered this tile from this direction before
    if direction in current_tile.input_directions:
        return next_tiles
    current_tile.input_directions.append(direction)

    transform_direction_list = TRANSFORM_DIRECTION_DICT[direction][current_tile.data]
    for out_direction in transform_direction_list:
        xy_deltas = TRANSFORM_XY_DICT[out_direction]
        x = current_tile.x + xy_deltas[0]
        y = current_tile.y + xy_deltas[1]
        if 0 <= x <= max_x and 0 <= y <= max_y:
            next_tiles.append((TILE_DICT[x, y], out_direction))

    return next_tiles


def main():
    input_list = open('input.txt', 'r').read().splitlines()
    # input_list = open('test.txt', 'r').read().splitlines()

    max_x = len(input_list[0]) - 1
    max_y = len(input_list) - 1

    # populate TILE_DICT
    for i, line in enumerate(input_list):
        for j, char in enumerate(line):
            TILE_DICT[(j, i)] = Tile(char, j, i)

    # list for recursive search. List of tuples in format (Tile, beam direction)
    tile_list = [(TILE_DICT[0, 0], 'r')]
    while len(tile_list) > 0:
        current_tile, direction = tile_list.pop()
        next_tiles = calc_next_tiles(current_tile, direction, max_x, max_y)
        for tile in next_tiles:
            tile_list.append(tile)

    total = 0
    for tile in TILE_DICT.values():
        if tile.energised is True:
            total += 1

    print(f'\nTotal: {total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")