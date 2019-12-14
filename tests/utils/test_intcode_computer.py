import pytest

from aoc.utils.intcode_computer import Computer

TEST_INPUTS = [
    (
        '1,9,10,3,2,3,11,0,99,30,40,50',
        [3500,9,10,70,2,3,11,0,99,30,40,50]
    ),
    (
        '1,0,0,0,99',
        [2,0,0,0,99]
    ),
    (
        '2,3,0,3,99',
        [2,3,0,6,99]
    ),
    (
        '2,4,4,5,99,0',
        [2,4,4,5,99,9801]
    ),
    (
        '1,1,1,4,99,5,6,0,99',
        [30,1,1,4,2,5,6,0,99]
    ),
    (
        '1002,4,3,4,33',
        [1002,4,3,4,99]
    )
]


@pytest.mark.parametrize('intcode,expected_result', TEST_INPUTS)
def test_compute_intcode(intcode, expected_result):
    computer = Computer()

    computer.run(intcode)
    result = computer.state.memory

    assert len(result) == len(expected_result)

    for i in range(len(result)):
        assert expected_result[i] == result[i]
