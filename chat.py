# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 653)
        MainWindow.setMinimumSize(QtCore.QSize(1044, 653))
        MainWindow.setMaximumSize(QtCore.QSize(1044, 653))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QPushButton \n"
"{\n"
"background:#7efff5;\n"
"color:black;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#f19066;\n"
"color:black;\n"
"border-radius:20px;\n"
"}\n"
"#MainWindow{\n"
"background: url(:/img/image.jpg);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_msg_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_msg_2.setGeometry(QtCore.QRect(220, 560, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(13)
        self.lineEdit_msg_2.setFont(font)
        self.lineEdit_msg_2.setAutoFillBackground(False)
        self.lineEdit_msg_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_msg_2.setText("")
        self.lineEdit_msg_2.setObjectName("lineEdit_msg_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(790, 560, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/inscription.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(200, 50, 20, 491))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(220, 540, 721, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.chatroom = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.chatroom.setEnabled(False)
        self.chatroom.setGeometry(QtCore.QRect(220, 50, 721, 491))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.chatroom.setFont(font)
        self.chatroom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(5, 0, 63);")
        self.chatroom.setUndoRedoEnabled(False)
        self.chatroom.setObjectName("chatroom")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 110, 111, 321))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChatRoom"))
        self.lineEdit_msg_2.setPlaceholderText(_translate("MainWindow", "Entrer votre message"))
        self.label.setText(_translate("MainWindow", "en ligne"))
        self.pushButton.setText(_translate("MainWindow", "Envoyer"))
        self.label_2.setText(_translate("MainWindow", "ChatRoom"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
