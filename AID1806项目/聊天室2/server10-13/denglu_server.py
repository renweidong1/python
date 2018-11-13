# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from send_friend_memebr import SendFirendMemebr

# 将昵称改为二进制作为当前用户的好友表名


def friend_table(name):
    ay = re.findall("\A[a-zA-Z]+\Z", name)

    if ay:
        return name
    else:
        table_name_first = str(name.encode()).split('\\x')[1:]
        table_name = "".join(table_name_first).split("'")[0]
        return table_name


class RegisterOrLogin(object):
    """用于登录注册
        analyze_type 判断用户请求的行为并执行相应的函数
        do_login 登录函数 返回值为flase 或 true
        do_register 注册函数 将注册信息存储到数据库中
        name_exists 注册时判断该用户名是否已存在"""

    def __init__(self, connfd, the_sql, data, addr):
        self.connfd = connfd
        self.sql = the_sql
        self.data = data
        self.addr = addr

    def analyze_type(self):
        data_list = self.data.decode().split("^^")
        request = data_list[0]
        name = data_list[1]
        pwd = data_list[2]

        # 消息头为1时为登录请求
        if request == 'L':
            print("登录")
            is_login = self.do_login(name, pwd)

            if is_login:
                self.connfd.sendto('true'.encode(), self.addr)
                # 登陆成功后服务器向客户端发送好友信息
                send_friend = SendFirendMemebr(
                    name, self.connfd, self.addr, self.sql)
                send_friend.send_friend_info()
                print("成功")

            else:
                self.connfd.sendto('false'.encode(), self.addr)
                print("失败")

        # 消息头为2时为注册请求
        elif request == 'R':
            print("注册")
            is_exist = self.name_exists(name)

            if is_exist:

                self.connfd.sendto('EXIST'.encode(), self.addr)
                print("失败")

            else:

                self.do_register(name, pwd)
                self.connfd.sendto('OK'.encode(), self.addr)
                print("成功")

    def do_login(self, username, password):

        sql = "select password from users where username = %s"
        user_password = self.sql.get_info(sql, [username])
        if user_password:

            if user_password[0][0] == password:
                addr = self.addr[0] + "+" + str(self.addr[1])
                sql = "insert into online values(%s,%s)"
                self.sql.change_info(sql, [addr, username])
                return True
        return False

    def name_exists(self, username):

        sql = "select * from users where username = %s"
        account = self.sql.get_info(sql, [username])
        if account:
            return True
        else:
            return False

    def do_register(self, username, password):

        sql = "insert into users(username,password) values (%s,%s)"
        self.sql.change_info(sql, [username, password])
        sql = "insert into online(address,username) values (%s,%s)"
        addr = self.addr[0] + "+" + str(self.addr[1])
        self.sql.change_info(sql, [addr, username])
        # table_sql = "create table %s (name varchar(30) not null,user_group varchar(30),addr varchar(6),foreign key(name) references user_info(name) on delete cascade on update cascade)" % table_name
        # self.sql.change_info(table_sql)
