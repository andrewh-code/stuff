import java.util.*;


public class Main
{
    public static void main(String args[])
    {
        
        //ServerMonitor testObject = new ServerMonitor;
        String serverName = "";
        String ipV4 = "";
        String ipV6 = "";
        boolean isProcessRunning;
        String processName = "javaw.exe";
        List<String> fileSystem = new ArrayList<String>();; 
        
        
        //serverName = ServerMonitor.getServerName();
        //ipV4 = ServerMonitor.getIPV4();
        //ipV6 = ServerMonitor.getIPV6();
        //isProcessRunning = ServerMonitor.isProcessRunning(processName);
        //fileSystem = ServerMonitor.getFileSystemUsage();
        
        System.out.println(ServerMonitor.getFreeRAM());
        System.out.println(ServerMonitor.getMaxRAM());
        
        /* 
         * Check to see if specific process is running
         */
        //Check to see if TIBCO is running
        //Check to see if DB2 is running
        //check to see if TSM is running
        
        System.exit(0);
    }


}