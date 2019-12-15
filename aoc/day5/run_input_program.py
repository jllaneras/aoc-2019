from aoc.utils.intcode_computer import Computer


def run(input_value):
    computer = Computer()
    from pathlib import Path
    curr_dir = Path(__file__).parent.absolute()
    with open(curr_dir / 'input.txt') as input:
        computer.load(input.read())
        computer.input(input_value)
        computer.run(input.read())

    return computer.last_output()
