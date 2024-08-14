import numpy as np

a = int(input("le nombre de lignes matrice 1 : ", ))
b = int(input("le nombre de lignes matrice 2 : ", ))
c = int(input("Que souhaitez-vous au cas ou la multiplication échoue : ", ))

CONSTANTE = 3

matrix_1 = np.random.rand(a, CONSTANTE)
matrix_2 = np.random.rand(b, CONSTANTE)

if CONSTANTE == b:
    double_matrix = np.dot(matrix_1, matrix_2)
    print("la produit de matrice est ")
    print(double_matrix)
else:
    try:
        match c:
            case 1:
                somme = matrix_1 + matrix_2
                print("La somme de matrice est ")
                print(somme)
            case 0:
                difference = matrix_1 - matrix_2
                print("La différence de matrice est ")
                print(difference)
    except:
        print("Le matrice sont incompatible pour la faire une sommation")
