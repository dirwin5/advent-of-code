from time import time

TILE_DICT = {}

TRANSFORM_XY_DICT = {
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, 1),
    'U': (0, -1)
}

DIRECTION_DICT = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U',
}


def get_next_vertex_xy(start_x, start_y, direction, distance):
    x = start_x
    y = start_y
    xy_deltas = TRANSFORM_XY_DICT[direction]
    x_delta = xy_deltas[0] * distance
    y_delta = xy_deltas[1] * distance
    x = x + x_delta
    y = y + y_delta

    return x, y


def calc_area(vertex_list):
    tot = 0
    for i, vertex in enumerate(vertex_list):
        if i >= len(vertex_list) - 1:
            break
        next_vertex = vertex_list[i + 1]
        x1 = vertex[0]
        y1 = vertex[1]
        x2 = next_vertex[0]
        y2 = next_vertex[1]
        tot += x1 * y2 - x2 * y1

    area = abs(tot / 2)

    return area


def main():
    input_list = open('input.txt', 'r').read().splitlines()
    # input_list = open('test.txt', 'r').read().splitlines()

    # create starting position
    x = 0
    y = 0

    # create vertex list
    distance_total = 0
    vertex_list = [(x, y)]
    for line in input_list:
        hex_code = line.split('#')[1][:-1]
        distance = int(hex_code[:-1], base=16)
        direction = DIRECTION_DICT[int(hex_code[-1:])]
        x, y = get_next_vertex_xy(x, y, direction, distance)
        vertex_list.append((x, y))
        distance_total += distance

    area = calc_area(vertex_list)

    # add area of outer boundary trench
    area += distance_total / 2 + 1

    print(f'Total area: {int(area)}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")