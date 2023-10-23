from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
import werkzeug
from datetime import datetime
from . import db
from .models import Users

import json
# from .models import Users

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def sign_up():
    if request.method == "POST":
        #register 
        signup_data = request.get_json()
        user_agent = request.headers.get("User-Agent")
        password = generate_password_hash(signup_data['password'], "scrypt")
        user_ = Users.query.filter_by(username=signup_data["username"]).all()
        exist = False
        for user in user_:
          if user.username == signup_data["username"] and user.device_detail == user_agent:
            exist = True
        if exist:
          return jsonify({"status": 409, "message": "Already Registered", "redirect": "/login"}), 409
        else:
          new_user = Users(username=signup_data["username"], auth_key=password, device_detail = user_agent, date = datetime.now())
          db.session.add(new_user)
          db.session.commit()
        
        #remember session
          login_user(new_user, remember=True)
          return jsonify({"status": 200, "message": "success", "redirect": "/home"}), 200
    return "<h1>Method Not Allowed</h1>"

@auth.errorhandler(405)
def method_not_allowed():
    return "<h1> method not allow</h1>"