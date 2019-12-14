#!/usr/bin/env python3

from aoc.day6.star12 import min_orbit_transfers_between_you_and_santa, answer


def test_min_orbit_transfers_between_you_and_santa():
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
    result = min_orbit_transfers_between_you_and_santa(orbit_map)
    assert 4 == result


def test_answer():
    assert 379 == answer()
