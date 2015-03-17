package set1;
import Libraries.CryptoConversions;

/*
 * Write a function that takes two equal-length buffers and produces their XOR combination.

    If your function works properly, then when you feed it the string:
    
    1c0111001f010100061a024b53535009181c
    ... after hex decoding, and when XOR'd against:
    
    686974207468652062756c6c277320657965
    ... should produce:
    
    746865206b696420646f6e277420706c6179
 
 */

public class Challenge2
{
    //take two base 64 strings, XOR them against each other
    public String Base64FixedXOR(String input, String mask){
       
      //make sure that both strings have the same length
        if (input.length() != mask.length()){
            System.out.println("String lengths do not match. Both strings must have the same length.\n");
            System.exit(1);
        }
        
        //instantiate new objects
        CryptoConversions crypto   = new CryptoConversions();
        StringBuilder finalMessage = new StringBuilder();
        //declare variables
        int i 					= 0;
        int size 				= input.length();
        byte[] arrayInput 		= new byte[size];
        byte[] arrayMask 		= new byte[size];
        byte[] arrayXORResult 	= new byte[size];
        
        String output = "";

        //convert input to byte array
        for (i = 0; i < input.length(); i++){
        	arrayInput[i] = (byte)crypto.HexToDec(input.substring(i, i+1));
        	arrayMask[i] = (byte)crypto.HexToDec(mask.substring(i, i+1));
        	arrayXORResult[i] = (byte)(arrayInput[i] ^ arrayMask[i]);
        	
        	//convert byte/integer to hex value
        	finalMessage.append(Integer.toHexString(arrayXORResult[i]));
        	//System.out.println(arrayInput[i] + "\t" + arrayMask[i] + "\t" + arrayXORResult[i] + "\t" + finalMessage + "\n");
        }
        output = finalMessage.toString();
        
        return output;
    }
}