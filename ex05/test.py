#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import find_dna_pattern_occurrences
# NB: la fonction métier de ex05 n'est pas encore implémentée dans main.py
# (le fichier ne s'importe même pas en l'état - cf. IndentationError).
# Renommez et adaptez la signature ci-dessous une fois l'exercice codé.

def test_find_dna_pattern_occurrences():

    ### Nominal Cases
    assert find_dna_pattern_occurrences("ACGT", "aacgtggcatgacgtggataa") == [2, 1, 11]
    # Une seule occurrence, en tout début de B
    assert find_dna_pattern_occurrences("aa", "aacgt") == [1, 0]
    # Occurrences non chevauchantes d'une séquence d'un seul caractère
    assert find_dna_pattern_occurrences("a", "aacgt") == [2, 0, 1]
    # A et B identiques : une unique occurrence à l'index 0
    assert find_dna_pattern_occurrences("acgt", "acgt") == [1, 0]
    ###

    ### Edge cases and corner cases
    # A n'apparaît pas dans B
    assert find_dna_pattern_occurrences("TTTT", "aacgtggcatgacgtggataa") is False

    # Comparaison insensible à la casse, comme pour l'exercice 04
    assert find_dna_pattern_occurrences("acgt", "AACGTGGCATGACGTGGATAA") == [2, 1, 11]

    # A plus long que B : ne peut pas s'y trouver
    assert find_dna_pattern_occurrences("aacgtggcatgacgtggataaaa", "acgt") is False
    ###
