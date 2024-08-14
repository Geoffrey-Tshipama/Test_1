import numpy as np

a = int(input("le nombre de lignes matrice 1 : ", ))
b = int(input("le nombre de lignes matrice 2 : ", ))


CONSTANTE = 3

matrix_1 = np.random.rand(a, CONSTANTE)
matrix_2 = np.random.rand(b, CONSTANTE)


def choose(c):
    match c:
        case 1:
            somme = matrix_1 + matrix_2
            print("La somme de matrice est ")
            return somme
        case 0:
            difference = matrix_1 - matrix_2
            print("La différence de matrice est ")
            return difference
        case _:
            print("Donner 0 ou 1 entrée")


if CONSTANTE == b:
    double_matrix = np.dot(matrix_1, matrix_2)
    print("la produit de matrice est ")
    print(double_matrix)
else:
    print("La multiplication à échoué")
    c = int(input("Que souhaitez-vous faire la soustraction(0) ou l'addition(1) ? : ", ))
    try:
        choose(c)
    except:
        print("Les matrices sont incompatible pour la faire une sommation")
