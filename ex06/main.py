#! /usr/bin/env python3
#coding : utf-8

from sys import argv
import re
import os

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass

import csv
def frontal_function(m,n,l,c) :
    """
    Rename and document this function accordingly.
    
        Parameters:
            
        
        Raises:
            
        
        Returns:
            
    """

    try:

        total=0.0
    
        with open (c, mode='r', newline="") as f:
            reader = csv.DictReader(f, delimiter=",")

            if reader.fieldnames is None:
                raise BadInputException
            for col in l:
                if col not in reader.fieldnames:
                      raise BadInputException()
            count=0
            for id,row in enumerate(reader):
                count+=1
                if m<=id<=n:
                    row_product= 1.0
                    for col in l:
                        try:
                            val = float(row[col])
                        except (ValueError, TypeError):
                            raise BadInputException()
                    
                        row_product*=val
                    total+=row_product 
            if n >= count:
                raise BadInputException()

    except (OSError, csv.Error):
        raise BadInputException()
                    
    return  total


def main(line: str):
    ### Line parsing and BAD INPUT checking
        
    ###

    clean_line = line.rstrip("\r\n")
    if not clean_line:
        raise BadInputException()


    line_split = clean_line.split(' ')
    if any(token == "" for token in line_split):
        raise BadInputException()
    
    
    if len(line_split) < 4: 
        raise BadInputException()
    try:
        m = int(line_split[0])
        n= int(line_split[1])
    except ValueError:
        raise BadInputException()
    
    if m > n or m < 0:
        raise BadInputException("m cannot be bigger than n")

    l=line_split[2:-1]
    if l == [] : raise BadInputException()
    for word in l:
        if not re.match(r"^[a-zA-Z]+$", word): raise BadInputException()
    c=line_split[-1]
    if not os.path.isfile(c) or not os.access(c, os.R_OK):
        raise BadInputException()

    
    
    return frontal_function(m,n,l,c.strip())
    ### Frontal function call and exceptions management
    
    ###


if __name__ == "__main__":
    
    ### Input file reading
    ### One line = one call to main function
    with open(argv[1]) as inputFile:
        for line in inputFile:
            try:
                print(main(line))
            except BadInputException:
                print("BAD INPUT")
    ###
