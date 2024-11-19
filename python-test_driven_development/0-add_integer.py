#!/usr/bin/python3
"""
This module provides the add_integer function.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats.
    If a or b is a float, it is cast to an integer before addition.
    Raises:
        TypeError: If a or b are not integers or floats.
        ValueError: If a or b are NaN values.
        OverflowError: If a or b are infinite values.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a != a or b != b:  # Check for NaN
        raise ValueError("cannot convert float NaN to integer")
    if a in [float('inf'), float('-inf')] or b in [float('inf'), float('-inf')]:
        raise OverflowError("cannot convert float infinity to integer")

    a = int(a)
    b = int(b)
    return a + b
