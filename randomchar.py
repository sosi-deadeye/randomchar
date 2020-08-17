#!/usr/bin/env python3

"""
This module is designed to make the task of generating random strings as easy as calling a function.
To generate a password all you have to do is call `randomchar.password(8)`
where 8 is the required length of the password.

Normally, to do this without randomchar you will have to write verbose code of up to 5 lines or more,
randomchar shortens that up to one short line.
"""

from random import choice, shuffle
from string import (
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase,
    punctuation,
    digits as ascii_digits,
)


def letter(length: int = 1) -> str:
    """
    Return random ascii_letters

    :param length: then length of the returned str
    """
    return "".join(choice(ascii_letters) for _ in range(length))


def lower_case(length: int = 1) -> str:
    """
    Return random ascii_lowercase

    :param length: the length of the returned str
    """
    return "".join(choice(ascii_lowercase) for _ in range(length))


def upper_case(length: int = 1) -> str:
    """
    Return random ascii_uppercase

    :param length: the length of the returned str
    """
    return "".join(choice(ascii_uppercase) for _ in range(length))


def digit(length: int = 1) -> str:
    """
    Return random ascii_digits

    :param length: the length of the returned str
    """
    return "".join(choice(ascii_digits) for _ in range(length))


def symbol(length: int = 1) -> str:
    """
    Return random ascii_symbols

    :param length: the length of the returned str
    """
    return "".join(choice(punctuation) for _ in range(length))


def all_ascii(length: int = 1) -> str:
    """
    Return random ascii_letter, digits and punctuation

    :param length: the length of the returned str
    """
    return "".join(
        choice(ascii_letters + ascii_digits + punctuation) for _ in range(length)
    )


def password(length: int) -> str:
    """
    Return a password with given length
    ascii_letters, digits and punctuation is used

    :param length: the length of the returned str
    :return:
    """
    char_sequence = list(all_ascii(length))
    shuffle(char_sequence)
    return "".join(char_sequence)
