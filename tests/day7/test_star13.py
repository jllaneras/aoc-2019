import pytest

from aoc.day7.star13 import amplify_output, answer

TEST_INPUTS = [
    (
        '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0',
        (4,3,2,1,0),
        43210
    ),
    (
        '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0',
        (0,1,2,3,4),
        54321
    ),
    (
        '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0',
        (1,0,4,3,2),
        65210
    )
]

@pytest.mark.parametrize('intcode_program,phase_setting,expected_output', TEST_INPUTS)
def test_amplify_output(intcode_program, phase_setting, expected_output):
    assert expected_output == amplify_output(intcode_program, phase_setting)

def test_answer():
    assert 368584 == answer()
