import socket

host = 'localhost'
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print("Server Listening for requests on port ", port)
con, address = s.accept()
print("Connection has been established from ", str(address))
try:
    filename=con.recv((1024))
    file=open(filename,'rb')
    readFile=file.read()
    con.send(readFile)
    file.close()
    con.close()
except:
    con.send("File Not Found".encode())
    con.close()