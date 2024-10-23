def attaquer():

    pass

def evaluer_combat(points_vie_attaquant: int, points_vie_victime: int, attaque_puissante: bool, bouclier_victime: bool):
    """
    Cette fonction évalue l'issue d'un combat en fonction des points de vie des personnages,
    de l'utilisation d'une attaque puissante et de la présence d'un bouclier.

    :param points_vie_attaquant: Les points de vie de l'attaquant.
    :param points_vie_victime: Les points de vie de la victime.
    :param attaque_puissante: Indique si l'attaquant utilise une attaque puissante.
    :param bouclier_victime: Indique si la victime utilise un bouclier pour se protéger.
    :return: Un message indiquant le résultat du combat.
    """

    while points_vie_attaquant > 0 and points_vie_victime < 0:
        degats = 20

        if attaque_puissante:
            if bouclier_victime:
                degats = degats * 1.5
                print("Attaque puissante mais partiellement bloquée par le bouclier, dégâts augmentés de 50%.")
            else:
                degats = degats * 2
                print("Attaque puissante réussie, dégâts doublés !")
        elif bouclier_victime:
            degats = degats // 2
            print("Le bouclier de la victime réduit les dégâts de moitié.")

        if points_vie_attaquant < 10 or points_vie_victime >= 30:
            print("L'attaquant est trop faible pour continuer, le combat est perdu.")
            return "Défaite de l'attaquant"

        if points_vie_victime <= 0:
            print(f"La victime a {points_vie_victime} points de vie restants. Elle est vaincue.")
            return "Victoire de l'attaquant"

        print(f"La victime survit avec {points_vie_victime} points de vie.")


def attaque(nom_attaquant, nom_victime, force_attaque, vie_restante):
    # Cette fonction performe un attaque d'une créature à une autre.
    vie = vie_restante - force_attaque
    print(f"{nom_attaquant} attaque ! {nom_victime} perd {force_attaque} points de vie.")
    print(f"Points de vie du {nom_victime} : {vie}")
    return vie



if __name__ == "__main__":
    # Points de vie initiaux
    points_vie_chevalier = 100
    points_vie_dragon = 120

    # Le chevalier attaque le dragon
    points_vie_dragon = attaque("Chevalier", "Dragon", 20, points_vie_dragon)

    # Le dragon attaque le chevalier
    points_vie_chevalier = attaque("Dragon", "chevalier", 25, points_vie_chevalier)

    # Le chevalier attaque de nouveau le dragon
    points_vie_dragon = attaque("Chevalier", "Dragon", 15, points_vie_dragon)

    # Le dragon attaque de nouveau le chevalier
    points_vie_chevalier = attaque("Dragon", "chevalier", 30, points_vie_chevalier)



