from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '2a48340099afdaa1b757452ba8d04744'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_man = LoginManager(app)
login_man.login_view = 'login'
login_man.login_message_category = 'info'

from flask_blog_pkg import routes