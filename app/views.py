from flask import Blueprint, render_template, redirect
from flask_login import current_user
views = Blueprint("views", __name__)

@views.route("/home")
def home():
  return render_template("index.html", name=current_user.username)
  
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