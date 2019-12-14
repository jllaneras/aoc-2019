#!/usr/bin/env python3

import sys
sys.path.insert(0, '../utils/')

from intcode_computer import Computer


if __name__ == '__main__':
    computer = Computer()

    with open('input.txt') as input:
        computer.run(input.read())
