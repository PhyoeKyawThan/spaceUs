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
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.String(100), nullable=False)
    caption = db.Column(db.String(255))
    image_path = db.Column(db.String(255))
    date = db.Column(db.DateTime, nullable=False)
    act_id = db.Column(db.Integer)
    actions = db.relationship("Actions", backref="posts", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    def __repr__(self):
        return f"<ID={self.id}, post_id={self.post_id}>"

class Actions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    love = db.Column(db.Boolean, default=False)
    interested = db.Column(db.Boolean, default=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    
    def __repr__(self):
        return f"<post_id={Posts.id}, status=(love={self.love}, interested={self.interested})"


