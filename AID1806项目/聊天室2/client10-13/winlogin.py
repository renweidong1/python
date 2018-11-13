# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets
from socket import *
import sys
from time import ctime
from winmain import *
import random as R


class Log_1(object):

    def setupUi(self, Form1):
        Form1.setObjectName("Form1")
        Form1.resize(425, 325)
        Form1.setMinimumSize(QtCore.QSize(425, 325))
        Form1.setMaximumSize(QtCore.QSize(425, 325))
        Form1.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Form1.setStyleSheet("border-image: url(:/pic/images/guo7.jfif);")

        self.stackedWidget = QtWidgets.QStackedWidget(Form1)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 425, 325))
        self.stackedWidget.setObjectName("stackedWidget")

        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")
        self.label_back = QtWidgets.QLabel(self.page_0)
        self.label_back.setGeometry(QtCore.QRect(0, 0, 425, 150))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("images/8.jpg"))
        self.label_back.setObjectName("label_back")

        self.label_char = QtWidgets.QLabel(self.page_0)
        self.label_char.setGeometry(QtCore.QRect(0, 0, 40, 20))
        self.label_char.setText("iClimb")
        self.label_char.setObjectName("label_char")
        self.label_mini = QtWidgets.QLabel(self.page_0)
        self.label_mini.setGeometry(QtCore.QRect(375, 0, 25, 25))
        self.label_mini.setText(
            "<style> a {text-decoration: none} </style><A href='#'>－</a>")
        self.label_mini.linkActivated.connect(self.showMinimized)
        self.label_mini.setObjectName("label_mini")
        self.label_close = QtWidgets.QLabel(self.page_0)
        self.label_close.setGeometry(QtCore.QRect(400, 0, 25, 25))
        self.label_close.setText(
            "<style> a {text-decoration: none} </style><A href='#'>×</a>")
        self.label_close.linkActivated.connect(self.close)
        self.label_close.setObjectName("label_close")

        # self.label_logo = QtWidgets.QLabel(self.page_0)
        # self.label_logo.setGeometry(QtCore.QRect(185, 135, 55, 55))
        # self.label_logo.setText("")
        # self.label_back.setPixmap(QtGui.QPixmap("images/earth1.jpg"))
        # self.label_logo.setObjectName("label_logo")

        self.lineEdit_user = QtWidgets.QLineEdit(self.page_0)
        self.lineEdit_user.setGeometry(QtCore.QRect(100, 180, 225, 30))
        self.lineEdit_user.setPlaceholderText("请输入登录用户名")
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_passwd = QtWidgets.QLineEdit(self.page_0)
        self.lineEdit_passwd.setGeometry(QtCore.QRect(100, 220, 225, 30))
        self.lineEdit_passwd.setPlaceholderText("请输入密码")
        self.lineEdit_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        self.pushButton_login = QtWidgets.QPushButton(self.page_0)
        self.pushButton_login.setGeometry(QtCore.QRect(100, 260, 225, 30))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_login.clicked.connect(self.log_in,)
        self.label_to1 = QtWidgets.QLabel(self.page_0)
        self.label_to1.setGeometry(QtCore.QRect(360, 300, 60, 12))
        self.label_to1.setObjectName("label_to1")
        self.label_to1.setText(
            "<style> a {text-decoration: none} </style><A href='#'>注册账号﹥</a>")
        self.label_to1.linkActivated.connect(self.to_index1)
        self.stackedWidget.addWidget(self.page_0)

        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.register_user = QtWidgets.QLineEdit(self.page_1)
        self.register_user.setGeometry(QtCore.QRect(100, 90, 225, 30))
        self.register_user.setPlaceholderText("请输入注册用户名（将用于登录）")
        self.register_user.setObjectName("register_user")
        self.register_passwd = QtWidgets.QLineEdit(self.page_1)
        self.register_passwd.setGeometry(QtCore.QRect(100, 130, 225, 30))
        self.register_passwd.setPlaceholderText("请输入用户密码")
        self.register_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_passwd.setObjectName("register_passwd")
        self.register_passwd1 = QtWidgets.QLineEdit(self.page_1)
        self.register_passwd1.setGeometry(QtCore.QRect(100, 170, 225, 30))
        self.register_passwd1.setPlaceholderText("请再次输入用户密码")
        self.register_passwd1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_passwd1.setObjectName("register_passwd1")

        self.pushButton_regist = QtWidgets.QPushButton(self.page_1)
        self.pushButton_regist.setGeometry(QtCore.QRect(100, 210, 225, 30))
        self.pushButton_regist.clicked.connect(self.register)
        self.pushButton_regist.setObjectName("pushButton_regist")
        self.label_to0 = QtWidgets.QLabel(self.page_1)
        self.label_to0.setGeometry(QtCore.QRect(360, 300, 60, 12))
        self.label_to0.setObjectName("label_to0")
        self.label_to0.setText(
            "<style> a {text-decoration: none} </style><A href='#'>返回登录﹥</a>")
        self.label_to0.linkActivated.connect(self.to_index0)
        self.stackedWidget.addWidget(self.page_1)

        self.retranslateUi(Form1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        # Form1.setWindowTitle(_translate("Form1", "iClimb"))
        self.pushButton_login.setText(_translate("Form1", "安全登录"))
        self.pushButton_regist.setText(_translate("Form1", "注册账号"))

    def to_index1(self):
        self.stackedWidget.setCurrentIndex(1)

    def to_index0(self):
        self.stackedWidget.setCurrentIndex(0)

    def log_in(self):
        pass
        # log_user = self.lineEdit_user.text()
        # log_passwd = self.lineEdit_passwd.text()
        # print("用户名为：",log_user)
        # print("密码为：", log_passwd)

    def register(self):
        pass
        # reg_user = self.register_user.text()
        # reg_passwd = self.register_passwd.text()
        # reg_passwd1 = self.register_passwd1.text()
        # print("注册用户名为：",reg_user)
        # print("第一次输入的密码为：",reg_passwd)
        # print("第二次输入的密码为：",reg_passwd1)


class LogWin(Log_1, QtWidgets.QWidget):

    def __init__(self, parent=None, sockfd=None, addr=None):
        super().__init__(parent)
        self.setupUi(self)
        self.s = sockfd
        self.status = []
        self.addr = addr

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def log_in(self):
        log_user = self.lineEdit_user.text()
        log_passwd = self.lineEdit_passwd.text()
        a = 'L^^' + log_user + '^^' + log_passwd
        print(a)
        try:
            self.s.sendto(a.encode("utf8"), self.addr)
            data, addr = self.s.recvfrom(1024)
            print(data)
            if data.decode("utf8"):
                self.status += [log_user, log_passwd]
                # eval("mainw.status = [%s, %s]" % (log_user, log_passwd))
                # eval("mainw.show()")
                friend_list = []
                group_list = []
                data, addr = self.s.recvfrom(1024)
                if data == b"begin_send_friend_list":

                    while True:
                        data, addr = self.s.recvfrom(1024)

                        if data == b"over_send_friend_list":
                            print("退出")
                            break
                        else:
                            friend_list.append(data.decode())
                data, addr = self.s.recvfrom(1024)

                if data == b"begin_send_group_list":
                    while True:
                        data, addr = self.s.recvfrom(1024)
                        if data == b"over_send_group_list":
                            break
                        else:
                            group_list.append(data.decode())

                info_my1 = [[], {}, {}]
                info_my1[0].append(log_user)
                info_my1[0].append(log_passwd)
                nums = range(10, 100)
                icons = R.sample(nums, 90)
                it = iter(icons)

                for i in friend_list:
                    info_my1[1][i] = str(next(it))
                    # info_my1[1][i] = '62'

                for j in group_list:
                    info_my1[2][j] = ['']
                mainw.info_my = info_my1
                mainw.start_m(info_my1)
                mainw.thread.start()
                eval("mainw.show()")
                self.close()

            else:
                QtWidgets.QMessageBox.about(self, "错误提示", "您输入的用户名或密码有误")
                self.lineEdit_user.clear()
                self.lineEdit_passwd.clear()
        except:
            QtWidgets.QMessageBox.about(
                self, "网络异常", "由于网络问题，导致发送失败。请检查您的网络状况")
            self.lineEdit_user.clear()
            self.lineEdit_passwd.clear()
            pass


# 此处通过self.s 向服务器收发消息

    def register(self):
        reg_user = self.register_user.text()
        reg_passwd = self.register_passwd.text()
        reg_passwd1 = self.register_passwd1.text()

        if reg_passwd != reg_passwd1:
            QtWidgets.QMessageBox.about(self, "错误提示", "您前后输入的密码不一致")
            self.register_passwd.clear()
            self.register_passwd1.clear()
            return

        a = 'R^^' + reg_user + '^^' + reg_passwd
        self.s.sendto(a.encode(), self.addr)
        data, addr = client.recvfrom(1024)
        if data.decode() == 'EXIST':
            QtWidgets.QMessageBox.about(self, "错误提示", "您输入的用户名已存在")
            self.register_user.clear()
            self.register_passwd.clear()
            self.register_passwd1.clear()
            return
        elif data.decode() == 'OK':
            QtWidgets.QMessageBox.about(self, "注册成功", "恭喜您注册成功，请返回登录页面")
            self.register_user.clear()
            self.register_passwd.clear()
            self.register_passwd1.clear()
            return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    client = socket(AF_INET, SOCK_DGRAM)
    addr = ('172.40.71.212', 9999)
    # addr1 = ('172.40.71.212', 9999)
    logw = LogWin(sockfd=client, addr=addr)
    qssStytle = '''
        #Form1{border-radius:15px}
        #label_close,#label_mini{color:yellow; font:24px;text-align:center;}
        #label_close:hover{background-color:red}
        #label_mini:hover{background-color:gray}
    '''
    logw.setStyleSheet(qssStytle)

    info_my = [[], {}, {}]
    mainw = MainWin(info_my, client, addr)
    # mainw.setStyleSheet(qssStytle)
    logw.show()
    sys.exit(app.exec_())

    #[[name, password, icon], friends, groups]
    # friends={name1:icon1, name2:icon, ...}
    # groups = {name1:[member1,member2,...]}

    # 聊天记录：{id:[[时间,发言人, 内容], [], ...], id2:[[][][]], ...}

    # eval("mainw.status = [%s, %s]" % (log_user,log_passwd) )
    # info_my = [
    # ['Anthony', 'Anthony', 'o1'],
    # {'Antoinette': 'o2', 'Antonia': 'o3', 'Arabella': 'o4', 'Archibald': 'o5',
    #     'Armstrong': 'o6', 'Arnold': 'o7', 'Arthur': 'o8', 'Attlee': 'o9'},
    # {'spring': ['Antonia', 'Augustine', 'Anthony'],
    #     'summer':['Arthur', 'Augustus', 'Anthony']}
    # ]

    # self.status += [reg_user, log_passwd]

    # pwd1 = input('请输入密码(5-15位):')
    # if len(pwd1) > 15 or len(pwd1) < 5:
    #     print('密码格式不对,请重新输入')
    #     continue
    # pwd2 = input('请确认密码:')
    # if pwd1 != pwd2:
    #     print('密码不一致')
    #     continue
    # question = input('请输入安全问题')
    # answer = input('请输入答案')
