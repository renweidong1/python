# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pymysql import *


# 创建连接数据库的对象(你服务端自己完成)
db = connect(host='localhost', user='root', password='021126eric',
             database='project', charset='utf8')
# 创建游标对象
cur = db.cursor()


# 函数需要传入套接字,目标用户名,目标IP,数据库操作对象
def change_pass(c, uname, addr, cur):
    print('启用更改密码')
    x = cur.execute('select * from user_info;')
    g = False
    for i in x:
        if i['name'] == uname:
            g = i
            break
    if g:
        c.sendto(('请输入旧密码').encode(), addr)
        data1, addr = c.recvfrom(1024)
        if g['password'] == data:
            c.sendto(('请输入新密码').encode(), addr)
            data2, addr = c.recvfrom(1024)
            c.sendto(('请重复输入新密码').encode(), addr)
            data3, addr = c.recvfrom(1024)
            if data2 == data3:
                cur.execute(
                    'update user_info set password=data2 where name == ' + g[name] + ';')
                c.sendto(('更改完成').encode(), addr)
            else:
                c.sendto(('两次新密码不相同').encode(), addr)
        else:
            c.sendto(('密码不正确').encode(), addr)
    else:
        c.sendto(('账号不存在').encode(), addr)
    db.commit()
    cur.close()
    db.close()
