import donnees as d
import fonctions as f

liste_mots = d.give_list()
mot_secret = f.give_secret_word(liste_mots)
liste_essais = []
vies = len(mot_secret)
trouve = f.afficher_mot(mot_secret, liste_essais)


while not trouve and vies > 0:
    lettre = input("Entrez la lettre : ").upper()
    liste_essais.append(lettre)
    if mot_secret.count(lettre) == 0:
        vies -= 1
    print("Vies : " + str(vies))
    trouve = f.afficher_mot(mot_secret, liste_essais)

if vies <= 0:
    print("Vous n'avez plus de vies !")
    print("Le mot était : " + mot_secret)
elif trouve:
    print("Félicitations vous avez trouvé la solution !")
    print("Vous avez gagné " + str(vies) + " points !")
    nom = str(input("Entrez votre nom : "))
    liste_joueurs = f.donne_liste_joueurs()
    try:
        liste_joueurs[nom] += vies
    except KeyError:
        liste_joueurs[nom] = 0
        liste_joueurs[nom] += vies
    f.maj_liste_joueurs(liste_joueurs)
    print("Votre score est désormais : " + str(liste_joueurs[nom]))
