#!/usr/bin/python3
"""
This module contains a function that prints a formatted string
based on first_name and last_name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name, optional.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Correction : éviter un espace supplémentaire si `last_name` est vide
    if last_name.strip():
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
