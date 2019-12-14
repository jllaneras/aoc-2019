#!/usr/bin/env python3

from aoc.day6.star11 import count_orbits, answer


def test_count_orbits():
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
    number_of_orbits = count_orbits(orbits)
    assert 42 == number_of_orbits


def test_answer():
    assert 200001 == answer()
