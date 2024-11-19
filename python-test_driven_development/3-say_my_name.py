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

    # Construction de la sortie avec un espace uniquement si nécessaire
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name} ")
