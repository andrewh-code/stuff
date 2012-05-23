#!/usr/bin/python

"""
Author: Andrew Ho
Project: Block Cipher Library
Ciphers: ECB, CBC, CFB, OFB
May 1, 2012
"""

import sys
from initializationVector import initializationVector
from CipherBlockChaining import CipherBlockChaining
from ElectronicCodeBook import ElectronicCodeBook
from OutputFeedBack import OutputFeedBack
from CounterMode import CounterMode
from CipherFeedback import CipherFeedback
from ConvertMsg import ConvertMsg
 
#	1. <user input> message 
#	2. <user input> choose cipher mode
#	3. <user input> choose chunk mode (depends on cipher chosen)
#

def main():

    iv = initializationVector()
    ecb = ElectronicCodeBook()
    cbc = CipherBlockChaining()
    cfb = CipherFeedback()
    ofb = OutputFeedBack()
    ctr = CounterMode()
    msg = ConvertMsg()
    
    """
    #variables
    plaintext_msg = ''  #user input message
    bin_msg = ''        #converted plaintext_msg to binary
    cipher_msg = ''     #cipher text output
    chunk_size = ''     #chunk size used in ECB, CBC
    iv = ''             #initialization vector
    """
    
    #plaintext_msg = raw_input("please input the message you want to encrypt:")
    plaintext_msg = "hello"
    
    print ("Choose cipher mode:")
    print ("1. Electronic Code Book (ECB)")
    print ("2. Cipher-Block Chaining (CBC)")
    print ("3. k-bit Cipher Feedback Mode")
    print ("4. k-bit Output Feedback Mode")
    print ("5. Counter Mode")
    
    cipher_mode = int(raw_input("Please enter the number next to the cipher mode:"))

    if (cipher_mode == 1):      #ECB chosen
        print("Electronic Code Book chosen")
        chunk_size = int(raw_input("choose the chunk size:"))      
        
        bin_msg = msg.Msg2Bin(plaintext_msg, chunk_size)
        print "\nplaintext message:", plaintext_msg, "in binary is:"
        print bin_msg, "\n"
        
        encrypt_bin_msg = ecb.EncryptECB(bin_msg)
        print "encrypted message in binary is:", encrypt_bin_msg
        
        decrypt_bin_msg = ecb.DecryptECB(encrypt_bin_msg)
        print "decrypted message in binary is:", decrypt_bin_msg
        
    elif (cipher_mode == 2):    #CBC chosen
        print("Cipher-Block Chaining chosen. Beginning cipher-mode encryption...")
        chunk_size = int(raw_input("choose the chunk/block size:"))
        
        iv = iv.InitializationVector(chunk_size)
        bin_msg = msg.Msg2Bin(plaintext_msg, chunk_size)
        print "\nplaintext message:", plaintext_msg, "in binary is:"
        print bin_msg, "\n"
        
        encrypt_bin_msg = cbc.EncryptCBC(iv, bin_msg, chunk_size)
        print "Encrypted message in binary is:", encrypt_bin_msg
        
        decrypt_bin_msg = cbc.DecryptCBC(encrypt_bin_msg, chunk_size)
        print "Decrypted message in binary is:", decrypt_bin_msg
        
        decrypt_msg = msg.Bin2Msg(decrypt_bin_msg, chunk_size)
        print "\nFinal decrypted message is:", decrypt_msg

    elif (cipher_mode == 3):    #CFM chosen     
        print("Cipher Feedback Mode chosen")        
        chunk_size = int(raw_input("choose the chunk/block size:"))
        
        iv = iv.InitializationVector(chunk_size)
        bin_msg = msg.Msg2Bin(plaintext_msg, chunk_size)
        print "\nplaintext message:", plaintext_msg, "in binary is:"
        print bin_msg, "\n"
        
        encrypt_bin_msg = cfb.EncryptCFB(iv, bin_msg, chunk_size)
        print "Encrypted message in binary is:", encrypt_bin_msg

        decrypt_bin_msg = cfb.DecryptCBC(encrypt_bin_msg, chunk_size)
        print "Decrypted message in binary is:", decrypt_bin_msg
        
        #decrypt_msg = msg.Bin2Msg(decrypt_bin_msg, chunk_size)
        #print "\nFinal decrypted message is:", decrypt_msg

    elif (cipher_mode == 4):    #OFM chosen
        print("Output Feedback Mode chosen")
        
        chunk_size = int(raw_input("choose the chunk/block size:"))
        iv = iv.InitializationVector(chunk_size)
        bin_msg = msg.Msg2Bin(plaintext_msg, chunk_size)
        print "\nplaintext message:", plaintext_msg, "in binary is:"
        print bin_msg, "\n"
        
        encrypt_bin_msg = ofb.EncryptOFB(iv, bin_msg, chunk_size)
        print "Encrypted message in binary is:", encrypt_bin_msg
        
        decrypt_bin_msg = ofb.DecryptOFB(iv, encrypt_bin_msg, chunk_size)
        print "Decrypted message in binary is:", decrypt_bin_msg
        
        decrypt_msg = msg.Bin2Msg(decrypt_bin_msg, chunk_size)
        print "\nFinal decrypted message is:", decrypt_msg
        
    elif (cipher_mode == 5):    #CTM chosen
        print("Counter Mode chosen")
        
        chunk_size = int(raw_input("choose the chunk/block size:"))
        iv = iv.InitializationVector(chunk_size)
        bin_msg = msg.Msg2Bin(plaintext_msg, chunk_size)
        print "\nplaintext message:", plaintext_msg, "in binary is:"
        print bin_msg, "\n"
        
        encrypt_bin_msg = ctr.EncryptCTR(iv, bin_msg, chunk_size)
        print "Encrypted message in binary is:", encrypt_bin_msg
        
        decrypt_bin_msg = ctr.DecryptCTR(iv, encrypt_bin_msg, chunk_size)
        print "Decrypted message in binary is:", decrypt_bin_msg
        
        decrypt_msg = msg.Bin2Msg(decrypt_bin_msg, chunk_size)
        print "\nFinal decrypted message is:", decrypt_msg
    else:
        print ("No cipher mode chosen, setting to default: Electronic Code Book")
    """
    chunk_size = 10  #delete when done testing
    """

if __name__ == "__main__":
    main()
