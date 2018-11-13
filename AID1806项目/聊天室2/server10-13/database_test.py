# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config['SQLCHEMY_DATABASE_URI'] = 'mysql://root:123456:'
