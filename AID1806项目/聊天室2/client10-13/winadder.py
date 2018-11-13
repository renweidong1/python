# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import pyqtSignal


class Adder_1(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 250)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"/pic/images/climb.jpg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        # Form.setStyleSheet(r"border-image: url(images/18.jpg);")
        self.label_back = QtWidgets.QLabel(Form)
        self.label_back.setGeometry(QtCore.QRect(0, 0, 400, 250))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("images/guo5.jpg"))
        self.label_back.setObjectName("label_back")

        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 20, 400, 230))
        self.tabWidget.setObjectName("tabWidget")

        self.label_close = QtWidgets.QLabel(Form)
        self.label_close.setGeometry(QtCore.QRect(380, 0, 20, 20))
        self.label_close.setText(
            "<style> a {text-decoration: none} </style><A href='#'>×</a>")
        self.label_close.linkActivated.connect(self.close)
        self.label_close.setObjectName("label_close")

        self.tab_addfriend = QtWidgets.QWidget()
        self.tab_addfriend.setObjectName("tab_addfriend")
        self.button_addfiend = QtWidgets.QPushButton(self.tab_addfriend)
        self.button_addfiend.setGeometry(QtCore.QRect(80, 100, 240, 25))
        self.button_addfiend.setObjectName("button_addfiend")
        self.line_addfiend = QtWidgets.QLineEdit(self.tab_addfriend)
        self.line_addfiend.setGeometry(QtCore.QRect(80, 60, 240, 25))
        self.line_addfiend.setObjectName("line_addfiend")
        self.line_addfiend.setPlaceholderText("请输入要查找的用户名")
        self.tabWidget.addTab(self.tab_addfriend, "")

        self.tab_addgroup = QtWidgets.QWidget()
        self.tab_addgroup.setObjectName("tab_addgroup")
        self.line_addgroup = QtWidgets.QLineEdit(self.tab_addgroup)
        self.line_addgroup.setGeometry(QtCore.QRect(80, 60, 240, 25))
        self.line_addgroup.setObjectName("line_addgroup")
        self.line_addgroup.setPlaceholderText("请输入要查找的群组名")
        self.button_addgroup = QtWidgets.QPushButton(self.tab_addgroup)
        self.button_addgroup.setGeometry(QtCore.QRect(80, 100, 240, 25))
        self.button_addgroup.setObjectName("button_addgroup")
        self.tabWidget.addTab(self.tab_addgroup, "")

        self.tab_newgroup = QtWidgets.QWidget()
        self.tab_newgroup.setObjectName("tab_newgroup")
        self.button_newgroup = QtWidgets.QPushButton(self.tab_newgroup)
        self.button_newgroup.setGeometry(QtCore.QRect(80, 100, 240, 25))
        self.button_newgroup.setObjectName("button_newgroup")
        self.line_newgroup = QtWidgets.QLineEdit(self.tab_newgroup)
        self.line_newgroup.setGeometry(QtCore.QRect(80, 60, 240, 25))
        self.line_newgroup.setObjectName("line_newgroup")
        self.line_newgroup.setPlaceholderText("请输入要新建的群组名")
        self.tabWidget.addTab(self.tab_newgroup, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_addfiend.setText(_translate("Form", "添  加"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_addfriend), _translate("Form", "   查 找 好 友 "))

        self.button_addgroup.setText(_translate("Form", "添  加"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_addgroup), _translate("Form", " 查 找 群 组 "))

        self.button_newgroup.setText(_translate("Form", "新  建"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_newgroup), _translate("Form", " 新 建 群 组   "))


class Adder(Adder_1, QtWidgets.QWidget):
    adder_sig = pyqtSignal(str)

    def __init__(self, uname, sockfd=None, addr=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.uname = uname
        self.s = sockfd
        self.addr = addr
        self.button_addfiend.clicked.connect(self.adder_addfiend)
        self.button_addgroup.clicked.connect(self.adder_addgroup)
        self.button_newgroup.clicked.connect(self.adder_newgroup)

    def adder_addfiend(self, msg):
        data = self.line_addfiend.text()
        if data:
            rsqt = "NF^^" + self.uname + "^^" + data
            self.s.sendto(rsqt.encode(), self.addr)
            self.line_addfiend.clear()
            QtWidgets.QMessageBox.about(self, "发送成功", "添加好友信息已发送")
        else:
            QtWidgets.QMessageBox.about(self, "错误提示", "请输入要查找的用户名")

    def adder_addgroup(self, msg):
        data = self.line_addgroup.text()
        if data:
            rsqt = "NG^^" + self.uname + "^^" + data
            self.s.sendto(rsqt.encode(), self.addr)
            self.line_addgroup.clear()
            QtWidgets.QMessageBox.about(self, "发送成功", "申请加入群组信息已发送")
        else:
            QtWidgets.QMessageBox.about(self, "错误提示", "请输入要加入的群组名")

    def adder_newgroup(self, msg):
        data = self.line_newgroup.text()
        if data:
            rsqt = "RG^^" + self.uname + "^^" + data
            self.s.sendto(rsqt.encode(), self.addr)
            self.line_newgroup.clear()
            QtWidgets.QMessageBox.about(self, "发送成功", "新建群组信息已发送")
        else:
            QtWidgets.QMessageBox.about(self, "错误提示", "请输入要新建的群组名")

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

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     adderw = Adder()
#     adderw.show()
#     sys.exit(app.exec_())
