#!/usr/bin/python3
"""Module pour trouver le maximum dans une liste."""

def max_integer(list=[]):
    """Fonction qui trouve et retourne le maximum dans une liste d'entiers.
       Si la liste est vide, retourne None.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
