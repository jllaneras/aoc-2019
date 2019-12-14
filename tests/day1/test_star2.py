#!/usr/bin/env python3

import pytest

from aoc.day1.star2 import calculate_fuel_amount, answer


TEST_INPUTS = [
    (14, 2),
    (1969, 966),
    (100756, 50346)
]


@pytest.mark.parametrize('mass,expected_amount', TEST_INPUTS)
def test_calculate_fuel_amount(mass, expected_amount):
    actual_amount = calculate_fuel_amount(mass)
    assert expected_amount == actual_amount


def test_answer():
    assert 5362136 == answer()
