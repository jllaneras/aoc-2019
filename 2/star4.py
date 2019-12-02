#!/usr/bin/env python3

# https://adventofcode.com/2019/day/2

import star3


if __name__ == '__main__':
    with open('input.txt') as input:
        intcode = [int(n) for n in input.readline().strip().split(',')]

    for noun in range(100):
        for verb in range(100):
            result = star3.compute_intcode(intcode, noun, verb)
            if result[0] == 19690720:
                print(100 * noun + verb)
                exit(0)

    exit(1)
