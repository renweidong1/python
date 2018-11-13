
����PyQt5���������̣��˻����ģ�
2017��12��23�� 03:02:51 ColinFred �Ķ�����1674 ��ǩ�� python ������ pyqt  ����
���˷��ࣺ python pyqt
��Ȩ����������Ϊ����ԭ�����£�δ������������ת�ء�	https://blog.csdn.net/windowsyun/article/details/78877939
��ƪ������Ҫ��Ϊ��ѧϰPython��PyQt����Ϊ��������Ϸ�Ƚ����ԣ����Դӹ���ϼ򵥵����������֣�����PyQt5ʵ��ͼ�ν��棬��һ�����Խ����˻����ĵĽű����������Ӧ�ó���AI���㷨����������������ɣ����ڿ�ѧTensorFlow�С�

��������Ϊ���������ܼ򵥣�������Сѧʱ����������������������һ���Ӯ������Ǻ����������鲢û����ô�򵥣����ڵ��������н���������� �����������֡� �������Ľ��֡������������֡��ȵȣ�����Ϊ����������һ����ʤ����Ҳ����ְҵ�����֣��԰ɣ����Խ���ʲô�ľͲ������ˣ�Ū���򵥵ĳ�Ʒ�����ͺ������ˡ�

����ȫ�Ǳ�ѧϰ��д�ģ���覴õĵط���ӭ�����

��һ�����ռ��ز�
��Ҫ�������ӡ����̵�ͼƬ�������������Ч

����дͼƬ����

����дͼƬ����

����дͼƬ����

��Ч�����һ����������

�ڶ�������������߼���
�ռ����زĺ󣬲��ż�����ı�д���Ƚ���������߼�д�ã�������߼�Ҫ�ֿ��������Ҫ��

����������������߼�����Ҫ����Щ������

���������̣�������15*15�������ʾ 
Ȼ�������ӣ�������1��ʾ��������2��ʾ���հ׾���0��ʾ 
��Ȼ��Ҫ��ȡָ��������꣬��ȡָ����ķ���ȵȡ� 
����Ҫ��Ҳ����΢�е��ѶȵĲ��־����ж���Ӯ��������ϵķ��������Լ�����⣬����������д�Ĵ��룬�����ο���

chessboard.py

# ----------------------------------------------------------------------
# �����������ͣ���Ӯ���
# ----------------------------------------------------------------------
EMPTY = 0
BLACK = 1
WHITE = 2


# ----------------------------------------------------------------------
# ���������࣬�������̵���״���л��Ⱥ��֣��ж���Ӯ��
# ----------------------------------------------------------------------
class ChessBoard(object):
    def __init__(self):
        self.__board = [[EMPTY for n in range(15)] for m in range(15)]
        self.__dir = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 1), (1, -1)], [(-1, -1), (1, 1)]]
        #                (��      ��)      (��       ��)     (����     ����)      (����     ����)

    def board(self):  # �����������
        return self.__board

    def draw_xy(self, x, y, state):  # ��ȡ���ӵ������״̬
        self.__board[x][y] = state

    def get_xy_on_logic_state(self, x, y):  # ��ȡָ���������״̬
        return self.__board[x][y]

    def get_next_xy(self, point, direction):  # ��ȡָ�����ָ�����������
        x = point[0] + direction[0]
        y = point[1] + direction[1]
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            return False
        else:
            return x, y

    def get_xy_on_direction_state(self, point, direction):  # ��ȡָ�����ָ�������״̬
        if point is not False:
            xy = self.get_next_xy(point, direction)
            if xy is not False:
                x, y = xy
                return self.__board[x][y]
        return False

    def anyone_win(self, x, y):
        state = self.get_xy_on_logic_state(x, y) # ��ǰ���µ����Ǻ��廹�ǰ��壬����״̬�洢��state��
        for directions in self.__dir:  # �����ֵ�4������ֱ����Ƿ���5����������
            count = 1  # ��ʼ��¼Ϊ1����Ϊ�����µ���Ҳ��
            for direction in directions:  # �����µ����ӵ�ͬһ���ߵ����඼Ҫ��⣬����ۻ�
                point = (x, y)  # ÿ��ѭ��ǰ��Ҫˢ��
                while True:
                    if self.get_xy_on_direction_state(point, direction) == state:
                        count += 1
                        point = self.get_next_xy(point, direction)
                    else:
                        break
            if count >= 5:
                return state
        return EMPTY

    def reset(self):  # ����
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
������Ĵ������chessboard.py����������������Ĳ����ˡ�

������������PyQt5ʵ��ͼ�ν���
�����˼·��

Ŀ������һ�����׵�������Ľ��棬������ֻ��Ҫһ��Widget�Ϳ�����

Widget�ı�������Ϊ����ͼƬ

���ÿ���һ�οհ����򣬸���������һ����ǩ���ڱ�ǩ�в�������ͼƬ

��Ϊ���˻����ģ����ִ���壬���Կ��Խ�����ɺ���ͼƬ����һ��Ƚϸ��ӣ���Ҫ��д��ǩ�ࣩ

�����߼��ǣ������һ�Ρ�->�������꣨UI���굽�������꣩��->�ж������Ƿ����->�������������ϡ�->�ж��Ƿ�Ӯ�塪->����˼����->�����°��塪->�ж��Ƿ�Ӯ�塭��

��ΪAI˼����Ҫʱ�䣬���Ի���Ҫ��һ���̣߳�������������AI���߷�

һЩϸ�����⣺ Ӯ���������ô�����Ի��򣩡�������ô�죨����Ȳ����ǣ�����Ϸ�������ӷǳ����ʱ�������ۻ�����֪��AI�ߵ�����ô�죨��һ��ָʾ��ͷ������Ч��ô���루��QSound���ȵ�

�������������룺

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
# �����߳���ִ��AI���㷨
# ----------------------------------------------------------------------
class AI(QtCore.QThread):
    finishSignal = QtCore.pyqtSignal(int, int)

    # ���캯���������β�
    def __init__(self, board, parent=None):
        super(AI, self).__init__(parent)
        self.board = board

    # ��д run() ����
    def run(self):
        self.ai = searcher()
        self.ai.board = self.board
        score, x, y = self.ai.search(2, 2)
        self.finishSignal.emit(x, y)


# ----------------------------------------------------------------------
# ���¶���Label��
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

        self.chessboard = ChessBoard()  # ������

        palette1 = QPalette()  # �������̱���
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('img/chessboard.jpg')))
        self.setPalette(palette1)
        # self.setStyleSheet("board-image:url(img/chessboard.jpg)")  # ��֪����Ϊʲô����
        self.setCursor(Qt.PointingHandCursor)  # �������ָ��״
        self.sound_piece = QSound("sound/luozi.wav")  # ����������Ч
        self.sound_win = QSound("sound/win.wav")  # ����ʤ����Ч
        self.sound_defeated = QSound("sound/defeated.wav")  # ����ʧ����Ч

        self.resize(WIDTH, HEIGHT)  # �̶���С 540*540
        self.setMinimumSize(QtCore.QSize(WIDTH, HEIGHT))
        self.setMaximumSize(QtCore.QSize(WIDTH, HEIGHT))

        self.setWindowTitle("GoBang")  # ��������
        self.setWindowIcon(QIcon('img/black.png'))  # ����ͼ��

        # self.lb1 = QLabel('            ', self)
        # self.lb1.move(20, 10)

        self.black = QPixmap('img/black.png')
        self.white = QPixmap('img/white.png')

        self.piece_now = BLACK  # ��������
        self.my_turn = True  # �������
        self.step = 0  # ����
        self.x, self.y = 1000, 1000

        self.mouse_point = LaBel(self)  # �����ͼƬ��Ϊ����
        self.mouse_point.setScaledContents(True)
        self.mouse_point.setPixmap(self.black)  #���غ���
        self.mouse_point.setGeometry(270, 270, PIECE, PIECE)
        self.pieces = [LaBel(self) for i in range(225)]  # �½����ӱ�ǩ��׼���������ϻ�������
        for piece in self.pieces:
            piece.setVisible(True)  # ͼƬ����
            piece.setScaledContents(True)  #ͼƬ��С���ݱ�ǩ��С�ɱ�

        self.mouse_point.raise_()  # ���ʼ�������ϲ�
        self.ai_down = True  # AI�����壬��Ҫ��Ϊ�˼�������ֵ��False��ʱ��˵��AI����˼������ʱ����������ʧЧ��Ҫ���Ե� mousePressEvent

        self.setMouseTracking(True)
        self.show()

    def paintEvent(self, event): # ����ָʾ��ͷ
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def mouseMoveEvent(self, e): # ��ɫ����������ƶ�
        # self.lb1.setText(str(e.x()) + ' ' + str(e.y()))
        self.mouse_point.move(e.x() - 16, e.y() - 16)

    def mousePressEvent(self, e):  # �������
        if e.button() == Qt.LeftButton and self.ai_down == True:
            x, y = e.x(), e.y()  # �������
            i, j = self.coordinate_transform_pixel2map(x, y)  # ��Ӧ��������
            if not i is None and not j is None:  # �������������ϣ��ų���Ե
                if self.chessboard.get_xy_on_logic_state(i, j) == EMPTY:  # �������ڿհ״�
                    self.draw(i, j)
                    self.ai_down = False
                    board = self.chessboard.board()
                    self.AI = AI(board)  # �½��̶߳��󣬴������̲���
                    self.AI.finishSignal.connect(self.AI_draw)  # �����̣߳���������
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
            self.pieces[self.step].setPixmap(self.black)  # ���ú�ɫ����
            self.piece_now = WHITE
            self.chessboard.draw_xy(i, j, BLACK)
        else:
            self.pieces[self.step].setPixmap(self.white)  # ���ð�ɫ����
            self.piece_now = BLACK
            self.chessboard.draw_xy(i, j, WHITE)

        self.pieces[self.step].setGeometry(x, y, PIECE, PIECE)  # ��������
        self.sound_piece.play()  # ������Ч
        self.step += 1  # ����+1

        winner = self.chessboard.anyone_win(i, j)  # �ж���Ӯ
        if winner != EMPTY:
            self.mouse_point.clear()
            self.gameover(winner)

    def drawLines(self, qp):  # ָʾAI��ǰ�µ�����
        if self.step != 0:
            pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
            qp.setPen(pen)
            qp.drawLine(self.x - 5, self.y - 5, self.x + 3, self.y + 3)
            qp.drawLine(self.x + 3, self.y, self.x + 3, self.y + 3)
            qp.drawLine(self.x, self.y + 3, self.x + 3, self.y + 3)

    def coordinate_transform_map2pixel(self, i, j):
        # �� chessMap ����߼����굽 UI �ϵĻ��������ת��
        return MARGIN + j * GRID - PIECE / 2, MARGIN + i * GRID - PIECE / 2

    def coordinate_transform_pixel2map(self, x, y):
        # �� UI �ϵĻ������굽 chessMap ����߼������ת��
        i, j = int(round((y - MARGIN) / GRID)), int(round((x - MARGIN) / GRID))
        # ��MAGIN, �ų���Եλ�õ��� i,j Խ��
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

        if reply == QMessageBox.Yes:  # ��λ
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
��Ҫ˵��һ��

class AI(QtCore.QThread):
    finishSignal = QtCore.pyqtSignal(int, int)

    # ���캯���������β�
    def __init__(self, board, parent=None):
        super(AI, self).__init__(parent)
        self.board = board

    # ��д run() ����
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
�������һ���߳�ִ��AI�ļ��㣬ǰ���и� from ai import searcher ��ai��û��д���ȴ���������һ�����ĵ��㷨��searcher��������AI�ࡣ���̴߳�������� board ��������״̬������self.ai.search(2, 2)����һ��2�ǲ���������ȣ�ֵԽ��AIԽ���������Ǽ���ʱ��ҲԽ�����ڶ���2��˵����ִ���壬���Ϊ1���Ǻ��塣�߳̽���������� x, y ����AI������̴߳����Ĳ�����

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
���¶���Label����Ϊ���ú���ͼƬ���������ƶ����ƶ������ֱ����QLabel�Ļ����ܴﵽԤ�ڵ�Ч��������Ϊʲô�Լ�ȥ�����ɡ�

��������еĽű����룬����֮�󻹻����ѧϰ�����ű�����ɿ�ִ���ļ������Ҽ�����������㷨��

https://github.com/ColinFred/GoBang#gobang