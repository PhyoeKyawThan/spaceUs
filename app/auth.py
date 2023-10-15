from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
# from .models import Users

auth = Blueprint('auth', __name__)

@auth.route('/signup', method=['POST'])
def sign_up():
    user_datas = request.get_json()
    return jsonify(user_datas), 201