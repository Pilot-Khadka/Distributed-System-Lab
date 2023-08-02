package java__rmi;
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface MyRemoteInterface extends Remote 
{
    public String sayHello() throws RemoteException;
}

