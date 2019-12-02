#!/usr/bin/env python3

# https://adventofcode.com/2019/day/2


def compute_intcode(intcode, input1=None, input2=None):
    output = intcode.copy()

    if input1 is not None:
        output[1] = input1
    if input2 is not None:
        output[2] = input2

    for i in range(0, len(output), 4):
        opcode = output[i]
        if opcode == 99:
            break

        op1 = output[output[i+1]]
        op2 = output[output[i+2]]
        result_pos = output[i+3]

        if opcode == 1:
            output[result_pos] = op1 + op2
        elif opcode == 2:
            output[result_pos] = op1 * op2
        else:
            raise ValueError(f'Unknown operand {opcode} at position {i}')

    return output


if __name__ == '__main__':
    with open('input.txt') as input:
        intcode = [int(n) for n in input.readline().strip().split(',')]
        result = compute_intcode(intcode, 12, 2)
        print(result[0])
