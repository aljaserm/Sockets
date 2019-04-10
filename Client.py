import socket

sc=socket.socket()
host = 'localhost'
port = 8080

sc.connect((host,port))
msg=sc.recv(1024)

while msg:
    print("Message",msg.decode())
    msg=sc.recv(1024)

sc.close()