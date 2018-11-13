# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(745, 491)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 200, 31))
        self.label.setStyleSheet("font: 14pt \"Algerian\";")
        self.label.setObjectName("label")
        self.put_file = QtWidgets.QPushButton(Form)
        self.put_file.setGeometry(QtCore.QRect(530, 20, 161, 41))
        self.put_file.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"font: 18pt \"Algerian\";\n"
"color: rgb(255, 255, 255);")
        self.put_file.setObjectName("put_file")
        self.load_file = QtWidgets.QPushButton(Form)
        self.load_file.setGeometry(QtCore.QRect(530, 120, 161, 41))
        self.load_file.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"font: 18pt \"Algerian\";\n"
"color: rgb(255, 255, 255);")
        self.load_file.setObjectName("load_file")
        self.myList = QtWidgets.QListWidget(Form)
        self.myList.setGeometry(QtCore.QRect(10, 50, 481, 411))
        self.myList.setObjectName("myList")
        self.update_file = QtWidgets.QPushButton(Form)
        self.update_file.setGeometry(QtCore.QRect(530, 320, 161, 41))
        self.update_file.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"font: 18pt \"Algerian\";\n"
"color: rgb(255, 255, 255);")
        self.update_file.setObjectName("update_file")
        self.exit_file = QtWidgets.QPushButton(Form)
        self.exit_file.setGeometry(QtCore.QRect(640, 430, 81, 31))
        self.exit_file.setStyleSheet("font: 18pt \"Algerian\";\n"
"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.exit_file.setObjectName("exit_file")
        # self.progressBar = QtWidgets.QProgressBar(Form)
        # self.progressBar.setGeometry(QtCore.QRect(20, 440, 411, 31))
        # self.progressBar.setProperty("value", 24)
        # self.progressBar.setObjectName("progressBar")
        self.label_fileInfo = QtWidgets.QLabel(Form)
        self.label_fileInfo.setGeometry(QtCore.QRect(440, 440, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_fileInfo.setFont(font)
        self.label_fileInfo.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_fileInfo.setText("")
        self.label_fileInfo.setObjectName("label_fileInfo")
        self.delete_file = QtWidgets.QPushButton(Form)
        self.delete_file.setGeometry(QtCore.QRect(530, 220, 161, 41))
        self.delete_file.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"font: 18pt \"Algerian\";\n"
"color: rgb(255, 255, 255);")
        self.delete_file.setObjectName("delete_file")

        self.retranslateUi(Form)
        self.put_file.clicked.connect(Form.put)
        self.load_file.clicked.connect(Form.download)
        self.delete_file.clicked.connect(Form.delete)
        self.update_file.clicked.connect(Form.refresh)
        self.exit_file.clicked.connect(Form.exit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "py86 制作^_^"))
        self.label.setText(_translate("Form", ""))
        self.put_file.setText(_translate("Form", "上传"))
        self.load_file.setText(_translate("Form", "下载"))
        self.update_file.setText(_translate("Form", "刷新"))
        self.exit_file.setText(_translate("Form", "退出"))
        self.delete_file.setText(_translate("Form", "删除"))

