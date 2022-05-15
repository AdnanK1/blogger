from enum import unique
from .extensions import db, b_crypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer(),primary_key = True)
    username = db.Column(db.String(length=30),nullable=False,unique=True)
    email = db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash = db.Column(db.String(length=60),nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash = b_crypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self,attempted_password):
        return b_crypt.check_password_hash(self.password_hash,attempted_password)

class Blog(db.Model):
    __tablename__ = 'Blogs'
    id = db.Column(db.Integer(),primary_key=True)
    blog = db.Column(db.String(),nullable=False)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key = True)
    comment = db.Column(db.String(),nullable=False)
