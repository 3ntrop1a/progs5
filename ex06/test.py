#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import frontal_function, BadInputException

# NB: ces tests s'appuient sur le fichier file.csv fourni dans ce dossier
# (productid,price,quantity - 8 lignes de valeurs, index 0 à 7) et
# supposent une exécution de pytest depuis le dossier ex06.

def testFrontalFunction():

    ### Nominal Cases
    assert frontal_function(2, 5, ["price", "quantity"], "file.csv") == 476.7
    # M == N : une seule ligne prise en compte
    assert frontal_function(0, 0, ["price"], "file.csv") == 10.0
    assert frontal_function(3, 3, ["quantity"], "file.csv") == 2.0
    # Une seule colonne sur toute la plage disponible
    assert frontal_function(0, 7, ["price"], "file.csv") == 429.6
    # Plusieurs colonnes multipliées entre elles, sur toute la plage
    assert frontal_function(0, 7, ["price", "quantity"], "file.csv") == 12542.7
    ###

    ### Edge cases and corner cases
    # N supérieur au nombre de lignes de valeurs disponibles dans le csv
    with pytest.raises(BadInputException):
        frontal_function(0, 100, ["price", "quantity"], "file.csv")

    # N strictement égal au nombre de lignes (index max valide == count-1)
    with pytest.raises(BadInputException):
        frontal_function(0, 8, ["price"], "file.csv")

    # Colonne demandée absente du fichier csv
    with pytest.raises(BadInputException):
        frontal_function(0, 1, ["nosuchcolumn"], "file.csv")

    # Fichier csv inexistant
    with pytest.raises(BadInputException):
        frontal_function(0, 1, ["price"], "does_not_exist.csv")
    ###