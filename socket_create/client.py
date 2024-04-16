import socket
c = socket.socket()
c.connect(('localhost',9999))
print(c.recv((),))
c.send('client')