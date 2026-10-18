
couts = [[5, 3, 4],
         [6, 7, 2]]
stocks = [8, 9]
demandes = [4, 5, 8]
def calculer_cout(sol):
    total = 0
    for i in range(2):
        for j in range(3):
            total += sol[i][j] * couts[i][j]
    return total

def est_valide(sol):
    for i in range(2):
        if sum(sol[i]) != stocks[i]:
            return False
    for j in range(3):
        if sol[0][j] + sol[1][j] != demandes[j]:
            return False
    return True

solution = [[4, 4, 0],
            [0, 1, 8]]
meilleure = solution
tabou = []

print("Solution initiale:", solution)
print("Cout initial:", calculer_cout(solution))
for it in range(10):
    voisin_choisi = solution
    cout_choisi = calculer_cout(solution)

    for x1 in range(demandes[0] + 1):
        for x2 in range(demandes[1] + 1):
            x3 = stocks[0] - x1 - x2

            if 0 <= x3 <= demandes[2]:
                voisin = [
                    [x1, x2, x3],
                    [demandes[0] - x1,
                     demandes[1] - x2,
                     demandes[2] - x3]
                ]

                if est_valide(voisin) and voisin not in tabou:
                    c = calculer_cout(voisin)
                    if c < cout_choisi:
                        voisin_choisi = voisin
                        cout_choisi = c

    if voisin_choisi == solution:
        break

    solution = voisin_choisi
    tabou.append(solution)

    if len(tabou) > 3:
        tabou.pop(0)

    if calculer_cout(solution) < calculer_cout(meilleure):
        meilleure = solution

    print("Iteration", it + 1, ":", solution,
          "Cout :", calculer_cout(solution))

print("Meilleure solution :", meilleure)
print("Cout total :", calculer_cout(meilleure))
print("Solution valide :", est_valide(meilleure))
