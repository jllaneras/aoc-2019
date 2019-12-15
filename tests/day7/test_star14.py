import pytest

from aoc.day7.star14 import amplify_output, answer
from aoc.utils.intcode_computer import Computer

TEST_INPUTS = [
    (
        '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5',
        (9,8,7,6,5),
        139629729
    ),
    (
        '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10',
        (9,7,8,5,6),
        18216
    )
]

@pytest.mark.parametrize('intcode_program,phase_setting,expected_output', TEST_INPUTS)
def test_amplify_output(intcode_program, phase_setting, expected_output):
    computer = Computer()
    computer.load(intcode_program)
    assert expected_output == amplify_output(computer, phase_setting)

# def test_answer():
#     assert 368584 == answer()
