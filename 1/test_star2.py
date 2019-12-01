#!/usr/bin/env python3
import star2


def test_calculate_fuel_amount(mass, expected_amount):
    actual_amount = star2.calculate_fuel_amount(mass)
    assert expected_amount == actual_amount, f'{mass} -> expected = {expected_amount}, actual = {actual_amount}'


if __name__ == '__main__':
    TEST_INPUTS = [
        (14, 2),
        (1969, 966),
        (100756, 50346)
    ]

    for i in TEST_INPUTS:
        test_calculate_fuel_amount(mass=i[0], expected_amount=i[1])

    print('Tests passed')
