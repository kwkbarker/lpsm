from lpsm import db, login_manager, admin
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    first_name = db.Column(db.String(18), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    listings = db.relationship('Listing', backref='created_by_user', lazy=True)
    city = db.Column(db.String(30))
    profile_pic = db.Column(db.String(60))
    comments = db.relationship('Comment', backref='commenter', lazy=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def __init__(self, username, email, password, first_name, last_name, city, profile_pic):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password, method='sha256')
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.profile_pic = profile_pic

    @classmethod
    def authenticate(cls, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')

        if not username or not password:
            return None

        user = cls.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return None
        
        return user


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seller = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    grade = db.Column(db.String(12), nullable=False)
    image_1 = db.Column(db.String(128), nullable=False)
    image_2 = db.Column(db.String(128), nullable=True)
    image_3 = db.Column(db.String(128), nullable=True)
    image_4 = db.Column(db.String(128), nullable=True)
    active = db.Column(db.Boolean, nullable=False, default=True)
    date = db.Column(db.DateTime, server_default=db.func.now())
    buyer = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return self.title

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listing = db.Column(db.Integer, db.ForeignKey('listing.id'))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.String(1024), nullable=False)
    date = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"{self.user}: {self.date}"

class Wantlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    artist = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    comment = db.Column(db.String(60), nullable=True)