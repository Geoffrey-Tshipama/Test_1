import numpy as np

a = int(input("le nombre de colonne : ", ))
b = int(input("le nombre de lignes : ", ))


matrix = np.random.randn(a, b)
double_matrix = np.dot(matrix, matrix)

print(double_matrix)
