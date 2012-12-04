#!/usr/bin/python

#import libraries
import sys
import os

def main():

    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for char in alphabet_list:
        file = '../data/' + char + '.txt'
        
        try:
            os.remove(file)
        except OSError:
            print file, "not deleted. Either it could not be found or did not exist in the first place"
            pass
        else:
            print file, "successfully deleted"


if __name__ == "__main__":
    main()