import sys
from PyQt5 import QtWidgets, QtGui
from loginer import  *
from indexr import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    HOST = '192.168.43.249'
    PORT = 8888
    ADDR = (HOST, PORT)
    s = socket()
    s.connect(ADDR)
    tftp = TftpClient(s)

    myshow = mywindow(tftp)
    myshow.show()
    sys.exit(app.exec_())
