from random import choice, shuffle
from string import (
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase,
    punctuation,
    digits as ascii_digits,
)


def letter(length=1):
    return "".join(choice(ascii_letters) for _ in range(length))


def lower_case(length=1):
    return "".join(choice(ascii_lowercase) for _ in range(length))


def upper_case(length=1):
    return "".join(choice(ascii_uppercase) for _ in range(length))


def digit(length=1):
    return "".join(choice(ascii_digits) for _ in range(length))


def symbol(length=1):
    return "".join(choice(punctuation) for _ in range(length))


def all_ascii(length=1):
    return "".join(
        choice(ascii_letters + ascii_digits + punctuation) for _ in range(length)
    )


def password(length):
    char_sequence = [
        choice(ascii_letters + ascii_digits + punctuation) for _ in range(length)
    ]
    shuffle(char_sequence)
    return "".join(char_sequence)
