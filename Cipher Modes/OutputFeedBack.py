#!/usr/bin/python

import sys
from StringBinaryToDecimal import StringBinaryToDecimal

global KEY
KEY = 5

class OutputFeedBack:
    def __init__(self):
        self.x = 0;
        self.y = 0;
        
    #iv XOR key, result XOR'd with plaintext,
    def EncryptOFB(self, iv, msg_list, chunk_size):
        self.iv = iv
        self.chunk_size = chunk_size
        self.msg_list = msg_list
        
        str = StringBinaryToDecimal()
        iv_dec = str.strbin2dec(iv)
        msg_bin = ''
        
        block_encryption = 0
        count = 0
        while (count < len(msg_list)):
            msg_list[count] = str.strbin2dec(msg_list[count])
            if (count == 0):
                block_encryption = iv_dec ^ KEY     #change encryption algorithm later
                msg_list[count] ^= block_encryption
            else:
                block_encryption ^= KEY
                msg_list[count] ^= block_encryption
            msg_list[count] = bin(msg_list[count])[2:].zfill(chunk_size)
            msg_bin += msg_list[count]
            count += 1
        
        return msg_bin

    def DecryptOFB(self, iv, msg_bin, chunk_size):
        self.iv = iv
        self.chunk_size = chunk_size
        self.msg_bin = msg_bin
        
        str = StringBinaryToDecimal()
        iv_dec = str.strbin2dec(iv)
        
        msg_list = [str.strbin2dec(msg_bin[x:x+chunk_size]) for x in xrange(0,len(msg_bin),chunk_size)]
        msg_block = ''
        
        block_encryption = 0
        count = 0
        while (count < len(msg_list)):
            if (count == 0):
                block_encryption = iv_dec ^ KEY     #change encryption algorithm later
                msg_list[count] ^= block_encryption
            else:
                block_encryption ^= KEY
                msg_list[count] ^= block_encryption
            msg_list[count] = bin(msg_list[count])[2:].zfill(chunk_size)
            msg_block += msg_list[count]
            count += 1
        
        return msg_block

        