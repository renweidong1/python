#!/usr/bin/env python 
# -*- coding:utf-8 -*-


# @Group：五人小队
# @Description: 图灵机器人文字对话接口，借用图灵机器人实现智能机器人功能
# 图灵官网：http://www.tuling123.com/
# 以下apikey 为‘五人小队’ 使用，非公用api
# 接入教程请参考：https://www.kancloud.cn/turing/www-tuling123-com/718227
import requests
import json

class TuringRobot(object):

    # 智能机器人的相关url,key,用户id
    def __init__(self):
        self.apikey = 'e02ebae04f114fd2ae6ee3bfa3433fbc'
        self.userid = '11782354'
        self.url = 'http://www.tuling123.com/openapi/api'
        self.city = '北京'

    # 接入信息参照 https://www.kancloud.cn/turing/www-tuling123-com/718227
    def talk(self, text):
        payload = {
            'key': self.apikey,
            'userid': self.userid,
            'info': text
        }

        # 向机器人发送格式为 JSON 的 POST 数据，接收返回的信息
        response = requests.post(url=self.url, data=payload)
        # 提取返回的文本信息
        return json.loads(response.text)['text']


if __name__ == '__main__':
    turingrobot = TuringRobot()
