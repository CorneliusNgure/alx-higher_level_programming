#!/usr/bin/python3

"""This module defines a matrix multiplication function"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: Result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   or contains non-integer/float elements.
        ValueError: If m_a or m_b is empty, or if matrices can't be multiplied.

    """
    # m_a's validation
    if not isinstance(m_a, list) or not all(
            isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if any(not isinstance(
        element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # m_b's validation
    if not isinstance(m_b, list) or not all(
            isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")
    if any(not isinstance(
        element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [
    [
        sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
        for j in range(len(m_b[0]))
    ]
    for i in range(len(m_a))
]

    return result
