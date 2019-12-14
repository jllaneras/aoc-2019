#!/usr/bin/env python3

import pytest

from aoc.day3.star6 import find_fewest_combined_steps_to_intersection, answer

TEST_INPUTS = [
    (
        'R8,U5,L5,D3\nU7,R6,D4,L4',
        30
    ),
    (
        'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83',
        610
    ),
    (
        'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7',
        410
    )
]


@pytest.mark.parametrize('wire_paths,expected_steps', TEST_INPUTS)
def test_find_fewest_combined_steps_to_intersection(wire_paths, expected_steps):
    number_of_steps = find_fewest_combined_steps_to_intersection(wire_paths)
    assert expected_steps == number_of_steps


def test_answer():
    assert 7534 == answer()
