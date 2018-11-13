# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys
import time
from winchat import *
from winadder import *
import requests

cities = {'北京': '101010100', '上海': '101020100', '天津': '101030100', '重庆': '101040100', '哈尔滨': '101050101', '齐齐哈尔': '101050201', '牡丹江': '101050301', '佳木斯': '101050401', '绥化': '101050501', '黑河': '101050601', '大兴安岭': '101050701', '伊春': '101050801', '大庆': '101050901', '鸡西': '101051101', '鹤岗': '101051201', '双鸭山': '101051301', '长春': '101060101', '吉林': '101060201', '延吉': '101060301', '四平': '101060401', '通化': '101060501', '白城': '101060601', '辽源': '101060701', '松原': '101060801', '白山': '101060901', '沈阳': '101070101', '大连': '101070201', '鞍山': '101070301', '抚顺': '101070401', '本溪': '101070501', '丹东': '101070601', '锦州': '101070701', '营口': '101070801', '阜新': '101070901', '辽阳': '101071001', '铁岭': '101071101', '朝阳': '101071201', '盘锦': '101071301', '葫芦岛': '101071401', '呼和浩特': '101080101', '包头': '101080201', '乌海': '101080301', '集宁': '101080401', '通辽': '101080501', '赤峰': '101080601', '鄂尔多斯': '101080701', '临河': '101080801', '锡林浩特': '101080901', '呼伦贝尔': '101081000', '海拉尔': '101081001', '乌兰浩特': '101081101', '阿拉善左旗': '101081201', '石家庄': '101090101', '保定': '101090201', '张家口': '101090301', '唐山': '101090501', '廊坊': '101090601', '沧州': '101090701', '衡水': '101090801', '邢台': '101090901', '邯郸': '101091001', '秦皇岛': '101091101', '太原': '101100101', '大同': '101100201', '阳泉': '101100301', '晋中': '101100401', '长治': '101100501', '晋城': '101100601', '临汾': '101100701', '运城': '101100801', '朔州': '101100901', '忻州': '101101001', '吕梁': '101101100', '离石': '101101101', '西安': '101110101', '咸阳': '101110200', '三原': '101110201', '延安': '101110300', '延长': '101110301', '榆林': '101110401', '渭南': '101110501', '商洛': '101110601', '安康': '101110701', '汉中': '101110801', '宝鸡': '101110901', '铜川': '101111001', '济南': '101120101', '青岛': '101120201', '淄博': '101120301', '德州': '101120401', '烟台': '101120501', '潍坊': '101120601', '济宁': '101120701', '泰安': '101120801', '临沂': '101120901', '菏泽': '101121001', '滨州': '101121101', '东营': '101121201', '威海': '101121301', '枣庄': '101121401', '日照': '101121501', '莱芜': '101121601', '聊城': '101121701', '乌鲁木齐': '101130101', '克拉玛依': '101130201', '石河子': '101130301', '昌吉': '101130401', '吐鲁番': '101130501', '库尔勒': '101130601', '阿拉尔': '101130701', '阿克苏': '101130801', '喀什': '101130901', '伊宁': '101131001', '塔城': '101131101', '哈密': '101131201', '和田': '101131301', '阿勒泰': '101131401', '阿图什': '101131501', '博乐': '101131601', '拉萨': '101140101', '日喀则': '101140201', '山南': '101140301', '林芝': '101140401', '昌都': '101140501', '那曲': '101140601', '阿里': '101140701', '西宁': '101150101', '海东': '101150201', '黄南': '101150301', '海南': '101150401', '果洛': '101150501', '玉树': '101150601', '海西': '101150701', '海北': '101150801', '兰州': '101160101', '定西': '101160201', '平凉': '101160301', '庆阳': '101160401', '武威': '101160501', '金昌': '101160601', '张掖': '101160701', '酒泉': '101160801', '天水': '101160901', '武都': '101161001', '临夏': '101161101', '合作': '101161201', '白银': '101161301', '银川': '101170101', '石嘴山': '101170201', '吴忠': '101170301', '固原': '101170401', '中卫': '101170501', '郑州': '101180101', '安阳': '101180201', '新乡': '101180301', '许昌': '101180401', '平顶山': '101180501', '信阳': '101180601', '南阳': '101180701', '开封': '101180801', '洛阳': '101180901', '商丘': '101181001', '焦作': '101181101', '鹤壁': '101181201', '濮阳': '101181301', '周口': '101181401', '漯河': '101181501', '驻马店': '101181601', '三门峡': '101181701', '济源': '101181801', '南京': '101190101', '无锡': '101190201', '镇江': '101190301', '苏州': '101190401', '南通': '101190501', '扬州': '101190601', '盐城': '101190701', '徐州': '101190801', '淮安': '101190901',
          '连云港': '101191001', '常州': '101191101', '泰州': '101191201', '宿迁': '101191301', '武汉': '101200101', '襄樊': '101200201', '鄂州': '101200301', '孝感': '101200401', '黄冈': '101200501', '黄石': '101200601', '咸宁': '101200701', '荆州': '101200801', '宜昌': '101200901', '恩施': '101201001', '十堰': '101201101', '神农架': '101201201', '随州': '101201301', '荆门': '101201401', '天门': '101201501', '仙桃': '101201601', '潜江': '101201701', '杭州': '101210101', '湖州': '101210201', '嘉兴': '101210301', '宁波': '101210401', '绍兴': '101210501', '台州': '101210601', '温州': '101210701', '丽水': '101210801', '金华': '101210901', '衢州': '101211001', '舟山': '101211101', '合肥': '101220101', '蚌埠': '101220201', '芜湖': '101220301', '淮南': '101220401', '马鞍山': '101220501', '安庆': '101220601', '宿州': '101220701', '阜阳': '101220801', '亳州': '101220901', '黄山站': '101221001', '滁州': '101221101', '淮北': '101221201', '铜陵': '101221301', '宣城': '101221401', '六安': '101221501', '巢湖': '101221601', '池州': '101221701', '福州': '101230101', '厦门': '101230201', '宁德': '101230301', '莆田': '101230401', '泉州': '101230501', '漳州': '101230601', '龙岩': '101230701', '三明': '101230801', '南平': '101230901', '南昌': '101240101', '九江': '101240201', '上饶': '101240301', '抚州': '101240401', '宜春': '101240501', '吉安': '101240601', '赣州': '101240701', '景德镇': '101240801', '萍乡': '101240901', '新余': '101241001', '鹰潭': '101241101', '长沙': '101250101', '湘潭': '101250201', '株洲': '101250301', '衡阳': '101250401', '郴州': '101250501', '常德': '101250601', '益阳': '101250700', '赫山区': '101250701', '娄底': '101250801', '邵阳': '101250901', '岳阳': '101251001', '张家界': '101251101', '怀化': '101251201', '黔阳': '101251301', '永州': '101251401', '吉首': '101251501', '贵阳': '101260101', '遵义': '101260201', '安顺': '101260301', '都匀': '101260401', '凯里': '101260501', '铜仁': '101260601', '毕节': '101260701', '六盘水': '101260801', '黔西': '101260901', '成都': '101270101', '攀枝花': '101270201', '自贡': '101270301', '绵阳': '101270401', '南充': '101270501', '达州': '101270601', '遂宁': '101270701', '广安': '101270801', '巴中': '101270901', '泸州': '101271001', '宜宾': '101271101', '内江': '101271201', '资阳': '101271301', '乐山': '101271401', '眉山': '101271501', '凉山': '101271601', '雅安': '101271701', '甘孜': '101271801', '阿坝': '101271901', '德阳': '101272001', '广元': '101272101', '广州': '101280101', '韶关': '101280201', '惠州': '101280301', '梅州': '101280401', '汕头': '101280501', '深圳': '101280601', '珠海': '101280701', '佛山': '101280800', '顺德': '101280801', '肇庆': '101280901', '湛江': '101281001', '江门': '101281101', '河源': '101281201', '清远': '101281301', '云浮': '101281401', '潮州': '101281501', '东莞': '101281601', '中山': '101281701', '阳江': '101281801', '揭阳': '101281901', '茂名': '101282001', '汕尾': '101282101', '昆明': '101290101', '大理': '101290201', '红河': '101290301', '曲靖': '101290401', '保山': '101290501', '文山': '101290601', '玉溪': '101290701', '楚雄': '101290801', '普洱': '101290901', '昭通': '101291001', '临沧': '101291101', '怒江': '101291201', '香格里拉': '101291301', '丽江': '101291401', '德宏': '101291501', '景洪': '101291601', '南宁': '101300101', '崇左': '101300201', '柳州': '101300301', '来宾': '101300401', '桂林': '101300501', '梧州': '101300601', '贺州': '101300701', '贵港': '101300801', '玉林': '101300901', '百色': '101301001', '钦州': '101301101', '河池': '101301201', '北海': '101301301', '防城港': '101301401', '海口': '101310101', '三亚': '101310201', '香港': '101320101', '澳门': '101330101', '台北县': '101340101', '高雄': '101340201', '台南': '101340301', '台中': '101340401', '桃园': '101340501', '新竹县': '101340601', '宜兰': '101340701', '马公': '101340801', '嘉义': '101340901'}


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
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("images/climb.jpg"),
        #                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # Form.setWindowIcon(icon)
        self.label_back = QtWidgets.QLabel(Form)
        self.label_back.setGeometry(QtCore.QRect(0, 0, 275, 700))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("images/guo2.jfif"))
        self.label_back.setObjectName("label_back")

        font1 = QtGui.QFont()
        font1.setFamily("Old English Text MT")
        font1.setPointSize(20)
        font1.setBold(False)
        # font1.setWeight(10)
        self.label_char = QtWidgets.QLabel(Form)
        self.label_char.setGeometry(QtCore.QRect(30, 5, 90, 35))
        self.label_char.setText("iClimb")
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
        self.label_close.linkActivated.connect(self.offline)
        self.label_close.setObjectName("label_close")
        self.label_close.setFont(font2)

        # self.label_profile = QtWidgets.QLabel(Form)
        # self.label_profile.setText("")
        # self.label_profile.setGeometry(QtCore.QRect(15, 35, 90, 90))
        # self.label_profile.setStyleSheet(
        #     r"border-image: url(:/pic/images/climb.jpg);")
        # self.label_profile.setPixmap(QtGui.QPixmap("./images/climb.jpg"))
        # self.label_profile.setObjectName("label_profile")
        self.textBrowser_weather = QtWidgets.QTextBrowser(Form)
        self.textBrowser_weather.setGeometry(QtCore.QRect(30, 40, 215, 80))
        self.textBrowser_weather.setObjectName("textBrowser_weather")
        self.textBrowser_weather.setStyleSheet(
            "background-color:rgba(255,255,255,0.5)")
        self.weatherComboBox = QtWidgets.QComboBox(Form)
        self.weatherComboBox.setGeometry(QtCore.QRect(30, 125, 215, 20))
        self.weatherComboBox.setObjectName("weatherComboBox")
        self.weatherComboBox.addItems(list(cities.keys()))
        self.weatherComboBox.currentIndexChanged.connect(self.queryWeather)

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
        self.pushButton_add.clicked.connect(self.adder)
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

    def adder(self):
        pass

    def offline(self):
        pass

    def queryWeather(self):
        print('* queryWeather  ')
        cityName = self.weatherComboBox.currentText()
        cityCode = cities[cityName]
        try:
            rep = requests.get(
                'http://www.weather.com.cn/data/sk/' + cityCode + '.html')
            rep.encoding = 'utf-8'
            print(rep.json())
            msg1 = '城市: %s' % rep.json()['weatherinfo']['city'] + '\n'
            msg2 = '风向: %s' % rep.json()['weatherinfo']['WD'] + '\n'
            msg3 = '温度: %s' % rep.json()['weatherinfo']['temp'] + ' 度' + '\n'
            msg4 = '风力: %s' % rep.json()['weatherinfo']['WS'] + '\n'
            msg5 = '湿度: %s' % rep.json()['weatherinfo']['SD'] + '\n'
            result = msg1 + msg2 + msg3 + msg4 + msg5
        except:
            result = '查询失败'
        self.textBrowser_weather.setText(result)


class MainWin(Main_1, QtWidgets.QWidget):

    def __init__(self, info_my, sockfd, addr, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.info_my = info_my
        # self.info_my[0][0] = info_my[0][0]
        self.s = sockfd
        self.to = addr
        # self.start_m(self.info_my)
        self.chat = {}
        self.thread = Receive(self.s)
        self.thread.sinOut.connect(self.chief)
        qssStytle1 = '''
        #Form{border-image:url(images/18.jpg)}
        #label_close,#label_mini{color:yellow; font:24px;text-align:center;}
        #label_close:hover{background-color:red}
        #label_mini:hover{background-color:gray}
        
    '''
        self.setStyleSheet(qssStytle1)

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

    def offline(self):
        data = "Q^^" + self.info_my[0][0] + "^^" + \
            self.info_my[0][1] + "^^" + "OFFLINE"
        self.s.sendto(data.encode(), self.to)
        self.close()

    def start_m(self, info_my):
        self.uname = info_my[0][0]
        for i in info_my[1]:
            item1 = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(r"images/" + info_my[1][i] + ".ico"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item1.setIcon(icon)
            item1.setText(i)
            self.listWidget_friends.addItem(item1)
            self.chat[i] = ChatWin(
                False, self.info_my[0][0], i, self.s, self.to)
            print(i)
        self.listWidget_friends.itemDoubleClicked.connect(self.chatting)
        for j in info_my[2]:
            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(r"images/群聊.jfif"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setText(j)
            self.listWidget_groups.addItem(item)
            self.chat[j] = ChatWin(
                True, self.info_my[0][0], j, self.s, self.to)
        self.listWidget_groups.itemDoubleClicked.connect(self.chatting)

    def chatting(self, item):
        self.chat[item.text()].show()
        itm = item
        self.listWidget_chatting.addItem(itm)

    def adder(self):
        self.adderw = Adder(self.info_my[0][0], self.s, self.to)
        self.adderw.show()

    def chief(self, info_str):
        print(info_str)
        rspns = info_str.split("^^")
        if rspns[0] == 'NF':
            if rspns[2] == self.uname:
                reply = QtWidgets.QMessageBox.information(self, "好友申请", rspns[
                    2] + "申请添加您为好友", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    data = "^^".join(rspns[0:2] + [self.uname] + ['YES'])
                elif reply == QMessageBox.No:
                    data = "^^".join(rspns[0:2] + [self.uname] + ['NO'])
                self.s.sendto(data.encode(), self.to)
            if rspns[1] == self.uname and rspns[3] == "YES":
                QtWidgets.QMessageBox.about(
                    self, "添加好友成功", rspns[2] + "通过了您的好友申请")
                item1 = QtWidgets.QListWidgetItem()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(r"images/" + rspns[4] + ".ico"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item1.setIcon(icon)
                item1.setText(rspns[2])
                self.listWidget_friends.addItem(item1)
            if rspns[1] == self.uname and rspns[3] == "NO":
                QtWidgets.QMessageBox.about(
                    self, "添加好友失败", rspns[2] + "拒绝了您的好友申请")
        elif rspns[0] == 'NG':
            if rspns[3] == self.uname and rspns[4] == "ask":
                reply = QtWidgets.QMessageBox.information(self, "申请加群", rspns[
                    1] + "申请加入群组" + rspns[2], QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    data = "^^".join(rspns[0:3] + [self.uname] + ['YES'])
                elif reply == QMessageBox.No:
                    data = "^^".join(rspns[0:3] + [self.uname] + ['NO'])
                self.s.sendto(data.encode(), self.to)
            if rspns[1] == self.uname and rspns[4] == "YES":
                QtWidgets.QMessageBox.about(
                    self, "加入群组成功", rspns[3] + "通过了您的加群申请")
            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(r"images/群聊.jfif"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setText(rspns[2])
            self.listWidget_groups.addItem(item)
            if rspns[1] == self.uname and rspns[4] == "NO":
                QtWidgets.QMessageBox.about(
                    self, "加入群组失败", rspns[3] + "拒绝了您的加群申请")
        elif rspns[0] == 'RG':
            if rspns[3] == "OK":
                QtWidgets.QMessageBox.about(self, "建群成功", "您已经是该群的群主")
            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(r"images/群聊.jfif"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setText(rspns[2])
            self.listWidget_groups.addItem(item)
            if rspns[1] == self.uname and rspns[4] == "NO":
                QtWidgets.QMessageBox.about(
                    self, "加入群组失败", rspns[3] + "拒绝了您的加群申请")
            elif rspns[3] == "EXIST":
                QtWidgets.QMessageBox.about(self, "建群失败", "该群名称已存在")

        elif rspns[0] == 'CF':
            if rspns[1] == self.uname and rspns[-1] == "OK":
                QtWidgets.QMessageBox.about(self, "发送成功", "消息接收人：" + rspns[2])
            if rspns[1] == self.uname and rspns[-1] == "OFFLINE":
                QtWidgets.QMessageBox.about(self, "对方不在线", "消息接收人：" + rspns[2])
            elif rspns[2] == self.uname:
                QtWidgets.QMessageBox.about(
                    self, "收到好友消息", "消息发送人：" + rspns[2])
                msg = "<p align:left>%s ：：： %s </p>" % (rspns[1], rspns[3])
                self.chat[rspns[1]].hist_body += msg
                self.chat[rspns[1]].hist = self.chat[
                    rspns[1]].hist_body + self.chat[rspns[1]].hist_tail
                self.chat[rspns[1]].textBrowser_display.setHtml(
                    self.chat[rspns[1]].hist)

        elif rspns[0] == 'CG':
            if rspns[1] == self.uname:
                QtWidgets.QMessageBox.about(self, "发送成功", "在线好友有：" + rspns[2])
            else:
                QtWidgets.QMessageBox.about(self, "收到群消息", "消息发送人：" + rspns[2])
                msg = "<p align:left>%s ：： %s </p>" % (rspns[1], rspns[3])
                self.chat[rspns[2]].hist_body += msg
                self.chat[rspns[2]].hist = self.chat[
                    rspns[2]].hist_body + self.chat[rspns[2]].hist_tail
                self.chat[rspns[2]].textBrowser_display.setHtml(
                    self.chat[rspns[2]].hist)


class Receive(Qt.QThread):
    sinOut = Qt.pyqtSignal(str)

    def __init__(self, sockfd, parent=None):
        super().__init__(parent)
        self.s = sockfd
        self.working = True

    def run(self):
        while self.working:
            data, addr = self.s.recvfrom(4096)
            print(data.decode())
            self.sinOut.emit(data.decode())


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)

    # mainw.show()
    # sys.exit(app.exec_())
