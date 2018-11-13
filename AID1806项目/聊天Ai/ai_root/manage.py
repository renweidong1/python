import os

from flask import Flask, render_template, request, make_response, redirect, session, Response
from flask_sqlalchemy import SQLAlchemy
import functools
from utils.tuling_talk import airoot
import time
import datetime
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/airoot'
app.config['SECRET_KEY'] = 'wangdu-airoot'


db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(30), nullable=True)
    passwd = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(30))
    pictures = db.relationship('Picture', backref='users', lazy='dynamic')

    def __init__(self, uname, passwd, email):
        self.uname = uname
        self.passwd = passwd
        self.email = email

    def __repr__(self):
        return "<User %r>"%self.uname



class Picture(db.Model):
    __tablename__ = 'picture'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    img = db.Column(db.String(30))

    def __init__(self, user_id, img):
        self.user_id = user_id
        self.img = img



# 装饰器, 用户登陆验证
def wapper(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        # user = session.get('id')
        user = request.cookies.get('id')
        print(user)
        if not user:
            return redirect('/login')
        return func(*args, **kwargs)
    return inner


# @app.before_request
# def process_request():
#     print('运行拦截')



@app.route('/')
@app.route('/index')
def index():
    if session:
        return render_template('index.html', key=True)
    else:
        return render_template('index.html')



# 登录功能
@app.route('/login')
def login():
    if session:
        return render_template('index.html', key=True)
    else:
        return render_template('login.html')

@app.route('/login-server', methods=['POST'])
def login_server():
    username = request.form['username']
    password = request.form.get('password')
    user = Users.query.filter_by(uname=username).first()
    print(user)
    if user is None:
        return render_template('login.html', msg='用户名不存在')

    if password == user.passwd:
        # 设置 session
        # session['id'] = user.id
        # session['uname'] = user.uname
        # 设置 cookie
        resp = make_response(render_template('index.html', key=True))
        resp.set_cookie('id', str(user.id), 300)
        resp.set_cookie('uname', user.uname, 300)
        session['id'] = user.id
        session['uname'] = user.uname
        return resp
    else:
        return render_template('login.html', msg='密码错误')


# 退出登录状态
@app.route('/delcookie')
def del_cookie_views():
    if 'id' in session and 'uname' in session:
        del session['id']
        del session['uname']

    # del session['talk']
    resp = make_response(render_template('index.html'))
    for key in request.cookies.keys():
        resp.delete_cookie(key)
    return resp


# 注册功能
@app.route('/register')
def register():
    if session:
        return render_template('index.html', key=True)
    else:
        return render_template('register.html')


@app.route('/register-server', methods=['POST', 'GET'])
def register_server():
    if request.method == 'GET':
        username = request.args.get('username')
        user = Users.query.filter_by(uname=username).first()
        print(username, user)
        if user is not None:
            return '用户已存在'
        else:
            return '用户名通过'
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        db.session.add(Users(username, password, email))
        db.session.commit()

        return render_template('success.html', msg='注册')




@app.route('/picture')
def picture_views():
    print(session.get('id'), session.get('uname'))
    user = Users.query.filter_by(id=session.get('id')).first()
    return render_template('picture.html', params=locals())



@app.route('/picture-server', methods=['post'])
def picture_server():
    img = request.files.get('picture')
    # 图片未上传, 返回相册
    if img is None:
        user = Users.query.filter_by(id=session.get('id')).first()
        return render_template('picture.html', params=locals())

    imgType = img.filename.split('.')[-1]
    imgTime = datetime.datetime.now().strftime('%y%m%d%H%M%S')
    imgName = '%s.%s' % (imgTime, imgType)

    print(os.getcwd())

    # 图片保存的地址
    static_url = os.path.join(os.getcwd(), 'static', 'picture')
    # 根据用户ID创建文件夹, 将每个用户的相册分开
    picture_li = os.listdir(static_url)
    id_dir = str(session.get('id'))
    if id_dir not in picture_li:
        os.mkdir(os.path.join(static_url, id_dir))

    img_url = os.path.join(static_url, id_dir, imgName)
    img.save(img_url)

    # 将图片地址和用户ID保存
    db.session.add(Picture(session.get('id'), 'picture/%s/%s'%(id_dir, imgName) ))
    db.session.commit()

    user = Users.query.filter_by(id=session.get('id')).first()

    print(locals())
    return render_template('picture.html', params=locals())


# ai 聊天机器人
@app.route('/airoot')
@wapper
def ai_root_views():
    return render_template('tuling_root.html')

@app.route('/aiserver', methods=['POST'])
def ai_server_views():
    if request.method == 'POST':
        word = request.form.get('word')
        res = airoot().getword(word)
        print(res)
        return res['text']




if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
