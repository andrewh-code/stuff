import java.net.*;
import java.util.*;
import java.lang.Object; 
import java.io.*;

public class ServerMonitor
{
    
    public static String getServerName()
    {
        String hostname = "";
        InetAddress addr;
        
        try {
            addr = InetAddress.getLocalHost();
            hostname = addr.getHostName();
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }

        return hostname;
    }
    
    public static String getIPV4()
    {
        InetAddress ip;
        String ipString = "";
        
        try
        {
            ip = InetAddress.getLocalHost();
            ipString = ip.getHostAddress();
        } catch (UnknownHostException e)
        {
            e.printStackTrace();
        }
        
        return ipString;
    }
    
    public static String getIPV6()
    {
        InetAddress ip;
        String ipString = "";
        
        try
        {
            ip = Inet6Address.getLocalHost();
            ipString = ip.getHostAddress();
        } catch (UnknownHostException e)
        {
            e.printStackTrace();
        }
        
        return ipString;
    }
    
    
    //check to see if process is running on windows
    public static boolean isProcessRunning(String processName)
    {

        String line = "";
        boolean processRunning = false;
        
        try
        {
            Process p = Runtime.getRuntime().exec(System.getenv("windir") + "\\system32\\" + "tasklist.exe");
            //Process p = Runtime.getRuntime().exec(System.getenv("windir") + "\\system32\\" + "tasklist.exe"); //ps -ef for linux/unix
            BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
            
            while ((line = input.readLine()) != null)
            {
                System.out.println(line);
                if (line.indexOf(processName) != -1)
                {
                    processRunning = true;
                    //break;
                }
            }
        
            input.close();
        }
        catch (Exception err)
        {
            err.printStackTrace();
        }

        return processRunning;
    }
    
    public static String getFileSystemUsage()
    {
        String line = "";
        List<String> fsList = new ArrayList<String>();
        
        try
        {
            Process p = Runtime.getRuntime().exec("df -gt");
            BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
            
            while ((line = input.readLine()) != null)
            {
                //fsList.add(line);
            }
            
        } catch (Exception err)
        {
            err.printStackTrace();
        }

        return "true";

    }
    
    /*
    public static void main (String args[])
    {
    }
    */
}