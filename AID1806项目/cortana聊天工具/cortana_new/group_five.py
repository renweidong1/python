import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        screen = QDesktopWidget().screenGeometry()
        self.resize(screen.width(), screen.height())
        self.setWindowIcon(QIcon('./static/images/group_five.ico'))
        self.setWindowTitle("五人小组")
        #相当于初始化这个加载web的控件
        self.browser = QWebEngineView()
        self.browser.setHtml('''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title></title>
            </head>
            <body>
                <h1>Hello PyQt5</h1>
                <h1>Hello PyQt5</h1>
                <h1>hello PyQt5</h1>
                <h1>hello PyQt5</h1>
                <h1>hello PyQt5</h1>
                <h1>Hello PyQt5</h1>

            </body>
        </html>

        ''')
        self.setCentralWidget(self.browser)
if __name__=='__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())