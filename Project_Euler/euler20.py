#!/usr/bin/python

#============================================================
# Project Euler: Problem 20
# http://projecteuler.net/problem=20
# 
# n! means n  (n  1)  ...  3  2  1
#
# For example, 10! = 10  9  ...  3  2  1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#============================================================

#import libraries/classes
import sys

#declare constants
TEN = 100

def factorial(n):
    if (n==1): 
        return n
    else: 
        return n * factorial(n-1)

def sumDigits(n):
    sum = 0
    while (n > 0):
        sum = sum + (n%10)
        n = n/10
    return sum
    
def main():
    x = 1
    x = factorial(TEN)
    
    result = sumDigits(x)
    print result
    
if __name__ == "__main__":
    main()
