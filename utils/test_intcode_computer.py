#!/usr/bin/env python3

import intcode_computer


def test_compute_intcode(intcode, expected_result):
    computer = intcode_computer.Computer()

    computer.run(intcode)
    actual_result = computer.state.memory

    assert len(actual_result) == len(expected_result),f'len(actual_result) is {len(actual_result)} but len(expected_result) is {len(expected_result)}'

    for i in range(len(intcode)):
        assert actual_result[i] == expected_result[i], f'actual_result[{i}] is {actual_result[i]} but expected_result[{i}] is {expected_result[i]}'


if __name__ == '__main__':
    TEST_INPUTS = [
        (
            [1,9,10,3,2,3,11,0,99,30,40,50],
            [3500,9,10,70,2,3,11,0,99,30,40,50]
        ),
        (
            [1,0,0,0,99],
            [2,0,0,0,99]
        ),
        (
            [2,3,0,3,99],
            [2,3,0,6,99]
        ),
        (
            [2,4,4,5,99,0],
            [2,4,4,5,99,9801]
        ),
        (
            [1,1,1,4,99,5,6,0,99],
            [30,1,1,4,2,5,6,0,99]
        ),
        (
            [1002,4,3,4,33],
            [1002,4,3,4,99]
        )
    ]

    for i, test_input in enumerate(TEST_INPUTS):
        intcode = test_input[0]
        expected_result = test_input[1]

        print(f'====Test {i}====')
        print(f'intcode =         {intcode}')
        print(f'expected result = {expected_result}')
        test_compute_intcode(intcode, expected_result)
        print('Test passed')
