import pytest
import simulation_combat


def test_attaquer():
    # Arrange
    attaquant = "Chevalier"
    victime = "dragon"
    degats = 10
    pv_victime = 50

    resultat_attendu = 40

    # Act
    rest_pv_victime = simulation_combat.attaquer(nom_attaquant=attaquant, nom_victime=victime, degats=degats, points_vie_victime=pv_victime)

    # Assert
    assert rest_pv_victime == resultat_attendu

def test_enchainer_attaques():
    # Arrange
    attaquant = "Chevalier"
    victime = "dragon"
    liste_degats = [20, 10, 10]
    pv_victime = 50

    resultat_attendu = 10

    # Act
    rest_pv_victime = simulation_combat.enchaîner_attaques(nom_attaquant=attaquant, nom_victime=victime, degats=liste_degats, points_vie_victime=pv_victime)

    # Assert
    assert rest_pv_victime == resultat_attendu

def test_lancer_combat_type_parametres():
    # Arrange:
    nb_parametres_attendu = 2

    # Act: Récupération du nombre de paramètres de la fonction
    nb_parametres_obtenu = simulation_combat.lancer_combat.__code__.co_argcount

    # Assert:
    assert nb_parametres_obtenu == nb_parametres_attendu, f"Le nombre de paramètres doit être {nb_parametres_attendu}, mais {nb_parametres_obtenu} ont été fournis."


def test_evaluer_combat_victoire_attaquant():
    result = simulation_combat.evaluer_combat(100, 20, True, False)
    assert result == "Victoire de l'attaquant"

def test_evaluer_combat_victoire_victime():
    result = simulation_combat.evaluer_combat(100, 20, False, True)
    assert result == "Victoire de l'attaquant"

def test_evaluer_combat_attaquant_trop_faible():
    result = simulation_combat.evaluer_combat(20, 40, False, False)
    assert result == "Défaite de l'attaquant"

def test_evaluer_combat_attaque_puissante():
    result = simulation_combat.evaluer_combat(100, 30, True, False)
    assert result == "Victoire de l'attaquant"

def test_evaluer_combat_attaquant_trop_faible_avec_bouclier():
    result = simulation_combat.evaluer_combat(10, 40, False, True)
    assert result == "Défaite de l'attaquant"
