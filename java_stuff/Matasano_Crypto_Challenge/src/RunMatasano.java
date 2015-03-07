/*
 * The main run file to run specific sets of the Matasano crypto Challenge
 * 
 * Author:      Andrew Ho
 * Date:        October 20, 2014
 * 
 */

//import classes/libraries
import java.util.*;
import set1.MatasanoLibraries;


class RunMatasano
{
    static Scanner userInput = new Scanner(System.in);
    
    public static void main(String [] args)
    {
        
        System.out.println("Matasano Crypto Challenge");
        System.out.println("========================================\n");
        
        
        /*
        System.out.println( "1 - Convert hext to base 64\n" +
                            "2 - Fixed XOR\n" +
                            "3 - Single-byte XOR Cipher\n" + 
                            "4 - Detect single-character XOR\n" +
                            "5 - Implement repeating-key XOR\n" + 
                            "6 - Break repeating-key XOR\n" + 
                            "7 - AES in ECB mode\n" + 
                            "8 - Detect AES in ECB mode\n");
        System.out.println("Please enter the corresponding number of the challenge you want to be run:\n");
        
        int input = userInput.nextInt();
        
        switch (input){
        
        case 1: System.out.println("hello world");
                break;
        }
        */
        
        MatasanoLibraries func = new MatasanoLibraries();
        
        String temp = func.HexToDecimal("04");
        //int temp = func.HexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d");
        System.out.print(temp);
        
        System.exit(0);
    }
}
