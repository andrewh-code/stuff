#!/usr/bin/python

import sys

class Encrypt():
    def __init__(self):
        self.x = 0
        self.y = 0
    
    #rotate shift function, basically split the lower and upper half of the binary representation of the char and swap the two
    #added for more complexity of the encryption algorithm (not implemented in current design)
    def RotateShift(self, block, chunk_size):
    
        block_l = block[0:chunk_size/2]
        block_r = block[chunk_size/2:chunk_size]
        block = block_r + block_l
        
        return block