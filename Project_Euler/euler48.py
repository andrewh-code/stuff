#!/usr/bin/python

#============================================================================
# Project Euler: http://wwww.projecteuler.net
# Problem 48:
# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000
#============================================================================


#import libriares
import sys
import math

sum = 0
mod = pow(10,10)
for i in range(1,1001):
    sum = sum + pow(i,i)

s = str(sum)[-10:]
print s