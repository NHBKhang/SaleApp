from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

s1 = 'Admin@123'
s2 = 'Abc111!'
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote(s2)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
