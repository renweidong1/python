from registe import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

class Registe(QtWidgets.QWidget,Ui_Form):
    def __init__(self,tftp):
        super(Registe,self).__init__()
        self.setupUi(self)
        self.tftp = tftp


    def addUser(self):
        rname = self.r_name.text()
        rpwd = self.r_passWord.text()
        if not rname:
            QMessageBox.warning(self, "Warning", "用户名不能为空")
        elif not rpwd:
            QMessageBox.warning(self, "Warning", "密码不能为空")
        elif len(rpwd) < 6 :
            QMessageBox.warning(self, "Warning", "密码不能少于6位")
        else:
            result = self.tftp.do_registe(rname,rpwd)
            if result == 'OK':
                QMessageBox.warning(self, "Warning", "注册成功")
            elif result == 'EXISTS':
                QMessageBox.warning(self, "Warning", "用户名已存在，请重新输入！")
            else:
                QMessageBox.warning(self, "Warning", "注册失败！")