package set1;
import Libraries.CryptoConversions;

import java.util.;


public class Challenge3{
    
    public String SingleByteXOR(String hexInput){
        
       int[] output = new int[hexInput.length()2]; 
       int i = 0;
       int j = 0;
       int resultXOR = 0;
       
       create character score look up table (httpwww.data-compression.comenglish.html)
       create a hash table 
       nevermind, use hash map as hashtables aren't used anymore
       HashMap Character, Double engCharFreq = new HashMapCharacter, Double();
       insert characters of the alphabet
       engCharFreq.put('A', 0.0651738);
       engCharFreq.put('B', 0.0124248);
       engCharFreq.put('C', 0.0217339);
       engCharFreq.put('D', 0.0349835);
       engCharFreq.put('E', 0.1041442);
       engCharFreq.put('F', 0.0197881);
       engCharFreq.put('G', 0.0158610);
       engCharFreq.put('H', 0.0492888);
       engCharFreq.put('I', 0.0558094);
       engCharFreq.put('J', 0.0009033);
       engCharFreq.put('K', 0.0050529);
       engCharFreq.put('L', 0.0331490);
       engCharFreq.put('M', 0.0202124);
       engCharFreq.put('N', 0.0564513);
       engCharFreq.put('O', 0.0596302);
       engCharFreq.put('P', 0.0137645);
       engCharFreq.put('Q', 0.0008606);
       engCharFreq.put('R', 0.0497563);
       engCharFreq.put('S', 0.0515760);
       engCharFreq.put('T', 0.0729357);
       engCharFreq.put('U', 0.0225134);
       engCharFreq.put('V', 0.0082903d);
       engCharFreq.put('W', 0.0171272);
       engCharFreq.put('X', 0.0013692);
       engCharFreq.put('Y', 0.0145984);
       engCharFreq.put('Z', 0.0007836);
       engCharFreq.put(' ', 0.1918182);
       
       set everything to upper case 
       hexInput.toUpperCase();
       
       output = HexToIntArray(hexInput);
       
       go through each value in the output array and XOR with the ascii char list 0-255
       for (i = 0; i  output.length; i++){
           for (j = 0; j = 255; j++){
               resultXOR = output[i] ^ j;
               System.out.print(i + t + j + t + output[i] +  XOR 1 =  + resultXOR + n);
           }
           
       }

        
        return hello;
    }
    
    private int[] HexToIntArray(String hexInput){
        
        CryptoConversions crypto = new CryptoConversions();
        
        int i = 0;
        int hexInt = 0;
        byte[] array = new byte[hexInput.length()];
        StringBuilder sbBinMsg = new StringBuilder();
        int[] intOutputArray = new int[hexInput.length()2];
        String strBinMsg = ;
        String temp = ;
        for (i = 0; i  hexInput.length(); i = i+2){
            
            hexInt = crypto.HexToDec(hexInput.substring(i, i+1));
            array[i] = crypto.DecToByte(hexInt); 
            hexInt = crypto.HexToDec(hexInput.substring(i+1, i+2));
            array[i+1] = crypto.DecToByte(hexInt); 
            sbBinMsg.append(crypto.DecToBin((int)array[i], 4));
            sbBinMsg.append(crypto.DecToBin((int)array[i+1], 4));
            System.out.println(array[i] + t + array[i+1] + t + sbBinMsg + n);
        }
        
        convert string builder to string
        strBinMsg = sbBinMsg.toString();
        
        for (i = 0; i  strBinMsg.length()8; i++){
            temp = sbBinMsg.substring(i8, i8+8);
            intOutputArray[i] = Integer.parseInt(temp, 2);
            
            System.out.println(intOutputArray[i] + t + temp + t + intOutputArray[i] + n);
        }
        
        return intOutputArray;
    }
    
}