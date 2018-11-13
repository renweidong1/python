from socket import *
from time import sleep
from signal import *
import sys,os,stat
from mysqlpython import *
import re

FILE_PATH = '/home/tarena/桌面/ftp/userpath/'
UESR_PAHT = 'userpath/'
path = []
class FtpServer(object):
    def __init__(self,connfd,mysql):
        self.connfd = connfd
        self.mysql = mysql

    def do_login(self,user,password):
        select = 'select username,password from user where username = %s;'
        result = self.mysql.all(select,[user])
        if not result:
            self.connfd.send(b"NONE")
        else:
            if result[0] == user and result[1] == password:
                self.connfd.send(b'OK')
                sleep(0.1)
                self.do_list(user)
            else:
                self.connfd.send(b'ERROR')

    def do_list(self,name):
        #获取列表
        file_list = os.listdir(FILE_PATH+name+'/')
        if not file_list:
            files= 'NONE'
        # else:
            # self.connfd.send(b'OK')
            # sleep(0.1)
        else:
            files = ''
            for file in file_list:
                if file[0] != '.':
                    size = os.path.getsize(FILE_PATH+name+'/'+file)/(1024**2)
                    if size<=1:
                        size = os.path.getsize(FILE_PATH+name+'/'+file)/1024
                        files = files + file +'  '+ str(round(size,2))+'kb'+ '#'
                    else:
                        files = files + file +'  '+ str(round(size,2))+'Mb'+ '#'

        self.connfd.send(files.encode())


    def do_register(self,user,password):
        select = 'select username from user where username = %s;'
        result = self.mysql.all(select,[user])
        if not result:
            insert = 'insert into user(username,password) values(%s,%s);'
            self.mysql.zhixing(insert,[user,password])
            self.connfd.send(b"OK")
            os.makedirs(UESR_PAHT+user)
        else:
            self.connfd.send(b'EXISTS')

    def do_put(self,filename,user,size1):
        PATH = FILE_PATH+user+'/'+filename
        if os.path.exists(PATH) and os.path.getsize(PATH) != int(size1):
            size = os.path.getsize(PATH)
            try:
                fw = open(PATH,'ab')
            except:
                self.connfd.send("无法上传".encode())
                return
            while True:
                data = self.connfd.recv(4096)
                if data == b'##':
                    break
                fw.write(data)
        elif os.path.exists(PATH) and os.path.getsize(PATH) == int(size1):
            lujing = PATH.split('.')
            L = []
            file_list = os.listdir(FILE_PATH+user+'/')
            spl = filename.split('.')[0]
            for i in file_list:
                add1 = re.findall(spl+'\(.\)',PATH.split('/')[-1])
                if not add1:
                    PATH = lujing[0]+'(1)' + '.'+lujing[-1]
                else:
                    add1 = add1.sort()[-1]
                    numbefore = re.findall('\(.\)',add1)
                    numafter = int(numbefore[0][1])+1
                    PATH = lujing[0]+'(%d)'%num + '.'+lujing[-1]

            try:
                fw = open(PATH,'wb')
            except:
                self.connfd.send("无法上传".encode())
                return
            self.connfd.send(b'OK')
            while True:
                data = self.connfd.recv(4096)
                if data == b'##':
                    break
                fw.write(data)
        else:
            try:
                fw = open(PATH,'wb')
            except:
                self.connfd.send("无法上传".encode())
                return
            while True:
                data = self.connfd.recv(4096)
                if data == b'##':
                    break
                fw.write(data)
        fw.close()
        print("%s 接收完成\n"%filename)
    def do_get(self,filename,user,url):
        if not url:
            self.connfd.send(b'NO')
            return
        print(FILE_PATH+user+'/'+filename)
        try:
            fd = open(FILE_PATH+user+'/'+filename,'rb')
        except:
            self.connfd.send('文件不存在'.encode())
            return
        self.connfd.send(b'OK')
        sleep(0.1)
        try:
            while True:
                data = fd.read(4096)
                print(data)
                self.connfd.send(data)
                if not data:
                    break
        except Exception as e:
            print(e)
        sleep(0.5)
        self.connfd.send(b'##')
        print("发送完成")

    def do_delete(self,name,user):
        os.remove(FILE_PATH+user+'/'+name)


    def judge(self,filename,user,size1):
        PATH = FILE_PATH+user+'/'+filename
        if os.path.exists(PATH) and os.path.getsize(PATH) != int(size1):
            size = os.path.getsize(PATH)
            print(size)
            self.connfd.send(("have"+' '+str(size)).encode())
            return size1
        else:
            self.connfd.send(b'OK')
            print('发送OK了')
            return size1


    def xuchuan(self,filename,user):
        PATH = FILE_PATH+user+'/'+filename
        sleep(0.1)
        try:
            fw = open(PATH,'ab')
        except:
            self.connfd.send("无法上传".encode())
            return

        while True:
            data = self.connfd.recv(4096)
            if data == b'##':
                break
            fw.write(data)
        fw.close()
        print("%s 接收完成\n"%filename)

    def notxuchuan(self,filename,user,size1):
        PATH = FILE_PATH+user+'/'+filename

        if os.path.exists(PATH) and os.path.getsize(PATH) == int(size1):
            print('进的if')
            lujing = PATH.split('.')
            file_list = os.listdir(FILE_PATH+user+'/')
            spl = filename.split('.')[0]
            for i in file_list:
                add1 = re.findall(spl+'\(.\)',PATH.split('/')[-1])
                if not add1:
                    PATH = lujing[0]+'(1)' + '.'+lujing[-1]
                else:
                    print('到了')
                    add1.sort()
                    numbefore = re.findall('\(.\)',add1[-1])
                    numafter = int(numbefore[0][1])+1
                    PATH = lujing[0]+'(%d)'%numafter + '.'+lujing[-1]

            try:
                fw = open(PATH,'wb')
            except:
                self.connfd.send("无法上传".encode())
                return
            sleep(0.5)
            while True:
                data = self.connfd.recv(4096)
                if data == b'##':
                    break
                fw.write(data)
        else:
            print("进的else")
            try:
                fw = open(PATH,'wb')
            except:
                self.connfd.send("无法上传".encode())
                return
            sleep(0.5)
            while True:
                data = self.connfd.recv(4096)
                if data == b'##':
                    break
                fw.write(data)
        fw.close()
        print("%s 接收完成\n"%filename)


def main():
    IP = '0.0.0.0'
    PORT = 8888
    ADDR = (IP,PORT)
    sqlobj = Mysqlpython('ftp')

    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    while True:
        try:
            connfd,addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit('已退出')
        except Exception as e:
            print(e)
            continue
        print('客户端',addr,'登录成功')

        pid = os.fork()
        if pid == 0:
            s.close()
            wds = FtpServer(connfd,sqlobj)
            while True:
                data = connfd.recv(1024).decode()
                if data[0] == 'D':
                    name = data.split(' ')[1]
                    pwd = data.split(' ')[2]
                    wds.do_login(name,pwd)
                elif data[0] == 'R':
                    name = data.split(' ')[1]
                    pwd = data.split(' ')[2]
                    wds.do_register(name,pwd)
                elif data[0] == 'S':
                    user = data.split(" ")[1]
                    wds.do_list(user)
                elif data[0] == 'P':
                    file = data.split(' ')[1]
                    user = data.split(' ')[2]
                    size = data.split(' ')[-1]
                    wds.do_put(file,user,size)
                elif data[0] == 'G':
                    file = data.split(' ')[1]
                    user = data.split(' ')[4]
                    url = data.split(' ')[-1]
                    wds.do_get(file,user,url)
                elif data[0] == 'F':
                    name = data.split(' ')[1]
                    wds.do_list(name)
                elif data[0] == 'L':
                    name = data.split(' ')[1]
                    user = data.split(' ')[-1]
                    wds.do_delete(name,user)
                elif data[0] == 'J':
                    print('panduan',data)
                    file = data.split(' ')[1]
                    user = data.split(' ')[2]
                    size = data.split(' ')[-1]
                    size = wds.judge(file,user,size)
                elif data[0] == 'X':
                    print('xuchuan',data)
                    file = data.split(' ')[1].split('/')[-1]
                    user = data.split(' ')[2]
                    wds.xuchuan(file,user)
                elif data[0] == 'C':
                    print('not xuchuan',data)
                    file = data.split(' ')[1].split('/')[-1]
                    user = data.split(' ')[2]
                    print(size) 
                    wds.notxuchuan(file,user,size)
                elif data[0] == 'Q':
                    print('客户端',addr,'已退出')
                    sys.exit(0)


        else:
            connfd.close()
            continue
if __name__ == '__main__':
    main()