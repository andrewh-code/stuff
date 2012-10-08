#!/usr/bin/python

# ============================================================
# Project Euler 34
# http://projecteuler.net/problem=34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
# ============================================================

import sys
import time

def factorial(n):
    if (n == 1) or (n == 0):
        return 1
    else:
        return n * factorial(n-1)

def main():
    
    digit = 0
    fact_digit = 0
    sum_digits = 0
    sum = 0
    t1 = time.time()
    for x in range(3,100000):
        i = x
        while (x>0):
            digit = x%10
            sum_digits += factorial(digit)
            x /=10
        if (sum_digits == i):
            sum += sum_digits
        sum_digits = 0
    
    t2 = time.time() - t1
    print sum, t2
    
if __name__ == "__main__":
    main()