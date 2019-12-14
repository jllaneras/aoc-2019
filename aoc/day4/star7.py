# https://adventofcode.com/2019/day/4


def valid_password(password):
    return has_increasing_digits(password) and has_repeated_digits(password)


def has_increasing_digits(password):
    prev_n = None

    for char in password:
        n = int(char)

        if prev_n is not None and prev_n > n:
            return False

        prev_n = n

    return True


def has_repeated_digits(password):
    prev_char = None

    for char in password:
        if prev_char == char:
            return True
        prev_char = char

    return False


def answer():
    number_of_valid_passwords = 0

    for password in range(158126, 624574):
        if valid_password(str(password)):
            number_of_valid_passwords += 1

    return number_of_valid_passwords


if __name__ == '__main__':
    print(answer())
