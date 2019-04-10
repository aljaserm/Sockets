import socket
from threading import Thread


def AcceptClientConnection():
    while True:
        clientConnection, clientAddress = s.accept()
        print(clientAddress, " has connected")
        clientConnection.send("Welecome to the Room \n please enter your name".encode("utf8"))
        addresses[clientConnection] = clientAddress
        Thread(target=HandleClients, args=(clientConnection, clientAddress)).start()


def broadcast(msg, prefix=""):
    for c in clients:
        c.send(bytes(prefix, "utf8") + msg)


def HandleClients(clientConnection, clientAddress):
    name = clientConnection.recv(1024).decode("utf8")
    welcome = "Welcome " + name + ", \nyou type #quit if you want to leave the room"
    clientConnection.send(bytes(welcome, "utf8"))
    msg = name + " has join the room"
    broadcast(bytes(msg, "utf"))
    clients[clientConnection] = name
    while True:
        msg = clientConnection.recv(1024)
        if msg != bytes("#quit", "utf8"):
            broadcast(msg, name + ": ")
        else:
            clientConnection.send(bytes("#quit", "utf8"))
            clientConnection.close()
            del clients[clientConnection]
            broadcast(bytes(name + " has left the room"))


clients = {}
addresses = {}

Host = '127.0.0.1'
Port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, Port))

if __name__ == "__main__":
    s.listen(5)
    print("The server has been started \nServer is listening to clients requests")
    t1 = Thread(target=AcceptClientConnection)
    t1.start()
    t1.join()
