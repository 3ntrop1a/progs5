#! /usr/bin/env python3
#coding : utf-8

from math import sin, sqrt
from sys import argv
import re

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def compute_sqrt_sinc_product(A: float, B: float) :
    """
    Rename and document this function accordingly.
    
        Parameters:
            
        
        Raises:
            
        
        Returns:
            
    """
    if A == 0 or B == 0:
        raise ArithmeticError("Division by zero")
    product = (sin(A) / A) * (sin(B) / B)
    if product < 0:
        raise ArithmeticError()
    return round(sqrt(product), 5)

def main(line: str):
    
    ### Line parsing and BAD INPUT checking
    line_split = line.split(' ')
    if len(line_split) != 2 : raise BadInputException()
    A, B = line_split
    A = float(A)
    B = float(B)
    ###

    ### Frontal function call and exceptions management
    try:
        print(compute_sqrt_sinc_product(A,B))
    except ArithmeticError:
        print("ARITHMETIC ERROR")
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
