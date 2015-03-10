package set1;
import java.util.*;
import java.io.*;
import java.lang.Math.*;
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
    
    public String HexToBase64(String hexInput){

    	/* take hex string input
    	 * grab only two bits ofthe hex string at a time, take the two bits and transform them into decimal representation
    	 * convert the decimal representation into a binary string (8 bit)
    	 * keep looping and appending the binary string values together until the entire hex string input is complete
    	 * check to see if the binary string is divisible by 6 (for base 64 representation)
    	 * divide binary string into 6 groups, convert each 6bit string into base64-encoded value
    	 */
        //declare variables
        int i                           = 0;
        int intConvertedHexToDec     	= 0;
        String strConvertedDecToBin		= "";
        String strIndividualHexValue    = "";
        StringBuilder sbBinary          = new StringBuilder();
        StringBuilder sbOutput			= new StringBuilder();
        int byte64Count 				= 0;
        String strBinMsg 				= "";
        int index = 0;
        char[] table					= Base64Table();
        int zeroPadCount				= 0;
        
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
            
            intConvertedHexToDec = HexToDec(strIndividualHexValue);
            
            strConvertedDecToBin = DecToBin(intConvertedHexToDec, 8);

            //System.out.println(strIndividualHexValue + "\t" + intConvertedHexToDec + "\t" + strConvertedDecToBin + "\n");
            
            sbBinary.append(strConvertedDecToBin);
            byte64Count += 1;
        }
        
               
        //check to see if binary string is divisible by 6.
        //If not, then add 0's to the last byte so it's divisible by 3
        strBinMsg = sbBinary.toString();
        //System.out.println(strBinMsg.length() + "\n");
        //System.out.println("message in binary:\n" + sbBinary.toString() + "\n");
        
        while (strBinMsg.length() % 24 != 0){
        	//System.out.println("adding an extra 0 to the binary message\n");
        	strBinMsg = strBinMsg + "0";
        	zeroPadCount++;
        }
        System.out.println(zeroPadCount + "\n");
        
        //System.out.println("final bin msg with padding:\n" + strBinMsg + "\n");
        
        //convert binary string to 6-bit integer
        for (i = 0; i < strBinMsg.length(); i = i+6){
        	
        	if ((i == strBinMsg.length() - 12) && (zeroPadCount == 16)){
        		sbOutput.append("==");
        		break;
        	}
        	else if ((i == strBinMsg.length() - 6) && (zeroPadCount == 8)){
        		sbOutput.append("=");
        		break;
        	}
        	else{
        		index = Integer.parseInt(strBinMsg.substring(i, i+6), 2);
        	}
        	//System.out.println(strBinMsg.substring(i, i+6) + "\t" + index + "\n");
        	
        	sbOutput.append(table[index]);
        }
        System.out.println(sbOutput.toString());
        return sbOutput.toString();
    }
    
    //create base64 look up table
    private char[] Base64Table(){
    	
    	char[] table = new char[64];
    	int i = 0;
    	
    	for (char c = 'A'; c <= 'Z'; c++){
    		table[i] = c;
    		i++;
    	}
    	for (char c= 'a'; c <= 'z'; c++){
    		table[i] = c;
    		i++;
    	}
    	for (char c = '0'; c <= '9'; c++){
    		table[i] = c;
    		i++;
    	}
    	table[i] = '+';
    	i++;
    	table[i] = '/';

    	return table; 
    }
    
    //converting hexadecimal to decimal
    private int HexToDec(String hexInput){
        
        int intOutput;
        
        //if (!isHex(hexInput)){
        //    System.exit(1);
        //}
        
        intOutput = Integer.parseInt(hexInput, 16);
        
        return intOutput;
    }
    
    //converting decimal to binary
    private String DecToBin(int decInput, int length){
        
        String strOutput = "";
        
        strOutput = Integer.toBinaryString(decInput);
        
        //add leading zeros to strOutput to match 8 bit binary
        while (strOutput.length() < length){
        	strOutput = "0" + strOutput;
        }

        return strOutput;
    }
    
    //converting binary to decimal
    private int BinToDec(String binInput){
    	
    	int intOutput = 0;
    	int intTemp = 0;
    	char chrTemp = ' ';
    	
    	if (!(isBin(binInput))){
    		System.exit(1);
    	}
    	
    	int i = binInput.length()-1;
    	while (i >= 0){
    		chrTemp = binInput.charAt(i);
    		intTemp = Character.getNumericValue(chrTemp);
    		
    		intOutput += intTemp * Math.pow(2, binInput.length() - i - 1);
    		i--;
    	}
    	return intOutput;
    }
    
    private static boolean isBin(String binInput){
    	
    	boolean result = true;
    	int i = 0;
    	char temp = ' ';
    	
    	for (i = 0; i < binInput.length(); i++){
    		temp = binInput.charAt(i);
    		
    		if ((temp != '0') && (temp != '1')){
    			System.out.println("String input is not a binary value\n");
    			result = false;
    		}
    	}
    	
    	return result;
    }
    
    private static boolean isHex(String hexInput){
        
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