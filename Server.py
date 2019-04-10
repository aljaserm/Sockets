import socket

host = 'localhost'
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print("Server Listening for requests on port ", port)
con, address = s.accept()
print("Connection has been established from ", str(address))
con.send("HI my name is MJ Server. Hoe can I help you?".encode())
con.close()
