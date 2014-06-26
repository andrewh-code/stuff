import java.net.*;
import java.util.*;
import java.lang.Object; 
import java.io.*;
import java.math.*;

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
            Process p = Runtime.getRuntime().exec(processName);
            //Process p = Runtime.getRuntime().exec(System.getenv("windir") + "\\system32\\" + "tasklist.exe"); //ps -ef for linux/unix
            BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
            
            while ((line = input.readLine()) != null)
            {
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
    
    public static List<String> getFileSystemUsage()
    {
        String line = "";
        List<String> fsList = new ArrayList<String>();
        
        try
        {
            Process p = Runtime.getRuntime().exec("df -gt");
            //File[] roots = File.listRoots();
            
            BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
            
            while ((line = input.readLine()) != null)
            {
                fsList.add(line);
            }
            
        } catch (Exception err)
        {
            err.printStackTrace();
        }
        
        return fsList;

    }
    
    public static float getFreeRAM()
    {
        float availableRAM = 0;
        availableRAM = Runtime.getRuntime().freeMemory();
        
        //convert result from Bytes to Gigabytes. Truncate to 2 decimal places.
        availableRAM = (float)(Math.floor(availableRAM / (1024*1024*1024) * 100) / 100);
        
        return availableRAM;
    }
    
    public static float getMaxRAM()
    {
        float maxRAM = 0;
        maxRAM = Runtime.getRuntime().maxMemory();
        
        //convert result from Bytes to Gigabytes
        
        maxRAM = (float)(Math.floor(maxRAM / (1024*1024*1024) * 100) / 100);
        
        return maxRAM;
    }
    
    /*
    public static void main (String args[])
    {
    }
    */
}