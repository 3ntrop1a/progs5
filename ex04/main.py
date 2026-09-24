#! /usr/bin/env python3
#coding : utf-8

from sys import argv
import re


class NotADNASequenceException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass

def convert_dna_to_rna(sequence: list) :
    """
    Rename and document this function accordingly.
    
        Parameters:
            
        
        Raises:
            
        
        Returns:
            
    """
    if not DNA_RE.match(sequence):
        raise NotADNASequenceException(
            f"Invalid DNA sequence: '{sequence}' contains non-DNA characters."
        )
    return sequence.upper().replace("T", "U")

DNA_RE = re.compile(r"^[acgtACGT]+$")

def main(line: str):

    line = line.strip()
    ### Line parsing and BAD INPUT checking
    if len(line)<1:
        raise NotADNASequenceException('String is empty')
    
    return convert_dna_to_rna(line)


if __name__ == "__main__":
    
    ### Input file reading
    ### One line = one call to main function
    with open(argv[1]) as inputFile:
        for line in inputFile:
            try:
                print(main(line))
            except NotADNASequenceException:
                print("NOT A DNA SEQUENCE")
    ###
