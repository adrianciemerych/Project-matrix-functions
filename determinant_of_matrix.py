

# Simple function calculating determinant of matrix for matrix 2x2 or 3x3

def determinant_of_matrix(matrix):
    determinant = 0
    if matrix.shape == (2,2):
        determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return determinant
    elif matrix.shape == (3,3):
        for column in range(matrix.shape[1]):
            if column == 0:
                complement = matrix[0,1]*matrix[2,2] - matrix[0,2]*matrix[2,1]
            elif column == 1:
                complement = matrix[0, 0] * matrix[2, 2] - matrix[0, 2] * matrix[2, 0]
            elif column == 2:
                complement = matrix[0, 0] * matrix[2, 1] - matrix[0, 1] * matrix[2, 0]
            determinant += matrix[1,column] * (-1) ** (2 + (column + 1)) * complement
        return determinant
    else:
        return 'Matrix has incorrect shape - should be 2x2 or 3x3'


# Checking if function works properly, using np.linalg function

# A = np.array([11,4,6,3,5,4,4,11,7]).reshape(3,3)
# B = np.array([5,11,33,44]).reshape(2,2)
# print('Determinant of matrix A: ', determinant_of_matrix(A))
# print('Determinant of matrix A (built-in function): ', np.linalg.det(A))
#
# print('')
# print('Determinant of matrix B:', determinant_of_matrix(B))
# print('Determinant of matrix B (built-in function): ', np.linalg.det(B))
