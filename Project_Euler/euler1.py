#!/usr/bin/python

#============================================================
# Project Euler: http://www.projecteuler.net
# Problem 1: Add all the natural numbers below one thousand that are multiples of 3 or 5.
# http://projecteuler.net/index.php?section=problems&id=1
#============================================================

#import libraries and modules
import math

#declare/initialize variables
i = 0;
sum = 0;

#def loop():
for i in range(0, 1000):
	if (i % 3 == 0) or (i % 5 == 0):
		sum += i
print "The sum of numbers is: ", sum
#loop();