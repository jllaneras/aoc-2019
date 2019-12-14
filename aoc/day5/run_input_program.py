# https://adventofcode.com/2019/day/5

from aoc.utils.intcode_computer import Computer


def answer():
    computer = Computer()
    from pathlib import Path
    curr_dir = Path(__file__).parent.absolute()
    with open(curr_dir / 'input.txt') as input:
        computer.run(input.read())

    return computer.state.last_output

if __name__ == '__main__':
    print(answer())
