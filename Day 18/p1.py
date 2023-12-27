from time import time

TILE_DICT = {}

TRANSFORM_XY_DICT = {
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, 1),
    'U': (0, -1)
}

MIN_X = 0
MAX_X = 0
MIN_Y = 0
MAX_Y = 0


class Tile:
    def __init__(self, x, y, colour=None, edge=False, interior=False):
        self.x = x
        self.y = y
        self.colour = colour
        self.edge = edge
        self.interior = interior
        self.update_min_max()

    def update_min_max(self):
        global MIN_X
        global MAX_X
        global MIN_Y
        global MAX_Y
        if self.x < MIN_X:
            MIN_X = self.x
        if self.x > MAX_X:
            MAX_X = self.x
        if self.y < MIN_Y:
            MIN_Y = self.y
        if self.y > MAX_Y:
            MAX_Y = self.y


def create_edge(start_x, start_y, direction, distance, colour):
    x = start_x
    y = start_y
    xy_deltas = TRANSFORM_XY_DICT[direction]
    for i in range(distance):
        x = x + xy_deltas[0]
        y = y + xy_deltas[1]
        TILE_DICT[(x, y)] = Tile(x, y, colour=colour, edge=True)

    return x, y


def count_internal_tiles(tile_dict):
    total = 0
    for tile in tile_dict.values():
        if tile.edge:
            total += 1
        elif tile.interior:
            total += 1

    return total


def print_dict(tile_dict, min_x, max_x, min_y, max_y):
    print('\n\n')
    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            if tile_dict[(x, y)].edge or tile_dict[(x, y)].interior:
                line += '#'
            else:
                line += '.'
        print(line)


def main():
    input_list = open('input.txt', 'r').read().splitlines()
    # input_list = open('test.txt', 'r').read().splitlines()

    # create starting tile
    x = 0
    y = 0
    TILE_DICT[(x, y)] = Tile(x, y, edge=True)

    # create edges
    for line in input_list:
        direction = line.split()[0]
        distance = int(line.split()[1])
        colour = line.split()[2]
        x, y = create_edge(x, y, direction, distance, colour)

    # create all other tiles
    for y in range(MIN_Y, MAX_Y + 1):
        for x in range(MIN_X, MAX_X + 1):
            try:
                TILE_DICT[(x, y)]
            except KeyError:
                TILE_DICT[(x, y)] = Tile(x, y)

    print_dict(TILE_DICT, MIN_X, MAX_X, MIN_Y, MAX_Y)



    # fill in interior
    for y in range(MIN_Y, MAX_Y + 1):
        inside = False
        top_edge = False
        bottom_edge = False
        for x in range(MIN_X, MAX_X + 1):

            if TILE_DICT[(x, y)].edge:
                tile_right = TILE_DICT.get((x + 1, y))
                tile_below = TILE_DICT.get((x, y + 1))
                tile_above = TILE_DICT.get((x, y - 1))
                if tile_right is not None and tile_right.edge:
                    if tile_below is not None and tile_below.edge:
                        top_edge = True
                    elif tile_above is not None and tile_above.edge:
                        bottom_edge = True
                elif top_edge:
                    if tile_below is not None and tile_below.edge:
                        top_edge = False
                    if tile_above is not None and tile_above.edge:
                        top_edge = False
                        inside = not inside
                elif bottom_edge:
                    if tile_below is not None and tile_below.edge:
                        bottom_edge = False
                        inside = not inside
                    if tile_above is not None and tile_above.edge:
                        bottom_edge = False
                else:
                    inside = not inside

            if TILE_DICT[(x, y)].edge is False:
                if inside:
                    TILE_DICT[(x, y)].interior = True

    print_dict(TILE_DICT, MIN_X, MAX_X, MIN_Y, MAX_Y)

    total = count_internal_tiles(TILE_DICT)

    print(f'Total internal tiles: {total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")