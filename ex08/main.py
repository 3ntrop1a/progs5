#! /usr/bin/env python3
#coding : utf-8

from sys import argv
import re

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def generate_wordsnumber_suite(suite : list) :
    """
    Rename and document this function accordingly.
    
        Parameters:
            
        
        Raises:
            
        
        Returns:
            
    """
    k = suite[-1]
    couples = suite[0]
    result = []
    for i in range(1, k + 1):
        chaine = ""
        for key in couples:
            if i % key == 0:
                chaine += couples[key]
        if chaine != "":
            result.append(chaine)
        else:
            result.append(str(i))
    return result



def main(line: str):
    
    ### Line parsing and BAD INPUT checking
    
    ###
    line = line.strip().split(' ')
        ### Line parsing and BAD INPUT checking
        
    if len(line)<1:
        raise BadInputException()
    ### Frontal function call and exceptions management
    s={}
    k=int(line[-1])
    for i in range(0,len(line)-1,2):
        s[int(line[i])]=line[i+1]

    

    results = generate_wordsnumber_suite([s, k])
    for item in results:
        print(item)

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
