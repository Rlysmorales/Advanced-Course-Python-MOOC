
my_matrix = [[1, 2], [3, 4]]

def row_sums(my_matrix: list):

    matrix1 = my_matrix[0][0] + my_matrix[0][1]
    my_matrix[0].append(matrix1)

    matrix2 = my_matrix[1][0] + my_matrix[1][1]
    my_matrix[1].append(matrix2)

    return my_matrix

print(row_sums(my_matrix))