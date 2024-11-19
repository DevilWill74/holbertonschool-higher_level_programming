#!/usr/bin/python3
"""
This module provides the add_integer function.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    If a or b is a float, it is cast to an integer before addition.
    Raises a TypeError if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Vérification pour les float spéciaux (NaN ou inf)
    if a != a or b != b:  # Vérifie si `a` ou `b` est NaN
        raise ValueError("cannot convert float NaN to integer")
    if (
        a in [float('inf'), float('-inf')]
        or b in [float('inf'), float('-inf')]
    ):
        raise OverflowError("cannot convert float infinity to integer")

    # Convertir les floats en int avant addition
    a = int(a)
    b = int(b)

    return a + b
