from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
from processer import *
from PyQt5.QtWidgets import QMessageBox
import loginer
import os
import index
import time

class WorkThread(QThread):
    trigger = pyqtSignal()

    def __init__(self,process,tftp,name,fileName1,size):
        print('进入workThread的init')
        super(WorkThread, self).__init__()
        self.process = process
        self.tftp = tftp
        self.name = name
        self.fileName1 = fileName1
        self.size = size

    def run(self):
        print('进入run方法')
        res = self.tftp.do_put(self.name, self.fileName1, self.size)
        print('上传文件后的结果',res)

        if res == 'OK':
            print('label上传成功')
            self.process.label.setText('上传成功！')
            return

        # 循环完毕后发出信号
        print('准备发送信号')
        self.trigger.emit()
        print('发送信号完成')

        return res


class Index(QtWidgets.QWidget,index.Ui_Form):
    def __init__(self,name,tftp,fileList):
        super(Index,self).__init__()
        self.setupUi(self)
        self.tftp = tftp
        self.name = name
        self.fileList = fileList
        self.myList.addItems(self.fileList)
        self.p = Process()

    #上传文件
    def put(self):

        self.label_fileInfo.setText('')

        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取文件",
                                                          "./",
                                                          "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注 意用双分号间隔
        if fileName1:
            size = os.path.getsize(fileName1)
            print(self.name, fileName1, size)
            res = self.tftp.do_name(self.name, fileName1, size)
            print('发送文件名字的回复',res[0])
            if res[0] == 'have':
                size = res[1]
                button = QMessageBox.question(self, "Question",
                                              self.tr("是否继续上传？"),
                                              QMessageBox.Ok | QMessageBox.Cancel,
                                              QMessageBox.Ok)
                if button == QMessageBox.Ok:
                    workThread = WorkThread(self.p,self.tftp, self.name, fileName1, size)
                    workThread.start()
                    self.showProcess()
                    return
                elif button == QMessageBox.Cancel:
                    return
                else:
                    return
            elif res[0] == 'OK':
                size = 0
                workThread = WorkThread(self.p,self.tftp, self.name, fileName1, size)
                workThread.start()
                self.showProcess()


    def end(self):
        print('接收到结束信号了')
    def showProcess(self):
        self.p.label.setText('读取数据中，请稍后...')
        self.p.show()


    #下载文件
    def download(self):
        self.label_fileInfo.setText('')
        row = self.myList.currentRow()
        print(row)
        if row < 0:
            QMessageBox.warning(self, "Warning", "请选择文件！")
            return
        file = self.myList.item(row).text()
        fname = file.split('  ')[0]
        print('file,',fname)

        #fileName2 文件保存的路径
        fileName2, ok2 = QFileDialog.getSaveFileName(self,
                                                     "文件保存",
                                                     fname,
                                                    "All Files (*);;Text Files (*.txt)")
        res = self.tftp.do_download(file, self.name,fileName2)
        if fileName2:
            if res == 'OK':
                self.tftp.download(fileName2)
                self.label_fileInfo.setText('下载成功!')
            elif res == 'NO':
                pass
            else:
                self.label_fileInfo.setText('下载失败!')
        else:
            pass
    #刷新
    def refresh(self):
        self.label_fileInfo.setText('')
        fileList = self.tftp.do_refresh(self.name)
        print(fileList)
        self.myList.clear()
        self.fileList = fileList
        self.myList.addItems(self.fileList)

    #退出
    def exit(self):
        self.myshow = loginer.mywindow(self.tftp)
        self.myshow.show()
        self.close()

    #删除
    def delete(self):
        self.label_fileInfo.setText('')
        row = self.myList.currentRow()
        print(row)
        if row < 0:
            QMessageBox.warning(self, "Warning", "请选择文件！")
            return
        file = self.myList.item(row).text()
        self.tftp.do_delete(file, self.name)
        self.myList.takeItem(row)
        self.label_fileInfo.setText('删除成功！')
