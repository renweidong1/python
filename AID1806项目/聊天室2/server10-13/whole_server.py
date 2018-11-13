# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from socket import *

from denglu_server import RegisterOrLogin
from user_info import MySql
from group_chat import GroupChat
from models import *

ADDR = ('172.40.71.212', 9999)

the_sql = MySql("project")


def main():
    sockfd = socket(AF_INET, SOCK_DGRAM)
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)

    while True:
        try:
            data, addr = sockfd.recvfrom(3096)
        except Exception:
            continue
        print(data, addr)
        data_list = data.decode().split("^^")
        request = data_list[0]
        uname = data_list[1]
        friend_name = data_list[2]
        print(request)
        if request == "CF":
            # 私聊
            print("私聊")
            do_chat_friend(the_sql, sockfd, uname, friend_name, data, addr)
            print("私聊结束")
        elif request == "CG":
            # 群聊
            print("群聊")
            GroupChat(uname, friend_name, data, sockfd, the_sql).send_message()
        elif request == "NF":
            # 添加好友
            print("添加好友")
            do_new_friend(the_sql, sockfd, data_list, addr)
        elif request == "NG":
            # 添加群组
            print("添加群组")
            do_new_group(the_sql, sockfd, data_list, addr)
        elif request == "RG":
            # 新建群组
            print("新建群组")
            do_register_group(the_sql, sockfd, data_list, addr)
        elif request == "HIST":
            # 查询聊天记录
            print("查询聊天记录")
            do_history(the_sql, sockfd, data_list, addr)
        elif request == "SET":
            # 配置个人信息
            print("配置个人信息")
            do_set(the_sql, sockfd, data_list, addr)
        elif request == "Q":
            # 退出
            print("退出")
            do_quit(the_sql, uname)
        else:
            print("注册登录")
            RegisterOrLogin(sockfd, the_sql, data, addr).analyze_type()
        print("重新循环")


if __name__ == "__main__":
    main()
