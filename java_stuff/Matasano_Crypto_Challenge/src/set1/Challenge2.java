package set1;
import java.util.*;


public class Challenge2
{
    
    /*
     * Write a function that takes two equal-length buffers and produces their XOR combination.

        If your function works properly, then when you feed it the string:
        
        1c0111001f010100061a024b53535009181c
        ... after hex decoding, and when XOR'd against:
        
        686974207468652062756c6c277320657965
        ... should produce:
        
        746865206b696420646f6e277420706c6179
     
     */
    
    //take two base 64 strings, XOR them against each other
    public String Base64FixedXOR(String input, String mask){
        
      //make sure that both strings have the same length
        if (input.length() != mask.length()){
            System.out.println("String lengths do not match. Both strings must have the same length.\n");
            System.exit(1);
        }
        
        //declare variables
        int i = 0;
        int size = input.length();

        int[] arrayInput = new int[size];
        int[] arrayMask = new int[size];
        int arrayResult;
        String output = "";
        arrayInput = HexToDec(input);
        arrayMask = HexToDec(mask);
        
        for (i = 0; i < size/2; i++){
            arrayResult = (arrayInput[i] ^ arrayMask[i]);
            output = DecToHex(arrayResult);
            
            System.out.println(arrayInput[i] + "\t" + arrayMask[i] + "\t" + arrayResult + "\t" + output + "\n");
            //output += table[arrayResult[i]];
        }
        
        
        return output;
    }
    

    public int[] HexToDec(String input){
        
        int[] array = new int[input.length()/2];
        int i = 0;
        int temp;
        
        for (i = 0; i < input.length() -2; i= i+2){
            temp = Integer.parseInt(input.substring(i, i+2), 16);
            array[i/2] = temp;
        }
        
        return array;
    }
    
    public String DecToHex(int input){
        
        String HEX_TABLE = "0123456789ABCDEF";
        int dividend = input;
        int remainder = 1;
        int result = 0;
        String output = "";
        
        //TO DO: figure out how to do this
        while (remainder >= 16){
            remainder = dividend % 16;
            result = (int)(dividend / 16);
            dividend = result * 16;
            output = HEX_TABLE.charAt(remainder) + output;
            
        }
        
        return output;
    }
}