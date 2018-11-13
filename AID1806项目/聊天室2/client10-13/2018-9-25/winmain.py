# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys
import time
from winchat import *


class Main_1(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(275, 700)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setMinimumSize(QtCore.QSize(275, 700))
        Form.setMaximumSize(QtCore.QSize(275, 700))
        # font = QtGui.QFont()
        # font.setFamily("Jokerman")
        # Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/climb.jpg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        font1 = QtGui.QFont()
        font1.setFamily("Arial")
        font1.setPointSize(14)
        font1.setBold(False)
        # font1.setWeight(10)
        self.label_char = QtWidgets.QLabel(Form)
        self.label_char.setGeometry(QtCore.QRect(0, 0, 80, 25))
        self.label_char.setText(" iClimb")
        self.label_char.setObjectName("label_char")
        self.label_char.setFont(font1)

        font2 = QtGui.QFont()
        font2.setFamily("Gulim")
        font2.setPointSize(18)
        font2.setBold(False)
        # font2.setWeight(10)
        font2.setUnderline(False)
        self.label_mini = QtWidgets.QLabel(Form)
        self.label_mini.setGeometry(QtCore.QRect(225, 0, 25, 25))
        self.label_mini.setText(
            "<style> a {text-decoration: none} </style><A href='#'>-</a>")
        self.label_mini.linkActivated.connect(self.showMinimized)
        self.label_mini.setObjectName("label_mini")
        self.label_mini.setFont(font2)
        self.label_close = QtWidgets.QLabel(Form)
        self.label_close.setGeometry(QtCore.QRect(250, 0, 25, 25))
        self.label_close.setText(
            "<style> a {text-decoration: none} </style><A href='#'>×</a>")
        self.label_close.linkActivated.connect(self.close)
        self.label_close.setObjectName("label_close")
        self.label_close.setFont(font2)

        self.graphicsView_profile = QtWidgets.QGraphicsView(Form)
        self.graphicsView_profile.setGeometry(QtCore.QRect(15, 35, 90, 90))
        self.graphicsView_profile.setObjectName("graphicsView_profile")
        self.textBrowser_weather = QtWidgets.QTextBrowser(Form)
        self.textBrowser_weather.setGeometry(QtCore.QRect(120, 30, 140, 70))
        self.textBrowser_weather.setObjectName("textBrowser_weather")
        self.textEdit_city = QtWidgets.QTextEdit(Form)
        self.textEdit_city.setGeometry(QtCore.QRect(120, 105, 140, 20))
        self.textEdit_city.setObjectName("textEdit_city")

        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 150, 275, 500))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(10)
        font.setBold(False)
        # font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_chatting = QtWidgets.QWidget()
        self.tab_chatting.setObjectName("tab_chatting")
        self.listWidget_chatting = QtWidgets.QListWidget(self.tab_chatting)
        self.listWidget_chatting.setGeometry(QtCore.QRect(0, 0, 275, 500))
        self.listWidget_chatting.setIconSize(QtCore.QSize(70, 70))
        self.listWidget_chatting.setObjectName("listWidget_chatting")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_chatting.addItem(item)
        self.tabWidget.addTab(self.tab_chatting, "")

        self.tab_friends = QtWidgets.QWidget()
        self.tab_friends.setObjectName("tab_friends")
        self.listWidget_friends = QtWidgets.QListWidget(self.tab_friends)
        self.listWidget_friends.setGeometry(QtCore.QRect(0, 0, 275, 500))
        self.listWidget_friends.setIconSize(QtCore.QSize(70, 70))
        self.listWidget_friends.setObjectName("listWidget_friends")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_friends.addItem(item)
        self.tabWidget.addTab(self.tab_friends, "")

        self.tab_groups = QtWidgets.QWidget()
        self.tab_groups.setObjectName("tab_groups")
        self.listWidget_groups = QtWidgets.QListWidget(self.tab_groups)
        self.listWidget_groups.setGeometry(QtCore.QRect(0, 0, 275, 500))
        self.listWidget_groups.setIconSize(QtCore.QSize(50, 50))
        self.listWidget_groups.setObjectName("listWidget_groups")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_groups.addItem(item)
        self.tabWidget.addTab(self.tab_groups, "")

        self.tab_apps = QtWidgets.QWidget()
        self.tab_apps.setObjectName("tab_apps")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_apps)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 250, 271, 221))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(self.tab_apps)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_apps)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_apps)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 50, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_apps)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 160, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_apps)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 50, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_apps)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 50, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_apps)
        self.pushButton_7.setGeometry(QtCore.QRect(100, 160, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_apps)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 160, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_apps, "")

        self.pushButton_set = QtWidgets.QPushButton(Form)
        self.pushButton_set.setGeometry(QtCore.QRect(0, 675, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.pushButton_set.setFont(font)
        self.pushButton_set.setObjectName("pushButton_set")
        self.pushButton_add = QtWidgets.QPushButton(Form)
        self.pushButton_add.setGeometry(QtCore.QRect(25, 675, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setAutoRepeatInterval(102)
        self.pushButton_add.setObjectName("pushButton_add")
        self.lcdNumber_time = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_time.setGeometry(QtCore.QRect(100, 675, 150, 25))
        self.lcdNumber_time.setObjectName("lcdNumber_time")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "iClimb"))
        __sortingEnabled = self.listWidget_chatting.isSortingEnabled()
        self.listWidget_chatting.setSortingEnabled(False)
        item = self.listWidget_chatting.item(0)
        item.setText(_translate("Form", "New Item"))

        self.listWidget_chatting.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_chatting), _translate("Form", "Chatting"))
        __sortingEnabled = self.listWidget_friends.isSortingEnabled()
        self.listWidget_friends.setSortingEnabled(False)
        item = self.listWidget_friends.item(0)
        item.setText(_translate("Form", "New Item"))

        self.listWidget_friends.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_friends), _translate("Form", "Friends"))
        __sortingEnabled = self.listWidget_groups.isSortingEnabled()
        self.listWidget_groups.setSortingEnabled(False)
        item = self.listWidget_groups.item(0)
        item.setText(_translate("Form", "New Item"))

        self.listWidget_groups.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_groups), _translate("Form", "Groups"))
        self.label.setText(_translate("Form", "TOOLS"))
        self.label_2.setText(_translate("Form", "GAMES"))
        self.pushButton_3.setText(_translate("Form", "BLOG"))
        self.pushButton_4.setText(_translate("Form", "Pan"))
        self.pushButton_5.setText(_translate("Form", "BLOG"))
        self.pushButton_6.setText(_translate("Form", "BLOG"))
        self.pushButton_7.setText(_translate("Form", "Pan"))
        self.pushButton_8.setText(_translate("Form", "Pan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_apps), _translate("Form", "APPS"))
        self.pushButton_set.setText(_translate("Form", "≡"))
        self.pushButton_add.setText(_translate("Form", "+"))


class MainWin(Main_1, QtWidgets.QWidget):

    def __init__(self, info_my, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.info_my = info_my
        # self.start_m(self.info_my)
        self.chat = {}

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

    def start_m(self, info_my):
        for i in info_my[1]:
            item1 = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(r"images/" + info_my[1][i] + ".ico"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item1.setIcon(icon)
            item1.setText(i)
            self.listWidget_friends.addItem(item1)
        self.listWidget_friends.itemDoubleClicked.connect(self.chatting)
        for j in info_my[2]:
            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(r"images/群聊.jfif"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setText(j)
            self.listWidget_groups.addItem(item)
        self.listWidget_groups.itemDoubleClicked.connect(self.chatting)

    def chatting(self, item):
        self.chat[item.text()] = ChatWin()
        self.chat[item.text()].show()


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)

    # mainw.show()
    # sys.exit(app.exec_())
