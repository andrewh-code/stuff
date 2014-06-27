import java.sql.*;


public class Main
{
    public static void main (String [] args)
    {
        
        //test Database class
        Connection db_connect = null;
        
        Database dbClass = new Database();
        
        String db = "test";
        String id = "Andrew";
        String pwd = "password";
        String email = "andre_who@tdbank.ca";
        
        email = email.substring(email.lastIndexOf("@")+1);
        
        System.out.println(email);
        
    }
}