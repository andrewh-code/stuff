#!/usr/bin/python

#============================================================
# Project Euler: Problem 25
# http://projecteuler.net/problem=25
# 
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?
#============================================================

#import classes and libraries
import sys

#constants
LIMIT = 1000

def fibonacci():
    
    n = 1
    n_1 = 0
    n_2 = 1
    
    i = 1
    
    while (len(str(n)) < LIMIT):    #while the length of the fibonacci number is less than 1000s
        n = n_1 + n_2               #fibonacci algorithm
        n_1 = n_2                   #set the previous value to the previous, previous value
        n_2 = n                     #set the previous previous value to the most recent value
        i = i+1                     #actual number being output
    print i
        
def main():
    
    fibonacci2()


if __name__ == "__main__":
    main()