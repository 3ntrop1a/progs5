#! /usr/bin/env python3
#coding : utf-8

from sys import argv
import re

class NotADNASequenceException(ValueError):
    """Raised when a given input isn't a DNA sequence"""
    pass

DNA_RE = re.compile(r"^[acgtACGT]+$")

def find_dna_pattern_occurrences(pattern : str, sequence: str) :
    """
    Rename and document this function accordingly.
    
        Parameters: sequences :
            pattern (str): sequence ADN A to find.
            sequence (str): sequence ADN B where we search.
            
        
        Raises:
            
        
        Returns:
            
    """
    pattern_lower = pattern.lower()
    sequence_lower = sequence.lower()
    if not DNA_RE.match(sequence_lower):
            raise NotADNASequenceException(
                f"Invalid DNA sequence: '{sequence}' contains non-DNA characters."
            )
    elif not DNA_RE.match(pattern_lower):
            raise NotADNASequenceException(
                f"Invalid DNA sequence: '{sequence}' contains non-DNA characters." 
            )
    else :
        positions = []
        start = 0
        while True:
            index = sequence_lower.find(pattern_lower, start)
            if index == -1:
                break
            positions.append(index)
            start = index + 1  
    if not positions:
        return False

    return [len(positions)] + positions
        



def main(line: str):

    line = line.strip()
    if len(line) < 1:
        raise NotADNASequenceException('String is empty')

    parts = line.split(" ")
    if len(parts) != 2:
        raise NotADNASequenceException(
            "Expected exactly two DNA sequences separated by a space"
        )

    pattern, sequence = parts
    return find_dna_pattern_occurrences(pattern.lower(), sequence.lower())


if __name__ == "__main__":
    
    ### Input file reading
    ### One line = one call to main function
    with open(argv[1]) as inputFile:
        for line in inputFile:
            try:
                main(line)

            except NotADNASequenceException:
                print("BAD INPUT")
    ###
