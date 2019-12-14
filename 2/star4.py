#!/usr/bin/env python3

# https://adventofcode.com/2019/day/2

import sys
sys.path.insert(0, '../utils/')

from intcode_computer import Computer

import star3


def main():
    with open('input.txt') as input:
        program = input.read()

    computer = Computer()
    for noun in range(100):
        for verb in range(100):
            computer.load(program)
            computer.state.memory[1] = noun
            computer.state.memory[2] = verb
            computer.run()
            if computer.state.memory[0] == 19690720:
                return 100 * noun + verb

    throw Exception('Solution not found')


if __name__ == '__main__':
    print(main())
