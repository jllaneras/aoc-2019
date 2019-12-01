#!/usr/bin/env python3

import star1


def test_calculate_fuel_amount(mass, expected_amount):
    actual_amount = star1.calculate_fuel_amount(mass)
    assert expected_amount == actual_amount, f'{mass} -> expected = {expected_amount}, actual = {actual_amount}'


if __name__ == '__main__':
    TEST_INPUTS = [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583)
    ]

    for i in TEST_INPUTS:
        test_calculate_fuel_amount(mass=i[0], expected_amount=i[1])

    print('Tests passed')
