import login
import inscription
import chat
import sys
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread 
from PyQt5.QtWidgets import QApplication,QMainWindow,QTabWidget,QTableWidgetItem
from PyQt5 import QtCore, QtGui
from PyQt5.uic import loadUi
import sqlite3


conn = sqlite3.connect("chat database.db",check_same_thread=False)
curs = conn.cursor()


class MainApp(object):
    
    def __init__(self):
        super(MainApp,self).__init__()
        self.event_handler()

    def event_handler(self):
        self.login = login()
        self.login.show() 
        self.login.commandLinkButton.clicked.connect(self.Show_Inscription)


    def Show_Inscription(self):
        self.add = Inscription()
        self.login.label_4.setText("")
        self.add.show()
        self.add.pushButton.clicked.connect(self.Add_Data)

    def Add_Data(self):
        self.add.label_12.setText("")
        self.add.label_11.setText("")
        nom = self.add.name_lineEdit.text()
        prenom = self.add.prenom_lineEdit.text()
        email = self.add.email_lineEdit.text()
        password = self.add.pass_lineEdit.text()
        age = self.add.dateEdit.date().toString("dd-MM-yyyy")

        if(self.add.radioButton.isChecked()):
            genre = "Homme"
        elif self.add.radioButton_2.isChecked():
            genre = "Femme"

        self.add.name_lineEdit.setText("")
        self.add.prenom_lineEdit.setText("")
        self.add.pass_lineEdit.setText("")
        self.add.email_lineEdit.setText("")

        r = curs.execute("SELECT * FROM login  WHERE prenom = ? AND email = ? AND password = ? ",(prenom,email,password))
        
        try:
            if(len(nom) and len(prenom) and len(email) and len(password)) > 0 and (self.add.radioButton.isChecked() or self.add.radioButton_2.isChecked()):
                curs.execute("INSERT INTO Inscription (nom,prenom,email,password,age,genre)VALUES(?,?,?,?,?,?)",(nom,prenom,email,password,age,genre))
                conn.commit()
                curs.execute("INSERT INTO login (prenom,email,password)VALUES(?,?,?)",(prenom,email,password))
                conn.commit()
                self.add.label_11.setText("Votre compte a été bien creé")
            else:
                self.add.label_12.setText("Veuillez remplir les données")
        except Exception as e :
            print(e)


class login(QMainWindow,login.Ui_MainWindow):

    HOST = '127.0.0.1'
    PORT = 33000
    ADDR = (HOST, PORT)

    def __init__(self):
        super(login,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login_check)

    def login_check(self):

        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        try : 
            result = curs.execute("SELECT * FROM login WHERE email = ? AND password = ? ",(email,password))
            
            
        except Exception as e :
            print(e)

        if (len(result.fetchall()) > 0 ):
            self.close()
            self.show_chat()
            
        else:
            self.label_4.setText("  Vous n'avez pas un compte")
        
    def show_chat(self):

        self.chat = ChatRoom()
        self.chat.show()
        self.chat.client_socket = socket(AF_INET, SOCK_STREAM)
        self.chat.client_socket.connect(self.ADDR)
        receive_thread =Thread(target=self.receive)
        receive_thread.start()
        self.chat.pushButton.clicked.connect(self.send)

    def receive(self):
        while  True:
            data = self.chat.client_socket.recv(1024).decode("utf8")
            if not data:
                break
            else:
                self.chat.chatroom.appendPlainText(str(data))
                query = "SELECT distinct prenom FROM chat "
                r = curs.execute(query)
                self.chat.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(r) :
                    self.chat.tableWidget.insertRow(row_number)
                    for colom_number, data in enumerate(row_data):
                        self.chat.tableWidget.setItem(row_number,colom_number, QTableWidgetItem(str(data)))
                    

    def send(self): 
        msg = self.chat.lineEdit_msg_2.text()
        self.chat.client_socket.send(bytes(msg, 'utf8'))
        self.chat.lineEdit_msg_2.setText("")

        if msg == "{quit}":
            self.chat.client_socket.close()
            self.chat.close()




class ChatRoom(QMainWindow,chat.Ui_MainWindow):
    def __init__(self):
        super(ChatRoom,self).__init__()
        self.setupUi(self) 



class Inscription(QMainWindow,inscription.Ui_MainWindow):
    def __init__(self):
        super(Inscription,self).__init__()
        self.setupUi(self)




app = QApplication(sys.argv)
win = MainApp()
app.exec_()

