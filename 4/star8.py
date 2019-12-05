#!/usr/bin/env python3

# https://adventofcode.com/2019/day/4

import star7


def valid_password(password):
    return star7.has_increasing_digits(password) and has_double_digit(password)


def has_double_digit(password):
    result = False
    last_char = None
    num_repetitions = None

    for char in password:
        if char == last_char:
            num_repetitions += 1
        elif num_repetitions == 2:
            break
        else:
            num_repetitions = 1

        last_char = char

    if num_repetitions == 2:
        result = True

    return result


if __name__ == '__main__':
    valid_passwords = 0

    for password in range(158126, 624574):
        if valid_password(str(password)):
            valid_passwords += 1

    print(valid_passwords)
