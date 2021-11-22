from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin


from lpsm.config import *


app = Flask(__name__, static_url_path='/lpsm/static')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lpsm.db"
# f"postgresql+psycopg2://{DB_USER}:{DB_PW}@/{DB_NAME}?host={DB_IP}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
db.drop_all()
db.create_all()

app.config["SECRET_KEY"] = SECRET_KEY

app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = 'filesystem'

login_manager = LoginManager()
login_manager.init_app(app)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, template_mode='bootstrap3')

from lpsm import routes