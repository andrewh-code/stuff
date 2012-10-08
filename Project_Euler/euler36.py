#!/usr/bin/python

# ============================================================
# Project Euler 36
# http://projecteuler.net/problem=36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)
# ============================================================

import sys
import time

def str2bin(s):
    return str(s) if s<=1 else str2bin(s>>1) + str(s&1)

def main():
    sum = 0

    t0 = time.time()
    for i in range(0,1000000):
        if ((str(i) == str(i)[::-1]) and (str2bin(i) == str2bin(i)[::-1])):
            #s = str2bin(i)
            sum += i
            #print i, s
    print sum
            
    t1 = time.time() - t0
    print "time it took:", t1
if __name__ == "__main__":
    main()