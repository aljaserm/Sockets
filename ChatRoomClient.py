from tkinter import *
import tkinter
import socket
from threading import Thread


def receiveMSG():
    while True:
        try:
            rMsg = s.recv(1024).decode("utf8")
            msgList.insert(tkinter.END, rMsg)
        except:
            print("Error on message")
            break


def onSend():
    msg = myMsg.get()
    myMsg.set("")
    s.send(bytes(msg, "utf8"))
    if msg == "#quit":
        s.close()
        window.quit()


def onQuit():
    myMsg.set("#quit")
    s.send()


window = Tk()
window.title("MJ Chat Room")
window.configure(bg="DeepSkyBlue2")
msgsFrame = Frame(window, height=100, width=100, bg="DeepPink3")
myMsg = StringVar()
myMsg.set("")
scrollBar = Scrollbar(msgsFrame)
msgList = Listbox(msgsFrame, height=15, width=100, bg="LightGoldenrod2", yscrollcommand=scrollBar.set)
scrollBar.pack(side=RIGHT, fill=Y)
msgList.pack(side=LEFT, fill=BOTH)
msgList.pack()
msgsFrame.pack()
lblSendMsg = Label(window, text="Enter Message", fg="white", font="Aerial", bg="RosyBrown4")
lblSendMsg.pack()
entMsg = Entry(window, textvariable=myMsg, fg="black", width=50, bg="PeachPuff2")
entMsg.pack()
btnSend = Button(window, text="Send", bg="chocolate3", font="Aerial", fg="white", command=onSend)
btnSend.pack()
btnQuit = Button(window, text="Quit", bg="tomato", font="Aerial", fg="white", command=onQuit)
btnQuit.pack()
window.protocol("WM_DELETE_WINDOW", onQuit)
Host = '127.0.0.1'
Port = 8080
s = socket.socket()
s.connect((Host, Port))
receiveThread = Thread(target=receiveMSG)
receiveThread.start()
mainloop()
