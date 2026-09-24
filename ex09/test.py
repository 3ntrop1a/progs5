#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import find_chain_in_words

def testFindChainInWords():

    ### Nominal Cases
    assert find_chain_in_words(
        "a*et",
        ["laoreet", "nascetur", "aliquet", "pharetra", "aliquet", "xyz"],
    ) == "laoreet nascetur aliquet pharetra aliquet"

    # Joker en fin de motif : toute suite de caractères après "cat"
    assert find_chain_in_words(
        "cat*", ["category", "catalog", "dog"]
    ) == "category catalog"

    # Respect strict de la casse
    assert find_chain_in_words(
        "Morb*a", ["Morbihan", "morbihan", "Something"]
    ) == "Morbihan"

    # Aucun mot ne correspond
    assert find_chain_in_words("zzz", ["laoreet", "aliquet"]) == ""
    ###

    ### Edge cases and corner cases
    # Le joker * doit pouvoir représenter une suite vide de caractères
    # entre deux tronçons littéraux
    assert find_chain_in_words("a*et", ["aet", "xax"]) == "aet"

    # Le joker en tout début de motif doit lui aussi pouvoir être vide
    assert find_chain_in_words(
        "*bihan", ["Morbihan", "bihan", "xbihan"]
    ) == "Morbihan bihan xbihan"

    # Liste de mots vide
    assert find_chain_in_words("a*et", []) == ""

    # Motif sans aucun joker : simple recherche de sous-chaîne exacte
    assert find_chain_in_words("cat", ["category", "concatenate", "dog"]) == "category concatenate"
    ###