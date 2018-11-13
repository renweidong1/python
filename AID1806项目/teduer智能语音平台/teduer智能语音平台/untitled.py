# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_untitled import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import urllib.request
import time,ssl,json,os




class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):  
        ssl._create_default_https_context = ssl._create_unverified_context
        url = r"http://t.weather.sojson.com/api/weather/city/101010100"
        page = urllib.request.urlopen(url)
        html = page.read().decode("utf-8")
        res = json.loads(html)
        a = json.dumps(res, ensure_ascii=False, indent=4)
        res = json.loads(a)
        today = res['data']
        yesterday = today['yesterday']
        forcast = res['data']['forecast'][0]
        tomorrow = res['data']['forecast'][1]
        #实时天气
        self.textBrowser.append(res['date'])
        self.textBrowser_2.append(res['cityInfo']['parent'])
        self.textBrowser_3.append(today['wendu'])
        self.textBrowser_4.append(today['shidu'])
        self.textBrowser_5.append(today['quality'])
        # 今日天气
        self.textBrowser_15.append(forcast['date'])
        self.textBrowser_19.append(res['cityInfo']['parent'])
        self.textBrowser_16.append(forcast['high'])
        self.textBrowser_21.append(forcast['low'])
        self.textBrowser_20.append(forcast['fx'])
        self.textBrowser_14.append(forcast['fl'])
        self.textBrowser_17.append(forcast['type'])
        self.textBrowser_18.append(forcast['notice'])
        #明日预报
        self.textBrowser_6.append(tomorrow['date'])
        self.textBrowser_7.append(res['cityInfo']['parent'])
        self.textBrowser_8.append(tomorrow['high'])
        self.textBrowser_9.append(tomorrow['low'])
        self.textBrowser_12.append(tomorrow['fx'])
        self.textBrowser_13.append(tomorrow['fl'])
        self.textBrowser_10.append(tomorrow['type'])
        self.textBrowser_11.append(tomorrow['notice'])
        #昨日天气
        self.textBrowser_27.append(yesterday['date'])
        self.textBrowser_29.append(res['cityInfo']['parent'])
        self.textBrowser_23.append(yesterday['high'])
        self.textBrowser_22.append(yesterday['low'])
        self.textBrowser_28.append(yesterday['fx'])
        self.textBrowser_26.append(yesterday['fl'])
        self.textBrowser_25.append(yesterday['type'])
        self.textBrowser_24.append(yesterday['notice'])





    
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        #天气信息播放
        from whaterinfo import Playwhater
        #新建对象
        self.bwThread = Playwhater()
        #开始执行run()函数里的内容
        self.bwThread.start()      
    
    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        self.textBrowser.setText("")
        self.textBrowser_2.setText("")
        self.textBrowser_3.setText("")
        self.textBrowser_4.setText("")
        self.textBrowser_5.setText("")
        self.textBrowser_6.setText("")
        self.textBrowser_7.setText("")
        self.textBrowser_8.setText("")
        self.textBrowser_9.setText("")
        self.textBrowser_10.setText("")
        self.textBrowser_11.setText("")
        self.textBrowser_12.setText("")
        self.textBrowser_13.setText("")
        self.textBrowser_14.setText("")
        self.textBrowser_15.setText("")
        self.textBrowser_16.setText("")
        self.textBrowser_17.setText("")
        self.textBrowser_18.setText("")
        self.textBrowser_19.setText("")
        self.textBrowser_20.setText("")
        self.textBrowser_21.setText("")
        self.textBrowser_22.setText("")
        self.textBrowser_23.setText("")
        self.textBrowser_24.setText("")
        self.textBrowser_25.setText("")
        self.textBrowser_26.setText("")
        self.textBrowser_27.setText("")
        self.textBrowser_28.setText("")
        self.textBrowser_29.setText("")
  
    @pyqtSlot()
    def on_action_5_triggered(self):
        #更新曲库
        from Downsongs import Down
        #新建对象
        self.bwThread = Down()
        #开始执行run()函数里的内容
        self.bwThread.start()

    @pyqtSlot()
    def on_action_triggered(self):
        os.system("start explorer .\\music")
        #打开音乐文件夹

    @pyqtSlot()
    def on_action_9_triggered(self):
        #播放歌曲
        #import 自己的进程类
        from Play import Playsongs
        #新建对象
        self.bwThread = Playsongs()
        #开始执行run()函数里的内容
        self.bwThread.start()

    @pyqtSlot()
    def on_action_3_triggered(self):
        ui.on_pushButton_clicked()
        


    def timestart(self):
        from Timingplay import Timing
        #新建对象
        self.bwThread = Timing()
        #开始执行run()函数里的内容
        self.bwThread.start()

    @pyqtSlot()
    def on_action_10_triggered(self):
        sys.exit(0)


    @pyqtSlot()
    def on_action_20_triggered(self):
        my_button = QMessageBox.about(self,"使用说明",'此版本为V1.0版本,\n"查看天气"功能\n     1.实时天气查看\n     2.今日天气查看\n     3.昨日天气查看\n     4.明日天气查看\n     可查询"最高温度""最低温度""风向""风速""天气状况"等信息\n"天气信息播放"功能\n     可播放查询到的天气信息，默认播放当前温度及明日气温\n"清除天气信息"功能\n     可以清除界面查询到的天气信息\n"打开目录"功能\n     可以直接打开音乐存放目录\n"更新曲库"功能\n     更新歌曲库中歌曲，默认一次下载30首热门歌曲\n"循环播放"\n     自动随机循环播放曲库中的音乐\n"日历"功能\n     查看日历便于对比天气信息\n"定时"功能\n     本功能为后台默认功能,程序启动即运行,默认设定13:55播放一首歌曲,20:30播放天气信息')

    @pyqtSlot()
    def on_action_21_triggered(self):
        my_button = QMessageBox.about(self,"关于","此程序为中期项目,\n项目组员为：齐文宇,孙浩,侯智平\n尽管程序存在着些许小bug，但是在日后的学习过程中随着慢慢的积累会继续完善此系统,感谢各位组员的努力以及达内学院的帮助")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    ui.timestart()
    sys.exit(app.exec_())
    
