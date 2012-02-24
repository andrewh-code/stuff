#!/usr/bin/python

#============================================================
# Project Euler: Problem 2
# http://projecteuler.net/index.php?section=problems&id=2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms
#============================================================

#import modules
import sys

#declare and initialize variables
def fib(x):
        sum = 0
        i, j = 0, 1
        while (j < x):
                print j
                i,j = j, j+i
                if (j%2 == 0):
                        sum = sum + j
        return sum

result = fib(4000000)
print "The sum of even valued numbers below 4,000,000 is:", result
#if __name__ == '__fibonacci__':
#       fibonacci()
