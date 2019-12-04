#!/usr/bin/env python3

# https://adventofcode.com/2019/day/3

import collections


def calculate_distance_to_closest_intersection(wire_paths):
    wire_paths = list(map(lambda p: p.split(','), wire_paths.strip().split('\n')))

    locs_wire_1 = locations_wire_path(wire_paths[0])
    locs_wire_2 = locations_wire_path(wire_paths[1])

    intersections = find_intersections(locs_wire_1, locs_wire_2)

    closest_distance = None
    for loc in intersections:
        distance = _manhattan_distance(loc)
        if distance > 0 and (closest_distance is None or distance < closest_distance):
            closest_distance = distance

    return closest_distance


def locations_wire_path(wire_path):
    locations = [(0, 0)]

    for instruction in wire_path:
        curr_pos = locations[-1]
        locations.extend(_locations_instruction(curr_pos, instruction))

    return locations


def find_intersections(locs_wire_1, locs_wire_2):
    intersections = set()
    set_locs_wire_2 = set(locs_wire_2)

    for loc in locs_wire_1:
        if loc != (0, 0) and loc in set_locs_wire_2:
            intersections.add(loc)

    return intersections

def _locations_instruction(curr_pos, instruction):
    curr_x, curr_y = curr_pos
    dir = instruction[0]
    distance = int(instruction[1:])
    locations = []

    if dir == 'L':
        curr_x -= 1
        for x in range(curr_x, curr_x - distance, -1):
            locations.append((x, curr_y))
            curr_x = x
    elif dir == 'U':
        curr_y += 1
        for y in range(curr_y, curr_y + distance):
            locations.append((curr_x, y))
            curr_y = y
    elif dir == 'R':
        curr_x += 1
        for x in range(curr_x, curr_x + distance):
            locations.append((x, curr_y))
            curr_x = x
    elif dir == 'D':
        curr_y -= 1
        for y in range(curr_y, curr_y - distance, -1):
            locations.append((curr_x, y))
            curr_y = y
    else:
        raise ValueError(f'Invalid direction: {dir}')

    return locations


def _manhattan_distance(loc):
    return abs(loc[0]) + abs(loc[1])


if __name__ == '__main__':
    with open('input.txt') as input:
        wire_paths = input.read()
        print(calculate_distance_to_closest_intersection(wire_paths))
