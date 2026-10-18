import random
import math
d = [
    [0, 14, 15, None, None, None, None, 17],
    [14, 0, 13, 14, 20, None, None, 21],
    [15, 13, 0, 11, 21, 17, 9, 9],
    [None, 14, 11, 0, 11, 10, 8, 20],
    [None, 20, 21, 11, 0, 15, 18, None],
    [None, None, 17, 10, 15, 0, 9, None],
    [None, None, 9, 8, 18, 9, 0, 13],
    [17, 21, 9, 20, None, None, 13, 0]
]
def cout(trajet):
    total = 0
    for i in range(len(trajet) - 1):
        a = trajet[i] - 1
        b = trajet[i + 1] - 1
        if d[a][b] is None:
            return 999999
        total += d[a][b]
    return total
def voisins(trajet):
    liste = []
    for i in range(1, len(trajet)):
        for j in range(i + 1, len(trajet)):
            v = trajet[:]
            v[i], v[j] = v[j], v[i]
            if cout(v + [v[0]]) < 999999:
                liste.append(v)
    return liste
def tabou():
    trajet = [1, 2, 3, 4, 5, 6, 7, 8]
    meilleure = trajet[:]
    liste_tabou = []

    print("recherche tabou:")
    for it in range(10):
        choix = None
        cout_choix = 999999

        for v in voisins(trajet):
            if v not in liste_tabou and cout(v + [v[0]]) < cout_choix:
                choix = v
                cout_choix = cout(v + [v[0]])

        if choix is None:
            break

        trajet = choix
        liste_tabou.append(trajet)
        if len(liste_tabou) > 3:
            liste_tabou.pop(0)

        if cout(trajet + [trajet[0]]) < cout(meilleure + [meilleure[0]]):
            meilleure = trajet[:]

        print("Iteration", it + 1, "Trajet :", trajet + [trajet[0]],
              "Cout :", cout(trajet + [trajet[0]]))

    print("Meilleur trajet Tabou :", meilleure + [meilleure[0]],
          "Cout :", cout(meilleure + [meilleure[0]]))


def recuit_simule():
    trajet = [1, 2, 3, 4, 5, 6, 7, 8]
    meilleure = trajet[:]
    T = 10

    print("\nrecuit simule")
    for it in range(5):
        liste = voisins(trajet)
        if not liste:
            break

        v = random.choice(liste)
        delta = cout(v + [v[0]]) - cout(trajet + [trajet[0]])

        if delta <= 0 or random.random() < math.exp(-delta / T):
            trajet = v

        if cout(trajet + [trajet[0]]) < cout(meilleure + [meilleure[0]]):
            meilleure = trajet[:]

        print("Iteration", it + 1, "T =", round(T, 2),
              "Trajet :", trajet + [trajet[0]],
              "Cout :", cout(trajet + [trajet[0]]))
        T = T * 0.8

    print("Meilleur trajet Recuit Simule :", meilleure + [meilleure[0]],
          "Cout :", cout(meilleure + [meilleure[0]]))


tabou()
recuit_simule()
