from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import cv2
import sys
from PyQt5.QtWidgets import *
import os
import time
from login import *
import json
import win32api
from main import *
import subprocess

# 注册
class Ui_RegistWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_RegistWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.buttondeclick()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 54, 12))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(120, 50, 161, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 54, 12))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 100, 161, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 54, 12))
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(120, 150, 161, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "用户名："))
        self.label_2.setText(_translate("Dialog", "密码："))
        self.label_3.setText(_translate("Dialog", "确认密码："))
        self.pushButton.setText(_translate("Dialog", "注册"))

    def buttondeclick(self):
        self.pushButton.clicked.connect(self.regist)

    def regist(self):
        f = open("users.txt", "r")
        users = json.load(f)
        f.close()
        username = self.textEdit.toPlainText()
        password = self.textEdit_2.toPlainText()
        repeatPassword = self.textEdit_3.toPlainText()

        if password != repeatPassword:
            QMessageBox.warning(self, "警告", "两次密码不一致！", QMessageBox.Yes)
        elif username in users.keys():
            QMessageBox.warning(self, "警告", "该用户名已存在！", QMessageBox.Yes)
        else:
            f = open("users.txt", "w")
            users[username] = password
            json.dump(users, f)
            f.close()
            QMessageBox.warning(self, "你好", "注册成功！", QMessageBox.Yes)
            sys.exit(0)