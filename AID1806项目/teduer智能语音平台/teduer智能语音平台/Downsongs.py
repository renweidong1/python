# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_untitled import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import urllib.request
import time,os,random
from ffpyplayer.player import MediaPlayer
from mutagen.mp3 import MP3
from download import *


class Down(QtCore.QThread):
    def __init__(self, parent=None):
        super(Down, self).__init__(parent)

    def run(self):
        page_url = 'http://fm.baidu.com/dev/api/?tn=channellist'
        channel_list = get_channel_list(page_url)
        count = 0
        while count < 30:
            channel_url = 'http://fm.baidu.com/dev/api/?tn=playlist&format=json&id=%s' % 'public_tuijian_rege'
            song_id_list = get_song_list(channel_url)
            song_info_list = []
            for song_id in song_id_list:
                song_url = "http://music.baidu.com/data/music/fmlink?type=mp3&rate=320&songIds=%s" % song_id['id']
                song_name, song_link, song_size = get_song_real_url(song_url)
                if song_size != 0:
                    donwn_mp3_by_link(song_link, song_name, song_size)
                    QApplication:processEvents()
                    count +=1
                    if count == 30:
                        break