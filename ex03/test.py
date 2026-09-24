#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import compute_sqrt_sinc_product

def testComputeSqrtSincProduct():

    ### Nominal Cases
    assert compute_sqrt_sinc_product(2.1, 3) == 0.13905
    assert compute_sqrt_sinc_product(1, 1) == 0.84147
    assert compute_sqrt_sinc_product(0.5, 0.5) == 0.95885
    assert compute_sqrt_sinc_product(10, 10) == 0.0544
    assert compute_sqrt_sinc_product(-1, 1) == 0.84147
    ###

    ### Edge cases and corner cases
    with pytest.raises(ArithmeticError):
        compute_sqrt_sinc_product(0.0, 1.0)

    with pytest.raises(ArithmeticError):
        compute_sqrt_sinc_product(1.0, 0.0)

    with pytest.raises(ArithmeticError):
        compute_sqrt_sinc_product(0.0, 0.0)

    # Produit négatif sous la racine carrée : aucun résultat réel possible,
    # la spécification impose ARITHMETIC ERROR dans ce cas.
    with pytest.raises(ArithmeticError):
        compute_sqrt_sinc_product(4, 1)

    with pytest.raises(ArithmeticError):
        compute_sqrt_sinc_product(1, 4)
    ###
