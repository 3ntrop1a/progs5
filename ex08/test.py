#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import generate_wordsnumber_suite

def testFrontalFunction():

    ### Nominal Cases
    assert generate_wordsnumber_suite([{3: "Fizz", 5: "Buzz"}, 15]) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
        "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
    ]
    assert generate_wordsnumber_suite([{2: "A", 3: "B", 5: "C"}, 15]) == [
        "1", "A", "B", "A", "C", "AB", "7", "A", "B", "AC",
        "11", "AB", "13", "A", "BC",
    ]
    # Un seul diviseur, qui tombe exactement sur K
    assert generate_wordsnumber_suite([{7: "Lucky"}, 7]) == [
        "1", "2", "3", "4", "5", "6", "Lucky",
    ]
    ###

    ### Edge cases and corner cases
    # Suite S vide : on affiche simplement les entiers de 1 à K
    assert generate_wordsnumber_suite([{}, 5]) == ["1", "2", "3", "4", "5"]

    # K == 1 : borne minimale, aucun diviseur ne peut s'appliquer avant 1
    assert generate_wordsnumber_suite([{2: "Even"}, 1]) == ["1"]

    # Suite vide et K == 1
    assert generate_wordsnumber_suite([{}, 1]) == ["1"]
    ###