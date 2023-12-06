import numpy as np
from determinant_of_matrix import determinant_of_matrix


# Function for square matrix with shape 4x4 or less to calculating determinant


def laplace_determinant(matrix):
    determinant = 0
    # Walk through the expressions that will determine the algebraic complement matrices
    for expression_column in range(matrix.shape[1]):
        algebraic_complements_list = []
        # Walk through rows and columns of matrix, ignoring first row
        for row in range(1, matrix.shape[0]):
            for column in range(matrix.shape[1]):
                if expression_column != column:
                    algebraic_complements_list.append(matrix[row][column])
        matrix_of_algebraic_complements = np.array(algebraic_complements_list).reshape(matrix.shape[0] - 1, matrix.shape[1] - 1)
        determinant_of_alg_compl_matrix = determinant_of_matrix(matrix_of_algebraic_complements)
        if expression_column % 2 == 0:
            determinant += matrix[0][expression_column] * determinant_of_alg_compl_matrix
        else:
            determinant -= matrix[0][expression_column] * determinant_of_alg_compl_matrix
    return determinant
