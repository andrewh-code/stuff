#!/usr/bin/python 

import sys
import binascii
from StringBinaryToDecimal import StringBinaryToDecimal

global ASCII_BIN_SIZE
ASCII_BIN_SIZE = 8

class ConvertMsg():
    def __init__(self):
        self.x = 0
        self.y = 0
    
    #converts the inputted message into a complete binary string representation
    #ex) msg = hi, msg_list = 0101010000111000
    def Msg2Bin(self, plaintext_msg, chunk_size):
        self.plaintext_msg = plaintext_msg
        self.chunk_size = chunk_size
        
        msg_list = []
        last_block_bit_count = 0
        z = ''
        
        #convert entire message into binary representation
        for x in plaintext_msg:
            y = bin(ord(x))[2:].zfill(ASCII_BIN_SIZE)
            z += y
        
        #split the entire message into chunk_size-bit blocks
        for i in range(0, len(z), chunk_size):
            msg_list.append(z[i:i+chunk_size])
       
        #while loop to check last block in list, make sure that it's CHUNK_SIZE bit length.
        #If not, keep padding 10 until last block reaches the CHUNK_SIZE length
        while (len(msg_list[-1]) < chunk_size):
            msg_list[-1] += '10'
            last_block_bit_count += 1
        #add another block to end of list to tell cbc how much the last block was filled by
        if (last_block_bit_count != 0):
            msg_list.append(bin(last_block_bit_count)[2:].zfill(chunk_size))

        return msg_list
        
    def Bin2Msg(self, decrypt_bin_msg, chunk_size):
        self.decrypt_bin_msg = decrypt_bin_msg
        self.chunk_size = chunk_size
        
        str = StringBinaryToDecimal()
        output_msg = ''
        
        msg_list = [str.strbin2dec(decrypt_bin_msg[x:x+ASCII_BIN_SIZE]) for x in xrange(0,len(decrypt_bin_msg),ASCII_BIN_SIZE)]
        
        for x in msg_list:
            y = chr(x)
            output_msg += y 
        
        return output_msg
        
        