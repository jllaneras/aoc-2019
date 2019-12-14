# https://adventofcode.com/2019/day/1

from math import floor


def calculate_fuel_amount(mass):
    return floor(mass / 3) - 2


def answer():
    from pathlib import Path
    curr_dir = Path(__file__).parent.absolute()

    total_amount = 0
    with open(curr_dir / 'input.txt') as input:
        for mass in input:
            total_amount += calculate_fuel_amount(float(mass))

    return total_amount

if __name__ == '__main__':
    print(answer())
