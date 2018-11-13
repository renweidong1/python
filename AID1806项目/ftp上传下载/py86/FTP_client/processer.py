from PyQt5 import QtWidgets
from PyQt5.QtCore import QBasicTimer

from process import Ui_Form


class Process(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Process,self).__init__()
        print('进入process的init')
        self.setupUi(self)
        # self.onStart()
        # self.timer = QBasicTimer()
        # self.step = 0

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.progressBar.setValue(self.step)

    def onStart(self):
        self.timer.start(100, self)