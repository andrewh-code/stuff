#!/usr/bin/python

#============================================================================
# Project Euler: http://wwww.projecteuler.net
# Problem 6: http://projecteuler.net/index.php?section=problems&id=6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#============================================================================
#import libraries and modules
import sys

x = int(sys.argv[1])
def sumOfSquares(n):
	if (n==0):
		return n 
	else:
		return n**2+sumOfSquares(n-1)

def squareOfSums(n):
	if (n==0):
		return n
	else:
		return n+squareOfSums(n-1)

print abs(sumOfSquares(x) - squareOfSums(x)**2)

"""
much easier way is to use the formulas for sum of squares and square of sums  
sum = x(x+1)/2;
square = (2*(n**3) + 3*(n**2) + n)/6
difference = sum - square
"""
