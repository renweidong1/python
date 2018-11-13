#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @Group：五人小队
# @Description:外部界面
import sys,time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
# from dispatcher import Dispatcher
# from baiduyuyin import BaiDuYuYin
from turing import TuringRobot
from localvoicer import Speaker

class clientUI(QtWidgets.QWidget):

    def __init__(self):
        super(clientUI, self).__init__()
        # self.dispatcher = Dispatcher()
        # self.baiduyuyin = BaiDuYuYin()
        self.turingrobot = TuringRobot()
        self.speaker = Speaker()
        self.initui()
    #     self.center()
        self.setGeometry(1200, 30, 350, 500)
    def initui(self):
        self.setWindowTitle("欢迎使用Cortana智能语音")


        # 顶部布局
        toplayout = QtWidgets.QHBoxLayout()
        self.textarea = QtWidgets.QTextBrowser()
        toplayout.addWidget(self.textarea)
        # 中间布局
        centerlayout = QtWidgets.QHBoxLayout()
        self.editline = QtWidgets.QLineEdit()
        # self.voicebutton = QtWidgets.QPushButton("点击说话")
        self.textbutton = QtWidgets.QPushButton("点击发文字")
        centerlayout.addWidget(self.editline)
        # centerlayout.addWidget(self.voicebutton)
        centerlayout.addWidget(self.textbutton)

        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./static/images/bk.jpg')))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        mainlayout = QtWidgets.QVBoxLayout()
        mainlayout.addLayout(toplayout)
        mainlayout.addLayout(centerlayout)

        self.setLayout(mainlayout)
        # eventhandler进行事件处理
        self.eventhandler()

    # 事件处理函数
    def eventhandler(self):
        # self.voicebutton.clicked.connect(self.pushvoice)
        self.textbutton.clicked.connect(self.pushtext)
        self.textbutton.setShortcut('enter')

    # def pushvoice(self):
    #     print('voice')
    #     # 先保存到本地，再调用语音接口上传
    #     self.dispatcher.record()
    #     response = self.baiduyuyin.parse()
    #     print('百度语音接口解析到的数据为：{}'.format(response))
    #     self.speaker.speak(text=response)
    #     # 更新一下窗体内容
    #     text = self.textarea.toPlainText()+"\n"+"<<< "+"上传音频中..."
    #     self.textarea.setText(text)
    #     text =  text +"\n>>> " +response
    #     self.textarea.setText(text)


    def pushtext(self):
        inputtext = self.editline.text()
        print(inputtext)
        trans = self.turingrobot.talk(inputtext)

        # 更新文本域内容
        self.editline.clear()
        # print(self.editline)

        text = self.textarea.toPlainText() + "\n<<<"+inputtext
        self.textarea.setText(text)
        text1 = self.textarea.toPlainText() + "\n>>> " + trans
        self.textarea.setText(text1)
        # time.sleep(10)
        self.speaker.speak(trans)
        if inputtext == "再见":
            self.clientWindow.hidden()



# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     app.setWindowIcon(QIcon("xn.png"))
#     clientWindow = clientUI()
#     # clientWindow.show()
#     sys.exit(app.exec_())