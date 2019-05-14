#!/usr/bin/env python3
"""
utils.py
Boucher, Govedič, Saowakon, Swanson 2019

Contains useful utility functions.

"""
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
