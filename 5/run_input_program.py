#!/usr/bin/env python3

import intcode_computer


if __name__ == '__main__':
    computer = intcode_computer.Computer()

    with open('input.txt') as input:
        intcode = [int(n) for n in input.readline().strip().split(',')]
        computer.run(intcode)
