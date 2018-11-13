# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 491)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(220, 360, 321, 41))
        self.loginButton.setStyleSheet("font: 14pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(71, 142, 213);")
        self.loginButton.setObjectName("loginButton")
        self.passWord = QtWidgets.QLineEdit(self.centralwidget)
        self.passWord.setGeometry(QtCore.QRect(240, 280, 291, 31))
        self.passWord.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passWord.setPlaceholderText("")
        self.passWord.setObjectName("passWord")
        self.userName = QtWidgets.QLineEdit(self.centralwidget)
        self.userName.setGeometry(QtCore.QRect(240, 220, 291, 31))
        self.userName.setPlaceholderText("")
        self.userName.setObjectName("userName")
        self.r_button = QtWidgets.QPushButton(self.centralwidget)
        self.r_button.setGeometry(QtCore.QRect(410, 320, 121, 21))
        self.r_button.setObjectName("r_button")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 23))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.loginButton.clicked.connect(MainWindow.login)
        self.r_button.clicked.connect(MainWindow.registe)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "py86云盘-登陆"))
        self.passWord.setPlaceholderText(_translate("MainWindow", " 请 输 入 密    码"))
        self.userName.setPlaceholderText(_translate("MainWindow", " 请 输 入 用 户 名"))
        self.loginButton.setText(_translate("MainWindow", "登陆"))
        self.r_button.setText(_translate("MainWindow", "没有账号？注册"))

