package set1;
import java.util.*;
import java.io.*;

/*
 * Matasano Crypto Challenge
 * Set 1 - Challenge 1
 * Description:
 *              The string:

                49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
                
                Should produce:
                SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
                
                So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

                Cryptopals Rule
                Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
 *
 * 
 * Author               Date                Version                 Description
 * =========            =========           =========               =========
 * Andrew Ho            Oct 29, 2014        v1.0                    Initial draft
 * 
 * 
 */

//
public class MatasanoLibraries
{
    
    public String HexToDecimal(String hexInput){

        //declare variables
        int i                           = 0;
        int intConvertedIntHexValue     = 0;
        String strIndividualHexValue    = "";
        StringBuilder sbResult          = new StringBuilder();
        StringBuilder sbBinary          = new StringBuilder();
        if (hexInput == null)   //empty string
        {
            System.out.println("An empty string has been passed, please input a valid string");
            return hexInput;
        }
        
        //convert everything to upper case
        hexInput = hexInput.toUpperCase();
        
        if (!isHex(hexInput)){
            System.exit(1);
        }
        
        for (i = 0; i <= hexInput.length()-2; i = i+2){
            strIndividualHexValue = hexInput.substring(i, i+2);
            intConvertedIntHexValue = Integer.parseInt(strIndividualHexValue, 16);
            
            sbResult.append(Integer.toString(intConvertedIntHexValue));
            sbBinary.append(Integer.toBinaryString(intConvertedIntHexValue));
            //System.out.format("strTemp is: %s, intTemp is: %d%n", strIndividualHexValue, intConvertedIntHexValue);
        }
        
        System.out.println(sbResult.toString());
        System.out.println(sbBinary.toString());
        
        return sbResult.toString();
    }
    
    
    public static int HexToDec(String hexInput){
        
        int intOutput;
        
        if (!isHex(hexInput)){
            System.exit(1);
        }
        
        intOutput = Integer.parseInt(hexInput);
        
        return intOutput;
    }
    
    //this is supposed to be a maximum of 127, 8 binary digits
    public static String DecToBin(int DecInput, int length){
        
        String strOutput = "";
        int pad = 0;
        
        strOutput = Integer.toBinaryString(DecInput);
        
        //add leading zeros to strOutput to match 8 bit binary
        pad = length - strOutput.length();
        if (pad > 0){
            
        }

        return strOutput;
    }
    
    
    public static boolean isHex(String hexInput){
        
        boolean result = true;
        String lookupTable = "0123456789ABCDEFG";
        int i = 0;
        int j = 0;
        char temp;

        //check to see if length of the hex string is an even number
        if (hexInput.length() % 2 != 0){
            System.out.println("please provide a proper hex value");
            result = false;
        }
        
        hexInput = hexInput.toUpperCase();
        //check to see that every character in the hex string is a hex value
        for (i = 0; i < hexInput.length(); i++){
            temp = hexInput.charAt(i);       
            
            if (lookupTable.toUpperCase().indexOf(temp) < 0)
            {
                System.out.println("A character in the input is not a HEX value, please provide a proper hex value");
                result = false;
            }
        }
        return result;
    }
}