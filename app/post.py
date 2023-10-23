from flask import Blueprint, request

post = Blueprint("post", __name__)

@post.route("/upload_post", methods=["POST"])
def upload_post():
    if 
