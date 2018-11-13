
from random import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from socket import *
from threading import Thread
from friendlist_window import Ui_Form
from addfriend import AddFriend
import codecs
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtGui import QIcon, QPainter, QColor
from PyQt5.QtWidgets import QApplication,QWidget


# 登录界面
from myplace_ui import MyPlace
import time

class SignInWidget(QWidget):
    is_admin_signal = pyqtSignal()
    is_student_signal = pyqtSignal(str)

    def __init__(self):
        super(SignInWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setObjectName("Cortana")
        self.setWindowIcon(QIcon('./static/images/icon.png'))
        self.setMinimumSize(344,554)
        self.setMaximumSize(344,554)

        # 窗体控件
        btn1 = QPushButton("",self)
        btn1.setFlat(True)
        btn1.clicked.connect(self.close)
        btn1.setObjectName('test')
        btn2 = QPushButton("",self)
        btn2.setFlat(True)
        btn2.clicked.connect(self.showMinimized)
        btn1.move(310,0)
        btn2.move(280,0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./static/images/x_alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./static/images/min.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        btn1.setIcon(icon1)
        btn2.setIcon(icon2)
        btn1.setIconSize(QSize(25,25))
        btn2.setIconSize(QSize(25,25))

        # 设置背景图片
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./static/images/timg1.jpg')))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # 注册按钮
        self.signUp = QtWidgets.QPushButton(self)
        self.signUp.setGeometry(QtCore.QRect(260, 50, 75, 23))
        self.signUp.setObjectName("pushButton")

        # 账号
        self.lineEdit1 = QtWidgets.QLineEdit(self)
        self.lineEdit1.setGeometry(QtCore.QRect(20, 200, 301, 31))
        self.lineEdit1.setObjectName("lineEdit")
        self.lineEdit1.setPlaceholderText("账号")

        # 密码
        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit2.setGeometry(QtCore.QRect(20, 250, 301, 31))
        self.lineEdit2.setObjectName("lineEdit_2")
        self.lineEdit2.setPlaceholderText("密码")
        self.lineEdit2.setEchoMode(QLineEdit.Password)


        # 登录
        self.signIn = QtWidgets.QPushButton(self)
        self.signIn.setGeometry(QtCore.QRect(20, 340, 301, 41))
        self.signIn.setObjectName("pushButton_2")

        # 我的地盘
        self.myplace = QtWidgets.QPushButton(self)
        self.myplace.setGeometry(QtCore.QRect(140,420,61,61))
        self.myplace.setObjectName("myplace")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./static/images/myplace.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.myplace.setIcon(icon3)
        self.myplace.setIconSize(QtCore.QSize(61, 61))

        # 最终版权归属@五人小组
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(86, 520, 155, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "欢迎使用Cortana"))
        self.signUp.setText(_translate("Form", "注 册"))
        self.signIn.setText(_translate("Form", "登    录"))
        self.myplace.clicked.connect(self.myplaceshow)
        self.myplace.setToolTip(_translate("Form", "我的地盘"))
        self.myplace.setWhatsThis(_translate("Form", "我的地盘"))
        self.myplace.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", "最终版权归属@五人小组"))

        with codecs.open('./static/qss/style.qss','r','utf-8') as f:
            styleSheet = f.readlines()
        style = '\r\n'.join(styleSheet)
        self.signUp.setStyleSheet(style)
        self.signIn.setStyleSheet(style)
        self.lineEdit1.setStyleSheet(style)
        self.lineEdit2.setStyleSheet(style)
        self.label_2.setStyleSheet(style)
        self.myplace.setStyleSheet(style)

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def myplaceshow(self):
        self.myplaceshow = MyPlace()
        self.myplaceshow.show()

    def signup_show(self):
        loginWindow.close()
        registWindow.show()

        # if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     loginwindow = SignInWidget()
#     loginwindow.show()
#     sys.exit(app.exec_())

        # 设置验证
        reg = QRegExp("PB[0~9]{8}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.lineEdit1.setValidator(pValidator)

        reg = QRegExp("[a-zA-z0-9]+$")
        pValidator.setRegExp(reg)
        self.lineEdit2.setValidator(pValidator)

        passwordFont = QFont()
        passwordFont.setPixelSize(10)
        self.lineEdit2.setFont(passwordFont)
        self.lineEdit2.setEchoMode(QLineEdit.Password)



#注册界面
class SignUpWidget(QWidget):
    signup_signal = pyqtSignal(str)

    def __init__(self):
        super(SignUpWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        # 窗体名称及尺寸,图标
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setObjectName("Cortana")
        self.setWindowIcon(QIcon('./static/images/icon.png'))
        self.setMinimumSize(344, 554)
        self.setMaximumSize(344, 554)

        # 设置背景图片
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./static/images/register.jpg')))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # 窗体控件
        btn1 = QPushButton("",self)
        btn1.setFlat(True)
        btn1.clicked.connect(self.close)
        btn1.setObjectName('test')
        btn2 = QPushButton("",self)
        btn2.setFlat(True)
        btn2.clicked.connect(self.showMinimized)
        btn1.move(310,0)
        btn2.move(280,0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./static/images/x_alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./static/images/min.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        btn1.setIcon(icon1)
        btn2.setIcon(icon2)
        btn1.setIconSize(QSize(25,25))
        btn2.setIconSize(QSize(25,25))

        # 返回登录按钮
        self.gobackbutton = QtWidgets.QPushButton(self)
        self.gobackbutton.setGeometry(QtCore.QRect(260, 50, 75, 23))
        self.gobackbutton.setObjectName("pushButton_4")


        # 账号
        self.IdLineEdit = QtWidgets.QLineEdit(self)
        self.IdLineEdit.setGeometry(QtCore.QRect(20, 160, 301, 31))
        self.IdLineEdit.setObjectName("lineEdit_3")
        self.IdLineEdit.setPlaceholderText("账号")
        self.IdLineEdit.setMaxLength(18)

        # 昵称
        self.NameLineEdit = QtWidgets.QLineEdit(self)
        self.NameLineEdit.setGeometry(QtCore.QRect(20, 210, 301, 31))
        self.NameLineEdit.setObjectName("lineEdit_6")
        self.NameLineEdit.setPlaceholderText("昵称")

        # 密码
        self.passwordLineEdit = QtWidgets.QLineEdit(self)
        self.passwordLineEdit.setGeometry(QtCore.QRect(20, 260, 301, 31))
        self.passwordLineEdit.setObjectName("lineEdit_4")
        self.passwordLineEdit.setPlaceholderText("密码")
        self.passwordLineEdit.setMaxLength(18)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        # 确认密码
        self.passwordConfirmLineEdit = QtWidgets.QLineEdit(self)
        self.passwordConfirmLineEdit.setGeometry(QtCore.QRect(20, 310, 301, 31))
        self.passwordConfirmLineEdit.setObjectName("lineEdit_5")
        self.passwordConfirmLineEdit.setPlaceholderText("确认密码")
        self.passwordConfirmLineEdit.setEchoMode(QLineEdit.Password)

        # 注册按钮
        self.signUpbutton = QtWidgets.QPushButton(self)
        self.signUpbutton.setGeometry(QtCore.QRect(20, 360, 301, 41))
        self.signUpbutton.setObjectName("pushButton_5")

        # 我的地盘
        self.myplace = QtWidgets.QPushButton(self)
        self.myplace.setGeometry(QtCore.QRect(140, 440, 61, 61))
        self.myplace.setObjectName("myplace")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./static/images/myplace.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.myplace.setIcon(icon3)
        self.myplace.setIconSize(QtCore.QSize(61, 61))

        # 最终版权归属@五人小组
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(86, 520, 155, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "欢迎使用Cortana"))
        self.gobackbutton.setText(_translate("Form", "返回登录"))
        self.signUpbutton.setText(_translate("Form", "注    册"))
        self.label_4.setText(_translate("Form", "最终版权归属@五人小组"))
        self.myplace.clicked.connect(self.myplaceshow)
        self.myplace.setToolTip(_translate("Form", "我的地盘"))
        self.myplace.setWhatsThis(_translate("Form", "我的地盘"))
        self.myplace.setText(_translate("Form", ""))

        with codecs.open('./static/qss/style.qss', 'r', 'utf-8') as f:
            styleSheet = f.readlines()
        style = '\r\n'.join(styleSheet)
        self.signUpbutton.setStyleSheet(style)
        self.gobackbutton.setStyleSheet(style)
        self.IdLineEdit.setStyleSheet(style)
        self.NameLineEdit.setStyleSheet(style)
        self.passwordLineEdit.setStyleSheet(style)
        self.passwordConfirmLineEdit.setStyleSheet(style)
        self.label_4.setStyleSheet(style)
        self.myplace.setStyleSheet(style)

    def myplaceshow(self):
        self.myplaceshow = MyPlace()
        self.myplaceshow.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     loginwindow = SignUpWidget()
#     loginwindow.show()
#     sys.exit(app.exec_())

        # 设置验证
        reg = QRegExp("PB[0~9]{8}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.IdLineEdit.setValidator(pValidator)

        reg = QRegExp("[a-zA-z0-9]+$")
        pValidator.setRegExp(reg)
        self.passwordLineEdit.setValidator(pValidator)
        self.passwordConfirmLineEdit.setValidator(pValidator)

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def myplaceshow(self):
        self.myplaceshow = MyPlace()
        self.myplaceshow.show()

    def signup_show(self):
        loginWindow.close()
        registWindow.show()

    def goback(self):
        registWindow.close()
        loginWindow.show()

#聊天界面
class chatWidget(QDialog):
    chat_signal = pyqtSignal(str,str)

    def __init__(self,s,friend_name,Id,chat_socket):
        self.s = s
        self.friend_name = friend_name
        self.Id = Id
        self.chat_socket = chat_socket

        super(chatWidget,self).__init__()
        # self.resize(200, 600)
        # L = friend_name.split(',')
        # print('打开群聊窗口',L)
        # if L == []:
        self.setWindowTitle("%s" % self.friend_name)
        # else:
        #     group_chat_name = ''
        #     L.remove('的群聊')
        #     L.sort()
        #     print('排序后',L)
        #     for i in L:
        #         group_chat_name = group_chat_name + i + ','
        #     group_chat_name = group_chat_name + '的群聊'
        #     print('群聊窗口标题为',group_chat_name)
        #     self.setWindowTitle("%s" % group_chat_name)

        self.setWindowIcon(QIcon('./static/images/icon.png'))
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.setupUi()

    def setupUi(self):
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setObjectName("chatWidget")
        self.setMinimumSize(782,566)
        self.setMaximumSize(782,566)

        # 窗体控件
        # btn1 = QPushButton("",self)
        # btn1.setFlat(True)
        # btn1.clicked.connect(self.close)
        # btn1.setObjectName('test')
        # btn2 = QPushButton("",self)
        # btn2.setFlat(True)
        # btn2.clicked.connect(self.showMinimized)
        # btn1.move(748,0)
        # btn2.move(718,0)
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap("./static/images/x_alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon2 = QtGui.QIcon()
        # icon2.addPixmap(QtGui.QPixmap("./static/images/min.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # btn1.setIcon(icon1)
        # btn2.setIcon(icon2)
        # btn1.setIconSize(QSize(25,25))
        # btn2.setIconSize(QSize(25,25))


        # 设置背景图片
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./static/images/timg3.jpg')))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # 显示窗口
        self.chatoutput = QtWidgets.QTextBrowser(self)
        self.chatoutput.setGeometry(QtCore.QRect(10, 30, 760, 281))
        self.chatoutput.setObjectName("textBrowser")

        # 输入窗口
        self.chatinput = QtWidgets.QTextEdit(self)
        self.chatinput.setGeometry(QtCore.QRect(10, 340, 760, 150))
        self.chatinput.setObjectName("textEdit")

        # 撤回按钮
        self.callbackmassege = QtWidgets.QPushButton(self)
        self.callbackmassege.setGeometry(QtCore.QRect(650, 510, 100, 40))
        self.callbackmassege.setObjectName("pushButton_7")

        # 发送按钮
        self.sendmessage = QtWidgets.QPushButton(self)
        self.sendmessage.setGeometry(QtCore.QRect(540, 510, 100, 40))
        self.sendmessage.setObjectName("pushButton_8")


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.chat_signal.connect(self.receive_chat_msg)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        L = self.friend_name.split(',')
        print('打开群聊窗口',L)
        if len(L) == 1:
            self.setWindowTitle(_translate("Form", "当前聊天 %s" % self.friend_name))
        else:
            group_chat_name = ''
            L.remove('的群聊')
            L.sort()
            print('排序后',L)
            for i in L:
                group_chat_name = group_chat_name + i + ','
            group_chat_name = group_chat_name + '的群聊'
            print('群聊窗口标题为',group_chat_name)
            self.setWindowTitle(_translate("Form", "当前聊天 %s" % group_chat_name))
        # self.setWindowTitle(_translate("Form", "当前聊天 %s" % self.friend_name))
        self.sendmessage.setText(_translate("Form", "发  送"))
        self.callbackmassege.setText(_translate("Form", "撤  回"))
        self.sendmessage.clicked.connect(self.getmsg)


        with codecs.open('./static/qss/style.qss', 'r', 'utf-8') as f:
            styleSheet = f.readlines()
        style = '\r\n'.join(styleSheet)
        self.sendmessage.setStyleSheet(style)
        self.callbackmassege.setStyleSheet(style)
        self.chatoutput.setStyleSheet(style)
        self.chatinput.setStyleSheet(style)

    # def mousePressEvent(self, event):
    #     if event.button()==Qt.LeftButton:
    #         self.m_drag=True
    #         self.m_DragPosition=event.globalPos()-self.pos()
    #         event.accept()
    #         self.setCursor(QCursor(Qt.OpenHandCursor))
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #     if Qt.LeftButton and self.m_drag:
    #         self.move(QMouseEvent.globalPos()-self.m_DragPosition)
    #         QMouseEvent.accept()
    #
    # def mouseReleaseEvent(self, QMouseEvent):
    #     self.m_drag=False
    #     self.setCursor(QCursor(Qt.ArrowCursor))
    #
    # def myplaceshow(self):
    #     self.myplaceshow = MyPlace()
    #     self.myplaceshow.show()
    # if __name__ == "__main__":
    #     app = QApplication(sys.argv)
    #     chatwindow = chatWindow()
    #     chatwindow.show()
    #     sys.exit(app.exec_())


    def getmsg(self):
        data = self.chatinput.toPlainText()
        if data == '':
            print(QMessageBox.information(loginWindow, "提示", "发送消息不能为空", QMessageBox.Yes, QMessageBox.Yes))
            return
        self.chatinput.clear()
        self.chatoutput.append("%s  %s\n%s\n" % (self.Id,time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())), data))
        main.chat_send(self.friend_name,data,self.chat_socket)
        # msg,addr = self.s.recvfrom(1024)
        # msgreturn = msg.decode()
        # self.chatoutput.append(msgreturn + '\n')

    def loginsucc(self):
        loginWindow.close()

    def receive_chat_msg(self,str,friend_name):
        print('收到发送的消息',str)
        self.chatoutput.append("%s  %s\n%s\n" % (friend_name,time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())), str))

#好友列表界面
class FriendList(QDialog, Ui_Form):
    # 分组信息存储
    grouplist = []
    # 用户信息存储
    group_chatlist = []
    userslist = []
    tmpuseritem = []

    def __init__(self, s, Id, chat_socket,parent=None):

        super(FriendList, self).__init__(parent)
        self.Id = Id
        self.s = s
        self.chat_socket = chat_socket
        # print("该用户好友列表为",self.L)
        self.setupUi(self)
        # main.get_friend_info(self.Id)
        self.Ui_init()

    def Ui_init(self):
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setColumnWidth(0, 50)
        self.treeWidget.setHeaderLabels(["好友"])
        self.treeWidget.setIconSize(QSize(70, 70))
        self.treeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.treeWidget.itemSelectionChanged.connect(self.getListitems)
        self.treeWidget.currentItemChanged.connect(self.restatistic)
        self.treeWidget.itemClicked.connect(self.isclick)
        self.treeWidget.itemDoubleClicked.connect(self.isDoubleClick)

        # 样式设置
        # with codecs.open('./res/treewidget.qss', 'r', 'utf-8') as f:
        #     styleSheet = f.readlines()
        # style = '\r\n'.join(styleSheet)
        # self.treeWidget.setStyleSheet(style)
        print('目前用户',self.Id)
        group_list = main.request_group(self.Id)
        print('获取到分组列表',group_list)



        for i in group_list:
            print(i)
            root = self.creategroup("%s" % i)
            root.setExpanded(True)

        root = self.create_chat_group()
        root.setExpanded(True)

        # 是否出现批量操作菜单的标志
        self.menuflag = 1

        # 搜索时自动填充姓名
        self.m_model = QStandardItemModel(0, 1, self)
        m_completer = QCompleter(self.m_model, self)
        self.lineEdit.setCompleter(m_completer)
        m_completer.activated[str].connect(self.onUsernameChoosed)

    def create_chat_group(self):
        group_chat_list = main.request_group_chat(self.Id)
        print("获取到群聊列表",group_chat_list)
        groupname = '群聊'
        hidernum = 0
        group = QTreeWidgetItem(self.treeWidget)
        groupdic = {'group': group, 'groupname': groupname, 'childcount': 0, 'childishide': 0}
        icon = self.searchicon(groupname)
        group.setIcon(0, icon)

        for i in group_chat_list:
            child = QTreeWidgetItem()
            name, randicon, font, ishider = self.createusers(i)
            userdic = {'user': child, 'username': name, 'ishide': 0}
            self.userslist.append(userdic)
            child.setText(0, i)
            child.setFont(15,font)
            child.setTextAlignment(0, Qt.AlignHCenter | Qt.AlignVCenter)
            if ishider == 1:
                hidernum += 1
                userdic['ishide'] = 1
            group.addChild(child)
        childnum = group.childCount()
        lastchildnum = childnum - hidernum
        groupdic['childcount'] = childnum
        groupdic['childishide'] = hidernum
        groupname += ' ' + str(lastchildnum) + '/' + str(childnum)
        group.setText(0, groupname)
        self.grouplist.append(groupdic)
        return group


    def creategroup(self, groupname):
        hidernum = 0
        group = QTreeWidgetItem(self.treeWidget)
        groupdic = {'group': group, 'groupname': groupname, 'childcount': 0, 'childishide': 0}
        icon = self.searchicon(groupname)
        group.setIcon(0, icon)
        friend_list = main.get_group_friend(self.Id,groupname)

        for i in friend_list:
            child = QTreeWidgetItem()
            name, randicon, font, ishider = self.createusers(i)
            userdic = {'user': child, 'username': name, 'ishide': 0}
            self.userslist.append(userdic)
            child.setText(0, i)
            child.setFont(0, font)
            child.setIcon(0, randicon)
            child.setTextAlignment(0, Qt.AlignHCenter | Qt.AlignVCenter)

            if ishider == 1:
                hidernum += 1
                userdic['ishide'] = 1
            group.addChild(child)
        childnum = group.childCount()
        lastchildnum = childnum - hidernum
        groupdic['childcount'] = childnum
        groupdic['childishide'] = hidernum
        groupname += ' ' + str(lastchildnum) + '/' + str(childnum)
        group.setText(0, groupname)
        self.grouplist.append(groupdic)
        return group

    def createusers(self, name):
        chooseicon = QIcon("./static/images/user/" + str(randint(0,25)) + ".jpg")
        font = QFont()
        font.setPointSize(16)
        ishider = main.is_hider(name)
        if ishider == 0:
            chooseicon = QIcon("./static/images/user/" + str(randint(0,25)) + "h.jpg")
        return name, chooseicon, font, ishider

    def contextMenuEvent(self, event):
        hititem = self.treeWidget.currentItem()
        if hititem:
            root = hititem.parent()
            if root is None:
                pgroupmenu = QMenu(self)
                pAddgroupAct = QAction('添加分组', self.treeWidget)
                pRenameAct = QAction('重命名', self.treeWidget)
                pDeleteAct = QAction('删除该组', self.treeWidget)
                pgroupmenu.addAction(pAddgroupAct)
                pgroupmenu.addAction(pRenameAct)
                pgroupmenu.addAction(pDeleteAct)
                pAddgroupAct.triggered.connect(self.addgroup)
                pRenameAct.triggered.connect(self.renamegroup)
                if self.treeWidget.itemAbove(hititem) is None:
                    pDeleteAct.setEnabled(False)
                else:
                    pDeleteAct.triggered.connect(self.deletegroup)
                pgroupmenu.popup(self.mapToGlobal(event.pos()))
            elif root.childCount() > 0:
                pItemmenu = QMenu(self)
                pDeleteItemAct = QAction('删除联系人', pItemmenu)
                pItemmenu.addAction(pDeleteItemAct)
                pDeleteItemAct.triggered.connect(self.delete)
                if len(self.grouplist) > 1:
                    pSubMenu = QMenu('转移联系人至', pItemmenu)
                    pItemmenu.addMenu(pSubMenu)
                    for item_dic in self.grouplist:
                        if item_dic['group'] is not root:
                            pMoveAct = QAction(item_dic['groupname'], pItemmenu)
                            pSubMenu.addAction(pMoveAct)
                            pMoveAct.triggered.connect(self.moveItem)
                if len(self.getListitems(self.menuflag)) == 1:
                    pRenameItemAct = QAction('设定备注', pItemmenu)
                    pItemmenu.addAction(pRenameItemAct)
                    pRenameItemAct.triggered.connect(self.renameItem)
                # if self.menuflag > 0 and root.childCount() > 1:
                #     pBatchAct = QAction('添加群聊', pItemmenu)
                #     pItemmenu.addAction(pBatchAct)
                #     pBatchAct.triggered.connect(self.add_GroupChat)
                if self.menuflag > 0 and root.childCount() > 1:
                    pBatchAct = QAction('分组内批量操作', pItemmenu)
                    pItemmenu.addAction(pBatchAct)
                    pBatchAct.triggered.connect(self.Batchoperation)

                elif self.menuflag < 0:
                    pCancelBatchAct = QAction('取消批量操作', pItemmenu)
                    pItemmenu.addAction(pCancelBatchAct)
                    pCancelBatchAct.triggered.connect(self.CancelBatchoperation)
                    pAddgroupchat = QAction('添加群聊',pItemmenu)
                    pItemmenu.addAction(pAddgroupchat)
                    pAddgroupchat.triggered.connect(self.AddGC)

                pItemmenu.popup(self.mapToGlobal(event.pos()))

    def addgroup(self):
        gname, ok = QInputDialog.getText(self, '提示信息', '请输入分组名称')
        if ok:
            if len(gname) == 0:
                QMessageBox.information(self, '提示', '分组名称不能为空哦')
            else:
                main.add_group(self.Id,gname)
                self.creategroup(gname)

    def renamegroup(self):
        hitgroup = self.treeWidget.currentItem()
        gnewname, ok = QInputDialog.getText(self, '提示信息', '请输入分组的新名称')
        if ok:
            if len(gnewname) == 0:
                QMessageBox.information(self, '提示', '分组名称不能为空哦')
            else:
                hitgroup.setText(0, gnewname)
                newicon = self.searchicon(hitgroup.text(0))
                hitgroup.setIcon(0, newicon)
                gindex = self.searchgroup(hitgroup)
                old_group_name = self.grouplist[gindex]['groupname']
                print('旧分组为',old_group_name)
                main.rename_group(self.Id,old_group_name,gnewname)
                self.grouplist[gindex]['groupname'] = gnewname
                print(hitgroup.child(0))
                if hitgroup.child(0):
                    self.treeWidget.setCurrentItem(hitgroup.child(0))
                else:
                    pass


    def deletegroup(self):
        hitgroup = self.treeWidget.currentItem()
        gindex = self.searchgroup(hitgroup)
        group_name = self.grouplist[gindex]['groupname']
        print(group_name)
        reply = QMessageBox.question(self, '警告', '确定要删除这个分组及其联系人吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.treeWidget.takeTopLevelItem(gindex)
            main.delete_group(self.Id,group_name)
            del self.grouplist[gindex]

    def moveItem(self):
        hituser = self.treeWidget.currentItem()
        uindex = self.searchuser(hituser)
        move_name = self.userslist[uindex]['username']
        print('移动好友',move_name)
        movelist = self.getListitems(self.menuflag)
        togroupname = self.sender().text()
        print('移动组',togroupname)
        mindex = self.searchgroup(togroupname)
        togroup = self.grouplist[mindex]['group']
        print('删除好友')
        self.deleteItems(movelist, flag=0)
        print('添加好友')
        self.add(togroup, movelist,togroupname)
        self.tmpuseritem.clear()

    def delete(self):
        delitems = self.getListitems(self.menuflag)
        self.deleteItems(delitems)
        self.tmpuseritem.clear()

    def deleteItems(self, items, flag=1):
        for delitem in items:
            print('准备获取姓名')
            delitem.setData(0, Qt.CheckStateRole, QVariant())  # 取消删除item的复选框
            pindex = delitem.parent().indexOfChild(delitem)
            dindex = self.searchuser(delitem)
            ishide = self.userslist[dindex]['ishide']
            move_name = self.userslist[dindex]['username']
            print('要删除的好友们:',move_name)
            main.delete_friend(self.Id,move_name)
            if flag == 1:
                del self.userslist[dindex]
            fathergroup = delitem.parent()
            findex = self.searchgroup(fathergroup)
            if ishide == 1:
                self.grouplist[findex]['childishide'] -= 1
                self.grouplist[findex]['childcount'] -= 1
            else:
                self.grouplist[findex]['childcount'] -= 1

            delitem.parent().takeChild(pindex)

    def add(self, group, items,group_name):
        gindex = self.searchgroup(group)
        for item in items:
            aindex = self.searchuser(item)
            ishide = self.userslist[aindex]['ishide']
            add_name = self.userslist[aindex]['username']
            print('要添加的好友为',add_name)
            main.add_friend(self.Id, add_name, group_name)
            if ishide == 1:
                self.grouplist[gindex]['childishide'] += 1
                self.grouplist[gindex]['childcount'] += 1
            else:
                self.grouplist[gindex]['childcount'] += 1
            group.addChild(item)
            self.treeWidget.setCurrentItem(item)

    def AddGC(self):
        additems = self.getListitems(self.menuflag)
        self.AddGroupChat(additems)
        self.tmpuseritem.clear()

    def AddGroupChat(self,items):
        print('准备添加群聊')
        s = ''
        for additem in items:
            print('准备获取姓名')
            additem.setData(0, Qt.CheckStateRole, QVariant())  # 取消删除item的复选框
            pindex = additem.parent().indexOfChild(additem)
            dindex = self.searchuser(additem)
            add_name = self.userslist[dindex]['username']
            print('要添加群聊的好友为',add_name)
            s = s + add_name + ','
        group_chat_name = s + self.Id + ',' + '的群聊'
        print(group_chat_name)
        mindex = self.searchgroup('群聊')
        togroup = self.grouplist[mindex]['group']
        font = QFont()
        font.setPointSize(16)
        child = QTreeWidgetItem()
        userdic = {'user': child, 'username': group_chat_name, 'ishide': 1}
        self.userslist.append(userdic)
        print('haol')
        child.setText(0, group_chat_name)
        child.setFont(0, font)
        child.setTextAlignment(0, Qt.AlignHCenter | Qt.AlignVCenter)
        togroup.addChild(child)
        main.AddGroupChat(self.Id,group_chat_name)
        self.CancelBatchoperation()

    def Batchoperation(self):
        self.menuflag *= -1

        group = self.getListitems()[0].parent()
        childnum = group.childCount()
        for c in range(childnum):
            child = group.child(c)
            child.setCheckState(0, Qt.Unchecked)

    def CancelBatchoperation(self):
        self.menuflag *= -1
        group = self.getListitems()[0].parent()
        childnum = group.childCount()
        for c in range(childnum):
            child = group.child(c)
            child.setData(0, Qt.CheckStateRole, QVariant())

    def isclick(self, item):

        if item.checkState(0) == Qt.Checked:
            if self.tmpuseritem.count(item) == 0:
                self.tmpuseritem.append(item)
        else:
            if len(self.tmpuseritem) > 0:
                if self.tmpuseritem.count(item) != 0:
                    i = self.tmpuseritem.index(item)
                    del self.tmpuseritem[i]

    def isDoubleClick(self):
        hituser = self.treeWidget.currentItem()
        uindex = self.searchuser(hituser)
        chat_name = self.userslist[uindex]['username']
        print('即将要聊天的对象为',chat_name)
        main.chat_show(chat_name,self.Id,self.chat_socket)

        #
        # chat = chatWidget(self.s,chat_name)
        # chat.show()
        # chat.exec_()

    def renameItem(self):
        hituser = self.treeWidget.currentItem()
        uindex = self.searchuser(hituser)
        unewname, ok = QInputDialog.getText(self, '提示信息', '请输入备注名称')
        if ok:
            if len(unewname) == 0:
                QMessageBox.information(self, '提示', '备注名称不能为空哦')
            else:
                hituser.setText(0, unewname)
                self.userslist[uindex]['username'] = unewname

    def searchgroup(self, hitgroup):
        if isinstance(hitgroup, str):
            for i, g in enumerate(self.grouplist):
                if g['groupname'] == hitgroup:
                    return i
        else:
            for i, g in enumerate(self.grouplist):
                if g['group'] == hitgroup:
                    return i

    def searchuser(self, hituser):
        if isinstance(hituser, str):
            for i, u in enumerate(self.userslist):
                if u['username'] == hituser:
                    return i
        else:
            for i, u in enumerate(self.userslist):
                if u['user'] == hituser:
                    return i

    def searchicon(self, gpname2):
        if gpname2.find('好友') >= 0:
            return QIcon('./res/group/buddy.ico')
        elif gpname2.find('同事') >= 0:
            return QIcon('./res/group/partner.ico')
        elif gpname2.find('黑名单') >= 0:
            return QIcon('./res/group/blacklist.ico')
        else:
            return QIcon('./res/group/buddy_default.ico')

    def getListitems(self, flag=1):
        if flag > 0:
            return self.treeWidget.selectedItems()
        else:
            return self.tmpuseritem

    def restatistic(self, item, preitem):
        if item:
            fathergroup = item.parent()
            if fathergroup:
                self.restatistic_op(fathergroup)
            else:
                self.restatistic_op(item)
        elif preitem.parent().childCount() == 1:
            lastgroupname = preitem.parent().text(0).split()[0] + ' 0/0'
            preitem.parent().setText(0, lastgroupname)
            self.menuflag = 1

    def restatistic_op(self, itemorgroup):
        gindex = self.searchgroup(itemorgroup)
        totalcount = self.grouplist[gindex]['childcount']
        hidecount = self.grouplist[gindex]['childishide']
        fathergroupname = self.grouplist[gindex]['groupname']
        fathergroupname += ' ' + str(totalcount - hidecount) + '/' + str(totalcount)
        itemorgroup.setText(0, fathergroupname)

    def onUsernameChoosed(self, name):
        self.lineEdit.setText(name)

    @pyqtSlot()
    def on_bt_search_clicked(self):

        username = self.lineEdit.text()
        if len(username) > 0:
            useritemindex = self.searchuser(username)
            useritem = self.userslist[useritemindex]['user']
            self.treeWidget.setCurrentItem(useritem)

    @pyqtSlot()
    def on_bt_adduser_clicked(self):
        adduser = AddFriend()
        for g in self.grouplist:
            adduser.comboBox.addItem(g['groupname'])
        r = adduser.exec_()
        if r > 0:
            newitem = QTreeWidgetItem()
            newname = adduser.lineEdit.text()
            print('新增好友名',newname)
            newicon = adduser.geticonpath()
            font = QFont()
            font.setPointSize(16)
            newitem.setFont(0, font)
            newitem.setText(0, newname)
            newitem.setTextAlignment(0, Qt.AlignHCenter | Qt.AlignVCenter)
            newitem.setIcon(0, QIcon(newicon))
            comboxinfo = adduser.comboBox.currentText()
            cindex = self.searchgroup(comboxinfo)
            group = self.grouplist[cindex]['group']
            group_name = self.grouplist[cindex]['groupname']
            print('选择分组为',group_name)
            result = main.add_friend(self.Id,newname,group_name)
            if result == "NoId":
                print(QMessageBox.information(loginWindow, "提示", "该账号不存在!", QMessageBox.Yes, QMessageBox.Yes))
                return
            self.grouplist[cindex]['childcount'] += 1
            userdic = {'user': newitem, 'username': newname, 'ishide': 0}
            self.userslist.append(userdic)
            group.addChild(newitem)
            self.treeWidget.setCurrentItem(newitem)

    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        namelist = []

        for itm in self.userslist:
            username = itm['username']
            if username.find(text) >= 0:
                namelist.append(itm['username'])
        self.m_model.removeRows(0, self.m_model.rowCount())

        for i in range(0, len(namelist)):
            self.m_model.insertRow(0)
            self.m_model.setData(self.m_model.index(0, 0), namelist[i])

# class friend_Widget(QDialog,QToolBox):
#     def __init__(self,L):
#         super(friend_Widget, self).__init__()
#         # self.resize(200, 600)
#         self.setWindowTitle("好友列表")
#         self.L = L
#         self.setupUi()
#
#     def setupUi(self):
#         self.resize(300, 600)
#         print(self.L)
#         vbox = QVBoxLayout()  # QVBoxLayout 类将各部件垂直排列
#         vbox.setContentsMargins(10,10,10,10)
#         vbox.setAlignment(Qt.AlignTop)
#         self.group = QLabel("我的好友")
#         vbox.addWidget(self.group)
#         for i in self.L:
#             exec("menu_%s = QMenu()" % i)
#             exec("m_addaction_%s = QAction(menu_%s)" % (i,i))
#             exec("m_chataction_%s = QAction(menu_%s)" % (i,i))
#             exec('''m_addaction_%s.setText('删除好友"%s"')''' % (i,i))
#             exec("m_chataction_%s.setText('聊天')" % i)
#             exec("menu_%s.addAction(m_addaction_%s)" % (i,i))
#             exec("menu_%s.addAction(m_chataction_%s)" % (i,i))
#             exec("m_addaction_%s.triggered.connect(lambda: main.delete_friends('%s'))" % (i,i))
#             exec("m_chataction_%s.triggered.connect(lambda: main.chat_show('%s'))" % (i,i))
#             if i == '':
#                 continue
#             self.i = QPushButton("%s" % i)
#             exec("self.i.setMenu(menu_%s)" % i)
#             vbox.addWidget(self.i)  # 主窗口动态加载
#             # QApplication.processEvents()
#         self.add = QPushButton("+")
#         self.add.setStyleSheet("font-size:30px")
#         vbox.addWidget(self.add)
#         self.setLayout(vbox)  # 布局
#         self.add.clicked.connect(self.do_add)
#
#     def do_add(self):
#         value, ok = QInputDialog.getText(self, "添加好友", "请输入好友ID账号:", QLineEdit.Normal,'')
#         if value == '':
#             print(QMessageBox.warning(registWindow, "警告", "好友ID不可为空，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
#         elif value != '':
#             main.add_friends(value)

#主执行函数
class do_main():
    def __init__(self,s,addr,chat):
        self.s = s
        self.addr = addr
        self.chat = chat
    def do_child(self):
        print('start')
        loginWindow.lineEdit2.returnPressed.connect(self.signInCheck)
        loginWindow.lineEdit1.returnPressed.connect(self.signInCheck)
        loginWindow.signIn.clicked.connect(self.signInCheck)
        registWindow.signUpbutton.clicked.connect(self.SignUp)
        registWindow.IdLineEdit.returnPressed.connect(self.SignUp)
        registWindow.NameLineEdit.returnPressed.connect(self.SignUp)
        registWindow.passwordLineEdit.returnPressed.connect(self.SignUp)
        registWindow.passwordConfirmLineEdit.returnPressed.connect(self.SignUp)

    # 注册函数
    def SignUp(self):
        print('进入注册')
        Id = registWindow.IdLineEdit.text()
        Name = registWindow.NameLineEdit.text()
        Password = registWindow.passwordLineEdit.text()
        confirmPassword = registWindow.passwordConfirmLineEdit.text()
        print(Id,Name,Password)
        registmsg = 'R' + ' ' + Id + ' ' + Name + ' ' + Password + ' ' + confirmPassword
        self.s.sendto(registmsg.encode(),self.addr)
        print("等待收答复")
        regist_return,addr = self.s.recvfrom(1024)
        msg = regist_return.decode()
        if msg == 'None':
            print(QMessageBox.warning(registWindow, "警告", "表单不可为空，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
        elif msg == 'Noconfirm':
            print(QMessageBox.warning(registWindow, "警告", "两次输入密码不一致，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
        elif msg == 'Succsess':
            print(QMessageBox.information(registWindow, "提醒", "您已成功注册账号!", QMessageBox.Yes, QMessageBox.Yes))
        elif msg == 'Exist':
            print(QMessageBox.warning(registWindow, "警告", "该账号已存在,请重新输入", QMessageBox.Yes, QMessageBox.Yes))

    # 登录函数
    def signInCheck(self):
        Id = loginWindow.lineEdit1.text()
        password = loginWindow.lineEdit2.text()
        loginmsg = "L" + ' ' + Id + ' ' + password
        self.s.sendto(loginmsg.encode(),self.addr)
        login_return,addr = self.s.recvfrom(1024)
        msg = login_return.decode()
        if msg == 'None':
            print(QMessageBox.warning(loginWindow, "警告", "账号和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes))
        elif msg == 'Noexist':
            print(QMessageBox.information(loginWindow, "提示", "该账号不存在!", QMessageBox.Yes, QMessageBox.Yes))
        elif msg == 'Succsess':
            address = '172.40.71.116'
            port = 8888
            addr = (address, port)
            chat_socket = socket(AF_INET, SOCK_DGRAM)
            msg = "RC" + ' ' + Id + ' ' + '准备聊天'
            chat_socket.sendto(msg.encode(), addr)
            # self.get_friend_info(Id)
            loginWindow.hide()
            self.receive_child(chat_socket, Id)
            friend_show1 = FriendList(self.s,Id,chat_socket)
            friend_show1.show()
            friend_show1.exec_()
        elif msg == 'Uncorrect':
            print(QMessageBox.information(loginWindow, "提示", "密码错误!", QMessageBox.Yes, QMessageBox.Yes))

    # 好友列表
    # def get_friend_info(self,Id):
    #     friend_msg = 'F' + ' ' + Id
    #     self.s.sendto(friend_msg.encode(),self.addr)
    #     msg_return,addr = self.s.recvfrom(1024)
    #     print(msg_return.decode())
    #     self.L = msg_return.decode().split(' ')
    #     return L
        # friend_show = friend_Widget(L)
        # friend_show.show()

    def request_group(self,Id):
        print(Id,'准备向服务器发送分组请求')
        group_msg = 'G' + ' ' + Id
        self.s.sendto(group_msg.encode(),self.addr)
        msg_return,addr = self.s.recvfrom(1024)
        print(msg_return.decode())
        group_list = msg_return.decode().split(' ')
        for i in group_list:
            if i == '':
                group_list.remove(i)
        return group_list

    def get_group_friend(self,Id,groupname):
        print(Id,'准备向服务器发送分组请求')
        friend_msg = 'F' + ' ' + Id + ' ' + groupname
        self.s.sendto(friend_msg.encode(),self.addr)
        msg_return,addr = self.s.recvfrom(1024)
        print(msg_return.decode())
        friend_list = msg_return.decode().split(' ')
        for i in friend_list:
            if i == '':
                friend_list.remove(i)
        print(friend_list)
        return friend_list

    def is_hider(self,name):
        print('查看',name,'是否在线')
        is_online = 'Online' + ' ' + name
        self.s.sendto(is_online.encode(),self.addr)
        msg_return,addr = self.s.recvfrom(1024)
        print(msg_return.decode())
        return int(msg_return.decode())

    def add_group(self,Id,groupname):
        print('给',Id,'添加分组',groupname)
        add_group_msg = 'AG' + ' ' + Id + ' ' + groupname
        self.s.sendto(add_group_msg.encode(),self.addr)
        msg,addr = self.s.recvfrom(1024)
        print(msg.decode())

    def rename_group(self,Id,old_group_name,new_group_name):
        print('重命名',Id,'的',old_group_name,'分组为',new_group_name)
        rename_group_msg = 'RG' + ' ' + Id + ' ' + old_group_name + ' ' + new_group_name
        self.s.sendto(rename_group_msg.encode(),self.addr)
        msg,addr = self.s.recvfrom(1024)
        print(msg.decode())

    def delete_group(self,Id,group_name):
        print('删除',Id,'的',group_name,'分组')
        delete_group_msg = 'DG' + ' ' + Id + ' ' + group_name
        self.s.sendto(delete_group_msg.encode(),self.addr)
        msg,addr = self.s.recvfrom(1024)
        print(msg.decode())

    def delete_friend(self,Id,friend_name):
        print('删除',Id,'的好友',friend_name)
        delete_friend_msg = 'DF' + ' ' + Id + ' ' + friend_name
        self.s.sendto(delete_friend_msg.encode(),self.addr)
        msg,addr = self.s.recvfrom(1024)
        print(msg.decode())

    def add_friend(self,Id,friend_name,group_name):
        print('给',Id,'添加',friend_name,'好友到',group_name)
        add_friend_msg = 'AF' + ' ' + Id + ' ' + friend_name + ' ' + group_name
        self.s.sendto(add_friend_msg.encode(),self.addr)
        msg,addr = self.s.recvfrom(1024)
        if msg.decode() == "NoId":
            return "NoId"
        else:
            print(msg.decode())


    # 添加好友
    # def add_friends(self,friend_name):
    #     print('加好友',friend_name)
    #     friend_add_msg = 'A' + ' ' + friend_name
    #     self.s.sendto(friend_add_msg.encode(),self.addr)
    #     add_return,addr = self.s.recvfrom(1024)
    #     s = add_return.decode().split(' ')
    #     if s[0] == 'NoId':
    #         print(QMessageBox.information(loginWindow, "提示", "该账号不存在!", QMessageBox.Yes, QMessageBox.Yes))
    #     elif s[0] == 'Succ':
    #         print(QMessageBox.information(loginWindow, "提示", "添加好友成功!", QMessageBox.Yes, QMessageBox.Yes))
    #         print(s[1])
    #         self.friend_list(s[1])
    #         friend_show2 = TIM(self.L)
    #         friend_show2.show()
    #         friend_show2.exec_()
    #
    #     elif s[0] == 'Exsit':
    #         print(QMessageBox.information(loginWindow, "提示", "此用户已是您的好友", QMessageBox.Yes, QMessageBox.Yes))

    # 删除好友
    # def delete_friends(self,friend_name):
    #     print(friend_name)
    #     friend_delete_msg = 'D' + ' ' + friend_name
    #     self.s.sendto(friend_delete_msg.encode(),self.addr)
    #     delete_return,addr = self.s.recvfrom(1024)
    #     s = delete_return.decode().split(' ')
    #     print(s)
    #     self.friend_list(s[1])
    #     friend_show = friend_Widget(self.L)
    #     friend_show.show()
    #     friend_show.exec_()

    def chat_show(self,friend_name,Id,chat_socket):
        print(friend_name)
        chatWindow = chatWidget(self.s,friend_name,Id,chat_socket)
        print('显示聊天界面')
        self.chat.add(chatWindow)
        chatWindow.show()
        chatWindow.exec_()

    def chat_send(self,friend_name,chatdata,chat_socket):
        chatmsg = 'C' + ' ' + friend_name + ' ' + chatdata
        print(chatmsg)
        chat_socket.sendto(chatmsg.encode(),self.addr)
        # msg,addr = self.s.recvfrom(1024)
        # msgreturn = msg.decode()
        # if msgreturn == 'NoOnline':
        #     print(QMessageBox.information(loginWindow, "提示", "该用户不在线", QMessageBox.Yes, QMessageBox.Yes))
        # elif msgreturn[0:4] == 'Succ':
        #     msg_to_friends = msgreturn[4:len(msgreturn)]

    def AddGroupChat(self,Id,group_chat_name):
        addmsg = "AGC" + ' ' + Id + ' ' + group_chat_name
        self.s.sendto(addmsg.encode(),self.addr)
        msg,addr = self.s.recvfrom(1024)
        print(msg.decode())

    def request_group_chat(self,Id):
        remsg = "RGC" + ' ' + Id
        self.s.sendto(remsg.encode(),self.addr)
        msg,addr = self.s.recvfrom(1024)
        msg_back = msg.decode()
        group_chat_list = msg_back.split(' ')
        for i in group_chat_list:
            if i == '':
                group_chat_list.remove(i)
        return group_chat_list

    def receive_child(self,chat_socket,Id):
        print('创建线程')
        t = Thread(target=self.receive_chat,args=(chat_socket,Id))
        t.start()
        # t.setDaemon(True)

    def receive_chat(self,chat_socket,Id):
        while True:
            msg,addr = chat_socket.recvfrom(1024)
            print('聊天的服务端地址为',addr)
            msgreturn = msg.decode()
            print(msgreturn)
            if msgreturn[0:8] == 'NoOnline':
                # friend_name = msgreturn[8:len(msgreturn)]
                # for chat_item in self.chat:
                #     print('发来好友名为',friend_name)
                #     print('打开的窗口名为',chat_item.windowTitle())
                #     window_title = chat_item.windowTitle().split(' ')
                #     if friend_name == window_title[1]:
                        pass

            elif msgreturn[0:4] == 'Succ' and msgreturn[0:5] != "SuccG":
                msg_to_friends = msgreturn[4:len(msgreturn)]
                L = msg_to_friends.split(" ")
                friend_name = L[0]
                for chat_item in self.chat:
                    print('私聊发来好友名为',friend_name)
                    print('私聊打开的窗口名为',chat_item.windowTitle())
                    window_title = chat_item.windowTitle().split(' ')
                    if friend_name == window_title[1]:
                        msg = ' '.join(L[1:len(L) + 1])
                        print('要显示的消息', msg)
                        chat_item.chat_signal.emit(msg,friend_name)
                        break
            elif msgreturn[0:5] == 'SuccG':
                print('收到群聊消息',msgreturn)
                msg_to_friends = msgreturn[5:len(msgreturn)]
                L = msg_to_friends.split(" ")
                friend_name = L[1]
                send_from_Id = L[0]
                print('要显示的群聊为',friend_name)
                paixu = friend_name.split(',')
                paixu.remove('的群聊')
                paixu.sort()
                to_group_name = ','.join(paixu) + ',的群聊'
                print('要显示的窗口为',to_group_name)
                for chat_item in self.chat:
                    window_title = chat_item.windowTitle().split(' ')
                    print('目前的窗口',window_title)
                    if to_group_name == window_title[1]:
                        print('已有的群聊窗口',to_group_name)
                        msg = L[2]
                        print('要显示的消息', msg)
                        chat_item.chat_signal.emit(msg,send_from_Id)
                        break
            else:
                pass


if __name__ == "__main__":
    chat = set()
    address = '172.40.71.116'
    port = 8888
    addr = (address,port)
    s = socket(AF_INET,SOCK_DGRAM)
    app = QApplication(sys.argv)
    loginWindow = SignInWidget()
    registWindow = SignUpWidget()
    # chatWindow = chatWidget()
    # friend_show = friend_Widget(s,addr)
    loginWindow.signUp.clicked.connect(loginWindow.signup_show)
    registWindow.gobackbutton.clicked.connect(registWindow.goback)
    loginWindow.show()
    main = do_main(s,addr,chat)
    main.do_child()
    # friend_show = friend_Widget(L)
    sys.exit(app.exec_())