#!/usr/bin/python

import sys
from StringBinaryToDecimal import StringBinaryToDecimal

global UPPER_BIT
global ASCII_BIN_SIZE
global KEY
UPPER_BIT = 10
ASCII_BIN_SIZE = 8
KEY = 5

class CipherBlockChaining():
    def __init__(self):
        self.x = 0
        self.y = 0

    def EncryptCBC(self, iv, msg_list, chunk_size):
        self.iv = iv
        self.msg_list = msg_list
        self.key = 0;
        
        #start the XOR-ing and encryption of the messages: m1 with iv, m2 with c1, m3 with c2
        str = StringBinaryToDecimal()
        iv_dec = str.strbin2dec(iv)
        msg_bin = ''
        #key = 5
        
        count = 0
        while (count < len(msg_list)):
            if (count == 0):
                #XOR the very first element in the block with the initialization vector
                msg_list[count] = str.strbin2dec(msg_list[count])
                msg_list[count] ^= iv_dec
                
                msg_list[count] = bin(msg_list[count])[2:].zfill(chunk_size)
                msg_list[count] = str.strbin2dec(msg_list[count])
                msg_list[count] ^= KEY  #change this algorithm 
            else:
                msg_list[count] = str.strbin2dec(msg_list[count])
                msg_list[count] ^= msg_list[count-1]
                
                msg_list[count] = bin(msg_list[count])[2:].zfill(chunk_size)
                msg_list[count] = str.strbin2dec(msg_list[count])
                msg_list[count] ^= KEY  #change this algorithm
            if (msg_list[count] > ((2**chunk_size)-1)):
                print "assert!!!!! You should not see this message. If you do....you messed up real bad"
            count += 1

        msg_list.append(str.strbin2dec(iv)) #append the iv to the very end of the message (only needed for client/server communication)

        #convert encrypted message back into binary
        for x_bin in msg_list:
            y_bin = bin(int(x_bin))[2:].zfill(chunk_size)
            msg_bin += y_bin        
        
        return msg_bin
        #convert to integer
        #XOR msg_chuck integer with integer of key
        #    m = int(strbin2dec(msg_chunk))

    def DecryptCBC(self, msg_bin, chunk_size):       #reverse of CipherBlockChaining
        #self.iv = iv
        self.msg_list = 0
        self.key = 0
        decrypted_msg = ''
        
        str = StringBinaryToDecimal()
        #b = [a[x:x+2] for x in xrange(0,len(a),2)]
        
        msg_list = [str.strbin2dec(msg_bin[x:x+chunk_size]) for x in xrange(0,len(msg_bin),chunk_size)]
        #grab last element of the CBC msg_list
        iv = msg_list[len(msg_list)-1]
        msg_list.pop(len(msg_list)-1)   #pop initialization vector out of the list
        
        count = len(msg_list) - 1
        while (count > 0):
            msg_list[count] ^= KEY
            msg_list[count] ^= msg_list[count-1]
            count -= 1
        msg_list[count] ^= KEY
        msg_list[count] ^= iv
        
        for msg_block in msg_list:
            y_bin = bin(int(msg_block))[2:].zfill(chunk_size)
            decrypted_msg += y_bin
        
        return decrypted_msg