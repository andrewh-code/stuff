#!/usr/bin/python

#============================================================================
# Project Euler: http://wwww.projecteuler.net
# Problem 12:
# What is the value of the first triangle number ot have over five hundred divisors
# First attempt
#============================================================================

import sys
import time
import math

#declare and initialize variables/constants
input = 1
count_factor = 1
limit = 1
FACTOR_LIMIT = 500

def triangleNumbers(x):
    return ((x**2 + x)/2)

start_time = time.time()

while count_factor < FACTOR_LIMIT:

    y = int((triangleNumbers(input)/2) + 1)
    count_factor = 1
    
    for possible_factor in range(1,y):
        if (y%possible_factor == 0):
            count_factor += 1
    print y, "\t", count_factor
    input += 1
    
end_time = time.time()

print y*2
print "it took", end_time - start_time, "seconds to complete"
