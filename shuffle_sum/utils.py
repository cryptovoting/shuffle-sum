#!/usr/bin/env python3
"""
utils.py
Boucher, Govedič, Saowakon, Swanson 2019

Contains useful utility functions.

"""
from functools import wraps
from math import gcd
from typing import Callable

from gmpy2 import mpz


DEBUG = False


def set_debug(debug: bool):
    """Sets the debug flag.

    :param debug: True to turn on debug printing, False otherwise.
    """
    global DEBUG
    DEBUG = debug


def debug(*args):
    """Prints debug statements."""
    global DEBUG

    if DEBUG:
        print(*args)


def int_to_mpz(func: Callable) -> Callable:
    """A decorator which converts all int arguments to mpz.

    :param func: The function to decorate.
    :return: The function `func` but with all int arguments converted to mpz.
    """
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        return func(*[mpz(arg) if isinstance(arg, int) else arg for arg in args],
                    **{key: mpz(value) if isinstance(value, int) else value for key, value in kwargs.items()})
    return func_wrapper


def _lcm(a: int, b: int) -> int:
    """Finds the least common multiple of two integers.

    :param a: An integer.
    :param b: An integer.
    """
    return a * b // gcd(a, b)


@int_to_mpz
def lcm(*args) -> int:
    """Computes the least common multiple of an arbitrary number of integers.

    :param args: The integers whose lcm will be found.
    :return: The lcm of the integers.
    """
    l = mpz(1)
    for arg in args:
        l = _lcm(l, arg)
    return l
