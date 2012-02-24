#!/usr/bin/python

#============================================================================
# Project Euler: http://wwww.projecteuler.net
# Problem 8: http://projecteuler.net/index.php?section=problems&id=9
# Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000.
#============================================================================

#import libraries
import sys
import math
import time

#initialize variables
i = 0
j = 0
tf = 0
tf2 = 0

"""============================================================================
The smallest Pythagorean triplet in a set of natural numbers is (3,4,5).
So instead of starting our search at 1, we can start our search at 3 as it is 
the lowest number any Pythagorean triplet can have. Also, one requirement 
(for this problem) is a < b, so we can start our second loop at 4.

Dr. Richard K. Guy proves that Pythagorean triplets share these characteristics:
    1. The product of a and b is divisible by 12
    2. The product of a, b, and c is divisible by 60
     
    Source: Guy, R. K. "Triangles with Integer Sides, Medians, and Area." 
              D21 in Unsolved Problems in Number Theory, 2nd ed. New York: 
              Springer-Verlag, pp. 188-190, 1994.
============================================================================"""
while i<10:
     t0 = time.clock()
     for a in range(3,1000):
          for b in range (4,1000-a):
               if a < b and (a*b)%12 == 0 and a+b+math.sqrt(a**2 + b**2)==1000:
                    print a, b, math.sqrt(a**2 + b**2)
                    print "product of a,b,c is: ", a*b*math.sqrt(a**2 + b**2)
     t1 = time.clock() - t0
     
     tf += t1
     i += 1
print "time:", tf/10

"""============================================================================
Although this method satisfies the requirements, it is not as robust as the previous solution
Solve through basic algebra given the two equations:
1.  a + b + c = 1000
2.  a^2 + b^2 = c^2

     a^2 + b^2 = (1000-a-b)(1000-a-b)
     a^2 + b^2 = 1000*1000 - 1000a - 1000b - 1000a + a^2 + ab - 1000b + ab + b^2
     0 = 1000*1000 - 1000a - 1000b - 1000a + a^2 + ab - 1000b + ab +b^2 - a^2 - b^2
     0 = 1000*1000 - 2000a - 2000b + 2ab
     0 = 500 - a - b + ab/1000
     500 = a + b - ab/1000
     500 - b = a - ab/1000
     500-b = a(1 - b/1000)
     a = 500-b/(1-b/1000)
     a = 500-b/(1000 - b)
============================================================================"""

t2 = time.clock()
for y in range(1,500):
     #(500-y) has to be multiplied by 1000 as (500-y)%(1000-y) ALWAYS == 0 (ie. x%(x+1) ALWAYS == 0 
     if 1000*(500-y)%(1000-y) == 0 and (1000*(500-y)/(1000-y)) < y:
          print 1000*(500-y)/(1000-y), y, int(math.sqrt((1000*(500-y)/(1000-y))**2 + y**2))
          #for readability purposes, use x and z variables
          x = 1000*(500-y)/(1000-y)
          z = 1000 - x - y
          print "product of x,y,z is: ", x*y*z 

t3 = time.clock() - t2 

print "time:", t3