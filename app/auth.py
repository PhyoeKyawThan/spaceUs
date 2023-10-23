from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
import werkzeug
from . import db
from .models import Users

import json
# from .models import Users

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def sign_up():
    if request.method == "POST":
        signup_data = request.get_json()
        user_agent = request.headers.get("User-Agent")
        password = generate_password_hash(signup_data['password'], "scrypt")
        new_user = Users(username=signup_data["username"], auth_key=password, device_detail = user_agent)
        db.session.add(new_user)
        print(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        return jsonify({"status": 200, "message": "success"}), 200
    return "<h1>Method Not Allowed</h1>"

@auth.errorhandler(405)
def method_not_allowed():
    return "<h1> method not allow</h1>"