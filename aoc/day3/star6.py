# https://adventofcode.com/2019/day/3#part2

from aoc.day3.star5 import locations_wire_path, find_intersections


def find_fewest_combined_steps_to_intersection(wire_paths):
    wire_paths = list(map(lambda p: p.split(','), wire_paths.strip().split('\n')))

    locs_wire_1 = locations_wire_path(wire_paths[0])
    locs_wire_2 = locations_wire_path(wire_paths[1])

    intersections = find_intersections(locs_wire_1, locs_wire_2)

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


def answer():
    from pathlib import Path
    curr_dir = Path(__file__).parent.absolute()

    with open(curr_dir / 'input.txt') as input:
        wire_paths = input.read()

    return find_fewest_combined_steps_to_intersection(wire_paths)


if __name__ == '__main__':
    print(answer())
