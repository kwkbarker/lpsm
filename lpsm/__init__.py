from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user

from lpsm.config import *


app = Flask(__name__, static_url_path="lpsm/static")

app.config["SQLALCHEMY_DATABASE_URI"] = F"postgresql+psycopg2://{DB_USER}:{DB_PW}@/{DB_NAME}?host={DB_IP}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
db.drop_all()
db.create_all()

app.config["SECRET_KEY"] = SECRET_KEY