#! /usr/bin/env python3
#coding : utf-8

from sys import argv
import re

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def find_chain_in_words(chain : str, words : str) :
    """
    Rename and document this function accordingly.
    
        Parameters:
            
        
        Raises:
            
        
        Returns:
            
    """
    element = chain.split("*")
    valid_word = []
    for word in words:
        start = 0
        find = True
        for elem in element:
            index = word.find(elem, start)
            if index == -1:
                find = False
                break
            start = index + len(elem)
        if find:
            valid_word.append(word)

    return " ".join(valid_word)

def main(line: str):
    
    ### Line parsing and BAD INPUT checking
    line = line.strip()
    if len(line) < 1:
        raise BadInputException('String is empty')
    
    ###
    args = line.split(" ")
    if not re.match(r"^[a-zA-Z\*]+$", args[0]): raise BadInputException()

    words=list()
    with open(args[1]) as inputFile:
        for line in inputFile:
            try:
                line = line.strip()
                if len(line) < 1:
                    raise BadInputException('String is empty')
                word = line.split(" ")
                for w in word:
                    if not re.match(r"^[a-zA-Z]+$", w): 
                        raise BadInputException()
                words.extend(word)
            except BadInputException:
                print("BAD INPUT")
    print(find_chain_in_words(args[0],words))

    ### Frontal function call and exceptions management
    
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
