package Libraries;
import java.util.*;


public class CryptoConversions{
    
    
    //no array inputs, all have to be either string or int/dec, do the conversion to byte if necessary inside
    
    //conversions
    
    //convert decimal to bytes
    public byte DecToByte(int decInput){
        
        byte byteOutput;
        
        if (decInput > 127){
            System.out.println("integer input is greater than 127. Unable to convert to byte value.\n");
            System.exit(1);
        }
        if (decInput < -128){
            System.out.println("Integer input is less than -128. Unable to convert to byte value.\n");
            System.exit(1);
        }
        
        byteOutput = (byte)decInput;
        
        //setting up for byte
        //byte b = (byte)129;
        //int i = b & 0xff;   //i = 129
        
        return byteOutput;
    }
    
    //convert hexadecimal to decimal
    public int HexToDec(String hexInput){
        
        int intOutput;
        
        if (!isHexadecimal(hexInput)){
            System.out.println(hexInput + "is not a HEX value.\n");
            System.exit(1);
        }
        
        intOutput = Integer.parseInt(hexInput, 16);
        
        return intOutput;
    }
    
    //convert decimal to binary
    public String DecToBin(int decInput, int length){
        
        String strOutput = "";
        
        strOutput = Integer.toBinaryString(decInput);
        
        //add leading zeros to strOutput to match 8 bit binary
        while (strOutput.length() < length){
            strOutput = "0" + strOutput;
        }

        return strOutput;
    }

    //convert binary to decimal
    public int BinToDec(String binInput){
        
        int intOutput = 0;
        int intTemp = 0;
        char chrTemp = ' ';
        
        if (!(isBinary(binInput))){
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
    
    //convert decimal to hex
    public String DecToHex(int input){
        
        //String HEX_TABLE = "0123456789ABCDEF";
        //int dividend = input;
        //int remainder = 1;
        //int result = 0;
        //String output = "";

        /*
        //TO DO: figure out how to do this
        while (remainder >= 16){
            remainder = dividend % 16;
            result = (int)(dividend / 16);
            dividend = result * 16;
            output = HEX_TABLE.charAt(remainder) + output;
        */
        String strOutput = "";
        strOutput = Integer.toHexString(input);
        return strOutput;
        
        }

    //is hexadecimal
    public static boolean isHexadecimal(String hexInput){
        
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
    
    //is binary
    public static boolean isBinary(String binInput){
        
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
    
    
    
}