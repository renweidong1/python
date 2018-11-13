#! -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_untitled import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import urllib.request
import time,os,random
from ffpyplayer.player import MediaPlayer
from mutagen.mp3 import MP3
import ssl,json,playsound
from aip import *

class Timing(QtCore.QThread):
    def __init__(self, parent=None):
        super(Timing, self).__init__(parent)

    def run(self):
        while True:
            a = time.time()
            b = time.localtime(a)
            if b[3] == 13 and b[4] == 55 and b[5] == 0:
                music = []
                path = r".\\music"
                for i in os.listdir(path):
                    music.append(i)    
                rmusic = random.randint(1,len(music)-1)
                random_music = music[rmusic]
                audio = MP3(path+"\\"+str(random_music))
                timelength = audio.info.length
                player = MediaPlayer(path+"\\"+str(random_music))
                time.sleep(timelength)
                continue
            elif b[3] == 20 and b[4] == 30 and b[5] == 0:
                time.sleep(3)
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
                        (res['date'][0:4],res['date'][5],res['date'][6:8],\
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
                else:
                    print(result)
                playsound.playsound("D://audio.mp3")
                continue

