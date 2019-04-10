import socket

sc=socket.socket()
host = 'localhost'
port = 8080

sc.connect((host,port))
fileName='MJ.txt'
sc.send(fileName.encode())
readFile=sc.recv(1024)
print(readFile.decode())
sc.close()