#!/usr/bin/env python3

import star7


def test_valid_password(password, expected_result):
    result = star7.valid_password(password)
    assert result == expected_result, f'Password = {password}, result = {result}'


if __name__ == '__main__':
    TEST_INPUTS = [
        ('122345', True), ('111123', True), ('111111', True), ('223450', False),
        ('123789', False)
    ]

    for i, test_input in enumerate(TEST_INPUTS):
        print(f'====Test {i}====')
        test_valid_password(test_input[0], test_input[1])
        print('Test passed')
