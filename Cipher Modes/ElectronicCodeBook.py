#!/usr/bin/python

import sys
from ConvertMsg import ConvertMsg
from encrypt import Encrypt
from StringBinaryToDecimal import StringBinaryToDecimal

global KEY
KEY = 5

class ElectronicCodeBook():
    def __init__(self):
        self.x = 0
        self.y = 0

    def EncryptECB(self, bin_msg):
        self.bin_msg = bin_msg
        
        str = StringBinaryToDecimal()
        encrypt_bin = []
        
        for x in bin_msg:
            y = bin(str.strbin2dec(x) ^ KEY)[2:]   #change encryption algorithm
            encrypt_bin.append(y)

        return encrypt_bin
        
    def DecryptECB(self, encrypt_bin_msg):
        self.encrypt_bin_msg = encrypt_bin_msg
        
        str = StringBinaryToDecimal()
        decrypt_bin = []
        
        for x in encrypt_bin_msg:
            y = bin(str.strbin2dec(x) ^ KEY)[2:]   #change encryption algorithm
            decrypt_bin.append(y)
        
        return decrypt_bin
        
        