def nombre_voisinages_ospf(nb_routeurs):
    if nb_routeurs <= 1:
        return 0
    return nb_routeurs - 1

nb_routeurs = int(input("Saisissez le nombre  de routeurs dans la zone : "))
print("Le nombre de voisinages attendus est :", nombre_voisinages_ospf(nb_routeurs))

