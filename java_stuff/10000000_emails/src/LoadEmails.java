import java.io.*;
import java.sql.*;

public class LoadEmails
{
    public static void main(String [] args)
    {
      //test Database class
        Connection db_connect = null;
        
        Database dbClass = new Database();
        
        String db           = "test";
        String id           = "andrew";
        String pwd          = "password";
        String tableName    = "";
        String fileName     = "";
        //TO DO: figure out how to load file from a place that's not the default mysql data file directory
        String fileDir      = "C:\\ProgramData\\MySQL\\MySQL Server 5.6\\data\\";
        String inputFile    = "";
        
        //inputFile = fileDir + args[0];
        inputFile = fileDir + "day1.txt";
        
        //connect to the database
        dbClass.connectToDB(db, id, pwd);
        
        //load e-mails into database
        //String sqlFileLoad = "LOAD DATA INFILE '" + inputFile + "' INTO TABLE test.mailing LINES TERMINATED BY '\r\n'";
        String sqlFileLoad = "LOAD DATA INFILE 'day1.txt' INTO TABLE test.mailing LINES TERMINATED BY '\r\n'";
        System.out.println("Now loading e-mails into the database using file: " + fileName);
        
        dbClass.insertStatement(sqlFileLoad);
        
        System.out.println("Sucessfully inserted e-mails into table " + tableName + "\n");
        
        //dbClass.dbCommit();
        dbClass.dbDisconnect();
        
    }

}