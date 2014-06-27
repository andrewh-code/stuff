import java.sql.*;


public class Database
{
    Connection connect          = null;
    Statement selectStatement   = null;
    Statement insertStatement   = null;
    ResultSet resultSet         = null;
    int rc                      = 0;
    
    String dbName;
    String userID;
    String password;
    Connection dbConnection;
    
    public Database()
    {
        this.dbName     = "";
        this.userID     = "";
        this.password   = "";
        this.dbConnection = null;
    }
    
    public void connectToDB(String db, String id, String pwd)
    {
        dbName                  = db;
        userID                  = id;
        password                = pwd;
        
        //set the default db to the localhost db
        dbName                  = "jdbc:mysql://localhost:3306/" + dbName;
        
        try
        {
            Class.forName("com.mysql.jdbc.Driver").newInstance();
        }
        catch (Exception err)
        {
            System.out.println("Unable to establish driver for database connection\n");
            System.exit(1);
        }
        
        try
        {
            dbConnection = DriverManager.getConnection(dbName, userID, password);
            System.out.println("Successfully connected to" + dbName + "\n");
        }
        catch (SQLException rc)
        {
            System.err.println(rc);
        }
    }
    
    public void selectStatement(String selectSQL)
    {
        Statement statement     = null;
        ResultSet results       = null;
        
        try
        {
            statement = dbConnection.prepareStatement(selectSQL);
            results = statement.executeQuery(selectSQL);
            
            while (results.next())
            {
                System.out.println(results);
            }
        }
        catch (SQLException rc)
        {
            System.err.println(rc);
        }

    }
    
    public void insertStatement(String insertSQL)
    {
        
    }
    
    public void dbCommit()
    {
        
    }
    
}