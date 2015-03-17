package set1;
import java.util.*;
import Libraries.CryptoConversions;

public class Challenge1{
	
	/*
	 * Take string hex input
	 * loop through hex string, convert hex input into raw bytes (byte array), take two at a time
	 * separate the two characters into separate 4 bytes, convert them into binary string
	 * combine the two separate binary strings together to form an 8-bit value
	 * concatenate the 8 string binary value to an output string until you reach the end of the hex input string
	 * add 0's to the binary string output until (binary string length % 24 == 0), add two separate flags to indicate
	 * how many 0's were padded (either 8 for one byte, or 16 for 2 bytes) which is necessary to convert the padded bytes into '='
	 * loop through the binary string every 6 bits which is the length ofr base64 notation.
	 * take the new 6-bit value and convert into decimal
	 * keep looping until finished, put the values into a byte array
	 * use a look up table to translate the converted 6-bit values (convert to decimal first) to the associated base 64
	 * char representation 
	 */
	
	public String HexToBase64(String hexInput){

		//instantiate new objects
		CryptoConversions crypto = new CryptoConversions();
		StringBuilder strBinMsg  = new StringBuilder();
		StringBuilder sbFinalMsg = new StringBuilder();
		
		//declare variables and constants
		int i 					= 0;
		int hexInputLength 		= hexInput.length();
		byte[] temp 			= new byte[hexInputLength];
		char[] charTable 		= crypto.Base64Table();
		int hexInt 				= 0;
		int trailingZeroCount 	= 0;
		String finalMessage 	= "";
		
		//convert everything to uppercase
		hexInput = hexInput.toUpperCase();
		
		//assume the input is an even length number
		if (!crypto.isHexadecimal(hexInput)){
            System.out.println(hexInput + " is not a HEX value.\n");
            System.exit(1);
        }
		
		//convert everything in the hex string into a byte array
		for (i = 0; i < hexInput.length(); i=i+2){
			
			hexInt = crypto.HexToDec(hexInput.substring(i, i+1));
			temp[i] = crypto.DecToByte(hexInt);
			hexInt = crypto.HexToDec(hexInput.substring(i+1, i+2));
			temp[i+1] = crypto.DecToByte(hexInt);
			strBinMsg.append(crypto.DecToBin((int)temp[i], 4));
			strBinMsg.append(crypto.DecToBin((int)temp[i+1], 4));

			//System.out.println(hexInt + "\t" + temp[i] + "\t" + strBinMsg.toString() + "\n");
		}
		
		//add the 0 padding to fill in the last bytes
		while (strBinMsg.length() % 24 != 0){
			strBinMsg.append("0");
			trailingZeroCount++;
		}
		//System.out.println("trailing zero count: " + trailingZeroCount + "\n");
		
		//set new byte array (for 6 bits) with new length of the sring binary message
		byte[] array6Bit = new byte[strBinMsg.length()/6];
		
		//convert binary message string into its 6 bits
		for (i = 0; i < strBinMsg.length(); i=i+6){
			
			if ((i == strBinMsg.length() - 12) && (trailingZeroCount == 16)){
				sbFinalMsg.append("==");
	    		break;
	    	}
	    	else if ((i == strBinMsg.length() - 6) && (trailingZeroCount == 8)){
	    		sbFinalMsg.append("=");
	    		break;
	    	}
	    	else{
	    		array6Bit[i/6] = Byte.valueOf(strBinMsg.substring(i, i+6), 2);
				sbFinalMsg.append(charTable[array6Bit[i/6]]);
	    	}
			//System.out.println(strBinMsg.substring(i, i+6) + "\t" + array6Bit[i/6] + "\t" + charTable[array6Bit[i/6]] + "\t" + i + "\n");
		}
		//convert string builder to string
		finalMessage = sbFinalMsg.toString();
		
		return finalMessage;
	}
}