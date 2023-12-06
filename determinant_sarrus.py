import numpy as np

A = np.array([9,2,3,6,2,3,2,3,2]).reshape(3,3)


def sarrus_determinant (matrix):
    matrix_list = []

    for i in range(-matrix.shape[0], matrix.shape[0] - 1):
        for j in range(matrix.shape[1]):
            matrix_list.append(matrix[i][j])

    extend_matrix = np.array(matrix_list).reshape(2*matrix.shape[0]-1,matrix.shape[0])

    determinant = 0
    for i in range(extend_matrix.shape[1]):
        expression = 1
        column = 0
        for j in range(extend_matrix.shape[1]):
            k = i + j
            expression = expression * extend_matrix[k][column]
            column += 1
        determinant += expression
    for i in range(extend_matrix.shape[1]):
        expression = 1
        column = 0
        for j in range(1, extend_matrix.shape[1] + 1):
            k = (-j) + (-i)
            expression = expression * extend_matrix[k][column]
            column += 1
        determinant -= expression
    return determinant
print(sarrus_determinant(A))
print("determinant of matrix", np.linalg.det(A))