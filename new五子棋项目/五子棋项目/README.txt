
基于PyQt5的五子棋编程（人机对弈）
2017年12月23日 03:02:51 ColinFred 阅读数：1674 标签： python 五子棋 pyqt  更多
个人分类： python pyqt
版权声明：本文为博主原创文章，未经博主允许不得转载。	https://blog.csdn.net/windowsyun/article/details/78877939
这篇博客主要是为了学习Python和PyQt，因为对棋类游戏比较热衷，所以从规则较简单的五子棋入手，利用PyQt5实现图形界面，做一个可以进行人机对弈的脚本，最后打包成应用程序。AI的算法打算用神经网络来完成，正在苦学TensorFlow中。

本来我以为五子棋规则很简单，不就像小学时候玩的那样，五个棋子连在一起就赢了嘛，但是后来发现事情并没有那么简单，现在的五子棋有禁手这个规则 ，“三三禁手” 、“四四禁手”、“长连禁手”等等，都是为了限制现行一方必胜。我也不是职业的棋手，对吧，所以禁手什么的就不考虑了，弄个简单的成品出来就很满足了。

代码全是边学习边写的，有瑕疵的地方欢迎提出。

第一步，收集素材
主要就是棋子、棋盘的图片，还有下棋的音效

这里写图片描述

这里写图片描述

这里写图片描述

音效与代码一起在最后给出

第二步，五子棋的逻辑类
收集完素材后，不着急界面的编写，先将五子棋的逻辑写好，界面和逻辑要分开，这很重要。

先想想在五子棋的逻辑类里要有哪些东西。

首先是棋盘，棋盘用15*15的数组表示 
然后是棋子，黑棋用1表示，白棋用2表示，空白就用0表示 
再然后还要获取指定点的坐标，获取指定点的方向等等。 
最重要的也是稍微有点难度的部分就是判断输赢。结合网上的方法和我自己的理解，下面贴出我写的代码，仅供参考。

chessboard.py

# ----------------------------------------------------------------------
# 定义棋子类型，输赢情况
# ----------------------------------------------------------------------
EMPTY = 0
BLACK = 1
WHITE = 2


# ----------------------------------------------------------------------
# 定义棋盘类，绘制棋盘的形状，切换先后手，判断输赢等
# ----------------------------------------------------------------------
class ChessBoard(object):
    def __init__(self):
        self.__board = [[EMPTY for n in range(15)] for m in range(15)]
        self.__dir = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 1), (1, -1)], [(-1, -1), (1, 1)]]
        #                (左      右)      (上       下)     (左下     右上)      (左上     右下)

    def board(self):  # 返回数组对象
        return self.__board

    def draw_xy(self, x, y, state):  # 获取落子点坐标的状态
        self.__board[x][y] = state

    def get_xy_on_logic_state(self, x, y):  # 获取指定点坐标的状态
        return self.__board[x][y]

    def get_next_xy(self, point, direction):  # 获取指定点的指定方向的坐标
        x = point[0] + direction[0]
        y = point[1] + direction[1]
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            return False
        else:
            return x, y

    def get_xy_on_direction_state(self, point, direction):  # 获取指定点的指定方向的状态
        if point is not False:
            xy = self.get_next_xy(point, direction)
            if xy is not False:
                x, y = xy
                return self.__board[x][y]
        return False

    def anyone_win(self, x, y):
        state = self.get_xy_on_logic_state(x, y) # 当前落下的棋是黑棋还是白棋，它的状态存储在state中
        for directions in self.__dir:  # 对米字的4个方向分别检测是否有5子相连的棋
            count = 1  # 初始记录为1，因为刚落下的棋也算
            for direction in directions:  # 对落下的棋子的同一条线的两侧都要检测，结果累积
                point = (x, y)  # 每次循环前都要刷新
                while True:
                    if self.get_xy_on_direction_state(point, direction) == state:
                        count += 1
                        point = self.get_next_xy(point, direction)
                    else:
                        break
            if count >= 5:
                return state
        return EMPTY

    def reset(self):  # 重置
        self.__board = [[EMPTY for n in range(15)] for m in range(15)]
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
将上面的代码放在chessboard.py里面就完成了最基本的操作了。

第三步，利用PyQt5实现图形界面
先想好思路。

目标是做一个简易的五子棋的界面，主窗口只需要一个Widget就可以了

Widget的背景设置为棋盘图片

鼠标每点击一次空白区域，该区域就添加一个标签，在标签中插入棋子图片

因为是人机对弈，玩家执黑棋，所以可以将鼠标变成黑棋图片（这一点比较复杂，需要重写标签类）

整体逻辑是：鼠标点击一次—->换算坐标（UI坐标到棋盘坐标）—->判断坐标是否合理—->黑棋落在棋盘上—->判断是否赢棋—->电脑思考—->电脑下白棋—->判断是否赢棋……

因为AI思考需要时间，所以还需要加一个线程，单独让它计算AI的走法

一些细节问题： 赢棋和输棋怎么处理（对话框）、和棋怎么办（这个先不考虑）、游戏后期棋子非常多的时候容易眼花，不知道AI走到哪怎么办（加一个指示箭头）、音效怎么插入（用QSound）等等

下面给出整体代码：

gobangGUI.py

from chessboard import ChessBoard
from ai import searcher

WIDTH = 540
HEIGHT = 540
MARGIN = 22
GRID = (WIDTH - 2 * MARGIN) / (15 - 1)
PIECE = 34
EMPTY = 0
BLACK = 1
WHITE = 2


import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QPainter
from PyQt5.QtMultimedia import QSound


# ----------------------------------------------------------------------
# 定义线程类执行AI的算法
# ----------------------------------------------------------------------
class AI(QtCore.QThread):
    finishSignal = QtCore.pyqtSignal(int, int)

    # 构造函数里增加形参
    def __init__(self, board, parent=None):
        super(AI, self).__init__(parent)
        self.board = board

    # 重写 run() 函数
    def run(self):
        self.ai = searcher()
        self.ai.board = self.board
        score, x, y = self.ai.search(2, 2)
        self.finishSignal.emit(x, y)


# ----------------------------------------------------------------------
# 重新定义Label类
# ----------------------------------------------------------------------
class LaBel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMouseTracking(True)

    def enterEvent(self, e):
        e.ignore()


class GoBang(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.chessboard = ChessBoard()  # 棋盘类

        palette1 = QPalette()  # 设置棋盘背景
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('img/chessboard.jpg')))
        self.setPalette(palette1)
        # self.setStyleSheet("board-image:url(img/chessboard.jpg)")  # 不知道这为什么不行
        self.setCursor(Qt.PointingHandCursor)  # 鼠标变成手指形状
        self.sound_piece = QSound("sound/luozi.wav")  # 加载落子音效
        self.sound_win = QSound("sound/win.wav")  # 加载胜利音效
        self.sound_defeated = QSound("sound/defeated.wav")  # 加载失败音效

        self.resize(WIDTH, HEIGHT)  # 固定大小 540*540
        self.setMinimumSize(QtCore.QSize(WIDTH, HEIGHT))
        self.setMaximumSize(QtCore.QSize(WIDTH, HEIGHT))

        self.setWindowTitle("GoBang")  # 窗口名称
        self.setWindowIcon(QIcon('img/black.png'))  # 窗口图标

        # self.lb1 = QLabel('            ', self)
        # self.lb1.move(20, 10)

        self.black = QPixmap('img/black.png')
        self.white = QPixmap('img/white.png')

        self.piece_now = BLACK  # 黑棋先行
        self.my_turn = True  # 玩家先行
        self.step = 0  # 步数
        self.x, self.y = 1000, 1000

        self.mouse_point = LaBel(self)  # 将鼠标图片改为棋子
        self.mouse_point.setScaledContents(True)
        self.mouse_point.setPixmap(self.black)  #加载黑棋
        self.mouse_point.setGeometry(270, 270, PIECE, PIECE)
        self.pieces = [LaBel(self) for i in range(225)]  # 新建棋子标签，准备在棋盘上绘制棋子
        for piece in self.pieces:
            piece.setVisible(True)  # 图片可视
            piece.setScaledContents(True)  #图片大小根据标签大小可变

        self.mouse_point.raise_()  # 鼠标始终在最上层
        self.ai_down = True  # AI已下棋，主要是为了加锁，当值是False的时候说明AI正在思考，这时候玩家鼠标点击失效，要忽略掉 mousePressEvent

        self.setMouseTracking(True)
        self.show()

    def paintEvent(self, event): # 画出指示箭头
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def mouseMoveEvent(self, e): # 黑色棋子随鼠标移动
        # self.lb1.setText(str(e.x()) + ' ' + str(e.y()))
        self.mouse_point.move(e.x() - 16, e.y() - 16)

    def mousePressEvent(self, e):  # 玩家下棋
        if e.button() == Qt.LeftButton and self.ai_down == True:
            x, y = e.x(), e.y()  # 鼠标坐标
            i, j = self.coordinate_transform_pixel2map(x, y)  # 对应棋盘坐标
            if not i is None and not j is None:  # 棋子落在棋盘上，排除边缘
                if self.chessboard.get_xy_on_logic_state(i, j) == EMPTY:  # 棋子落在空白处
                    self.draw(i, j)
                    self.ai_down = False
                    board = self.chessboard.board()
                    self.AI = AI(board)  # 新建线程对象，传入棋盘参数
                    self.AI.finishSignal.connect(self.AI_draw)  # 结束线程，传出参数
                    self.AI.start()  # run

    def AI_draw(self, i, j):
        if self.step != 0:
            self.draw(i, j)  # AI
            self.x, self.y = self.coordinate_transform_map2pixel(i, j)
        self.ai_down = True
        self.update()

    def draw(self, i, j):
        x, y = self.coordinate_transform_map2pixel(i, j)

        if self.piece_now == BLACK:
            self.pieces[self.step].setPixmap(self.black)  # 放置黑色棋子
            self.piece_now = WHITE
            self.chessboard.draw_xy(i, j, BLACK)
        else:
            self.pieces[self.step].setPixmap(self.white)  # 放置白色棋子
            self.piece_now = BLACK
            self.chessboard.draw_xy(i, j, WHITE)

        self.pieces[self.step].setGeometry(x, y, PIECE, PIECE)  # 画出棋子
        self.sound_piece.play()  # 落子音效
        self.step += 1  # 步数+1

        winner = self.chessboard.anyone_win(i, j)  # 判断输赢
        if winner != EMPTY:
            self.mouse_point.clear()
            self.gameover(winner)

    def drawLines(self, qp):  # 指示AI当前下的棋子
        if self.step != 0:
            pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
            qp.setPen(pen)
            qp.drawLine(self.x - 5, self.y - 5, self.x + 3, self.y + 3)
            qp.drawLine(self.x + 3, self.y, self.x + 3, self.y + 3)
            qp.drawLine(self.x, self.y + 3, self.x + 3, self.y + 3)

    def coordinate_transform_map2pixel(self, i, j):
        # 从 chessMap 里的逻辑坐标到 UI 上的绘制坐标的转换
        return MARGIN + j * GRID - PIECE / 2, MARGIN + i * GRID - PIECE / 2

    def coordinate_transform_pixel2map(self, x, y):
        # 从 UI 上的绘制坐标到 chessMap 里的逻辑坐标的转换
        i, j = int(round((y - MARGIN) / GRID)), int(round((x - MARGIN) / GRID))
        # 有MAGIN, 排除边缘位置导致 i,j 越界
        if i < 0 or i >= 15 or j < 0 or j >= 15:
            return None, None
        else:
            return i, j

    def gameover(self, winner):
        if winner == BLACK:
            self.sound_win.play()
            reply = QMessageBox.question(self, 'You Win!', 'Continue?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            self.sound_defeated.play()
            reply = QMessageBox.question(self, 'You Lost!', 'Continue?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:  # 复位
            self.piece_now = BLACK
            self.mouse_point.setPixmap(self.black)
            self.step = 0
            for piece in self.pieces:
                piece.clear()
            self.chessboard.reset()
            self.update()
        else:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoBang()
    sys.exit(app.exec_())
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
简要说明一下

class AI(QtCore.QThread):
    finishSignal = QtCore.pyqtSignal(int, int)

    # 构造函数里增加形参
    def __init__(self, board, parent=None):
        super(AI, self).__init__(parent)
        self.board = board

    # 重写 run() 函数
    def run(self):
        self.ai = searcher()
        self.ai.board = self.board
        score, x, y = self.ai.search(2, 2)
        self.finishSignal.emit(x, y)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
这里加了一个线程执行AI的计算，前面有个 from ai import searcher ，ai还没有写，先从网上找了一个博弈的算法。searcher（）就是AI类。该线程传入参数是 board 就是棋盘状态。调用self.ai.search(2, 2)，第一个2是博弈树的深度，值越大AI越聪明，但是计算时间也越长。第二个2是说电脑执白棋，如果为1则是黑棋。线程结束后传入参数 x, y 就是AI计算后线程传出的参数。

class LaBel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMouseTracking(True)

    def enterEvent(self, e):
        e.ignore()
1
2
3
4
5
6
7
重新定义Label类是为了让黑棋图片随着鼠标的移动而移动。如果直接用QLabel的话不能达到预期的效果，具体为什么自己去摸索吧。

最后是所有的脚本代码，在这之后还会继续学习，将脚本打包成可执行文件，并且加入神经网络的算法。

https://github.com/ColinFred/GoBang#gobang