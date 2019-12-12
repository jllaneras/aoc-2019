#!/usr/bin/env python3

import star11


def test_star11(orbits, expected_number_of_orbits):
    number_of_orbits = star11.count_orbits(orbits)
    assert expected_number_of_orbits == number_of_orbits


if __name__ == '__main__':
    orbits = """
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
"""

    test_star11(orbits, expected_number_of_orbits=42)
    print("Test passed")

