# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from time import ctime


class Chat_1(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(675, 475)
        Form.setMinimumSize(QtCore.QSize(850, 475))
        Form.setMaximumSize(QtCore.QSize(850, 475))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/climb.jpg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label_back = QtWidgets.QLabel(Form)
        self.label_back.setGeometry(QtCore.QRect(0, 0, 850, 475))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("images/ying3.jpg"))
        self.label_back.setObjectName("label_back")
        # Form.setStyleSheet("border-image: url(images/ying.jpg);")

        # self.textBrowser_advertise = QtWidgets.QTextBrowser(Form)
        # self.textBrowser_advertise.setGeometry(QtCore.QRect(0, 0, 200, 475))
        # self.textBrowser_advertise.setObjectName("textBrowser_advertise")

        self.textBrowser_display = QtWidgets.QTextBrowser(Form)
        self.textBrowser_display.setGeometry(QtCore.QRect(200, 3, 475, 320))
        self.textBrowser_display.setObjectName("textBrowser_display")
        self.textBrowser_display.setStyleSheet(
            "background-color:rgba(255,255,255,0.8)")

        # self.textBrowser_hist = QtWidgets.QTextBrowser(Form)
        # self.textBrowser_hist.setGeometry(QtCore.QRect(675, 0, 175, 475))
        # self.textBrowser_hist.setObjectName("textBrowser_hist")

        self.layoutWidget_style = QtWidgets.QWidget(Form)
        self.layoutWidget_style.setGeometry(QtCore.QRect(210, 310, 200, 25))
        self.layoutWidget_style.setObjectName("layoutWidget_style")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_style)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # self.pushButton = QtWidgets.QPushButton(self.layoutWidget_style)
        # self.pushButton.setObjectName("pushButton")
        # self.horizontalLayout.addWidget(self.pushButton)
        # self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_style)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.horizontalLayout.addWidget(self.pushButton_2)
        # self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_style)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.horizontalLayout.addWidget(self.pushButton_3)
        # self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_style)
        # self.pushButton_4.setObjectName("pushButton_4")
        # self.horizontalLayout.addWidget(self.pushButton_4)
        # self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget_style)
        # self.pushButton_5.setObjectName("pushButton_5")
        # self.horizontalLayout.addWidget(self.pushButton_5)

        self.textEdit_input = QtWidgets.QTextEdit(Form)
        self.textEdit_input.setGeometry(QtCore.QRect(200, 340, 475, 100))
        self.textEdit_input.setObjectName("textEdit_input")
        self.textEdit_input.setStyleSheet(
            "background-color:rgba(255,255,255,0.8)")

        self.layoutWidget_send = QtWidgets.QWidget(Form)
        self.layoutWidget_send.setGeometry(QtCore.QRect(500, 450, 100, 25))
        self.layoutWidget_send.setObjectName("layoutWidget_send")

        self.horizontalLayout_send = QtWidgets.QHBoxLayout(
            self.layoutWidget_send)
        self.horizontalLayout_send.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_send.setObjectName("horizontalLayout_send")

        self.pushButton_close = QtWidgets.QPushButton(self.layoutWidget_send)
        self.pushButton_close.setGeometry(QtCore.QRect(350, 450, 60, 25))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_send.addWidget(self.pushButton_close)
        self.pushButton_send = QtWidgets.QPushButton(self.layoutWidget_send)
        self.pushButton_send.setGeometry(QtCore.QRect(400, 450, 60, 25))
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout_send.addWidget(self.pushButton_send)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "与**聊天中..."))
        # self.pushButton.setText(_translate("Form", "字体"))
        # self.pushButton_2.setText(_translate("Form", "表情"))
        # self.pushButton_3.setText(_translate("Form", "语音"))
        # self.pushButton_4.setText(_translate("Form", "视频"))
        # self.pushButton_5.setText(_translate("Form", "文件"))
        self.pushButton_close.setText(_translate("Form", "关闭"))
        self.pushButton_send.setText(_translate("Form", "发送"))


class ChatWin(Chat_1, QtWidgets.QDialog):

    def __init__(self, isgroup, uname=None, toname=None, sockfd=None, toaddr=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.isgroup = isgroup
        self.uname = uname
        self.toname = toname
        self.s = sockfd
        self.to = toaddr
        self.setWindowTitle("与 %s 聊天中" % self.toname)
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_send.clicked.connect(self.send)
        self.hist_body = "<!DOCTYPE html><html><head><meta charset='utf-8'></head><body>"
        self.hist_tail = "</body></html>"
        self.hist = self.hist_body + self.hist_tail

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

    def send(self):
        text = self.textEdit_input.toPlainText()
        if self.isgroup:
            rsqt = "CG^^" + self.uname + "^^" + self.toname + "^^" + text
        else:
            rsqt = "CF^^" + self.uname + "^^" + self.toname + "^^" + text
        self.s.sendto(rsqt.encode(), self.to)
        self.textEdit_input.clear()
        self.hist_body += "<p text-align:center> %s </p>" % str(ctime())
        self.hist_body += "<p text-align:right>MyReply：： %s  <p>" % text
        self.hist = self.hist_body + self.hist_tail
        self.textBrowser_display.clear()
        self.textBrowser_display.setHtml(self.hist)


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)

#     demo = ChatWin()
#     demo.show()
#     sys.exit(app.exec_())
