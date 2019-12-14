#!/usr/bin/env python3

import pytest

from aoc.day1.star1 import calculate_fuel_amount, answer

TEST_INPUTS = [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583)
]


@pytest.mark.parametrize('mass,expected_amount', TEST_INPUTS)
def test_calculate_fuel_amount(mass, expected_amount):
    actual_amount = calculate_fuel_amount(mass)
    assert expected_amount == actual_amount


def test_answer():
    assert 3576689 == answer()
