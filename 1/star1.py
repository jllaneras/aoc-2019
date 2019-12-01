#!/usr/bin/env python3

# https://adventofcode.com/2019/day/1

from math import floor


def calculate_fuel_amount(mass):
    return floor(mass / 3) - 2


if __name__ == '__main__':
    total_amount = 0
    with open('input.txt') as input:
        for mass in input:
            total_amount += calculate_fuel_amount(float(mass))

    print(total_amount)
