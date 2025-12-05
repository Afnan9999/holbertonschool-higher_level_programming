#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix
by a given divisor. It validates that the matrix is a list of lists
containing only integers or floats, that each row is the same size,
and that the divisor is a non-zero number. Returns a new matrix with
all elements divided and rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int or float): The divisor; must not be zero.

    Returns:
        new_matrix (list of lists of float): New matrix with divided elements.
    """
    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate matrix structure
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix) or
            len(matrix) == 0 or
            any(len(row) == 0 for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Perform division
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
