# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_untitled import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import urllib.request
import time,ssl,json,playsound,os,random
from aip import *


class Playwhater(QtCore.QThread):
    def __init__(self, parent=None):
        super(Playwhater, self).__init__(parent)

    def run(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        url = r"http://t.weather.sojson.com/api/weather/city/101010100"
        page = urllib.request.urlopen(url)
        html = page.read().decode("utf-8")
        res = json.loads(html)
        a = json.dumps(res, ensure_ascii=False, indent=4)
        res = json.loads(a)
        today = res['data']
        tomorrow = res['data']['forecast'][1]
        text = "今天是%s年%s月%s日,\
                温度为%s度,当前湿度%s\
                ,空气质量%s,\
                \
                明天\
                温度为%s,气温%s\
                天气状况%s,温馨提示%s,今天的播报\
                就到这里,感谢大家的收听"%\
                (res['date'][0:4],res['date'][4:6],res['date'][6:8],\
                today['wendu'],today['shidu']\
                ,today['quality']\
                #明天天气播报
                ,tomorrow['high'],tomorrow['low']
                ,tomorrow['type'],tomorrow['notice'])
        APP_ID = "11687967"
        API_KEY = "GEjlCy7qc2yl9quEeVlscuPk"
        SECRET_KEY ="4u6nQpIDBVSVtqC4X2rb4IH8K1mQlxaB"
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        result = client.synthesis(text,options={'vol':15,"per":0,"spd":5})
        if not isinstance(result,dict):
            with open(r'D://audio.mp3','wb') as f:
                f.write(result)
        playsound.playsound("D://audio.mp3")
