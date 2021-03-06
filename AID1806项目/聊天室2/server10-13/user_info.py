# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pymysql


class MySql(object):

    def __init__(self, database,
                 host="localhost",
                 user="root",
                 password="tarena",
                 port=3306,
                 charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.db = database
        self.charset = charset

    def connect(self):
        self.con = pymysql.connect(host=self.host,
                                   user=self.user,
                                   password=self.password,
                                   port=self.port,
                                   database=self.db,
                                   charset=self.charset)
        self.cur = self.con.cursor()

    def close(self):
        self.cur.close()
        self.con.close()

    def change_info(self, sql, l=[]):
        try:
            self.connect()
            self.cur.execute(sql, l)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print("失败", e)
        self.close()

    def get_info(self, sql, l=[]):
        try:
            self.connect()
            self.cur.execute(sql, l)
            info = self.cur.fetchall()
            return info
        except Exception as e:
            print("失败", e)
            return False


# a = MySql("project")aa
# sql = "select * from user_info where name = '%s'" % "sds"
# c = a.get_info(sql)
# if not c :
#     print("dsds")
# print(c)
# sql = "insert into user_info(account,name,password) values(%s,%s,%s)"
# L = ["1414180210","wang","123456"]
# a.change_info(sql,L)
