#!/usr/bin/python 
import sys

# ============================================================
# Name:             Andrew Ho, hoa9@mcmaster.ca
#                   Arvi Narayanan, narayaa@mcmaster.ca
# Student Number:   0655827, 0658512
# Course:           Software Engineering 4C03
# Assignment:       2
# Date:             March 30, 2012
#
# Notes:
#   Documentation:  Refer to documentation_a2.txt
#   Dependencies:   none, standalone file.
# ============================================================

class StringBinaryToDecimal:
    def __init__(self):
        self.x = 0
        self.y = 0
        
 #transform this to recurssion
    def strbin2dec(self, s):
        self.s = s
        
        count = 0
        dec = 0
        for x in s[::-1]:
            if (x == '1'):
                dec += pow(2, count)
            count += 1
        return int(dec)
