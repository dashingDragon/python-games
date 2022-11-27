from random import randrange
from math import ceil

montant = 100
while montant > 0:
    print("$$$ | Vous avez {0}$ en poche ! | $$$".format(montant).center(50))
    numero = input('Entrez le numéro sur lequel vous voulez parier: ')
    somme = input('Entrez la somme que vous voulez parier: ')
    try:
        numero = int(numero)
        somme = int(somme)
        assert 49 >= numero >= 0
        assert montant >= somme > 0
    except AssertionError:
        print("La mise ou la case est incorrecte.")
    except ValueError:
        print("Vous n'avez pas entré d'entier.")
    else:
        case = randrange(49)
        print("La roulette s'arrête sur la case numéro {0} !".format(str(case)).center(50))
        if numero == case:
            print("Bravo ! Vous venez de remporter {0}$ !".format(somme*3).center(50))
            montant += somme*3
        elif numero % 2 == case % 2:
            print("Bravo ! Vous venez de remporter {0}$ !".format(ceil(somme / 2)).center(50))
            montant += ceil(somme / 2)
        else:
            print("Pas de chance ! Vous venez de perdre {0}$ !".format(somme).center(50))
            montant -= somme

print("Vous n'avez plus d'argent à miser ! Revenez une prochaine fois !".center(50))