import numpy as np

a = int(input("le nombre de lignes matrice 1 : ", ))
b = int(input("le nombre de lignes matrice 2 : ", ))

CONSTANTE = 3

matrix_1 = np.random.rand(a, CONSTANTE)
matrix_2 = np.random.rand(b, CONSTANTE)

if CONSTANTE == b:
    double_matrix = np.dot(matrix_1, matrix_2)
    print("la produit de matrice est ")
    print(double_matrix)
else:
    try:
        somme = matrix_1 + matrix_2
        print("La somme de matrice est ")
        print(somme)
    except:
        print("Le matrice sont incompatible pour la faire une sommation")
