from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import cloudinary

s1 = 'Admin@123'
s2 = 'Abc111!'
app = Flask(__name__)
app.secret_key = '12$@**$@_!+____!#@KMS,dglsdd@$#%!!)%*^&$(!'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote(s2)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 4

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

cloudinary.config(
    cloud_name="dd0qzygo7",
    api_key="544345494632949",
    api_secret="rsMExum_c-Ga0DTQOfB92R0aONw"
)
