#!/usr/bin/python

import sys
import random

class initializationVector():
    def __self__(init):
        self.x = 0;
        self.y = 0;
    
    def InitializationVector(self, chunk_size):
        self.count = 0
        self.diff = 0
        
        count = 0
        diff = 0
        
        #create two random numbers with an integer range between 0 and UPPER_BIT
        iv_a = random.randint(0,pow(2,chunk_size/2)-1)
        iv_b = random.randint(0,pow(2,chunk_size/2)-1)
        
        #append the two random numbers to create a whole CHUNK_SIZE bit initialization vector (iv)
        iv = (iv_a << chunk_size/2) + iv_b
        iv = bin(iv)[2:]   #remove the prefix '0b' from the binary representation
        iv = iv.zfill(chunk_size)
        #diff = chunk_size - len(iv)
        while (count < (chunk_size - len(iv))):
            iv = '0' + iv
            count += 1
        
        return iv