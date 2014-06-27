import java.io.*;
import java.util.*;

public class GenerateEmails
{
    public static void writeToFile(String fileName)
    {
        //declare variables
        final int MAX = 10000000;
    	File checkFile = new File(fileName);
        String email = "";
        
        
        //check to see if the file exists already
        if (checkFile.exists())
        {
            System.err.println(fileName + " Already exists, please use another file name");
            System.exit(1);
        }
        
        try 
        {
            //File checkFile = new File(fileName);
            FileWriter outputFile = new FileWriter(fileName);
            BufferedWriter output = new BufferedWriter(outputFile);
            
            for (int i = 0; i < MAX; i++)
            {
            	//email = funcGenerate() + "\n";
            	output.write(funcGenerate() + "\n");
            	//System.out.println(funcGenerate() + "\n");
            }
            
            output.flush();
            output.close();
                
            System.out.println("successfully wrote to file " + fileName);
                
        }
        catch (Exception e)
        {
            System.err.println("Error: " + e.getMessage());
        }
        
    }

    public static String funcGenerate()
    {
    	//declare variables
    	final int MAX_LENGTH		= 8;	//to keep things simple, set the local and domain length to be the same
    	
    	String localChars		= "ABCDEFGHIJKLMNOPQRSTUVWXYZ";	//don't worry about numbers, can be changed to include them 
    	String domainChars		= "abcdefghij";
    	String email			= "";
    	Random indexRndm		= new Random();
    	
    	char [] localCharArray 	= new char [MAX_LENGTH];
    	char [] domainCharArray = new char [MAX_LENGTH];
    	String localString;
    	String domainString;
    	
    	
    	//generate the local part of e-mail
    	for (int i = 0; i < MAX_LENGTH; i++)
    	{
    		localCharArray[i] = localChars.charAt(indexRndm.nextInt(localChars.length()));
    		domainCharArray[i] = domainChars.charAt(indexRndm.nextInt(domainChars.length()));
    	}
    	
    	localString = new String(localCharArray);
    	domainString = new String(domainCharArray);
    	
    	email = localString + "@" + domainString + ".com";
    	
    	return email;
    }
    
    public static void main (String[] args)
    {
        //declare and initialize variables/constants
        int argumentLength          = 1;
        String outputFileName       = "";
        String illegalChars         = "[^~#@*+%{}<>\\[\\]|\"\\_^]";
        
        //parse the command line arguments
        if (args.length < argumentLength)
        {
            System.err.println("Error: Please input a file name as the argument");
            System.exit(1);
        }
        if (args[0].matches(illegalChars))
        {
            System.err.println("filename " + outputFileName + "contains illegal characters.");
            System.exit(1);
        }
        
        outputFileName = args[0];
        System.out.println("filename is: " + outputFileName + "\n");
        
        
        /*
         * Start the timing
         */
        long startTime = System.currentTimeMillis();
        //execute function
        writeToFile(outputFileName);
        long endTime = System.currentTimeMillis();
        
        System.out.println("Time it took to write 10000000 emails to the file: " + (endTime - startTime));
        
        System.exit(0);
        
    }
}