#!/usr/bin/python3
"""
This module provides the matrix_divided function.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number (div).
    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide each element of the matrix.
    Returns:
        list of lists: A new matrix with the results rounded to 2 decimal places.
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if div is not a number.
        TypeError: If rows of the matrix are not of the same size.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
