#!/usr/bin/python

import sys
from StringBinaryToDecimal import StringBinaryToDecimal

global UPPER_BIT
global ASCII_BIN_SIZE
global KEY
UPPER_BIT = 10
ASCII_BIN_SIZE = 8
KEY = 5

class CipherFeedback():
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def EncryptCFB(self, iv, msg_list, chunk_size):
        self.iv = iv
        self.msg_list = msg_list
        self.chunk_size = chunk_size
        
        str = StringBinaryToDecimal()
        iv_dec = str.strbin2dec(iv)
        msg_bin = ''
        
        count = 0
        while (count < len(msg_list)):
            msg_list[count] = str.strbin2dec(msg_list[count])
            if (count == 0):
                block_encryption = iv_dec ^ KEY     #change encryption algorithm
                msg_list[count] ^= block_encryption
            else:
                block_encryption = msg_list[count-1] ^ KEY      #change encryption algorithm
                msg_list[count] ^= block_encryption
            msg_bin += bin(int(msg_list[count]))[2:].zfill(chunk_size)
            count += 1

        return msg_bin
            
    def DecryptCFB(self, encrypt_bin_msg, chunk_size):
        self.encrypt_bin_msg = encrypt_bin_msg
        self.chunk_size = chunk_size
        
        str = StringBinaryToDecimal()
        decrypted_msg = ''
        
        msg_list = [str.strbin2dec(msg_bin[x:x+chunk_size]) for x in xrange(0,len(msg_bin),chunk_size)]