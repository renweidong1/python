from flask import Flask, make_response, request, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/dict_06"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SECRET_KEY'] = 'INPUT A STRING'
db=SQLAlchemy(app)

import pymysql
pymysql.install_as_MySQLdb()

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    pwd = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(32), nullable=False)

    def __init__(self,name,pwd,email):
        self.name = name
        self.pwd = pwd
        self.email = email

    def __repr__(self):
        return "<Users %r>" % self.name

class Hist(db.Model):
    __tablename__ = "hist"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    word = db.Column(db.String(64), nullable=False)
    time = db.Column(db.DateTime)

    def __init__(self, name, word, time):
        self.name = name
        self.word = word
        self.time = time

class Words(db.Model):
    __tablename__ = "words"
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(64))
    jieshi = db.Column(db.String(220))
    yinbiao = db.Column(db.String(300))
    liju = db.Column(db.Text)

    def __init__(self, word, jieshi, yinbiao, liju):
        self.word = word
        self.jieshi = jieshi
        self.yinbiao = yinbiao
        self.liju = liju
    def __repr__(self):
        return "<Words %s>" % self.word

# db.drop_all()
db.create_all()


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        # 判断之前是否有成功登录过(id和uname是否存在于cookie上)
        if 'uname' in request.cookies and 'upwd' in request.cookies:
            uname = request.cookies['uname']
            upwd = request.cookies['upwd']
        return render_template('login.html',params=locals())
    else:
        # 1.接收用户名和密码
        uname = request.form['uname']
        upwd = request.form['upwd']
        # 2.验证用户名和密码是否正确(数据库查询)
        user = Users.query.filter_by(name=uname,pwd=upwd).first()
        # 3.如果正确的话,判断是否记住密码
        if user:
            resp = redirect('/index')
            # 登录成功
            session['uname'] = uname
            session['upwd'] = upwd
            if 'isSaved' in request.form:
                # 将　id 和　uname 保存进cookie
                m_age = 60*60*24*365
                resp.set_cookie('uname',uname,max_age=m_age)
                resp.set_cookie('upwd',upwd,max_age=m_age)
            return resp
        else:
            # 4.如果不正确的话,则给出提示
            err = '用户名或密码不正确'

            return render_template('login.html',params=locals())


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        uname = request.form['uname']
        uemail = request.form['uemail']
        upwd = request.form['upwd']
        user = Users(uname,upwd,uemail)
        db.session.add(user)
        return render_template('login.html',params=locals())

@app.route('/forgot')
def forgot():
    return render_template('forgot-password.html')

@app.route('/sign_out')
def sign_out():
    if 'uname' in session and 'upwd' in session:
        del session['uname']
        del session['upwd']
    return redirect('/index')

@app.route('/username_verification',methods=['POST'])
def username_verification():
    uname=request.form['uname']
    user = Users.query.filter_by(name=uname).first()
    if user:
        return "该用户名称已存在"
    else:
        return "✔"

@app.route('/email_verification',methods=['POST'])
def email_verification():
    email=request.form['uemail']
    user = Users.query.filter_by(email=email).first()
    if user:
        return "该邮箱已经被注册"
    else:
        return "✔"

@app.route('/')
@app.route('/index')
def index():
    # 判断用户是否登录成功
    if 'uname' in session and 'upwd' in session:
        uname = session['uname']
    return render_template('index.html', params=locals())

@app.route('/dict_kinds')
def dict_kinds():
    if 'uname' in session and 'upwd' in session:
        uname = session['uname']
    return render_template('dict.html',params=locals())

@app.route('/history_kinds')
def history_kinds():
    if 'uname' in session and 'upwd' in session:
        uname = session['uname']
    return render_template('history.html',params=locals())

@app.route('/history_show')
def history_show():
    if 'uname' in session and 'upwd' in session:
        uname = session['uname']
        dict = request.args.get('dict')
        print(dict)
        hists = Hist.query.filter_by(name=uname).all()
        print(hists)
        if dict == "ch-en":
            return render_template('history_show.html',params=locals())

    else:
        return redirect('/login')

@app.route('/history_show_entire')
def history_show_entire():
    if 'uname' in session and 'upwd' in session:
        uname = session['uname']
        word = request.args.get('word')
        dict = request.args.get('dict')
        id = request.args.get('id')
        print(dict)

        word_sea = Words.query.filter_by(word=word).first()

        # 获取解释列表
        if word_sea:
            if word_sea.jieshi:
                jieshi = word_sea.jieshi.split('||||')
                jieshis = []

                for i in jieshi:
                    jieshis.append(i.split('||'))
            # 获取音标列表
            if word_sea.yinbiao:
                yinbiao = word_sea.yinbiao.split('||||')
                yinbiao_mei = yinbiao[0].split('||')
                yinbiao_ying = yinbiao[1].split('||')
            # 获取例句列表
            if word_sea.liju:
                liju = word_sea.liju.split('||||')
                lijus = []
                for j in liju:
                    lijus.append(j.split('||'))
        # hist = Hist.query.filter_by(word=word,name=uname).first()
        hist = Hist.query.filter_by(id=id).first()

        prevword = Hist.query.filter(Hist.id<hist.id,Hist.name==uname).order_by('id desc').first()

        nextword = Hist.query.filter(Hist.id>hist.id,Hist.name==uname).first()

        return render_template('history_show_entire.html',params=locals())



@app.route('/search_before',methods=['GET','POST'])
def search_before():
    dict = request.args.get('dict')
    if 'uname' in session and 'upwd' in session:
        uname = session['uname']
    if request.method == 'GET':
        if dict == "ch-en":
            return render_template('search_before.html',params=locals())
        return "not found"
    else:
        dict = request.form.get('dict')
        word = request.form['searchword']
        word_sea = Words.query.filter_by(word=word).first()
        # 获取解释列表
        if word_sea:
            if word_sea.jieshi:
                jieshi = word_sea.jieshi.split('||||')
                jieshis = []

                for i in jieshi:
                    jieshis.append(i.split('||'))
            # 获取音标列表
            if word_sea.yinbiao:
                yinbiao = word_sea.yinbiao.split('||||')
                yinbiao_mei = yinbiao[0].split('||')
                yinbiao_ying = yinbiao[1].split('||')
            # 获取例句列表
            if word_sea.liju:
                liju = word_sea.liju.split('||||')
                lijus = []
                for j in liju:
                    lijus.append(j.split('||'))
        # 存入历史
            import datetime
            if 'uname' in session and 'upwd' in session:
                uname = session['uname']
                hist = Hist(session['uname'],word_sea.word,datetime.datetime.now())
                db.session.add(hist)

        return render_template('search.html',params=locals())



# @app.route('/search',methods=['GET','POST'])
# def search():
#     word = request.form['word']
#     word_sea = Words.query.filter_by(word=word).first()
#
#     if word_sea:
#         print(word_sea)
#         return word_sea.interpret
#     else:
#         return ""


@app.route('/game_kinds')
def game_kinds():
    if 'uname' in session and 'upwd' in session:
        uname = session['uname']
    return render_template('game.html',params=locals())

@app.route('/game')
def games():
    if 'uname' in session and 'upwd' in session:
        uname = session['uname']
    game = request.args.get('game')
    if game == 'sea-fish':
        return render_template('hi_fish.html',params=locals())




if __name__ == '__main__':
    app.run(debug=True,port=5500)
