#!/usr/bin/env python3

# https://adventofcode.com/2019/day/4


def valid_password(password):
    if len(password) != 6:
        return False

    prev_n = None
    double_digit = False
    for char in password:
        n = int(char)
        if prev_n is not None and prev_n > n:
            return False

        if prev_n == n:
            double_digit = True

        prev_n = n

    return double_digit


if __name__ == '__main__':
    valid_passwords = 0

    for password in range(158126, 624574):
        if valid_password(str(password)):
            valid_passwords += 1

    print(valid_passwords)
