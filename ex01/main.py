#! /usr/bin/env python3
#coding : utf-8

from sys import argv
import re

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


INPUT_REGEX = re.compile(r'^-?\d+(\.\d+)?([eE][+-]?\d+)?$')


def to_compact_representation(value_str: str) -> str:
    """
    Convertit un littÃ©ral entier ou flottant vers sa reprÃ©sentation
    dÃ©cimale la plus compacte (notation classique ou scientifique),
    en conservant le comportement d'arrondi par dÃ©faut de Python.
    
        Parameters:
            value_str (str): le littÃ©ral numÃ©rique Ã  convertir
        
        Raises:
            BadInputException: si value_str n'est pas un entier ou un flottant signÃ© valide
        
        Returns:
            str: la reprÃ©sentation la plus courte de la valeur
    """
    if isinstance(value_str, (int, float)):
        value_str = str(value_str)

    if not isinstance(value_str, str) or not INPUT_REGEX.match(value_str):
        raise BadInputException(f"Invalid numeric literal: {value_str!r}")

    is_float = '.' in value_str or 'e' in value_str.lower()
    value = float(value_str) if is_float else int(value_str)

    # Si c'est un flottant, on le formate en notation fixe standard pour éviter que str() produise déjà un 'e'
    classic_repr = f"{value:.15f}".rstrip('0').rstrip('.') if is_float else str(value)

    raw_sci = f"{float(value):.6e}"
    mantissa, exponent = raw_sci.split('e')
    mantissa = mantissa.rstrip('0').rstrip('.')
    exp_sign = '-' if exponent[0] == '-' else ''
    exp_digits = exponent[1:].lstrip('0') or '0'
    scientific_repr = f"{mantissa}e{exp_sign}{exp_digits}"

    return classic_repr if len(classic_repr) <= len(scientific_repr) else scientific_repr


def main(line: str):
    
    ### Line parsing and BAD INPUT checking
    value_str = line.strip()
    if value_str == "":
        raise BadInputException("Empty line")
    ###
    
    
    ### Frontal function call and exceptions management
    result = to_compact_representation(value_str)
    print(result)
    ###


if __name__ == "__main__":
    
    ### Input file reading
    ### One line = one call to main function
    with open(argv[1]) as inputFile:
        for line in inputFile:
            try:
                main(line)
            except BadInputException:
                print("BAD INPUT")
    ###