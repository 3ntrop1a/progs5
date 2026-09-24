#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import find_words_occurrences

def testFindWordsOccurrences():

    ### Nominal Cases
    assert find_words_occurrences(["alice", "bob"]) == "alice:1,bob:1"
    # Répétitions simples, déjà en ordre alphabétique
    assert find_words_occurrences(["a", "a", "a", "b"]) == "a:3,b:1"
    # Un seul mot
    assert find_words_occurrences(["single"]) == "single:1"
    # Plusieurs mots avec des fréquences différentes
    assert find_words_occurrences(
        ["mango", "apple", "mango", "cherry"]
    ) == "apple:1,cherry:1,mango:2"
    ###

    ### Edge cases and corner cases
    # Comptage insensible à la casse, restitution en minuscule, et tri
    # alphabétique du résultat
    assert find_words_occurrences(["Bob", "alice", "BOB"]) == "alice:1,bob:2"

    # Tri alphabétique nécessaire alors que l'ordre d'apparition est
    # différent de l'ordre alphabétique
    assert find_words_occurrences(
        ["Zoo", "apple", "zoo", "Apple", "mango"]
    ) == "apple:2,mango:1,zoo:2"
    ###
