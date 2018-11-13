#!/usr/bin/env python 
# -*- coding:utf-8 -*-


# @Group：五人小队
# @Description: 实现客户端的语音朗读。
import win32com.client
import time

class Speaker(object):
    def __init__(self):
        self.engine = win32com.client.Dispatch("SAPI.SpVoice")

    def speak(self, text):

        self.engine.Speak(text)



if __name__ == '__main__':
    Speaker()
    # speaker = Speaker()
    # speaker.speak("Hello Python")