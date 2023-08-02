import socket

s = socket.socket()
print('socket created')

port = 8080
host = '127.0.0.1'

s.bind((host,port))
print('socket binded to port :{}'.format(port))

s.listen(5) # 5 : max 5 connection for network to listen to
print('Socket is listening')

while True:
    c, address = s.accept()
    print('Connected to', address)
    message = ('Sucessfully connected')
    c.send(message.encode())
    
    # Receive data from the client
    data = c.recv(1024).decode('utf-8')
    print('Received:', data)
    
    c.close()