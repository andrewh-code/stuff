#!/usr/bin/python

#============================================================
# Project Euler: http://www.projecteuler.net
# http://projecteuler.net/index.php?section=problems&id=3
# Problem 3: Find the largest prime factor of a composite number.
#============================================================
#http://thetaoishere.blogspot.com/2009/04/finding-largest-prime-factor.html

#import libraries
import sys

#x = 600851475143
x = input("Enter the real number: ")
def input_check(n):
	if (n < 0):
		print "number can not be negative number"
		exit()
	else:
		return n
x2 = input_check(x)	
#better if you put it in a while loop. You know why?
for i in range(2, x2):
	for j in range (2, i):
		if (i % j == 0):
			break
	else:
		prime = i

print "the largest prime number is", prime

