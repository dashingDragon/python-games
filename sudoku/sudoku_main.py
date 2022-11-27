import numpy as np


def test_ligne(i, j, nombre, M):
    for index in range(0, 9):
        if M[i, index] == nombre and index != j:
            return False
    return True


def test_colonne(i, j, nombre, M):
    for index in range(0, 9):
        if M[index, j] == nombre and index != i:
            return False
    return True


def test_carre(i, j, nombre, M):
    a = i // 3
    b = j // 3
    for x in range(3):
        for y in range(3):
            if M[3*a+x, 3*b+y] == nombre:
                if a+x != i and b+y != j:
                    return False
    return True


def test(i, j, nombre, M):
    if test_colonne(i, j, nombre, M):
        if test_ligne(i, j, nombre, M):
            if test_carre(i, j, nombre, M):
                return True
    return False


def protection(matrice_originale):
    liste_protegee = []
    for x in range(0, 9):
        for y in range(0, 9):
            if matrice_originale[x, y] != 0:
                liste_protegee.append((x, y))
    return liste_protegee


def remplissage(i, j, M, liste_protegee, sens):
    #  if i in liste_protegee and j in liste_protegee:
    if (i, j) in liste_protegee:
        return sens
    else:
        nombre = M[i, j] + 1
        while nombre < 10:
            if test(i, j, nombre, M):
                M[i, j] = nombre
                return True
            else:
                nombre += 1
        M[i, j] = 0
        return False


def avance_case(i, j):
    if j == 8:
        return i + 1, 0
    else:
        return i, j + 1


def recule_case(i, j):
    if j == 0:
        return i - 1, 8
    else:
        return i, j - 1


def resolution(M):
    tournetourne = True
    i = 0
    j = 0
    matrice_originale = M.copy()
    liste_protegee = protection(matrice_originale)
    sens = True
    iterations = 0
    while tournetourne:
        print('index : ' + str(i) + ' ; ' + str(j))
        print(iterations)
        iterations += 1
        if remplissage(i, j, M, liste_protegee, sens):
            (i, j) = avance_case(i, j)
            sens = True
        else:
            (i, j) = recule_case(i, j)
            sens = False
        if i == 9:
            tournetourne = False
            print(M)
        if i == -1:
            tournetourne = False
            print('Pas de solution.')


M = np.zeros((9, 9), int)  # 9x9 matrix filled with zeros
M[0, 3] = 1
M[0, 4] = 2
M[1, 0] = 7
M[1, 6] = 5
M[1, 8] = 2
M[2, 0] = 2
M[2, 4] = 4
M[2, 5] = 7
M[2, 8] = 9
M[3, 0] = 8
M[3, 1] = 4
M[3, 3] = 5
M[3, 6] = 2
M[3, 8] = 1
M[5, 0] = 5
M[5, 2] = 7
M[5, 5] = 6
M[5, 7] = 8
M[5, 8] = 4
M[6, 0] = 1
M[6, 3] = 3
M[6, 4] = 8
M[6, 8] = 5
M[7, 0] = 9
M[7, 2] = 3
M[7, 8] = 7
M[8, 4] = 5
M[8, 5] = 2
resolution(M)
