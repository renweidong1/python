from login import  Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
from socket import  *
from client import *
from PyQt5.QtWidgets import QMessageBox
from Register import *
from indexr import *
from time import sleep


class mywindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self,tftp):
        super(mywindow,self).__init__()
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("indexa.jpg")))
        self.setPalette(window_pale)
        self.setAutoFillBackground(True)
        self.setupUi(self)
        self.tftp = tftp

    #定义槽函数
    def login(self):
        name = self.userName.text()
        pwd = self.passWord.text()
        if not name:
            QMessageBox.warning(self, "Warning", "请输入用户名")
        elif not pwd:
            QMessageBox.warning(self, "Warning", "请输入密码")
        else:
            d,fileList = self.tftp.do_login(name,pwd)
            print('dddd',d)
            if d == 'OK':
                #登陆成功显示主界面
                print('show show show ')
                print(name,fileList)

                self.showIndex(name,fileList)
            elif d == 'NONE':
                QMessageBox.warning(self, "Warning", "用户名不存在！")
            elif d == 'ERROR':
                QMessageBox.warning(self, "Warning", "密码不正确！")

    def registe(self):
        self.registe = Registe(self.tftp)
        self.registe.show()

    def showIndex(self,name,fileList):
        self.i = Index(name,self.tftp,fileList)
        self.i.label.setText(name)
        print('showIndex')
        self.i.show()
        self.close()
