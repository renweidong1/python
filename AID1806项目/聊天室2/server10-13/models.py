# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
import random


def do_new_friend(conn, s, data_request, addr):
    uname = data_request[1]
    fname = data_request[2]
    if len(data_request) == 3:
        forward = "^^".join(data_request) + "^^ask"
        sql = 'select address from online where username = %s;'
        faddr = conn.get_info(sql, [fname])
        if faddr:
            for i in faddr:
                for addr_str in i:
                    faddr_list = addr_str.split('+')
                    faddr = (faddr_list[0], int(faddr_list[1]))
                    s.sendto(forward.encode(), faddr)
        else:
            content = '^^'.join(data_request)
            sql1 = 'insert into cookie (fname,content) values(%s,%s);'
            conn.change_info(sql1, [fname, content])
    else:
        reply = data_request[-1]
        if reply == 'YES':
            sql2 = 'insert into friends (username1, username2) values(%s,%s);'
            conn.change_info(sql2, [uname, fname])
            sql3 = 'insert into friends (username1, username2) values(%s,%s);'
            conn.change_info(sql3, [fname, uname])
            sql = 'select address from online where username = %s;'
            uaddr = conn.get_info(sql, [uname])
            if uaddr:
                sql4 = 'select icon from users where username = %s;'
                icon = conn.get_info(sql4, [fname])
                for y in icon:
                    for uicon in y:
                        msg = uicon
                for x in uaddr:
                    for addr_str in x:
                        uaddr_list = addr_str.split('+')
                        uaddr = (uaddr_list[0], int(uaddr_list[1]))
                        s.sendto(msg.encode(), uaddr)
            else:
                content = '^^'.join(data_request)
                sql1 = 'insert into cookie (fname,content) values(%s,%s);'
                conn.change_info(sql1, [uname, content])

        elif reply == "NO":
            sql = 'select address from online where username = %s;'
            uname = conn.get_info(sql, [uname])
            if uname:
                for x in uname:
                    for addr_str in x:
                        uaddr_list = addr_str.split('+')
                        uaddr = (uaddr_list[0], int(uaddr_list[1]))
                        msg = '^^'.join(data_request)
                        s.sendto(msg.encode(), uaddr)
            else:
                content = '^^'.join(data_request)
                sql1 = 'insert into cookie (fname,content) values(%s,%s);'
                conn.change_info(sql1, [uname, content])


def do_new_group(conn, s, data_request, addr):
    uname = data_request[1]
    gname = data_request[2]
    sql = 'select groupowner from mygroup where groupname = %s;'
    owenr = conn.get_info(sql, [gname])
    ownername = owenr[0][0]
    if len(data_request) == 3:
        forward = "^^".join(data_request) + '^^' + ownername + "^^ask"
        sql = 'select address from online where username = %s;'
        owner_addr = conn.get_info(sql, [ownername])
        if owner_addr:
            for i in owner_addr:
                for addr_str in i:
                    faddr_list = addr_str.split('+')
                    faddr = (faddr_list[0], int(faddr_list[1]))
                    s.sendto(forward.encode(), faddr)
        else:
            content = '^^'.join(data_request)
            sql1 = 'insert into cookie (fname,content) values(%s,%s);'
            conn.change_info(sql1, [ownername, content])
    else:
        reply = data_request[-1]
        if reply == 'YES':
            sql2 = 'insert into group_user (username, groupname) values(%s,%s);'
            conn.change_info(sql2, [uname, gname])
            sql = 'select address from online where username = %s;'
            uaddr = conn.get_info(sql, [uname])
            if uaddr:
                for x in uaddr:
                    for addr_str in x:
                        uaddr_list = addr_str.split('+')
                        uaddr = (uaddr_list[0], int(uaddr_list[1]))
                        msg = '^^'.join(data_request)
                        s.sendto(msg.encode(), uaddr)
            else:
                content = '^^'.join(data_request)
                sql1 = 'insert into cookie (fname,content) values(%s,%s);'
                conn.change_info(sql1, [uname, content])
        elif reply == "NO":
            sql = 'select address from online where username = %s;'
            uaddr = conn.get_info(sql, [uname])

            if uaddr:
                for x in uaddr:
                    for addr_str in x:
                        uaddr_list = addr_str.split('+')
                        uaddr = (uaddr_list[0], int(uaddr_list[1]))
                        msg = '^^'.join(data_request)
                        s.sendto(msg.encode(), uaddr)
            else:
                content = '^^'.join(data_request)
                sql1 = 'insert into cookie (fname,content) values(%s,%s);'
                conn.change_info(sql1, [uname, content])


def do_register_group(conn, s, data_request, addr):
    uname = data_request[1]
    gname = data_request[2]
    sql = "select groupname from mygroup where groupname = %s;"
    account = conn.get_info(sql, [gname])
    if account:
        msg = '^^'.join(data_request) + "EXIST"
        s.sendto(msg.encode(), addr)
    else:
        sql = "insert into users(groupname,groupowner) values (%s,%s);"
        conn.change_info(sql, [gname, uname])
        msg = '^^'.join(data_request) + "OK"
        s.sendto(msg.encode(), addr)


def do_chat_friend(conn, s, uname, fname, data, addr):
    sql = "select address from online where username=%s;"
    faddr = conn.get_info(sql, [fname])
    print(faddr)
    now_time = time.strftime('%Y%m%d%H%M%S')
    if faddr:
        faddr_list = faddr[0][0].split("+")
        print(faddr_list)
        faddr = (faddr_list[0], int(faddr_list[1]))
        print(faddr)
        s.sendto(data, faddr)
    else:
        content = data
        sql = "insert into cookie (shijian,speaker,fname,content) values(%s,%s,%s,%s);"
        cookie_insert = conn.change_info(
            sql, [now_time, uname, fname, content])
        sql = "insert into hist (speaker,fname,content) values(%s,%s,%s);"
        hist_insert = conn.change_info(sql, [uname, fname, content])
    print("over")


def do_quit(conn, name):
    sql = "delete from online where username = %s"
    conn.change_info(sql, [name])


def do_history(conn, s, data_request, addr):
    pass


def do_set(conn, s, data_request, addr):
    pass

    #     if user_password[0][0] == password:

    #         sql = "update user_info set addr = '%s' where name = %s"
    #         self.sql.change_info(sql, [addr[1], username])
    #         return True
    # return False


# 将昵称改为二进制作为当前用户的好友表名
# def friend_table(name):
#     ay = re.findall("\A[a-zA-Z]+\Z", name)

#     if ay:
#         return name
#     else:
#         table_name_first = str(name.encode()).split('\\x')[1:]
#         table_name = "".join(table_name_first).split("'")[0]
#         return table_name

#     def __init__(self, connfd, the_sql, data, addr):
#         self.connfd = connfd
#         self.sql = the_sql
#         self.data = data
#         self.addr = addr

#     def analyze_type(self):
#         data_list = self.data.decode().split("^^")
#         request = data_list[0]
#         name = data_list[1]
#         pwd = data_list[2]

#         # 消息 头为1时为登录请求
#         if request == 'L':
#             print("登录")
#             is_login = self.do_login(name, pwd, self.addr)

#             if is_login:
#                 self.connfd.sendto('true'.encode(), self.addr)
#                 # 登陆成功后服务器向客户端发送好友信息
#                 send_friend = SendFirendMemebr(
#                     name, self.connfd, self.addr, self.sql)
#                 send_friend.send_friend_info()
#                 print("成功")

#             else:
#                 self.connfd.sendto('false'.encode(), self.addr)
#                 print("失败")
