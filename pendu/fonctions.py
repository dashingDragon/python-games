import pickle as p
import random as r


def give_secret_word(liste):
    l = len(liste)
    num = r.randrange(l)
    return liste[num]


def afficher_mot(mot, liste):
    aff = []
    trouve = True
    for i in range(len(mot)):
        if liste.__contains__(mot[i]):
            aff.append(mot[i])
        else:
            aff.append('_')
            trouve = False
    ch = str()
    for i in range(len(aff)):
        ch += aff[i]
    print(ch)
    return trouve


def donne_liste_joueurs():
    try:
        with open('scores', 'rb') as file:
            pickler = p.Unpickler(file)
            return pickler.load()
    except FileNotFoundError:
        with open('scores', 'wb') as file:
            pickler = p.Pickler(file)
            pickler.dump({})
        with open('scores', 'rb') as file:
            pickler = p.Unpickler(file)
            return pickler.load()


def maj_liste_joueurs(liste):
    with open('scores', 'wb') as file:
        pickler = p.Pickler(file)
        pickler.dump(liste)