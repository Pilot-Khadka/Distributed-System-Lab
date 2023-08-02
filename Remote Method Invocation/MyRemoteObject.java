package java__rmi;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class MyRemoteObject extends UnicastRemoteObject implements MyRemoteInterface 
{
	private static final long serialVersionUID = 1L;
	private String message;
	public MyRemoteObject(String msg) throws RemoteException {
        message = msg;
    }

    public String sayHello() throws RemoteException {
        return message;
    }
}
