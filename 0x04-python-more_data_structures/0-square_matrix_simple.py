def square_matrix_simple(matrix=[]):
    """
    This function computes the square value of all integers of a matrix
    """
    return [[x**2 for x in row] for row in matrix]
