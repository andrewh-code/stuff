#!/usr/bin/python

#============================================================
# Project Euler: http://www.projecteuler.net
# http://projecteuler.net/index.php?section=problems&id=4
# Problem 4: Find the largest palindrome made from the product of two 3-digit numbers.
#============================================================

product = 0
for i in range(100,1000):
     for j in range(100,1000):
          if str(i*j) == str(i*j)[::-1]:
               if (product < i*j):
                    product = i*j
          
print "The maximum palindromic number is:", product

          
