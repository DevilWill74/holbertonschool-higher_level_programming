#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(lst=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if not isinstance(lst, list):  # Vérifie si l'argument est une liste
        raise TypeError("The argument must be a list")

    if len(lst) == 0:
        return None

    result = lst[0]
    for i in lst[1:]:
        if i > result:
            result = i
    return result
