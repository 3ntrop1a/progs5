#! /usr/bin/env python3
#coding : utf-8

from sys import argv
import re

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def find_words_occurrences(words : str) :
    """
    Rename and document this function accordingly.
    
        Parameters:
            
        
        Raises:
            
        
        Returns:
            
    """
    dict_word={}
    for word in words:
        if word.lower() not in dict_word:
            dict_word[word.lower()]=1
        else:
            dict_word[word.lower()]+=1
    

    return ",".join(f"{a}:{b}" for a, b in sorted(dict_word.items()))

def main(line: str):
    
    ### Line parsing and BAD INPUT checking
    
    ###
    line = line.strip()
    if len(line) < 1:
        raise BadInputException('String is empty')

    words = line.split(" ")
    for word in words:
            if not re.match(r"^[a-zA-Z]+$", word): raise BadInputException()
    
    
    ### Frontal function call and exceptions management
    
    ###
    print(find_words_occurrences(words))


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
