#!/usr/bin/python3
"""
This module provides the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers/floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows of the matrix are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
