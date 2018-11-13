from flask import Flask, render_template, request, redirect, session, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import *
import pymysql
from wuziqi import chess

pymysql.install_as_MySQLdb()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/gobang'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SECRET_KEY'] = "MY USER"
socketio = SocketIO(app)
db=SQLAlchemy(app)


class Players(db.Model):
    __tablename__='players'
    id = db.Column(db.Integer,primary_key=True)
    pname = db.Column(db.String(30),nullable=False,unique=True)
    ppwd = db.Column(db.String(50),nullable=False)
    game_num = db.Column(db.Integer)
    game_victory = db.Column(db.Integer)
    def __init__(self,pname,ppwd,game_nem,game_victory):
        self.pname = pname
        self.ppwd = ppwd
        self.game_num = game_nem
        self.game_victory = game_victory


# db.drop_all()
db.create_all()


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html',solely='-1')
    else:
        pname = request.form.get('uname')
        ppwd = request.form.get('pwd1')
        ppwd2 = request.form.get('pwd2')
        user_num = Players.query.filter_by(pname=pname).count()
        if user_num > 0:
            return render_template('register.html',solely='0')
        elif ppwd != ppwd2:
            return render_template('register.html', solely='1')
        else:
            players = Players(pname,ppwd,0,0)
            db.session.add(players)
            return render_template('index.html',login_ok='0')


@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html',login_ok='0')
    else:
        # 1.接收用户名和密码
        pname = request.form['uname']
        ppwd = request.form['upwd']
        # 2.验证用户名和密码是否正确(数据库查询)
        player = Players.query.filter_by(pname=pname,ppwd=ppwd).first()
        if player:
            if pname in login_user:
                #如果用户已登录，给出提示
                return render_template('index.html',login_ok='2')
            # 登录成功
            login_user.append(pname)#记录所有的登录用户
            if not temp:
                temp.append(pname)
            else:
                L = [0 for _ in range(15*15)]#存储棋盘信息
                room_user[(temp[0],pname)] = L#用户名为键，棋盘信息为值
                print(room_user)
                temp.pop(0)
            return render_template('wait_login.html',username=pname)
        else:
            # 4.如果不正确的话,则给出提示
            return render_template('index.html',login_ok='1')


@app.route('/game',methods=["GET","POST"])
def game_wiq():
    if request.method == "GET":
        return render_template('index.html')
    else:
        user_name = request.form['users']
        players = Players.query.filter_by(pname=user_name).first()
        # vic = players['game_victory']
        # num = players['game_num']
        # print(vic)
        # print(num)
        for users in room_user:
            if user_name in users:
                if user_name == users[1]:
                    #二号玩家白色方
                    return render_template('wiq.html',name=user_name,isblack='0',color='白子')
                else:
                    #一号玩家黑色方
                    return render_template('wiq.html',name=user_name,isblack='1',color='黑子')


@socketio.on('go_game')
def go_game(data):
    user_name = data['name']
    for users in room_user:
        if user_name in users:
            if user_name == users[1]:
                # 当第二个玩家按下对战，通知对手与自己进入
                emit("begin",{"wait":'0','name':user_name,'name1':users[0]},broadcast=True)
                break
            else:
                #第一位玩家按下对战，等待第二位
                emit('begin', {"wait": '1'})
                break
    else:
        # 尚为匹配到对手
        emit('begin',{"wait":'1'})


@socketio.on('msg_handling')
def on_join(data):
    #获取用户名
    user_name = data['name']
    #横坐标
    x = int(data['x'])
    #纵坐标
    y = int(data['y'])
    print((x,y))
    for users in room_user:
        if user_name in users:
            #白色方
            if user_name == users[1]:
                result = chess(x,y,room_user[users],False)
                if result == -1:
                    emit('result_reduction', {'name1':'','names': user_name,'x':"",'y':"",'victory':''}, broadcast=True)
                if result == 0:
                    emit('result_reduction', {'name1':users[1],'names': users[0],"x":x,'y':y,'black':'0','victory':''},broadcast=True)
                if result == 1:
                    emit('result_reduction', {'name1':users[1],'names': users[0],"x":x,'y':y,'black':'0','victory':'2'},broadcast=True)
                break
            #黑色方
            else:
                result = chess(x,y,room_user[users])
                if result == -1:
                    emit('result_reduction', {'name1':'','names': user_name,'x':"",'y':"",'victory':''}, broadcast=True)
                if result == 0:
                    emit('result_reduction', {'name1':users[0],'names': users[1],"x":x,'y':y,'black':'1','victory':''},broadcast=True)
                if result == 1:
                    emit('result_reduction', {'name1':users[0],'names': users[1],"x":x,'y':y,'black':'1','victory':'1'},broadcast=True)
                break


if __name__ == "__main__":
    login_user = []#记录所有已登录的用户
    temp=[]#等待对手时暂时记录自己的信息
    room_user = {}#进入对战的用户,用户名为键，棋盘信息为值
    socketio.run(app,host='0.0.0.0',port=int("5000"),debug=True)