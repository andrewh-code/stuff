
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
        
        serverName = ServerMonitor.getServerName();
        ipV4 = ServerMonitor.getIPV4();
        ipV6 = ServerMonitor.getIPV6();
        isProcessRunning = ServerMonitor.isProcessRunning(processName);
        
        //ServerMonitor.isProcessRunningWindows(processName);
        
        System.out.println(serverName);
        System.out.println(ipV4);
        System.out.println(ipV6);
        System.out.println(isProcessRunning);
        System.exit(0);
    }


}