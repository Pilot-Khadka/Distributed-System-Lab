package java__rmi;

import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;

public class Myserver {
    public static void main(String[] args) {
        try {
            MyRemoteInterface remoteObject = new MyRemoteObject("Hello World");
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("MyRemoteObject", remoteObject);
            System.out.println("Server is ready.");
        } 
        catch (Exception e) 
    	{
        	System.out.println("Hello Server failed "+e);
    	}
    }
}
