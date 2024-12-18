#!/usr/bin/python3
"""
This module provides a function to print a square using the character `#`.
"""


def print_square(size):
    """
    Prints a square with the size `size` using the `#` character.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(3)
        ###
        ###
        ###
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
