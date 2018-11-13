# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import csv
import random
import time
import socket
import http.client
from bs4 import BeautifulSoup


def get_content(url, data=None):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept - Encoding': 'gzip, deflate,sdch',
        'Accept - Language': 'zh - CN,zh;q = 0.9',
        'Connection': 'keep - alive',
        'User - Agent': 'Mozilla/5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 69.0.3497.100Safari / 537.36'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url, headers=header, timeout=timeout)
            rep.encoding = 'utf-8'
            break
        except socket.timeout as e:
            print('3', e)
            time.sleep(random.choice(range(8, 15)))
        except socket.error as e:
            print(4, e)
            time.sleep(random.choice(range(20, 60)))
        except http.client.BadStatusLine as e:
            print(5, e)
            time.sleep(random.choice(range(30, 80)))
        except http.client.IncompleteRead as e:
            print(6, e)
            time.sleep(random.choice(range(5, 15)))
    return rep.text


def get_data(html_text):
    final = []
    bs = BeautifulSoup(html_text, 'html.parser')
    body = bs.body
    data = body.find('div', {'id': "7d"})
    ul = data.find("ul")
    li = ul.find_all("li")

    for day in li:
        temp = []
        date = day.find("h1").string
        temp.append(date)
        inf = day.find_all("p")
        temp.append(inf[0].string)
        if inf[1].find("span") is None:
            temperature_higest = None
        else:
            temperature_higest = inf[1].find("span").string
            temperature_higest = temperature_higest.replace("℃", "")
        temperature_lowest = inf[1].find("i").string
        temperature_lowest = temperature_lowest.replace("℃", "")
        temp.append(temperature_higest)
        temp.append(temperature_lowest)
        final.append(temp)
    return final


def write_data(data, name):
    file_name = name
    with open(file_name, "a", errors='ignore', newline="") as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


def crawler_weaher():
    print(1)
    url = "http://www.weather.com.cn/weather/101010100.shtml"
    html = get_content(url)
    print(2)
    result = get_data(html)
    print(3)
    write_data(result, "weater.csv")
    print(4)
if __name__ == "__main__":
    crawler_weaher()
