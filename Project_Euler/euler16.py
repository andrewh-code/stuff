#!/usr/bin/python

#=================================================================
# Project Euler: http://www.projecteuler.net
# Problem 16: What is the sum of the digits of the number 2^1000
#
#=================================================================
y = 0
for x in str(2**1000):
    y = y + int(x)
print y

