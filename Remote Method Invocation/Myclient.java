package java__rmi;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Myclient {
    public static void main(String[] args) 
    {
        try 
        {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            MyRemoteInterface remoteObject = (MyRemoteInterface) registry.lookup("MyRemoteObject");
            String result = remoteObject.sayHello();
            System.out.println(result);
        } 
        catch (Exception e) 
        	{
            	System.out.println("Hello Server failed "+e);
        	}
    }
}
