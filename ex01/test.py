import pytest
from main import to_compact_representation


def testFrontalFunction():

    ### Nominal Cases
    
    assert to_compact_representation(17) == "17"
    assert to_compact_representation(-42) == "-42"
    assert to_compact_representation(0) == "0"
    
    assert to_compact_representation(3.14) == "3.14"
    assert to_compact_representation(2.5) == "2.5"
    assert to_compact_representation(-38345.6789098765452) == "-3.834568e4"
    ###

    ### Edge cases and corner cases
    assert to_compact_representation(0.0000001) == "1e-7"
    # Très grande valeur flottante : idem
    assert to_compact_representation(100000000.0) == "1e8"
    # Valeur négative proche de zéro
    assert to_compact_representation(-0.0000001) == "-1e-7"
    # Flottant dont la partie entière est nulle
    assert to_compact_representation(0.5) == "0.5"
    ###
