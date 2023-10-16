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
    # data from client new user
    user_datas = request.get_json()
    device = request.headers.get("User-Agent")
    
    # add to database
    password = generate_password_hash(user_datas["password"], method="scrypt")
    new_user = Users(username=user_datas["username"], auth_key=password, device_detail=device)
    db.session.add(new_user)
    db.session.commit()
    users = Users.query.all()
    print(users)

    login_user(new_user, remember=True)
    return jsonify(user_datas), 201