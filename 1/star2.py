#!/usr/bin/env python3

# https://adventofcode.com/2019/day/1

import star1


def calculate_fuel_amount(mass):
    total_amount = 0

    while True:
        amount = star1.calculate_fuel_amount(mass)
        if amount > 0:
            total_amount += amount
            mass = amount
        else:
            break

    return total_amount


if __name__ == '__main__':
    total_amount = 0
    with open('input.txt') as input:
        for mass in input:
            total_amount += calculate_fuel_amount(float(mass))

    print(total_amount)
