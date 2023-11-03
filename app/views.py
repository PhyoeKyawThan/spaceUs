from flask import Blueprint, render_template, redirect, request, jsonify, current_app
from flask_login import current_user
from .models import Posts, Users
views = Blueprint("views", __name__)

@views.route("/home")
def home():
  return render_template("index.html", name=current_user.username)
  

@views.route("/upload")
def upload():
  return render_template("upload.html")

@views.route('/signup')
def signup():
  if current_user.is_authenticated:
    return redirect("home")
  else:
    return render_template("signup.html")

@views.route('/login')
def login():
  if current_user.is_authenticated:
    return redirect("home")
  else:
    return render_template("login.html")
  
@views.route("/posts", methods=["GET"])
def get_posts():
  if request.method == 'GET':
    posts = Posts.query.all()
    datas = []
    
    for data in posts:
      posted_user = Users.query.get(data.id)
      datas.append({
        "id": data.id, 
        "username": posted_user.username,
        "post_id": data.post_id,
        "profile": current_app.config["UPLOAD_FOLDER"] + "profiles" + "",
        "image": data.image_path
      })
    print(datas)
    return render_template("index.html", posts = datas)