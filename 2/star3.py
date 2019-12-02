#!/usr/bin/env python3

# https://adventofcode.com/2019/day/2


def compute_intcode(intcode):
    for i in range(0, len(intcode), 4):
        opcode = intcode[i]
        if opcode == 99:
            break

        op1 = intcode[intcode[i+1]]
        op2 = intcode[intcode[i+2]]
        result_pos = intcode[i+3]

        if opcode == 1:
            intcode[result_pos] = op1 + op2
        elif opcode == 2:
            intcode[result_pos] = op1 * op2
        else:
            raise ValueError(f'Unknown operand {opcode} at position {i}')


if __name__ == '__main__':
    with open('input.txt') as input:
        intcode = [int(n) for n in input.readline().strip().split(',')]
        intcode[1] = 12
        intcode[2] = 2
        compute_intcode(intcode)
        print(intcode[0])
