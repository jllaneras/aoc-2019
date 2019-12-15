# https://adventofcode.com/2019/day/7#part2

import itertools

from aoc.utils.intcode_computer import Computer

AVAILABLE_PHASE_SETTINGS = [5, 6, 7, 8, 9]

def max_amplified_output(intcode_program):
    all_phase_settings = list(itertools.permutations(AVAILABLE_PHASE_SETTINGS))
    computer = Computer()
    computer.load(intcode_program)

    max_output = None
    for phase_setting in all_phase_settings:
        output = amplify_output(computer, phase_setting)

        if max_output is None or output > max_output:
            max_output = output

    return max_output


def amplify_output(computer, phase_setting):
    i = 0
    while not computer.program_completed():
        computer.run()

        if computer.input_required() and i < len(phase_setting):
            print(f'phase setting {i} -> {phase_setting[i]}')
            computer.input(phase_setting[i % len(phase_setting)])
            computer.run()

        if computer.input_required():
            last_output = computer.last_output() if i > 0 else 0
            print(f'last output {last_output} to next input (i = {i})')
            computer.input(last_output)

        i += 1

    return computer.last_output()


def answer():
    from pathlib import Path
    curr_dir = Path(__file__).parent.absolute()

    with open(curr_dir / 'input.txt') as input:
        input_program = input.read()

    return max_amplified_output(input_program)

if __name__ == '__main__':
    print(answer())
