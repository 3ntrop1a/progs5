#! /usr/bin/env python3
#coding : utf-8

from sys import argv
import re

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


class NotEnoughValues(ValueError):
    """
    Raised when a given input word is longer than 16 characters
    """
    pass

def find_first_ranked_word(words) :
    """
    Rename and document this function accordingly.
    
        Parameters:
            
        
        Raises:
            
        
        Returns:
            
    """
    
    if len(words)<2:
        raise NotEnoughValues
    win_word=words[0]
    for word in words[1:]:
        if word.lower() < win_word.lower() :
            win_word=word

    
    return win_word



def main(line: str):
    
    ### Line parsing and BAD INPUT checking
    
    ###
    line_split = line.split(' ')
    if len(line_split) < 2 : raise BadInputException()
    for word in line_split:
        if not re.match(r"^[a-zA-Z]+$", word): raise BadInputException()

    
    ### Frontal function call and exceptions management
    
    print(find_first_ranked_word(line_split))
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
