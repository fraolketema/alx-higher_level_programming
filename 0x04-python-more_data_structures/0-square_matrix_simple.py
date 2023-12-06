#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_deploy_to = matrix.copy()
    leng = len(matrix)
    for i in range(leng):
        matrix_deploy_to[i] = list(map(lambda x: x**2, matrix[i]))
    return (matrix_deploy_to)
