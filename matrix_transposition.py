import numpy as np


# This is the function for transpose matrix

def transpose_matrix(matrix):
    # Creating new_list for appending values in appropriate order
    new_list = []
    num_of_columns = matrix.shape[1]
    num_of_rows = matrix.shape[0]
    # Passing through all rows for particular columns and appending them to the new_list
    for column in range(num_of_columns):
        for row in range(num_of_rows):
            new_list.append(matrix[row, column])
    # Creating np.array from made list and reshaping it in inverse order relative to original matrix
    transposed_matrix = np.array(new_list).reshape(num_of_columns, num_of_rows)
    return transposed_matrix


# Checking results on an example matrix

# A = np.array([[3,2,4,1,8,0],
#               [2,3,5,6,0,3],
#               [7,7,2,1,4,5]])
#
# B = np.array([[1,1],
#               [2,2],
#               [2,3],
#               [1,4],
#               [1,5],
#               [1,6]])
# print(transpose_matrix(A), '\n')
#
# print(transpose_matrix(B))