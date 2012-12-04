#!/usr/bin/python

#import libraries
import sys
import re
import Constants as c

class Preprocess:
    def __init__(self):
        self.string_input = ''

    #==================================================
    # Reorders string into alphabetical order
    # Input: search_string
    # Output: 
    #==================================================
    def reorderString(self, string_input):
        self.string_input = string_input
        
        #quick sort
        #if (string_input == ''):
        #    return None
        #else:
        #
        #    pivot = string_input[0]
        #    lesser = reorderString([x for x in string_input[1:] if x < pivot])
        #    greater = reorderString([x for x in string_input[1:] if x >= pivot])
            
        #    return lesser + [pivot] + greater
    
        return sorted(self.string_input.lower()) #last resort :P

    #==================================================
    # Checks for only alphabet characters (should be lower case) and the number of tiles inputted
    # Input: search_string
    # Output: boolean; True if it passes checks, False if fails checks
    #==================================================
    def checkInput(self, search_string):
        self.search_string = search_string
        charAllowed = 'abcdefghijklmnopqrstuvwxyz_'
        #match = 0
        
        #check for no input
        if ((self.search_string == '') or (self.search_string == ' ')):
            print "Error: null value inputted, exiting."
            return False

        #check length of string
        if ((len(self.search_string) < 1) or (len(self.search_string) > c.TILES)):
            print "Error: Please input string of proper length between 1 and ", c.TILES,'.'
            return False
        
        match = re.match("^[a-z]|_{0,2}$",self.search_string)
        if match:
            return True
        else:
            print "Error: Only characters from a-z and underscore are allowed. Maximum 2 underscores allowed"
            return False
            
        