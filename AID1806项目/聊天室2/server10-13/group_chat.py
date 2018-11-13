# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time


class GroupChat(object):

    def __init__(self, uname, gname, data, connfd, sql):

        self.uname = uname
        self.gname = gname
        self.data = data
        self.connfd = connfd
        self.sql = sql

    def send_message(self):
        unonline = {}
        now_time = time.strftime('%Y%m%d%H%M%S')
        group_sql = "select username from group_user where groupname = '%s'" % self.gname
        group_memebr = self.sql.get_info(group_sql)
        print(group_memebr)

        for fname_tup in group_memebr:

            online_member = "select address from online where username = %s"
            addrstr = self.sql.get_info(online_member, [fname_tup[0]])
            if addrstr:
                addr = addrstr[0][0].split("+")
                try:
                    port = int(addr[1])
                    print(fname_tup, (addr[0], port), self.data)
                    self.connfd.sendto(self.data, (addr[0], port))
                    print("data" + self.data)
                except Exception:
                    continue
            else:

                content = self.data
                sql = "insert into cookie (shijian,speaker,groupname,fname,content) values(%s,%s,%s,%s,%s);"
                cookie_insert = self.sql.change_info(
                    sql, [now_time, self.uname, self.gname, fname_tup[0], content])
                sql = "insert into hist (speaker,groupname,fname,content) values(%s,%s,%s,%s);"
                hist_insert = self.sql.change_info(
                    sql, [self.uname, self.uname, fname_tup[0], content])
