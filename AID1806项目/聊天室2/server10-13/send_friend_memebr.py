# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class SendFirendMemebr(object):
    '''
        用户登录成功后返给客户端的好友名称和群聊名称
        find_friend_table_name 通过用户名在数据库中查找当前用户的好友信息表名
        send_friend_info 向客户端发送好友名称和群聊名称
    '''

    def __init__(self, uname, connfd, addr, sql):
        self.uname = uname
        self.connfd = connfd
        self.addr = addr
        self.sql = sql

    # def find_friend_table_name(self):
    #     sql_table = "select username2 from friends where username1 = %s"
    #     tuple_table_name = self.sql.get_info(sql_table, [self.uname])
    #     friend_table_name = tuple_table_name[0][0]
    #     return friend_table_name

    def send_friend_info(self):

        sql = "select username2 from friends where username1=%s"
        firend_list = self.sql.get_info(sql, [self.uname])

        self.connfd.sendto(b'begin_send_friend_list', self.addr)

        if firend_list:
            for friend_name in firend_list:
                self.connfd.sendto(friend_name[0].encode(), self.addr)

        self.connfd.sendto(b'over_send_friend_list', self.addr)

        sql = "select groupname from group_user where username=%s"
        group_list = self.sql.get_info(sql, [self.uname])
        self.connfd.sendto(b'begin_send_group_list', self.addr)
        if group_list:
            for group_name in group_list:
                self.connfd.sendto(group_name[0].encode(), self.addr)
        # for group in set(group_list):
        #     self.connfd.sendto(group.encode(), self.addr)
        self.connfd.sendto(b"over_send_group_list", self.addr)
