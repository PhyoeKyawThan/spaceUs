from . import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):

    __tablename__ = "users"

    id  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    auth_key = db.Column(db.String(255), nullable=False)
    device_detail = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    post_id = db.relationship("Posts", backref="users", lazy=True)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"
    

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    act_id = db.Column(db.Integer)
    actions = db.relationship("Actions", backref="posts", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

class Actions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    love = db.Column(db.Boolean, default=False)
    interested = db.Column(db.Boolean, default=False)
    save_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("posts.id"))

class Saved(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    save_id = db.Column(db.Integer)
    post_id = db.Column(db.String(100))
    save_date = db.Column(db.DateTime, nullable=False)
