import numpy as np
from determinant_of_matrix import determinant_of_matrix
from matrix_transposition import transpose_matrix

# This is a function, which calculates inverse matrix for shapes 2x2 and 3x3,
# using previously created functions - determinant_of_matrix and transpose_matrix

def inverse_matrix(matrix):
    # Checking shape of matrix
    if (matrix.shape == (3,3)) | (matrix.shape == (2,2)):
        # Using function determinant_of_matrix created for arrays 2x2 and 3x3
        # and checking if the determinant of matrix isn't equal to zero
        matrix_det = determinant_of_matrix(matrix)
        if matrix_det != 0:
            list_of_algebraic_complements = []
            rows = matrix.shape[0]
            columns = matrix.shape[1]
            # Passing through rows and columns, using two loops
            for row in range(rows):
                for column in range(columns):
                    # Passing one more time through the same matrix and rule out expressions
                    # which have equal row or column compared to expression from first two loops
                    list_of_mini_matrix = []
                    for complement_row in range(rows):
                        for complement_column in range(columns):
                            if row != complement_row and column != complement_column:
                                # After validating expressions, for matrix3x3 is supplementing
                                # a list with expressions that will be used for calculating
                                # algebraic complement. For matrix2x2 it is calculating without
                                # this list (list_of_mini_matrix)
                                list_of_mini_matrix.append(matrix[complement_row][complement_column])
                                if matrix.shape == (2,2):
                                    Dij = (-1)**(row + 1 + column + 1)*matrix[complement_row][complement_column]
                                    list_of_algebraic_complements.append(Dij)
                                if len(list_of_mini_matrix) == 4:
                                    Dij = (-1)**(row+1 + column+1)*(list_of_mini_matrix[0]*list_of_mini_matrix[3] -
                                                                    list_of_mini_matrix[1]*list_of_mini_matrix[2])
                                    list_of_algebraic_complements.append(Dij)
            # Creating matrix from algebraic complements, transposing it using own function and
            # in the end dividing it by determinant of original matrix
            matrix_of_algebraic_complements = np.array(list_of_algebraic_complements).reshape(rows, columns)
            transposed_matrix_of_alg_complements = transpose_matrix(matrix_of_algebraic_complements)
            inversed_matrix = transposed_matrix_of_alg_complements/matrix_det
            return inversed_matrix
        else:
            return "Can't calculate inverse matrix. Determinant is equal zero"
    else:
        return 'Matrix has to be 2x2 or 3x3 shape'


A = np.array([1,0,5,2,7,6,8,3,2]).reshape(3,3)
B = np.array([3,-1,1,5,1,4,-1,3,2]).reshape(3,3)
C = np.array([2,5,6,1]).reshape(2,2)

print('Inverse matrix to matrix A:\n', inverse_matrix(A))
print()
print('Inverse matrix to matrix A:\n', np.linalg.inv(A))
print()
print('Inverse matrix to matrix B:\n', inverse_matrix(B))
print()
print('Inverse matrix to matrix B:\n', np.linalg.inv(B))
print()
print('Inverse matrix to matrix C:\n', inverse_matrix(C))
print()
print('Inverse matrix to matrix C:\n', np.linalg.inv(C))