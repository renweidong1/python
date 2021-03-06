# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Chat_1(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(675, 475)
        Form.setMinimumSize(QtCore.QSize(850, 475))
        Form.setMaximumSize(QtCore.QSize(850, 475))

        self.listView_advertise = QtWidgets.QListView(Form)
        self.listView_advertise.setGeometry(QtCore.QRect(0, 0, 200, 475))
        self.listView_advertise.setObjectName("listView_advertise")

        self.textBrowser_display = QtWidgets.QTextBrowser(Form)
        self.textBrowser_display.setGeometry(QtCore.QRect(200, 0, 475, 300))
        self.textBrowser_display.setObjectName("textBrowser_display")

        self.textBrowser_hist = QtWidgets.QTextBrowser(Form)
        self.textBrowser_hist.setGeometry(QtCore.QRect(675, 0, 175, 475))
        self.textBrowser_hist.setObjectName("textBrowser_hist")

        self.layoutWidget_style = QtWidgets.QWidget(Form)
        self.layoutWidget_style.setGeometry(QtCore.QRect(210, 310, 200, 25))
        self.layoutWidget_style.setObjectName("layoutWidget_style")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_style)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.layoutWidget_style)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_style)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_style)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_style)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget_style)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)

        self.textEdit_input = QtWidgets.QTextEdit(Form)
        self.textEdit_input.setGeometry(QtCore.QRect(200, 340, 475, 100))
        self.textEdit_input.setObjectName("textEdit_input")

        self.layoutWidget_send = QtWidgets.QWidget(Form)
        self.layoutWidget_send.setGeometry(QtCore.QRect(500, 450, 100, 25))
        self.layoutWidget_send.setObjectName("layoutWidget_send")

        self.horizontalLayout_send = QtWidgets.QHBoxLayout(
            self.layoutWidget_send)
        self.horizontalLayout_send.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_send.setObjectName("horizontalLayout_send")

        self.pushButton_close = QtWidgets.QPushButton(self.layoutWidget_send)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_send.addWidget(self.pushButton_close)
        self.pushButton_send = QtWidgets.QPushButton(self.layoutWidget_send)
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout_send.addWidget(self.pushButton_send)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "与**聊天中..."))
        self.pushButton.setText(_translate("Form", "字体"))
        self.pushButton_2.setText(_translate("Form", "表情"))
        self.pushButton_3.setText(_translate("Form", "语音"))
        self.pushButton_4.setText(_translate("Form", "视频"))
        self.pushButton_5.setText(_translate("Form", "文件"))
        self.pushButton_close.setText(_translate("Form", "关闭"))
        self.pushButton_send.setText(_translate("Form", "发送"))


class ChatWin(Chat_1, QtWidgets.QDialog):

    def __init__(self, sockfd=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.s = sockfd
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_send.clicked.connect(self.send)
        self.hist = ""

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
        print(text)
        self.hist += text
        self.textBrowser_hist.setHtml(self.hist)


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)


#     demo = ChatWin()
#     demo.show()
#     sys.exit(app.exec_())
