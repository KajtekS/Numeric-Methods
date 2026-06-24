import numpy as np


def LU(matrix):
    A = matrix.copy()

    n = matrix.shape[0]

    for i in range(n):
        for j in range(i + 1, n):
            matrix[j, i] = matrix[j, i] / matrix[i, i]
            matrix[j, i + 1:] -= matrix[j, i] * matrix[i, i + 1:]

    return A - (np.tril(matrix, k=-1) + np.eye(n)) @ np.triu(matrix)


matrix = np.random.rand(5, 5)
b = np.random.rand(5)

wynik = LU(matrix)
print(wynik)