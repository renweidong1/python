# [#将棋盘信息以列表形式存储，0为空白1为黑子2为白子
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def victory_or_defeat(chess_color,temp_x,temp_y,L,call_num):
    # temp_x = x 临时变量提供横向下标
    # temp_y = y 临时变量提供纵向下标      
    plus_or_minus = True    #判断下标是增还是减
    chess_num = 1           #记录棋子相连的个数,以此坐标为原点
    x, y = temp_x, temp_y   #记录原坐标，以便重新赋值
    while True:
        if call_num == 0:#第一次调用，做横向判断
            if plus_or_minus:
                temp_x += 1
            else:
                temp_x -= 1
        if call_num == 1:#第二次调用，做纵向判断
            if plus_or_minus:
                temp_y += 1
            else:
                temp_y -= 1
        if call_num == 2:#第三次调用，做正斜(\)判断
            if plus_or_minus:
                temp_x += 1
                temp_y += 1
            else:
                temp_x -= 1
                temp_y -= 1
        if call_num == 3:#第四次调用，做反斜(/)判断
            if plus_or_minus:
                temp_x -= 1
                temp_y += 1
            else:
                temp_x += 1
                temp_y -= 1
        if plus_or_minus:
            if (temp_x < 0) or (temp_x == 15) or (temp_y == 15) or (L[temp_y*15+temp_x] != chess_color):
                plus_or_minus = False   #改变判断条件
                temp_x, temp_y = x, y   #下标重新赋值
                continue       #判断条件发生变化结束本次循环
            chess_num += 1
        else:
            if (temp_x < 0) or (temp_x == 15) or (temp_y < 0) or (L[temp_y*15+temp_x] != chess_color):
                if chess_num == 5:
                    return 1
                return 0
            chess_num += 1


def chess(x,y,L,black = True):
    #判断要下的位置是否已有棋子
    if L[y*15+x] != 0:
        return -1 #返回-1表示该处已有棋子
    #黑子方
    if black:
        L[y*15+x] = 1 
        chess_color = 1     #判断是哪一方的棋子
    #白子方
    else:
        L[y*15+x] = 2
        chess_color = 2     #判断是哪一方的棋子
    for i in range(4):
        victory = victory_or_defeat(chess_color,x,y,L,i)
        if victory == 1:
            return 1 #返回1表示胜利
    return 0#返回0表示继续