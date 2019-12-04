#!/usr/bin/env python3

# https://adventofcode.com/2019/day/3

import star5


def find_fewest_combined_steps_to_intersection(wire_paths):
    wire_paths = list(map(lambda p: p.split(','), wire_paths.strip().split('\n')))

    locs_wire_1 = star5.locations_wire_path(wire_paths[0])
    locs_wire_2 = star5.locations_wire_path(wire_paths[1])

    intersections = star5.find_intersections(locs_wire_1, locs_wire_2)

    fewest_comb_steps = None
    for loc in intersections:
        comb_steps = _count_combined_steps(loc, [locs_wire_1, locs_wire_2])
        if fewest_comb_steps == None or comb_steps < fewest_comb_steps:
            fewest_comb_steps = comb_steps

    return fewest_comb_steps


def _count_combined_steps(location_intersection, wire_locations_list):
    combined_steps = 0

    for wire_locations in wire_locations_list:
        steps = 0

        for loc in wire_locations:
            if loc == location_intersection:
                break
            else:
                steps += 1

        combined_steps += steps

    return combined_steps


if __name__ == '__main__':
    with open('input.txt') as input:
        wire_paths = input.read()
        print(find_fewest_combined_steps_to_intersection(wire_paths))
