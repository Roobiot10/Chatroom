from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread  
import sys
import chat
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sqlite3

conn = sqlite3.connect("chat database.db",check_same_thread=False)
curs = conn.cursor()

class ChatServer(QMainWindow,chat.Ui_MainWindow):

    clientsNames = {}
    addresses = {}
    HOST = '127.0.0.1'
    PORT = 33000
    ADDR = (HOST, PORT)

    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.bind(ADDR)

    

    def __init__(self):
        super(ChatServer,self).__init__()
        self.setupUi(self) 
        self.SERVER.listen(5)
        print("Attente de la connexion...")

        ACCEPT_THREAD = Thread(target=self.accept_connections)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        self.SERVER.close()

    def accept_connections(self):
        while True:
            client, client_address = self.SERVER.accept()
            print("%s:%s est connecté." % client_address)
            client.send(
                bytes(" Salut ! Tapez maintenant votre nom et appuyez sur Envoyer ", "utf8"))
            self.addresses[client] = client_address
            HANDLE_THREAD = Thread(target=self.handle_client, args=(client,))
            HANDLE_THREAD.start()


    def handle_client(self,client):           
        name = client.recv(1024).decode("utf8")
        welcome = ' %s  Si jamais tu veux arrêter la discussion tapez {quit} pour arrêter.' % name
        client.send(bytes(welcome, "utf8"))
        msg = "%s à rejoint la discussion! " % name
        self.broadcast(bytes(msg, "utf8"))
        self.clientsNames[client] = name

        while True:
            msg = client.recv(1024)
            curs.execute("INSERT INTO chat(prenom,message)VALUES(?,?)",(name,msg,))
            conn.commit()
            if msg != bytes("{quit}", "utf8"):
                self.broadcast(msg, name+": ")
            else:
                client.send(bytes("{quit}", "utf8"))
                client.close()
                del self.clientsNames[client]

                self.broadcast(bytes("%s à quitte la discussion" % name, "utf8"))
                break


    def broadcast(self,msg, prefix=""):
        print("Tous les clients connectés : ",  self.clientsNames.values())
        for sock in self.clientsNames:
            print("Sock : ", sock)
            sock.send(bytes(prefix, "utf8") + msg)




app = QApplication(sys.argv)
winn = ChatServer()    
app.exec_()


