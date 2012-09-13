#!/usr/bin/python

#============================================================
# Project Euler: Problem 14
# http://projecteuler.net/problem=14
# 
"""
The following iterative sequence is defined for the set of positive integers:
n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
#============================================================


#start from 999,999
#if odd, 3n+1. If even n/2  --> implement through recursion, break case when n = 1 (implement a counter)
#check length of chain, if length is longer than previous, replace length of longest chain and corresponding number

#import libraries and classes
import sys
import time

#define constants
START = 999999
 
def collatz_recursion(cache, n):
    if n in cache:
        return cache[n]
    if (n&1)==0: 
        cache[n] = 1 + collatz_recursion(cache, n/2)
    else:
        cache[n] = 1 + collatz_recursion(cache, 3*n + 1)
    return cache[n]
    
def main():
    count = 0
    longest_count = 0
    associated_number = 0
    iteration = START
    x = 0
    cache = {1:1}
    t = time.time()
    
    for iteration in range(1, START):
        x = collatz_recursion(cache, iteration)
        if (x > longest_count):
            associated_number = iteration
            longest_count = x
    print "longest chain is:", longest_count, "at number:", associated_number
    print "it took this long:", (time.time()-t)   


if __name__ == "__main__":
    main()

