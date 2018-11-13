import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import *

from audioui import clientUI


class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

    def setupUi(self, MainWindow):
        screen = QDesktopWidget().screenGeometry()
        size = MainWindow.geometry()
        self.move(screen.width()-size.width(), 0)
        # MainWindow.setGeometry(791, 293, 350, 500)
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(250, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(250, 500))
        MainWindow.setMaximumSize(QtCore.QSize(250, 500))
        MainWindow.setWindowIcon(QIcon('./static/images/cortana.png'))
        palette = QtGui.QPalette()
        palette.setBrush(MainWindow.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./static/images/bk3.jpg')))
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setObjectName("splitter")
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我的地盘"))

class MyPlace(QMainWindow, Ui_MainWindow,clientUI):
    def __init__(self):
        super(MyPlace, self).__init__()

        # # 主窗口初始化时实现主窗口布局
        self.setupUi(self)


        # 实例化QToolBox
        self.toolBox = QToolBox()

        # 给QToolBox添加子项目；添加了4个子项目
        self.groupbox1 = QGroupBox()
        self.groupbox2 = QGroupBox()
        self.groupbox3 = QGroupBox()
        self.groupbox4 = QGroupBox()
        self.toolBox.addItem(self.groupbox4,QIcon('./static/images/cortana.png'), "Cortana智能聊天")
        self.toolBox.addItem(self.groupbox1,QIcon('./static/images/ss.jpg'), "搜索引擎")
        self.toolBox.addItem(self.groupbox2, QIcon('./static/images/sp.jpg'),"视频网站")
        self.toolBox.addItem(self.groupbox3, QIcon('./static/images/study.jpg'),"学习天地")

        self.toolBox.setCurrentIndex(0)  # 设置软件启动时默认打开导航栏的第几个 Item；这里设置的是打开第1个 Item。

        # 给QSsplitter添加第一个窗体（QToolBox）
        self.splitter.addWidget(self.toolBox)

        # QToolBox 的 QToolBoxButton 按钮切换时发出的信号；也是信号与槽的连接
        # self.toolBox.currentChanged.connect(self.mylinktowindows)
        self.toolBox.currentChanged.connect(self.Cortana)
        self.toolBox.currentChanged.connect(self.Sousuo)
        self.toolBox.currentChanged.connect(self.Shipin)
        self.toolBox.currentChanged.connect(self.Study)

    def Cortana(self):
        vlayout = QVBoxLayout(self.groupbox4)
        vlayout.setAlignment(Qt.AlignCenter)
        toolButton1 = QToolButton()
        toolButton1.setText("Cortana")
        toolButton1.setIcon(QIcon("./static/images/cortana.ico"))
        toolButton1.setIconSize(QSize(64, 64))
        toolButton1.setAutoRaise(True)
        toolButton1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        vlayout.addWidget(toolButton1)
        toolButton1.clicked.connect(self.Jqr)

        toolButton2 = QToolButton()
        toolButton2.setText("Video")
        toolButton2.setIcon(QIcon("./static/images/video.ico"))
        toolButton2.setIconSize(QSize(64, 64))
        toolButton2.setAutoRaise(True)
        toolButton2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        vlayout.addWidget(toolButton2)
        toolButton2.clicked.connect(self.Video)

    def Jqr(self):
        if self.sender().text() == 'Cortana':
            self.clientWindow = clientUI()
            self.clientWindow.show()

    def Video(self):
        pass

    def Sousuo(self):
        favorites = [
                {'des': '百度搜索', 'pic': './static/images/baidu.ico'},
                {'des': '搜狗搜索', 'pic': './static/images/sogou.ico'},
                {'des': '必应搜索', 'pic': './static/images/bing.ico'},
                {'des': '360搜索', 'pic': './static/images/360.ico'},
                {'des': '谷歌搜索', 'pic': './static/images/google.ico'},
                {'des': '雅虎搜索', 'pic': './static/images/yahoo.ico'}
            ]

        vlayout = QVBoxLayout(self.groupbox1)
        vlayout.setAlignment(Qt.AlignCenter)
        for category in favorites:
            toolButton = QToolButton()
            toolButton.setText(category['des'])
            toolButton.setIcon(QIcon(category['pic']))
            toolButton.setIconSize(QSize(64, 64))
            toolButton.setAutoRaise(True)
            toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            vlayout.addWidget(toolButton)
            toolButton.clicked.connect(self.run)

    def Shipin(self):
        favorites = [
                {'des': '腾讯视频', 'pic': './static/images/tx.ico'},
                {'des': '搜狐视频', 'pic': './static/images/souhu.ico'},
                {'des': '优酷视频', 'pic': './static/images/youku.ico'},
                {'des': '土豆视频', 'pic': './static/images/tudou.ico'},
                {'des': '哔哩哔哩', 'pic': './static/images/bilibili.ico'}
            ]

        vlayout = QVBoxLayout(self.groupbox2)
        vlayout.setAlignment(Qt.AlignCenter)
        for category in favorites:
            toolButton = QToolButton()
            toolButton.setText(category['des'])
            toolButton.setIcon(QIcon(category['pic']))
            toolButton.setIconSize(QSize(64, 64))
            toolButton.setAutoRaise(True)
            toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            vlayout.addWidget(toolButton)
            toolButton.clicked.connect(self.run)

    def Study(self):
        favorites = [
                {'des': 'CSDN', 'pic': './static/images/csdn.ico'},
                {'des': '开源中国', 'pic': './static/images/oschina.ico'},
                {'des': '博客园', 'pic': './static/images/cnblogs.ico'},
                {'des': '知乎', 'pic': './static/images/zhihu.ico'},
                {'des': 'GitHub', 'pic': './static/images/github.ico'},
                {'des': '慕课网', 'pic': './static/images/imooc.ico'},
                {'des': 'V2EX', 'pic': './static/images/v2ex.ico'},
                {'des': '程序员客栈', 'pic': './static/images/proginn.ico'}
            ]

        vlayout = QVBoxLayout(self.groupbox3)
        vlayout.setAlignment(Qt.AlignCenter)
        for category in favorites:
            toolButton = QToolButton()
            toolButton.setText(category['des'])
            toolButton.setIcon(QIcon(category['pic']))
            toolButton.setIconSize(QSize(64, 64))
            toolButton.setAutoRaise(True)
            toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            vlayout.addWidget(toolButton)
            toolButton.clicked.connect(self.run)

    def run(self):
        if self.sender().text() == '百度搜索':
            webbrowser.open('https://www.baidu.com')
        elif self.sender().text() == '搜狗搜索':
            webbrowser.open('https://www.sogou.com/')
        elif self.sender().text() == '必应搜索':
            webbrowser.open('http://cn.bing.com/')
        elif self.sender().text() == '360搜索':
            webbrowser.open('https://www.so.com/')
        elif self.sender().text() == '谷歌搜索':
            webbrowser.open('https://www.google.com/')
        elif self.sender().text() == '雅虎搜索':
            webbrowser.open('https://www.yahoo.com/')
        elif self.sender().text() == '腾讯视频':
            webbrowser.open('https://v.qq.com/')
        elif self.sender().text() == '搜狐视频':
            webbrowser.open('https://film.sohu.com')
        elif self.sender().text() == '优酷视频':
            webbrowser.open('http://www.youku.com/')
        elif self.sender().text() == '土豆视频':
            webbrowser.open('http://www.tudou.com/')
        elif self.sender().text() == '哔哩哔哩':
            webbrowser.open('https://www.bilibili.com/')
        elif self.sender().text() == 'CSDN':
            webbrowser.open('http://www.csdn.net/')
        elif self.sender().text() == '开源中国':
            webbrowser.open('http://www.oschina.net/')
        elif self.sender().text() == '博客园':
            webbrowser.open('https://www.cnblogs.com/')
        elif self.sender().text() == '知乎':
            webbrowser.open('http://www.zhihu.com/')
        elif self.sender().text() == 'GitHub':
            webbrowser.open('https://github.com/')
        elif self.sender().text() == '慕课网':
            webbrowser.open('https://www.imooc.com/')
        elif self.sender().text() == 'V2EX':
            webbrowser.open('http://www.v2ex.com/')
        elif self.sender().text() == '程序员客栈':
            webbrowser.open('http://www.proginn.com')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myplace = MyPlace()
    myplace.show()
    sys.exit(app.exec_())

