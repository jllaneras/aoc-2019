#!/usr/bin/env python3

import star12


def test_min_orbit_transfers_between_you_and_santa(orbit_map, expected_result):
    result = star12.min_orbit_transfers_between_you_and_santa(orbit_map)
    assert result == expected_result, f'{result} != {expected_result}'


if __name__ == '__main__':
    orbit_map = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""
    test_min_orbit_transfers_between_you_and_santa(orbit_map, 4)
    print('Test passed')
