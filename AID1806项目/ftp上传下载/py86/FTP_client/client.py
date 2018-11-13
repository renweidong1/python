import time
from PyQt5.QtWidgets import QApplication
import threading

locked = threading.RLock()

#功能封装为类
class TftpClient(object):
    def __init__(self,s):
        self.sockfd = s

    #发送登陆请求
    def do_login(self,name,pwd):
        msg = 'D '+ name + ' '+ pwd
        self.sockfd.send(msg.encode())
        #等待服务器确认
        data = self.sockfd.recv(1024).decode()
        print('登陆请求的recv',data)
        if data == 'OK':
            print('接收L')
            L = self.sockfd.recv(1024).decode()
            if L == 'NONE':
                return ('OK', [])
            fileList = L.split('#')
            fileList.pop()
            return ('OK',fileList)
        elif data == 'NONE':
            return ('NONE',[])
        else:
            return ('ERROR',[])

    #发送刷新请求
    def do_refresh(self,name):
        msg = 'F ' + name
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(1024).decode()
        fileList = data.split('#')
        fileList.pop()
        return fileList

    #发送注册请求
    def do_registe(self,name,pwd):
        msg = 'R '+ name + ' '+ pwd
        self.sockfd.send(msg.encode())
        #等待服务器确认
        data = self.sockfd.recv(1024).decode()
        print(data)
        if data == 'OK':
            return 'OK'
        elif data == 'No':
            return 'NO'
        elif data == 'EXISTS':
            return 'EXISTS'

    #发送文件名
    def do_name(self,name,fileName1,size):
        print('进入 d0_name 方法')
        fn = fileName1.split('/')
        data = 'J ' + fn[-1] + ' ' + name + ' ' + str(size)
        self.sockfd.send(data.encode())
        data = self.sockfd.recv(1024).decode()
        print('recv 的data',data)
        if data[:2] == 'OK':
            return ("OK",)
        elif data[:4] == 'have':
            size = int(data.split(' ')[1])
            return ("have",size,)

    #发送上传请求
    def do_put(self,name,fileName1,size):
        print('进入 do——put方法')
        try:
            fd = open(fileName1, 'rb')
        except:
            print("上传文件不存在")
        print('size------------------------>',size)
        if size == 0:
            msg = 'C ' + fileName1 + ' ' + name
            self.sockfd.send(msg.encode())
            time.sleep(1)
            fd = open(fileName1, 'rb')
            while True:
                data = fd.read(4096)
                if not data:
                    break
                self.sockfd.send(data)
                print(data)
            fd.close()
            time.sleep(1)
            self.sockfd.send(b'##')

            print('上传成功')
            return 'OK'
        else:
            msg = 'X ' + fileName1 + ' ' + name
            self.sockfd.send(msg.encode())
            time.sleep(1)
            fd = open(fileName1, 'rb')
            fd.seek(size, 0)
            print('seeek--->63520768',size)
            while True:
                data = fd.read(4096)
                print(data)
                if not data:
                    break
                self.sockfd.send(data)
            fd.close()
            time.sleep(1)
            self.sockfd.send(b'##')
            return 'OK'

    #发送下载请求
    def do_download(self,filename,name,fileurl):
        msg = 'G '+ filename + ' ' + name + ' ' + fileurl
        print(msg)
        self.sockfd.send(msg.encode())
        #等待服务器确认
        data = self.sockfd.recv(1024).decode()
        print('下载请求的回复：',data)
        if data == 'OK':
            return 'OK'
        elif data == 'NO':
            return 'NO'
        else:
            return 'ERROR'

    #下载
    def download(self,filename):
        fd = open(filename, 'wb')
        while True:
            data = self.sockfd.recv(4096)
            if data == b'##':
                break
            fd.write(data)
            QApplication.processEvents()
        fd.close()
        print("%s 下载完成\n" % filename)

    #删除
    def do_delete(self,filename,name):
        msg = 'L '+ filename + ' ' + name
        print(msg)
        self.sockfd.send(msg.encode())
