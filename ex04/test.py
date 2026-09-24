#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import convert_dna_to_rna, NotADNASequenceException

def testConvertDnaToRna():

    ### Nominal Cases
    assert convert_dna_to_rna("GATTACA") == "GAUUACA"
    assert convert_dna_to_rna("gattaca") == "GAUUACA"
    assert convert_dna_to_rna("gAtTaCa") == "GAUUACA"
    assert convert_dna_to_rna("ACGT") == "ACGU"
    # Séquence sans aucun T/t : uniquement une mise en majuscule
    assert convert_dna_to_rna("acg") == "ACG"
    # Séquence d'un seul caractère
    assert convert_dna_to_rna("t") == "U"
    assert convert_dna_to_rna("A") == "A"
    ###

    ### Edge cases and corner cases
    # Caractère hors de l'alphabet ADN
    with pytest.raises(NotADNASequenceException):
        convert_dna_to_rna("x")

    # Séquence par ailleurs valide mais contenant un caractère invalide
    with pytest.raises(NotADNASequenceException):
        convert_dna_to_rna("ACGTx")

    # Séquence contenant déjà de l'ARN (U n'est pas un caractère ADN valide)
    with pytest.raises(NotADNASequenceException):
        convert_dna_to_rna("ACGU")

    # Chaîne vide
    with pytest.raises(NotADNASequenceException):
        convert_dna_to_rna("")
    ###
