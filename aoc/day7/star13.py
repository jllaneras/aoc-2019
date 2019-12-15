# https://adventofcode.com/2019/day/7

import itertools

from aoc.utils.intcode_computer import Computer

AVAILABLE_PHASE_SETTINGS = [0, 1, 2, 3, 4]

def max_amplified_output(intcode_program):
    all_phase_settings = list(itertools.permutations(AVAILABLE_PHASE_SETTINGS))

    max_output = None
    for phase_setting in all_phase_settings:
        output = amplify_output(intcode_program, phase_setting)

        if max_output is None or output > max_output:
            max_output = output

    return max_output


def amplify_output(intcode_program, phase_setting):
    computer = Computer()
    last_output = 0

    for setting in phase_setting:
        computer.load(intcode_program)
        computer.input(setting)
        computer.input(last_output)
        computer.run()
        last_output = computer.last_output()

    return last_output


def answer():
    from pathlib import Path
    curr_dir = Path(__file__).parent.absolute()

    with open(curr_dir / 'input.txt') as input:
        input_program = input.read()

    return max_amplified_output(input_program)

if __name__ == '__main__':
    print(answer())
