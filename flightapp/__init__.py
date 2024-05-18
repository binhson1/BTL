import cloudinary as cloudinary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from urllib.parse import quote
# from flask_babelex import Babel


app = Flask(__name__,template_folder='template')
app.secret_key ="%^%^$%#$%#$%#$#$%56262626%&^%^&%"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb2?charset=utf8mb4" % quote(
    'Sonhaian123.')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CART_KEY'] = 'cart'
cloudinary.config(cloud_name='dy2dgfaiq', api_key='376561342321139', api_secret='fuf5FQ4BVaHNwBCyP74b4b-uS_g')

db = SQLAlchemy(app = app)

login = LoginManager(app = app)

gio_mua_toi_da = 12
gio_ban_toi_da = 4
thoi_gian_bay_toi_thieu= 1
san_bay_trung_gian_toi_da = 5
thoi_gian_dung_toi_da= 2
thoi_gian_dung_toi_thieu= 0.1

# babel = Babel(app=app)
# @babel.localeselector
# def load_locale():
#     return 'vi'