import java.io.*;
 

public class GenerateEmails
{
    public static void generate(String fileName)
    {
        //declare variables
        File checkFile = new File(fileName);
        
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
            

            output.write("hello world");
            output.flush();
            output.close();
                
                System.out.println("successfully wrote to file " + fileName);
                
        }
        catch (Exception e)
        {
            System.err.println("Error: " + e.getMessage());
        }
        
    }
    
    public static void main (String[] args)
    {
        //declare and initialize variables/constants
        int argumentLength          = 1;
        String outputFileName       = "";
        String illegalChars         = "[^~#@*+%{}<>\\[\\]|\"\\_^]";
        
        //parse the command line arguments
        if (args.length < 1)
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
        System.out.println("filename is: " + outputFileName);
        
        //execute function
        generate(outputFileName);
        
        System.exit(0);
        
    }
}