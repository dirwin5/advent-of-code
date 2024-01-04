from time import time
from dataclasses import dataclass

TILES_DICT = {}

TRANSFORM_XY_LIST = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


@dataclass(frozen=True)
class Tile:
    name: str
    x: int
    y: int


def main():
    input_list = open('input.txt', 'r').read().splitlines()
    # input_list = open('test.txt', 'r').read().splitlines()

    max_x = len(input_list[0]) - 1
    max_y = len(input_list) - 1

    # populate TILES_DICT and find starting tile
    start_x: int
    start_y: int
    for y, line in enumerate(input_list):
        for x, char in enumerate(line):
            TILES_DICT[(x, y)] = Tile(char, x, y)
            if char == 'S':
                start_x = x
                start_y = y

    required_steps = 64
    reachable_tiles = [TILES_DICT[(start_x, start_y)]]

    # take x steps
    for i in range(required_steps):
        reachable_tiles_new = []
        for tile in reachable_tiles:
            for transform in TRANSFORM_XY_LIST:
                x = tile.x + transform[0]
                y = tile.y + transform[1]
                if x in range(0, max_x) and y in range(0, max_y):
                    if TILES_DICT[(x, y)].name in ['.', 'S']:
                        reachable_tiles_new.append(TILES_DICT[(x, y)])

        reachable_tiles = list(set(reachable_tiles_new.copy()))

    print(f'Total reachable tiles in {required_steps} steps: {len(reachable_tiles)}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
