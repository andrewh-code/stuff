#!/usr/bin/python

#============================================================
# Project Euler: http://www.projecteuler.net
# http://projecteuler.net/index.php?section=problems&id=5
# Problem 5: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#============================================================

#this is one of those problems that make you think and realize how easy it
#is to do in your head but when you have to explain it to a computer,
#it's hard.

#import modules/libraries
import sys

def denominator(x,y):
     return x if y==0 else denominator(y,x%y)
     """
     if (x%y == 0):
          return x
     else:
          return denominator(y, x%y)
     #This needs to be tweaked a bit to work
     """  

def multiple(x,y):
     return x*y/denominator(x,y) 

#soo many shortcuts in python...need to look them up
print reduce(multiple, range(2,21))