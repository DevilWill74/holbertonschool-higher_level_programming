#!/usr/bin/python3
"""
Module that defines a function to print full name
"""

def say_my_name(first_name, last_name=""):
    """
    Function that prints 'My name is <first_name> <last_name>'
    Args:
        first_name: first name string
        last_name: last name string (optional)
    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Supprime l'espace superflu à la fin en ajustant la gestion des chaînes
    if last_name:
        print("My name is {} {} ".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
