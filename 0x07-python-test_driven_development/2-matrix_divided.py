#!/usr/bin/python3

"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): Matrix containing only integers or floats.
        div (int or float): The number to divide the matrix by.

    Returns:
        list of lists: New matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix doesn't have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix(list of lists) "
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []

    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        result_matrix.append(new_row)

    return result_matrix
