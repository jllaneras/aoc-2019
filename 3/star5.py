#!/usr/bin/env python3

# https://adventofcode.com/2019/day/3

import collections


def find_closest_wire_cross_distance(wire_paths):
    grid = collections.OrderedDict()

    wire_paths = list(map(lambda p: p.split(','), wire_paths.strip().split('\n')))
    for wire_index, wire_path in enumerate(wire_paths):
        _store_locations_wire_path(wire_index, wire_path, grid)

    closest_cross_distance = None
    for loc, loc_info in grid.items():
        _, number_of_wires = loc_info
        if number_of_wires > 1:
            cross_distance = _manhattan_distance(loc)
            if cross_distance > 0 and (closest_cross_distance is None or cross_distance < closest_cross_distance):
                closest_cross_distance = cross_distance

    return closest_cross_distance


def _store_locations_wire_path(wire_index, wire_path, grid):
    curr_pos = (0, 0)
    for instruction in wire_path:
        curr_pos =_store_locations_instruction(wire_index, curr_pos, instruction, grid)


def _store_locations_instruction(wire_index, curr_pos, instruction, grid):
    dir = instruction[0]
    distance = int(instruction[1:])
    curr_x, curr_y = curr_pos

    if dir == 'L':
        curr_x -= 1
        for x in range(curr_x, curr_x - distance, -1):
            _store_location(wire_index, (x, curr_y), grid)
            curr_x = x
    elif dir == 'U':
        curr_y += 1
        for y in range(curr_y, curr_y + distance):
            _store_location(wire_index, (curr_x, y), grid)
            curr_y = y
    elif dir == 'R':
        curr_x += 1
        for x in range(curr_x, curr_x + distance):
            _store_location(wire_index, (x, curr_y), grid)
            curr_x = x
    elif dir == 'D':
        curr_y -= 1
        for y in range(curr_y, curr_y - distance, -1):
            _store_location(wire_index, (curr_x, y), grid)
            curr_y = y
    else:
        raise ValueError(f'Invalid direction: {dir}')

    return (curr_x, curr_y)


def _store_location(wire_index, loc, grid):
    loc_wire_index, number_of_wires = grid.get(loc, (None, 0))
    if wire_index != loc_wire_index:
        number_of_wires += 1
        grid[loc] = (wire_index, number_of_wires)


def _manhattan_distance(loc):
    return abs(loc[0]) + abs(loc[1])


if __name__ == '__main__':
    with open('input.txt') as input:
        wire_paths = input.read()
        print(find_closest_wire_cross_distance(wire_paths))
