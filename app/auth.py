from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from flask_login import login_user
from . import db
from .models import Users
import json
# from .models import Users

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def sign_up():
    user_datas = request.get_json()
    password = generate_password_hash(user_datas["password"], method="scrypt")
    new_user = Users(username=user_datas["username"], auth_key=password, device_detail=user_datas["USER_AGENT"])
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user, remember=True)
    return jsonify(user_datas), 201