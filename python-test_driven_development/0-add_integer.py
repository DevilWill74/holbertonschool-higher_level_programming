#!/usr/bin/python3
"""
Module for add_integer function
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns their sum.
    Arguments:
    a: The first number (must be int or float).
    b: The second number (must be int or float, default is 98).

    Returns:
    The sum of a and b as an integer.

    Raises:
    TypeError: If either a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

