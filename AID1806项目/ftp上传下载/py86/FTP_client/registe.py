# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registe.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("注册")
        Form.resize(475, 350)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.r_save = QtWidgets.QPushButton(Form)
        self.r_save.setGeometry(QtCore.QRect(60, 260, 161, 31))
        self.r_save.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Algerian\";")
        self.r_save.setObjectName("r_save")
        self.r_name = QtWidgets.QLineEdit(Form)
        self.r_name.setGeometry(QtCore.QRect(150, 100, 201, 31))
        self.r_name.setPlaceholderText("")
        self.r_name.setObjectName("r_name")
        self.r_passWord = QtWidgets.QLineEdit(Form)
        self.r_passWord.setGeometry(QtCore.QRect(150, 160, 201, 31))
        self.r_passWord.setEchoMode(QtWidgets.QLineEdit.Password)
        self.r_passWord.setPlaceholderText("")
        self.r_passWord.setObjectName("r_passWord")
        self.r_name.setClearButtonEnabled(True)
        self.r_passWord.setClearButtonEnabled(True)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 100, 61, 31))
        self.label.setStyleSheet("font: 14pt \"Algerian\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 170, 61, 21))
        self.label_2.setStyleSheet("font: 14pt \"Algerian\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(360, 160, 101, 31))
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.rB_pwd = QtWidgets.QRadioButton(Form)
        self.rB_pwd.setGeometry(QtCore.QRect(150, 210, 89, 16))
        self.rB_pwd.setObjectName("rB_pwd")
        self.r_exit = QtWidgets.QPushButton(Form)
        self.r_exit.setGeometry(QtCore.QRect(260, 260, 161, 31))
        self.r_exit.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Algerian\";")
        self.r_exit.setObjectName("r_exit")

        self.retranslateUi(Form)
        self.r_save.clicked.connect(Form.addUser)
        self.r_passWord.cursorPositionChanged['int','int'].connect(self.label_3.clear)
        self.rB_pwd.clicked.connect(self.yanma)
        self.r_exit.clicked.connect(self.register_exit)
        QtCore.QMetaObject.connectSlotsByName(Form)
    #关闭创新账号窗口
    def register_exit(self):
        self.close()

    def yanma(self):
        if self.rB_pwd.isChecked():
            self.r_passWord.setEchoMode(QLineEdit.Normal)
        else:
            self.r_passWord.setEchoMode(QLineEdit.Password)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "欢迎注册 ^0^"))
        self.r_save.setText(_translate("Form", "提交"))
        self.r_name.setPlaceholderText(_translate("Form", "请输入用户名"))
        self.r_passWord.setPlaceholderText(_translate("Form", "请输入密码  密码不少于6位"))
        self.label.setText(_translate("Form", "用户名"))
        self.label_2.setText(_translate("Form", "密   码"))
        self.rB_pwd.setText(_translate("Form", "显示密码"))
        self.r_exit.setText(_translate("Form", "退出"))

