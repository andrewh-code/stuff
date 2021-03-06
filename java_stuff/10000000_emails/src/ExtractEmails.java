import java.io.*;
import java.lang.*;
import java.sql.*;
import java.text.*;
import java.util.*;


public class ExtractEmails
{
    
    /*
     * connect to database
     * execute SQL statement to retrieve domain IDs
          Could use database and SQL to do the heavy processing but that's easy
          SELECT date(now()),  substr(addr,locate('@',addr)+1) as maildomain, count (*) as mailcount FROM mailing GROUP BY maildomain ORDER BY mailcount DESC
          use simple SQL statement (do not truncate)
        
        restriction: simple SQL statement being used
          select * from mailing
        retrieve domain IDs and put them into list (or file)
        go through list and strip the local part of email out, save the domain (base on @)
        assume that the e-mails have already went through a validation/verification process before being put into the table
         
     */
    
    //initialize variables/constants
    
    //database objects/variables
    Connection con          = null;
    Statement qry           = null;
    Statement insert        = null;
    ResultSet rs            = null;
    String database         = "test_database";
    String username         = "andrew";
    String password         = "password";
    final String table1     = "mailing";
    final String table1C1   = "ADDR";
    final String table2     = "addresscount";
    //final String fileName   = ""      //figure out if need to insert by file or by sQL statement
    String SQLRetrive       = "SELECT * FROM " + table1;
    //String SQLLoad          = "LOAD DATA INFILE " + fileName + " INTO TABLE " + table2;       //figure out if need to insert by file or SQL statement
    
    //data variables
    List <String> emailList         = new ArrayList<String>();
    SimpleDateFormat dateFormat     = new SimpleDateFormat("MM-dd-YYYY");
    Calendar calDate                = Calendar.getInstance();
    String date                     = dateFormat.format(calDate);
    
    
    //Connect to database
    
    String strRS = null;
    Hashtable <String, Integer> domainCount = new Hashtable<String, Integer>();
    int i = 0;
    int dupEmailCount = 0;
    
    //execute SQL statement, SELECT * FROM mailing
    //rs = ...
    while (rs.next())
    {
        strRS = rs.getString(table1C1);
        strRS = strRS.substring(strRS.lastIndexOf("@")+1);
        emailList.add(strRS);
    }
    //sort list in alphabetical order (duplicates included)
    Collections.sort(emailList);
    
    for (i=0; i < emailList.length(); i++)
    {
        //create out of bounds exception emailList.get(-1)
        if (emailList.get(i) == emailList.get(i-1))
        {
            dupEmailCount++;
        }
        else
        {
            //insert domain email, dupEmailCount into hashtable
            domainCount.put(emailList.get(i), dupEmailCount);
            dupEmailCount = 0;
        }
    }
        
    //count the duplicates
    //use TreeSet as a solution?
    
    
    
}
}