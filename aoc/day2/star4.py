# https://adventofcode.com/2019/day/2

from aoc.utils.intcode_computer import Computer

import aoc.day2.star3


def answer():
    from pathlib import Path
    curr_dir = Path(__file__).parent.absolute()

    with open(curr_dir / 'input.txt') as input:
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

    raise Exception('Solution not found')


if __name__ == '__main__':
    print(answer())
