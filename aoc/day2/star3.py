# https://adventofcode.com/2019/day/2

from aoc.utils.intcode_computer import Computer


def answer():
    from pathlib import Path
    curr_dir = Path(__file__).parent.absolute()

    with open(curr_dir / 'input.txt') as input:
        computer = Computer()
        computer.load(input.read())
        computer.state.memory[1] = 12
        computer.state.memory[2] = 2
        result = computer.run()
        return computer.state.memory[0]


if __name__ == '__main__':
    print(answer())
