#!/usr/bin/env python3

import star8


def test_valid_password(password, expected_result):
    result = star8.valid_password(password)
    assert result == expected_result, f'Password = {password}, result = {result}'


if __name__ == '__main__':
    TEST_INPUTS = [
        ('112233', True), ('123444', False), ('111122', True)
    ]

    for i, test_input in enumerate(TEST_INPUTS):
        print(f'====Test {i}====')
        test_valid_password(test_input[0], test_input[1])
        print('Test passed')
