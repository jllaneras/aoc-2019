#!/usr/bin/env python3

# https://adventofcode.com/2019/day/2

import sys
sys.path.insert(0, '../utils/')

from intcode_computer import Computer


def main():
    with open('input.txt') as input:
        computer = Computer()
        computer.load(input.read())
        computer.state.memory[1] = 12
        computer.state.memory[2] = 2
        result = computer.run()
        return computer.state.memory[0]


if __name__ == '__main__':
    print(main())
