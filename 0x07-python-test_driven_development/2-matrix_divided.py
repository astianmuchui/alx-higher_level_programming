#!/usr/bin/python3

"""
Module for matrix_divided method.
"""


def matrix_divided(matrix, div):

    """
    A function to divide a matrix by a number.

    Parameters:
    matrix (list): A list of lists of integers or floats.
    div (int or float): The divisor.

    matrix must be a list of lists of integers or floats, otherwise
    raise a TypeError exception with the message matrix must be a
    matrix (list of lists) of integers/floats Each row of the matrix
    must be of the same size, otherwise raise a TypeError exception
    with the message Each row of the matrix must have the same size
    div must be a number (integer or float), otherwise raise a
    TypeError exception with the message div must be a number
    div cannot be equal to 0, otherwise raise a ZeroDivisionError
    exception with the message division by zero
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places

    Returns a new matrix
    """

    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    for row in matrix:

        if isinstance(row, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

        if len(row) == 0:

            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

        if len(row) != len(matrix[0]):

            raise TypeError("Each row of the matrix must have the same size")

        for element in row:

            if isinstance(element, int) is False \
                    and isinstance(element, float) is False:

                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if isinstance(div, int) is False and isinstance(div, float) is False:

        raise TypeError("div must be a number")

    if div == 0:

        raise ZeroDivisionError("division by zero")

    mtrx = []

    for row in matrix:

        mtrx.append(list(map(lambda x: round(x / div, 2), row)))

    return mtrx
