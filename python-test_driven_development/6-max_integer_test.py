#!/usr/bin/python3
"""Module to find the max integer in a list
"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
    If the list is empty, returns None
    """
    if not list:
        return None
    max_val = list[0]
    for i in list:
        if i > max_val:
            max_val = i
    return max_val