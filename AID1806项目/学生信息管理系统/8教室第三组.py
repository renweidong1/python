# 初始化项目
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo, askokcancel
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
# 配置连接数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://mysql:Xwp910620!f@119.147.172.235:34307/student_project"
# 配置数据库更改时自动提交
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# 数据库初始化
db = SQLAlchemy(app)

# 控制所有的实体类

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30))
    # 反向引用：返回与课程相关的teacher信息
    teachers = db.relationship('Teacher', backref="course", lazy="dynamic")
    scores = db.relationship(
        'Score',
        secondary="course_score",
        backref=db.backref(
            "course_score",
            lazy="dynamic"
        )
    )

    def __init__(self,cname):
        self.cname=cname


class Teacher(db.Model):
    __tablename__="teacher"
    id = db.Column(db.Integer,primary_key=True)
    relname = db.Column(db.String(30))
    tpwd = db.Column(db.String(50),nullable=False)
    tname = db.Column(db.String(50),nullable=False)
    tage = db.Column(db.Integer)
    ttel = db.Column(db.String(11),nullable=False)
    # 引用course.id增加外键列
    course_id = db.Column(db.Integer,db.ForeignKey('course.id'))

    def __init__(self, tname, tpwd, ttel):
        self.tname = tname
        self.tpwd = tpwd
        self.ttel = ttel

    def __repr__(self):
        return "<Teacher %r>"%self.tname


class Student(db.Model):
    __tablename__="student"
    id = db.Column(db.Integer, primary_key=True)
    relname = db.Column(db.String(30))
    spwd = db.Column(db.String(50), nullable=False)
    sname = db.Column(db.String(50), nullable=False)
    sage = db.Column(db.Integer)
    stel = db.Column(db.String(11), nullable=False)
    scores = db.relationship(
        'Score',
        secondary="student_score",
        lazy="dynamic",
        backref=db.backref(
            "students",
            lazy="dynamic"
        )
    )
    courses = db.relationship(
        'Course',
        secondary='student_course',
        lazy='dynamic',
        backref=db.backref(
            'students',
            lazy='dynamic'
        )
    )

    def __init__(self, sname, spwd, stel):
        self.sname = sname
        self.spwd = spwd
        self.stel = stel

    def __repr__(self):
        return "<String %r>" % self.sname


class Score(db.Model):
    __tablename__="score"
    id = db.Column(db.Integer, primary_key=True)
    scores = db.Column(db.Integer)

    def __init__(self, scores):
        self.scores = scores

    def __repr__(self):
        return "<Score %r>"%self.scores


student_course = db.Table(
        "student_course",
        db.Column('id', db.Integer, primary_key=True),
        db.Column('student_id', db.Integer, db.ForeignKey("student.id")),
        db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
    )

student_score = db.Table(
    "student_score",
    db.Column('id', db.Integer, primary_key=True),
    db.Column("student_id", db.Integer, db.ForeignKey("student.id")),
    db.Column("score_id", db.Integer, db.ForeignKey("score.id"))
)

course_score = db.Table(
    "course_score",
    db.Column('id', db.Integer,primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id")),
    db.Column("score_id", db.ForeignKey("score.id"))
)

db.create_all()
# ====================================================================================================


def teacher_window():
    te = Tk()
    te.title("客户端管理系统第一版教师端 by: 第三组")
    te.geometry("1068x681+200+200")
    menubar = Menu(te)
    usermenu = Menu(menubar)
    usermenu.add_command(label="登录", command=do_login)
    usermenu.add_command(label="注册", command=do_register)
    usermenu.add_command(label="退出", command=te.destroy)
    menubar.add_cascade(label="用户", menu=usermenu)
    aboutmenu = Menu(menubar)
    aboutmenu.add_command(label="作者", command=author)
    aboutmenu.add_command(label="版权", command=power)
    menubar.add_cascade(label="关于", menu=aboutmenu)
    te.config(menu=menubar)
    l1 = Label(te, text="学生基本信息")
    l1.grid(row=0, column=0)
    l2 = Label(te, text="学生课程信息")
    l2.grid(row=0, column=12)
    t1 = Text(te, width=67, height=40)
    t1.grid(row=1, column=0, rowspan=10, columnspan=10)
    t2 = Text(te, width=70, height=40)
    t2.grid(row=1, column=12, rowspan=15, columnspan=10)

    def search_student():
        t = Toplevel(te)
        t.transient()
        t.title("查找")
        t.geometry("260x60+200+300")
        Label(t, text="请输入学生姓名:").grid(row=0, column=0, sticky=E)
        e = Entry(t, width=20)
        e.grid(row=0, column=1, padx=2, pady=2, sticky="we")

        def find():
            relname = e.get()
            student = Student.query.filter_by(relname=relname).first()
            if not student:
                messagebox.showerror("Error", "未找到您所查询的学生")
            else:
                relname = student.relname
                sage = student.sage
                stel = student.stel
                if t1.get(1.0, END):
                    t1.delete(1.0, END)
                info = "学生姓名:%s\r\n学生年龄:%s\r\n学生电话:%s" % (relname, sage, stel)
                t1.insert(INSERT, info)
                courses = student.courses
                if courses:
                    course_info = "%s学习的课程有: " % relname
                    for cou in courses:
                        course_info += "\r\n        " + cou.cname

                    if t2.get(1.0, END):
                        t2.delete(1.0, END)
                    t2.insert(INSERT, course_info)
                else:
                    t2.delete(1.0, END)
                    t2.insert(INSERT, "该生未选择课程")

        b1 = Button(t, text="查询", command=find)
        b1.grid(row=2, column=0, sticky="w", padx=2, pady=2)
        b2 = Button(t, text="退出", command=t.destroy)
        b2.grid(row=2, column=1, sticky="e", padx=2, pady=2)

    def add_student():
        t = Toplevel(te)
        t.transient()
        t.title("添加学生信息")
        t.geometry("600x300+200+300")

        l1 = Label(t, text="学生姓名:")
        l1.grid(row=0, column=0)
        e1 = Entry(t)
        e1.grid(row=0, column=1, padx=2, pady=5)

        l2 = Label(t, text="登录名称:")
        l2.grid(row=1, column=0)
        e2 = Entry(t)
        e2.grid(row=1, column=1, padx=2, pady=5)

        l3 = Label(t, text="登录密码")
        l3.grid(row=2, column=0)
        e3 = Entry(t)
        e3["show"] = "*"
        e3.grid(row=2, column=1, padx=2, pady=5)

        l4 = Label(t, text="学生年龄:")
        l4.grid(row=3, column=0)
        e4 = Entry(t)
        e4.grid(row=3, column=1, padx=2, pady=5)

        l5 = Label(t, text="学生电话:")
        l5.grid(row=4, column=0)
        e5 = Entry(t)
        e5.grid(row=4, column=1, padx=2, pady=5)

        def submit():
            relname = e1.get()
            sname = e2.get()
            spwd = e3.get()
            sage = e4.get()
            stel = e5.get()
            student = Student(sname, spwd, stel)
            student.relname = relname
            student.sage = sage
            db.session.add(student)
            db.session.commit()
            messagebox.showinfo("Success", "添加学生成功！")

        b_s = Button(t, text="提交", command=submit)
        b_s.grid(row=5, column=1, sticky="w")
        ex = Button(t, text="退出", command=t.destroy)
        ex.grid(row=5, column=2, sticky="e")

    def change_student():
        t = Toplevel(te)
        t.transient()
        t.title("查找")
        t.geometry("260x60+200+300")
        Label(t, text="请输入学生姓名:").grid(row=0, column=0, sticky=E)
        e = Entry(t, width=20)
        e.grid(row=0, column=1, padx=2, pady=2, sticky="we")

        def find():
            sname = e.get()
            student = Student.query.filter_by(relname=sname).first()
            if not student:
                messagebox.showerror("Error", "未找到您所查询的学生")
            else:
                chang = Toplevel(t)
                chang.title("修改学生信息")
                chang.geometry("600x300+200+300")
                relname = student.relname
                sname = student.sname
                spwd = student.spwd
                sage = student.sage
                stel = student.stel

                l1 = Label(chang, text="学生姓名:")
                l1.grid(row=0, column=0)
                e1 = Entry(chang)
                e1.insert(20, relname)
                e1.grid(row=0, column=1, padx=2, pady=5)

                l2 = Label(chang, text="登录名称:")
                l2.grid(row=1, column=0)
                e2 = Entry(chang)
                e2.insert(20, sname)
                e2.grid(row=1, column=1, padx=2, pady=5)

                l3 = Label(chang, text="登录密码")
                l3.grid(row=2, column=0)
                e3 = Entry(chang)
                e3["show"] = "*"
                e3.insert(20, spwd)
                e3.grid(row=2, column=1, padx=2, pady=5)

                l4 = Label(chang, text="学生年龄:")
                l4.grid(row=3, column=0)
                e4 = Entry(chang)
                e4.insert(20, sage)
                e4.grid(row=3, column=1, padx=2, pady=5)

                l5 = Label(chang, text="学生电话:")
                l5.grid(row=4, column=0)
                e5 = Entry(chang)
                e5.insert(20, stel)
                e5.grid(row=4, column=1, padx=2, pady=5)

                def submit():
                    relname = e1.get()
                    sname = e2.get()
                    spwd = e3.get()
                    sage = e4.get()
                    stel = e5.get()
                    student = Student(sname, spwd, stel)
                    student.relname = relname
                    student.sage = sage
                    db.session.add(student)
                    db.session.commit()
                    messagebox.showinfo("Success", "学生信息修改成功！")

                b_s = Button(chang, text="提交", command=submit)
                b_s.grid(row=5, column=1, sticky="w")
                ex = Button(chang, text="退出", command=chang.destroy)
                ex.grid(row=5, column=3, sticky="e")

        b = Button(t, text="查询", command=find)
        b.grid(row=2, column=0, sticky="w", padx=2, pady=2)
        ex = Button(t, text="退出", command=t.destroy)
        ex.grid(row=2, column=1, sticky="e")

    def delete_student():
        t = Toplevel(te)
        t.transient()
        t.title("查找")
        t.geometry("260x60+200+300")
        Label(t, text="请输入学生姓名:").grid(row=0, column=0, sticky=E)
        e = Entry(t, width=20)
        e.grid(row=0, column=1, padx=2, pady=2, sticky="we")

        def find():
            sname = e.get()
            student = Student.query.filter_by(relname=sname).first()
            if not student:
                messagebox.showerror("Error", "未找到您所查询的学生")
            else:
                con = askokcancel("删除？", "是否删除")
                if con:
                    db.delete(student)
                else:
                    messagebox.showinfo("取消删除", "取消删除成功")
        b = Button(t, text="查询", command=find)
        b.grid(row=2, column=0, sticky="e" + "w", padx=2, pady=2)
        ex = Button(t, text="退出", command=t.destroy)
        ex.grid(row=2, column=1, sticky="e")

    b1 = Button(te, text="查询学生信息", bg="lightblue", width=10, command=search_student)
    b1.grid(row=1, column=11)
    b2 = Button(te, text="添加学生信息", bg="lightblue", width=10, command=add_student)
    b2.grid(row=2, column=11)
    b3 = Button(te, text="修改学生信息", bg="lightblue", width=10, command=change_student)
    b3.grid(row=3, column=11)
    b4 = Button(te, text="删除学生信息", bg="lightblue", width=10, command=delete_student)
    b4.grid(row=4, column=11)
    te.mainloop()


def student_window(name):
    stu = Tk()
    stu.title("客户端管理系统第一版学生端 by: 第三组")
    stu.geometry("1068x681+200+200")
    menubar = Menu(stu)
    usermenu = Menu(menubar)
    usermenu.add_command(label="登录", command=do_login)
    usermenu.add_command(label="注册", command=do_register)
    usermenu.add_command(label="退出", command=stu.destroy)
    menubar.add_cascade(label="用户", menu=usermenu)
    aboutmenu = Menu(menubar)
    aboutmenu.add_command(label="作者", command=author)
    aboutmenu.add_command(label="版权", command=power)
    menubar.add_cascade(label="关于", menu=aboutmenu)
    stu.config(menu=menubar)
    l1 = Label(stu, text="显示个人信息")
    l1.grid(row=0, column=0)
    l2 = Label(stu, text="学生课程信息")
    l2.grid(row=0, column=12)
    t1 = Text(stu, width=67, height=40)
    t1.grid(row=1, column=0, rowspan=10, columnspan=10)
    t2 = Text(stu, width=70, height=40)
    t2.grid(row=1, column=12, rowspan=15, columnspan=10)

    student = Student.query.filter_by(sname=name).first()
    info = "学生姓名:%s\r\n学生年龄:%s\r\n学生电话:%s" % (student.relname, student.sage, student.stel)
    t1.delete(1.0, END)
    t1.insert(INSERT, info)

    def change_self():
        ch = Toplevel(stu)
        ch.title("修改个人信息")
        ch.geometry("600x300+200+300")
        student= Student.query.filter_by(sname=name).first()
        relname = student.relname
        sname = student.sname
        spwd = student.spwd
        sage = student.sage
        stel = student.stel

        if relname == None:
            relname = name
        if sage == None:
            sage = 0

        l1 = Label(ch, text="学生姓名:")
        l1.grid(row=0, column=0)
        e1 = Entry(ch)
        e1.insert(20, relname)
        e1.grid(row=0, column=1, padx=2, pady=5)

        l2 = Label(ch, text="登录名称:")
        l2.grid(row=1, column=0)
        e2 = Entry(ch)
        e2.insert(20, sname)
        e2.grid(row=1, column=1, padx=2, pady=5)

        l3 = Label(ch, text="登录密码")
        l3.grid(row=2, column=0)
        e3 = Entry(ch)
        e3["show"] = "*"
        e3.insert(20, spwd)
        e3.grid(row=2, column=1, padx=2, pady=5)

        l4 = Label(ch, text="学生年龄:")
        l4.grid(row=3, column=0)
        e4 = Entry(ch)
        e4.insert(20, sage)
        e4.grid(row=3, column=1, padx=2, pady=5)

        l5 = Label(ch, text="学生电话:")
        l5.grid(row=4, column=0)
        e5 = Entry(ch)
        e5.insert(20, stel)
        e5.grid(row=4, column=1, padx=2, pady=5)

        def submit():
            relname = e1.get()
            sname = e2.get()
            spwd = e3.get()
            sage = e4.get()
            stel = e5.get()
            student = Student(sname, spwd, stel)
            student.relname = relname
            student.sage = sage
            db.session.add(student)
            db.session.commit()
            messagebox.showinfo("Success", "学生信息修改成功！")

            student = Student.query.filter_by(relname=relname).first()
            info = "学生姓名:%s\r\n学生年龄:%s\r\n学生电话:%s" % (student.relname, student.sage, student.stel)
            t1.delete(1.0, END)
            t1.insert(INSERT, info)

        b_s = Button(ch, text="提交", command=submit)
        b_s.grid(row=5, column=1, sticky="w")
        ex = Button(ch, text="退出", command=ch.destroy)
        ex.grid(row=5, column=3, sticky="e")

    # def select_course():
    #     ch = Toplevel(stu)
    #     ch.title("修改个人信息")
    #     ch.geometry("600x300+200+300")
    #     cour_all = Course.query.all()
    #     all_courses = '可选课程有:'
    #     for co in cour_all:
    #         all_courses += "\r\n" + str(co.id) + "." + co.cname
    #     Label(ch, text="可选课程").grid(row=0, column=0, sticky="w")
    #     t1 = Text(ch, width=30, height=20)
    #     t1.grid(row=1, column=0)
    #     t1.insert(INSERT, all_courses)
    #     Label(ch, text="请选择课程编号，多选时以逗号“，”隔开").grid(row=0, column=1, sticky="e")
    #     t2 = Text(ch, width=30, height=20)
    #     t2.grid(row=1, column=1)
    #
    #     def sub():
    #         cou = t2.get(1.0, END)
    #         cour = cou.split(",")
    #         for i in cour:
    #             # print(int(i))
    #             # c = Course.query.filter_by(cname=i).first()
    #             # print(c)
    #             student.courses = int(i)
    #         db.session.add(student)
    #         db.session.commit()
    #
    #     b = Button(ch, text="提交", command=sub)
    #     b.grid(row=1, column=2, sticky="e")



    b1 = Button(stu, text="修改个人信息", bg="lightblue", width=10, command=change_self)
    b1.grid(row=1, column=11)
    # b2 = Button(stu, text="个人选课", bg="lightblue", width=10, command=select_course)
    # b2.grid(row=2, column=11)


def do_register():
    f = Toplevel(root)
    f.transient()
    f.geometry("400x300+20+20")
    f.title("欢迎注册")
    l1 = Label(f, text="注册账号：")
    l1.grid(row=0, column=0, padx=5, pady=5)
    uname = Entry(f)
    uname.grid(row=0, column=1, ipadx=5)

    l2 = Label(f, text="注册密码：")
    l2.grid(row=1, column=0, padx=5, pady=5)
    upwd = Entry(f)
    upwd["show"] = "*"
    upwd.grid(row=1, column=1, ipadx=5)

    l3 = Label(f, text="确认密码：")
    l3.grid(row=2, column=0, padx=5, pady=5)
    cpwd = Entry(f)
    cpwd["show"] = "*"
    cpwd.grid(row=2, column=1, ipadx=5)

    l4 = Label(f, text="手机号：")
    l4.grid(row=3, column=0, padx=5, pady=5)
    tel = Entry(f)
    tel.grid(row=3, column=1, ipadx=5)

    def register_teacher():
        name = uname.get()
        pwd = upwd.get()
        c_pwd = cpwd.get()
        telp = tel.get()
        if c_pwd == pwd:
            user = Teacher.query.filter_by(tname=name).first()
            if user:
                messagebox.showerror("Error", "用户名已存在")
                uname.delete(0, len(name))
                upwd.delete(0, len(pwd))
                cpwd.delete(0, len(c_pwd))
                tel.delete(0, len(telp))
            else:
                new_user = Teacher(name, pwd, telp)
                db.session.add(new_user)
                db.session.commit()
                messagebox.showinfo("Success", "注册成功")
                teacher_window()
        else:
            messagebox.showerror("Error", "两次密码不匹配，请确认密码!")
            cpwd.delete(0, len(c_pwd))

    def register_student():
        name = uname.get()
        pwd = upwd.get()
        c_pwd = cpwd.get()
        telp = tel.get()
        if c_pwd == pwd:
            user = Student.query.filter_by(sname=name).first()
            if user:
                messagebox.showerror("Error","用户名已存在")
                uname.delete(0, len(name))
                upwd.delete(0, len(pwd))
                cpwd.delete(0, len(c_pwd))
                tel.delete(0, len(telp))
            else:
                new_user = Student(name, pwd, telp)
                db.session.add(new_user)
                db.session.commit()
                messagebox.showinfo("Success", "注册成功")
                student_window(name)
        else:
            messagebox.showerror("Error", "两次密码不匹配，请确认密码!")
            cpwd.delete(0, len(c_pwd))

    tea_button = Button(f, text="老师注册", command=register_teacher)
    tea_button.grid(row=4, column=0, padx=5, pady=5)
    stu_button = Button(f, text="学生注册", command=register_student)
    stu_button.grid(row=4, column=1, padx=5, pady=5)
    exit_re = Button(f, text="退出", command=f.destroy)
    exit_re.grid(row=4, column=2, padx=5, pady=5)


def do_login():
    f = Toplevel(root)
    f.transient()
    f.geometry("400x300+20+20")
    l1 = Label(f, text="账号：")
    l1.grid(row=0, sticky=W)
    uname = Entry(f)
    uname.grid(row=0, column=1, sticky=E)

    l2 = Label(f, text="密码：")
    l2.grid(row=1, sticky=W)
    upwd = Entry(f)
    upwd["show"] = "*"
    upwd.grid(row=1, column=1, sticky=E)

    def login_teacher():
        name = uname.get()
        pwd = upwd.get()

        user = Teacher.query.filter_by(tname=name, tpwd=pwd).first()
        if user:
            messagebox.showinfo("Success", "登录成功")
            teacher_window()
        else:
            messagebox.showerror("Error", "用户名或密码错误")
            uname.delete(0, len(name))
            upwd.delete(0, len(pwd))

    def login_student():
        name = uname.get()
        pwd = upwd.get()

        user = Student.query.filter_by(sname=name, spwd=pwd).first()
        if user:
            messagebox.showinfo("Success", "登录成功")
        else:
            messagebox.showerror("Error", "用户名或密码错误")
            uname.delete(0, len(name))
            upwd.delete(0, len(pwd))
    login_teacher = Button(f, text="老师登录", command=login_teacher)
    login_teacher.grid(row=2, column=1, sticky=W)
    login_student = Button(f, text="学生登录", command=login_student)
    login_student.grid(row=2, column=1, sticky=E)

    register = Button(f, text="没有账号？点击注册", command=do_register)
    register.grid(row=2, sticky=W)


def author():
    showinfo("作者信息", "第三小组学生信息管理系统第一版")


def power():
    showinfo("版权信息", "用于测试的学生信息管理系统第一版，随便用")


def create_root():
    root = Tk()
    root.title("客户端管理系统第一版 by: 第三组")
    root.geometry("1068x681+200+200")

    menubar = Menu(root)
    usermenu = Menu(menubar)
    usermenu.add_command(label="登录", command=do_login)
    usermenu.add_command(label="注册", command=do_register)
    usermenu.add_command(label="退出", command=root.destroy)
    menubar.add_cascade(label="用户", menu=usermenu)
    aboutmenu = Menu(menubar)
    aboutmenu.add_command(label="作者", command=author)
    aboutmenu.add_command(label="版权", command=power)
    menubar.add_cascade(label="关于", menu=aboutmenu)
    root.config(menu=menubar)

    l1 = Label(root, text="账号：")
    l1.grid(row=0, sticky=W)
    uname = Entry(root)
    uname.grid(row=0, column=1, sticky=E)

    l2 = Label(root, text="密码：")
    l2.grid(row=1, sticky=W)
    upwd = Entry(root)
    upwd["show"] = "*"
    upwd.grid(row=1, column=1, sticky=E)

    def login_teacher():
        name = uname.get()
        pwd = upwd.get()

        user = Teacher.query.filter_by(tname=name, tpwd=pwd).first()
        if user:
            messagebox.showinfo("Success", "登录成功")
            teacher_window()
        else:
            messagebox.showerror("Error", "用户名或密码错误")
            uname.delete(0, len(name))
            upwd.delete(0, len(pwd))

    def login_student():
        name = uname.get()
        pwd = upwd.get()

        user = Student.query.filter_by(sname=name, spwd=pwd).first()
        if user:
            messagebox.showinfo("Success", "登录成功")
            student_window(name)
        else:
            messagebox.showerror("Error", "用户名或密码错误")
            uname.delete(0, len(name))
            upwd.delete(0, len(pwd))

    login_teacher = Button(root, text="老师登录", command=login_teacher)
    login_teacher.grid(row=2, column=1, sticky=W)
    login_student = Button(root, text="学生登录", command=login_student)
    login_student.grid(row=2, column=1, sticky=E)

    register = Button(root, text="没有账号？点击注册", command=do_register)
    register.grid(row=2, sticky=W)

    return root


root = create_root()
if __name__ == "__main__":
    root.mainloop()
