import unittest
from unittest.mock import patch

from aoc.day5.run_input_program import answer

@patch('builtins.input', lambda *args: '1')
def test_answer():
    assert 9006673 == answer()
