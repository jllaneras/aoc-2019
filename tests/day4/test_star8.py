#!/usr/bin/env python3

import pytest

from aoc.day4.star8 import valid_password, answer

TEST_INPUTS = [
    ('112233', True), ('123444', False), ('111122', True)
]


@pytest.mark.parametrize('password,expected_result', TEST_INPUTS)
def test_valid_password(password, expected_result):
    result = valid_password(password)
    assert result == expected_result, f'Password = {password}, result = {result}'


def test_answer():
    assert 1131 == answer()
