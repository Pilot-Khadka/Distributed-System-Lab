import socket
s = socket.socket()

port = 8080
host = '127.0.0.1'

# connect to server
s.connect((host, port))

message = 'Hello, server!'
s.send(message.encode('utf-8'))

# Receive the response from the server
response = s.recv(1024).decode('utf-8')
print('Response:', response)
s.close()
