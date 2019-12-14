#!/usr/bin/env python3

import pytest

from aoc.day4.star7 import valid_password, answer

TEST_INPUTS = [
    ('122345', True), ('111123', True), ('111111', True), ('223450', False),
    ('123789', False)
]


@pytest.mark.parametrize('password,expected_result', TEST_INPUTS)
def test_valid_password(password, expected_result):
    result = valid_password(password)
    assert expected_result == result


def test_answer():
    assert 1665 == answer()
