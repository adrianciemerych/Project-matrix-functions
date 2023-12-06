import numpy as np
from determinant_of_matrix import determinant_of_matrix
from laplace_determinant import laplace_determinant


# Function for calculating rank of matrix 4x4 and 3x3

def rank_of_matrix (matrix):
    # Checking shape of matrix
    if matrix.shape == (4,4):
        # Calculating determinant of matrix 4x4 using Laplace expansion
        determinant = laplace_determinant(matrix)
        if determinant != 0:
            return 'The rank of the matrix is equal: %s. Determinant of the matrix is: %s' %(matrix.shape[0], determinant)
        # If determinant is equal to 0, we create a loops going two times over each expression of the matrix
        # and by using condition 'if', we create matrices 3x3 from matrix4x4 and check their determinant.
        # If any is different from 0 then rank of the matrix is 3
        else:
            for first_pass_row in range(matrix.shape[0]):
                for first_pass_column in range(matrix.shape[1]):
                    list_of_matrix3x3 = []
                    for second_pass_row in range(matrix.shape[0]):
                        for second_pass_column in range(matrix.shape[1]):
                            if first_pass_row != second_pass_row and first_pass_column != second_pass_column:
                                list_of_matrix3x3.append(matrix[second_pass_row][second_pass_column])
                    matrix3x3 = np.array(list_of_matrix3x3).reshape(matrix.shape[0] - 1, matrix.shape[1] - 1)
                    determinant3x3 = determinant_of_matrix(matrix3x3)
                    if determinant3x3 != 0:
                        return 'The rank of the matrix is: %s. The determinant of matrix: \n %s \n is different from 0 ' \
                               'and equals: %s' % (matrix.shape[0]-1, matrix3x3, determinant3x3)
            # If the rank of the matrix isn't equal 3 we create matrixes 2x2 in similar way to matrixes 3x3
            # but with another condition
            # and check their determinant using the same function (determinant_of_matrix)
            for first_pass_row in range(matrix.shape[0]):
                for first_pass_column in range(matrix.shape[1]):
                    for second_pass_row in range(matrix.shape[0]):
                        for second_pass_column in range(matrix.shape[1]):
                            list_of_matrix2x2 = []
                            if second_pass_row > first_pass_row and second_pass_column > first_pass_column:
                                list_of_matrix2x2.append(matrix[first_pass_row][first_pass_column])
                                list_of_matrix2x2.append(matrix[first_pass_row][second_pass_column])
                                list_of_matrix2x2.append(matrix[second_pass_row][first_pass_column])
                                list_of_matrix2x2.append(matrix[second_pass_row][second_pass_column])
                                matrix2x2 = np.array(list_of_matrix2x2).reshape(matrix.shape[0]-2, matrix.shape[1]-2)
                                det_matrix2x2 = determinant_of_matrix(matrix2x2)
                                if det_matrix2x2 != 0:
                                    return 'The rank of the matrix is: %s. The determinant of matrix: \n %s \n is ' \
                                           'different from 0 and equals: %s' %(matrix.shape[0]-2, matrix2x2, det_matrix2x2)
            # If the rank of the matrix isn't 2 we check each expression of matrix.
            # If any is different from 0, the rank of the matrix is 1, if not rank = 0
            for first_pass_row in range(matrix.shape[0]):
                for first_pass_column in range(matrix.shape[1]):
                    if matrix[first_pass_row][first_pass_column] != 0:
                        return 'The rank of the matrix is 1'
                    else:
                        return 'The rank of the matrix is 0, because all of the numbers in this matrix are zeros'
    # For matrix 3x3 the procedure is almost identical to that for a 4x4 matrix
    if matrix.shape == (3,3):
        determinant = determinant_of_matrix(matrix)
        if determinant != 0:
            return 'The rank of the matrix is %s. Determinant of the matrix is: %s' %(matrix.shape[0], determinant)
        else:
            for first_pass_row in range(matrix.shape[0]):
                for first_pass_column in range(matrix.shape[1]):
                    list_of_matrix2x2 = []
                    for second_pass_row in range(matrix.shape[0]):
                        for second_pass_column in range(matrix.shape[1]):
                            if first_pass_row != second_pass_row and first_pass_column != second_pass_column:
                                list_of_matrix2x2.append(matrix[second_pass_row][second_pass_column])
                    matrix2x2 = np.array(list_of_matrix2x2).reshape(matrix.shape[0]-1, matrix.shape[1]-1)
                    det_matrix2x2 = determinant_of_matrix(matrix2x2)
                    if det_matrix2x2 != 0:
                        return 'The rank of the matrix is: %s. Determinant of the matrix: \n %s \n is different ' \
                               'from 0 and equals %s' %(matrix.shape[0]-1, matrix2x2, det_matrix2x2)
            for row in range(matrix.shape[0]):
                for column in range(matrix.shape[1]):
                    if matrix[row][column] != 0:
                        return 'The rank of the matrix is 1'
                    else:
                        return 'The rank of the matrix is 0, because all of the numbers in this matrix are zeros'

# Test how function working


A = np.array([1,1,5,2,0,6,8,3,2]).reshape(3,3)

B = np.array([3,-1,1,5,1,4,-1,3,2]).reshape(3,3)

C = np.array([1,3,-2,4,1,-1,3,5,0,1,4,-2,10,-2,5,1]).reshape(4,4)

D = np.array([2,8,3,-4,1,4,1,-2,5,20,0,-10,-3,-12,-2,6]).reshape(4,4)

print(rank_of_matrix(A))
print()
print(rank_of_matrix(B))
print()
print(rank_of_matrix(C))
print()
print(rank_of_matrix(D))

