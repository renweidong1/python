import os
from flask import Flask, render_template, request, json, session, make_response, redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql
from datetime import *
pymysql.install_as_MySQLdb()


app = Flask(__name__)


app.config['SECRET_KEY'] = "Sa!l2Q&6$g.>J9\;n_P+=Y(}^$AJ|71jcnjJdivn&(j"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/chatroom'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(20), nullable=False, unique=True)
    nickName = db.Column(db.String(20), nullable=False)
    upwd = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.String(2))
    birthday = db.Column(db.String(20))
    uphone = db.Column(db.String(12))
    realName = db.Column(db.String(30))
    email = db.Column(db.String(50))
    headImg = db.Column(db.String(100))
    uage = db.Column(db.SmallInteger)
    friends = db.relationship('Friend', backref='users', lazy='dynamic')
    messages = db.relationship('Message', backref='users', lazy='dynamic')
    group_messages = db.relationship('GroupMessage', backref='users', lazy='dynamic')

    def to_dic(self):
        dic = {
            "uname": self.uname,
            "uid": self.id,
            "nickName": self.nickName,
            "headImg": self.headImg,
        }
        return dic

    def __init__(self, uname, upwd, nickname):
        self.nickName = nickname
        self.upwd = upwd
        self.uname = uname

    def __repr__(self, uname):
        return '<User %r>' % self.uname


class Friend(db.Model):
    __tablename__ = 'friends'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    friendId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    friendName = db.Column(db.String(30))

    def __init__(self, userid, friendid):
        self.userId = userid
        self.friendId = friendid

    def __repr__(self):
        return '<Friend %r>' % self.userId


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(300))
    send_time = db.Column(db.DateTime, default=datetime.now)
    fromUserId = db.Column(db.Integer, nullable=False)
    toUserId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, from_user_id, message, to_user_id):
        self.message = message
        self.fromUserId = from_user_id
        self.toUserId = to_user_id

    def __repr__(self):
        return "<Message: %r>" % self.message


class GroupMessage(db.Model):
    __tablename__ = 'group_messages'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    message = db.Column(db.String(300))
    send_time = db.Column(db.DateTime, default=datetime.now)

    def to_dic(self):
        dic = {
            "id": self.id,
            "userId": self.user,
            "message": self.message
        }
        return dic

    def __init__(self, user, message):
        self.user = user
        self.message = message

    def __repr__(self):
        return "<GroupMessage: %r>" % self.user


# db.drop_all()
db.create_all()
online_users = {}


@app.route('/', methods=['POST', 'GET'])
def index_views():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        uname = request.form['uname']
        upwd = request.form['upwd']
        user = User.query.filter_by(uname=uname, upwd=upwd).first()
        if user:
            # 登录成功, 将信息保存进session
            session['id'] = user.id
            session['uname'] = user.uname
            headImg = user.headImg
            if user.headImg:
                online_users[str(user.id)] = user.nickName + "#" + user.headImg
            else:
                online_users[str(user.id)] = user.nickName + "#5.jpg"
            return render_template('chat.html', params=locals())
        else:
            # 登录失败, 回到sign_in界面
            return render_template("index.html", errMsg="用户名或密码错误!")


@app.route("/regist", methods=["GET", "POST"])
def regist_views():
    if request.method == 'GET':
        return render_template("regist.html")
    else:
        uname = request.form.get("uname")
        upwd = request.form.get("upwd")
        nick_name = request.form.get("nickName")
        user = User.query.filter_by(uname=uname).first()
        if user:
            return "0"
        else:
            user = User(uname, upwd, nick_name)
            db.session.add(user)
            return "1"


@app.route('/searchFriend')
def search_friend_views():
    uid = request.args.get('uid')
    user = User.query.filter_by(id=uid).first()
    if user:
        # l = []
        # for u in user:
        #     l.append(u.to_dic())
        return json.dumps(user.to_dic())
    else:
        return "noUser"


@app.route("/sendMessage")
def send_message_views():
    send_id = request.args.get("senderId")
    message = request.args.get("message")
    msg = GroupMessage(send_id, message)
    db.session.add(msg)
    return "收到消息"


@app.route("/selectMessages")
def select_message_views():
    messages = GroupMessage.query.order_by('id desc').limit(9).all()
    l = []
    for msg in messages:
        user = User.query.filter_by(id=msg.user).first()
        nick_name = user.nickName
        user_head = user.headImg
        dic = msg.to_dic()
        dic["nickName"] = nick_name
        dic['headImg'] = user_head
        l.append(dic)
    l.reverse()
    # 一个全局的变量online_users的字典存储在线的所有用户键位用户的id, 值为uname
    for key in online_users:
        user = User.query.filter_by(id=key).first()
        online_users[key] = user.nickName + "#" + user.headImg
    l.append(online_users)
    return json.dumps(l)


# 更改头像
@app.route('/changeHead', methods=['GET', 'POST'])
def up_file():
    if request.method == "POST":
        f = request.files['file']
        user_id = request.form['userId']
        user = User.query.filter_by(id=user_id).first()
        # print(userId)
        ext = f.filename.split('.')[1]
        ftime = datetime.now().strftime("%Y%m%d%H%M%S%f")
        filename = ftime + '.' + ext
        print(filename)
        user.headImg = filename
        # 将文件保存至服务器
        basedir = os.path.dirname(__name__)
        upload_path = os.path.join(basedir, "static/head_img", filename)
        f.save(upload_path)
        db.session.add(user)
        return filename


# 退出聊天室
@app.route('/logout')
def logout_views():
    user_id = request.args.get('userId')
    if 'id' in session and 'uname' in session:
        del session['id']
        del session['uname']
    print(online_users)
    del online_users[user_id]
    print(online_users)
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
