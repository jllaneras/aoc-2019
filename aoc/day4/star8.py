# https://adventofcode.com/2019/day/4

from aoc.day4.star7 import has_increasing_digits


def valid_password(password):
    return has_increasing_digits(password) and has_double_digit(password)


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


def answer():
    number_of_valid_passwords = 0

    for password in range(158126, 624574):
        if valid_password(str(password)):
            number_of_valid_passwords += 1

    return number_of_valid_passwords


if __name__ == '__main__':
    print(answer())
