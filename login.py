from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from main import *
from regist import *
from PyQt5.QtWidgets import *
import json

class Ui_LoginWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_LoginWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
# 登陆页面
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setWindowIcon(QIcon('logo.png'))

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.label_0 = QtWidgets.QLabel(self.centralWidget)
        self.label_0.setGeometry(QtCore.QRect(140, 40, 120, 15))
        self.label_0.setTextFormat(QtCore.Qt.AutoText)
        self.label_0.setObjectName("label_0")

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(75, 110, 60, 15))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(75, 160, 60, 15))
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 100, 150, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 150, 150, 30))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 220, 80, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 220, 80, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.pushButton.clicked.connect(self.verifyLogin)
        self.pushButton_2.clicked.connect(self.regist)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登入页面"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入帐号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.label_0.setText(_translate("MainWindow", "宠物监控系统2.0"))
        self.label.setText(_translate("MainWindow", "登录名："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "注册"))


    def verifyLogin(self):
        login_user = self.lineEdit.text()
        login_password = self.lineEdit_2.text()
        f = open("users.txt","r")
        users = json.load(f)

        if login_user not in users.keys():
            QMessageBox.warning(self,
                                "警告",
                                "不存在该用户！",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()

        elif login_user in users.keys() and login_password != users[login_user]:
            QMessageBox.warning(self,
                                "警告",
                                "密码错误！",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()

        elif login_user in users.keys() and login_password == users[login_user]:
            ui_hello.show()
            MainWindow.close()

    def regist(self):
        ui_regis.show()
        MainWindow.close()

import sys

if __name__ == "__main__":
    name = '可以了。'
    bool = 1
    type = '狗'
    import sys
    exec_count = 0
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui_hello = Ui_MainWindow()
    ui_regis = Ui_RegistWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
