from socket import *
from threading import Thread
import hashlib
import pymysql
import time

def main():
    ADDR = ('0.0.0.0',8888)
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    child(s)

def do_login(s,msg,addr,user):
    print('执行登录数据库操作')
    Id = msg[0]
    password = msg[1]
    print(Id,password)
    if (Id == "" or password == ""):
        s.sendto('None'.encode(),addr)
        return
    # 打开数据库连接
    db,cur = connect_mysql()
    exist = cur.execute("select * from setup where Id = '%s';" % Id)
    data = cur.fetchall()
    print('查找数据',data)
    print('账号存在吗：',exist)
    if exist == 0:
        s.sendto('Noexist'.encode(),addr)
    else:
        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))
        md5password = hl.hexdigest()
        print(md5password)
        print(data[0][2])
        if md5password == data[0][2]:
            s.sendto('Succsess'.encode(),addr)
            for key,value in list(user.items()):
                if value == Id:
                    del user[key]
            user[addr] = Id
            print(user)
        else:
            s.sendto('Uncorrect'.encode(),addr)
    return

def do_regist(s,msg,addr):
    print('执行注册数据库操作')
    Id = msg[0]
    Name = msg[1]
    Password = msg[2]
    confirmPassword = msg[3]
    print(Id,Name,Password,confirmPassword)
    if (Id == "" or Name == "" or Password == "" or confirmPassword == ""):
        s.sendto('None'.encode(),addr)
        return
    else:  #1.账号已存在;2.密码不匹配;3.插入user表
        if confirmPassword != Password:
            s.sendto('Noconfirm'.encode(),addr)
            return
        elif confirmPassword == Password:
            # md5编码
            hl = hashlib.md5()
            hl.update(Password.encode(encoding='utf-8'))
            md5password = hl.hexdigest()
            db,cur = connect_mysql()
            exist = cur.execute("select * from setup where Id = '%s';" % Id)
            print('存在',exist)
            if exist == 0:
                cur.execute("insert into setup(Id,Name,password) values('%s','%s','%s');" % (Id,Name,md5password))
                sql = "select I from setup where Id = '%s';" % Id
                cur.execute(sql)
                I = cur.fetchall()
                sql = "insert into group_list(user,groupname) values(%d,'%s')" %(I[0][0],'我的好友')
                cur.execute(sql)
                sql = "insert into group_list(user,groupname) values(%d,'%s')" %(I[0][0],'我的群聊')
                cur.execute(sql)
                s.sendto('Succsess'.encode(),addr)
            else:
                s.sendto('Exist'.encode(),addr)
                return
            print('ok')
            db.commit()
            cur.close()
            db.close()
            return

def do_findfriend(s,msg,addr):
    print(msg)
    db,cur = connect_mysql()
    sql = "select I from setup where Id = '%s';" % msg
    cur.execute(sql)
    I = cur.fetchall()
    sql = "select friend_name from friend_list where user_group = %d;" % I[0][0]
    cur.execute(sql)
    print(I[0][0])
    friends = cur.fetchall()
    print(friends)
    msg_back = ''
    for i in friends:
        msg_back = msg_back + i[0] + ' '
    db.commit()
    cur.close()
    db.close()
    s.sendto(msg_back.encode(),addr)

def do_addfriends(s,msg,addr,user):
    print(msg)
    userId = user[addr]
    db,cur = connect_mysql()
    sql = "select I from setup where Id = '%s'" % userId
    exsit = cur.execute(sql)
    I = cur.fetchall()
    print(I)
    sql = "select * from setup where Id = '%s'" % msg
    exsit = cur.execute(sql)
    if exsit == 0:
        sendmsg = 'NoId' + ' ' + userId
        s.sendto(sendmsg.encode(),addr)
    else:
        sql = "select * from friend_list where Id = '%s' and I = %d" % (msg,I[0][0])
        exsit = cur.execute(sql)
        # print(exsit)
        if exsit != 0:
            sendmsg = 'Exsit' + ' ' + userId
            s.sendto(sendmsg.encode(),addr)
        else:
            sql = "insert into friend_list values(%d,'%s') " % (I[0][0],msg)
            cur.execute(sql);
            db.commit()
            cur.close()
            db.close()
            sendmsg = 'Succ' + ' ' + userId
            print(sendmsg)
            s.sendto(sendmsg.encode(),addr)

def do_deletefriends(s,friend_name,addr,user):
    print(friend_name)
    userId = user[addr]
    db,cur = connect_mysql()
    sql = "select I from setup where Id = '%s'" % userId
    exsit = cur.execute(sql)
    I = cur.fetchall()
    print(I)
    sql = "delete from friend_list where I = %d and Id = '%s' " % (I[0][0],friend_name)
    cur.execute(sql);
    db.commit()
    cur.close()
    db.close()
    sendmsg = 'Succ' + ' ' + userId
    print(sendmsg)
    s.sendto(sendmsg.encode(),addr)

def do_friendgroup(s,Id,addr,user):
    print('获取',Id,'的分组')
    db,cur = connect_mysql()
    sql = "select I from setup where Id = '%s'" % Id
    cur.execute(sql)
    I = cur.fetchall()
    print('用户',Id,'的主键为',I)
    sql = "select groupname from group_list where user = %d" % I[0][0]
    cur.execute(sql);
    group_search = cur.fetchall()
    print(group_search)
    group_member = ''
    for i in group_search:
        group_member += i[0]+' '
    print('分组列表为：',group_member)
    db.commit()
    cur.close()
    db.close()
    s.sendto(group_member.encode(),addr)

def do_findfriend(s,Id,groupname,addr):
    print('查询',Id,'用户',groupname,'分组的好友')
    db,cur = connect_mysql()
    sql = "select I from setup where Id = '%s'" % Id
    cur.execute(sql)
    I = cur.fetchall()
    print('用户',Id,'的主键为',I)
    sql = "select Id from group_list where user = %d and groupname = '%s'" % (I[0][0],groupname)
    cur.execute(sql)
    I = cur.fetchall()
    print('此分组的主键为',I)
    sql = "select friend_name from friend_list where user_group = %d" % I[0][0]
    cur.execute(sql)
    friend_name = cur.fetchall()
    print(friend_name)
    msg = ''
    for i in friend_name:
        msg += i[0] + ' '
    print(Id,'的好友为',msg)
    db.commit()
    cur.close()
    db.close()
    s.sendto(msg.encode(),addr)

def do_chat(s,msg,addr,chatdic):
    print(chatdic)
    IdName = chatdic[addr]
    friend_name = msg[0]
    msg.remove(msg[0])
    chatdata = ' '.join(msg)
    print(chatdata)
    print(IdName,'想发送的是',friend_name)
    is_group_chat = friend_name.split(',')
    if len(is_group_chat) == 1:
        for key in chatdic.keys():
            print(IdName,'目前在线好友：',chatdic[key])
            if chatdic[key] == friend_name:
                msgsend = 'Succ' + IdName + ' ' + chatdata
                s.sendto(msgsend.encode(),key)
                # s.sendto(msgsend.encode(),addr)
                return
                # s.sendto(msgsend.encode(),addr)
        else:
            back_msg = "NoOnline" + friend_name
            s.sendto(back_msg.encode(),addr)
    else:
        print('想要群聊的好友为',is_group_chat)
        for i in is_group_chat:
            if i == '的群聊':
                pass

            else:
                for key in chatdic.keys():
                    print(IdName, '目前在线好友：', chatdic[key])
                    if chatdic[key] == IdName:
                        pass
                    elif chatdic[key] == i:
                        msgsend = 'SuccG' + IdName + ' ' + friend_name + ' ' + chatdata
                        s.sendto(msgsend.encode(), key)
                        # s.sendto(msgsend.encode(),addr)
                        # s.sendto(msgsend.encode(),addr)
                        continue
                # else:
                #     back_msg = "NoOnline" + friend_name
                #     s.sendto(back_msg.encode(), addr)


def do_isOnline(s,friend_name,addr,user):
    if friend_name in user.values():
        s.sendto('1'.encode(),addr)
    else:
        s.sendto('0'.encode(),addr)

def do_add_group(s,Id,add_groupname,addr):
    print('即将为',Id,'添加分组',add_groupname)
    db,cur = connect_mysql()
    sql = "select I from setup where Id = '%s'" % Id
    cur.execute(sql)
    I = cur.fetchall()
    print('此用户主键为',I[0][0])
    sql =  "insert into group_list(user,groupname) values(%d,'%s')" % (I[0][0],add_groupname)
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()
    s.sendto('添加分组成功'.encode(),addr)

def do_rename_group(s,Id,old_group_name,new_group_name,addr):
    print('即将为',Id,'修改分组名',old_group_name,'为',new_group_name)
    db,cur = connect_mysql()
    sql = "select I from setup where Id = '%s'" % Id
    cur.execute(sql)
    I = cur.fetchall()
    print('此用户主键为',I[0][0])
    sql = "update group_list set groupname = '%s' where (user = %d and groupname = '%s')" % (new_group_name,I[0][0],old_group_name)
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()
    s.sendto('修改分组名成功'.encode(),addr)

def do_delete_group(s,Id,group_name,addr):
    print('服务器即将删除',Id,'的',group_name,'分组')
    db,cur = connect_mysql()
    sql = "select I from setup where Id = '%s'" % Id
    cur.execute(sql)
    I = cur.fetchall()
    print('此用户主键为',I[0][0])
    sql = "select Id from group_list where (user = %d and groupname = '%s')" % (I[0][0],group_name)
    cur.execute(sql)
    Id = cur.fetchall()
    sql = "delete from friend_list where user_group = %d" % Id[0][0]
    cur.execute(sql)
    sql = "delete from group_list where (user = %d and groupname = '%s')" % (I[0][0],group_name)
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()
    s.sendto('删除分组成功'.encode(),addr)

def do_delete_friend(s,Id,friend_name,addr):
    db,cur = connect_mysql()
    sql = "select I from setup where Id = '%s'" % Id
    cur.execute(sql)
    I = cur.fetchall()
    sql = "select Id from group_list where user = %d" % I[0][0]
    cur.execute(sql)
    group_Id = cur.fetchall()
    print(len(group_Id))
    for i in group_Id:
        sql = "delete from friend_list where (user_group = %d and friend_name = '%s')" % (i[0],friend_name)
        cur.execute(sql)
    db.commit()
    cur.close()
    db.close()
    s.sendto('删除好友成功'.encode(),addr)


def do_add_friend(s,Id,friend_name,group_name,addr):
    db,cur = connect_mysql()
    sql = "select * from setup where Id = '%s'" % friend_name
    exsit = cur.execute(sql)
    if exsit == 0:
        sendmsg = 'NoId'
        s.sendto(sendmsg.encode(),addr)
    else:
        sql = "select I from setup where Id = '%s'" % Id
        cur.execute(sql)

        I = cur.fetchall()
        sql = "select Id from group_list where (user = %d and groupname='%s')" % (I[0][0],group_name)
        cur.execute(sql)
        group_Id = cur.fetchall()
        sql = "insert into friend_list(user_group,friend_name) values(%d,'%s')" % (group_Id[0][0],friend_name)
        cur.execute(sql)
        s.sendto('添加好友成功'.encode(), addr)
    db.commit()
    cur.close()
    db.close()

def do_ready_chat(s,Id,msg,addr,chatdic):
    for key,value in list(chatdic.items()):
        print(key,value)
        if value == Id:
            del chatdic[key]
    print('准备开始聊天'+ msg+Id)
    chatdic[addr] = Id
    print(chatdic)

def do_AddGroupChat(s,Id,group_chat_name,addr):
    db,cur = connect_mysql()
    sql = "select I from setup where Id = '%s'" % Id
    cur.execute(sql)
    I = cur.fetchall()
    sql = "insert into group_chat(idname,group_name) values(%d,'%s')" % (I[0][0],group_chat_name)
    cur.execute(sql)
    s.sendto('添加群聊'.encode(), addr)
    db.commit()
    cur.close()
    db.close()

def do_ready_GroupChat(s, Id, addr):
    db,cur = connect_mysql()
    sql = "select I from setup where Id = '%s'" % Id
    cur.execute(sql)
    I = cur.fetchall()
    sql = "select group_name from group_chat where idname=%d" % I[0][0]
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    return_msg = ''
    for i in result:
        return_msg += i[0] + ' '
    s.sendto(return_msg.encode(),addr)
    db.commit()
    cur.close()
    db.close()

def connect_mysql():
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", database="chat",
                         charset="utf8")
    print('数据库连接成功')
    cur = db.cursor()
    print('游标创建成功')
    return db,cur

def child(s):
    global chat
    chat = {}
    global user
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        message = msg.decode()
        msglist = message.split(' ')
        print('发送方为',addr)
        print(msglist[0])
        print(msglist[1:len(msglist)+1])
        print('子线程启动')
        t = Thread(target=handler, args=(s,msglist,addr,user,chat,))
        t.setDaemon(True)
        t.start()

def handler(s,msglist,addr,user,chat):
        if msglist[0] == "L":
            do_login(s,msglist[1:len(msglist)+1],addr,user)
        elif msglist[0] == "R":
            do_regist(s,msglist[1:len(msglist)+1],addr)
        elif msglist[0] == "C":
            do_chat(s,msglist[1:len(msglist)+1],addr,chat)
        elif msglist[0] == "F":
            do_findfriend(s,msglist[1],msglist[2],addr)
        elif msglist[0] == 'A':
            do_addfriends(s,msglist[1],addr,user)
        elif msglist[0] == 'D':
            do_deletefriends(s,msglist[1],addr,user)
        elif msglist[0] == 'G':
            do_friendgroup(s,msglist[1],addr,user)
        elif msglist[0] == 'Online':
            do_isOnline(s,msglist[1],addr,user)
        elif msglist[0] == 'AG':
            do_add_group(s,msglist[1],msglist[2],addr)
        elif msglist[0] == 'RG':
            do_rename_group(s,msglist[1],msglist[2],msglist[3],addr)
        elif msglist[0] == 'DG':
            do_delete_group(s,msglist[1],msglist[2],addr)
        elif msglist[0] == 'DF':
            do_delete_friend(s,msglist[1],msglist[2],addr)
        elif msglist[0] == 'AF':
            do_add_friend(s,msglist[1],msglist[2],msglist[3],addr)
        # elif msglist[0] == 'CF':
        #     print(msglist)
        elif msglist[0] == 'RC':
            do_ready_chat(s,msglist[1],msglist[2],addr,chat)
        elif msglist[0] == 'AGC':
            do_AddGroupChat(s, msglist[1], msglist[2], addr)
        elif msglist[0] == 'RGC':
            do_ready_GroupChat(s, msglist[1],addr)

if __name__ == "__main__":
    main()