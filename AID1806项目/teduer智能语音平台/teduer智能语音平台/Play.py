# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_untitled import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import urllib.request
import time,os,random
from ffpyplayer.player import MediaPlayer
from mutagen.mp3 import MP3

class Playsongs(QtCore.QThread):
    def __init__(self, parent=None):
        super(Playsongs, self).__init__(parent)

    def run(self):
        music = []
        path = r".\\music"
        for i in os.listdir(path):
            music.append(i)
        while True:
            rmusic = random.randint(1,len(music)-1)
            random_music = music[rmusic]
            audio = MP3(path+"\\"+str(random_music))
            timelength = audio.info.length
            player = MediaPlayer(path+"\\"+str(random_music))
            time.sleep(timelength)
          
