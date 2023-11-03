from flask import Blueprint, request, jsonify, current_app
from flask_login import current_user, login_required
from . import db
from .models import Posts, Actions
from uuid import uuid4
from datetime import datetime
from werkzeug.utils import secure_filename

post = Blueprint("post", __name__)

@post.route("/upload_post", methods=["POST"])
@login_required
def upload_post():
    if request.method == "POST":
        caption = request.form.get("caption", "")
        if "image" not in request.files:
            new_post = Posts(post_id = str(uuid4()), caption=caption, date = datetime.now(), user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            return jsonify({"status": 200, "message": "Upload Success"}), 200
        else:
            image = request.files["image"]
            new_post = Posts(post_id = str(uuid4()), caption=caption, image_path= "static/post_image/" + secure_filename(image.filename), date = datetime.now(), user_id=current_user.id)
            image.save(current_app.config['UPLOAD_FOLDER'] + "/" + secure_filename(image.filename))
            # new_post = Posts(post_id = str(uuid4()), caption=caption, image_path=current_app.config["UPLOAD_FOLDER"] + secure_filename(image.filename), date = datetime.now(), user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            return jsonify({"status": 200, "message": "Upload Success"}), 200

@post.route("/react/love/<string:post_id>", methods=['PUT'])
def love_react(post_id):
    if request.method == "PUT":
        post_exist = Posts.query.filter_by(post_id=post_id).first()
        if Actions.query.filter_by(post_id=post_exist.id).first().love == 1:
          return jsonify({"status": 201, "message": "Already loved"}), 201
        if post_exist:
            post_action = Posts(post_id = post_id, act_id = current_user.id)
            new_action = Actions(love=True, post_id=post_exist.id)
            post_action.vertified = True
            db.session.commit()
            db.session.add(new_action)
            db.session.commit()
            return jsonify({"status": 200, "Message": "You have react"}), 200
        return jsonify({"status": 404, "message": "Post not found"}), 404
@post.route("/interested/<string:post_id>", methods=["PUT"])
def interested(post_id):
      if request.method == "PUT":
        post_exist = Posts.query.filter_by(post_id=post_id).first()
        if post_exist:
            post_action = Posts(post_id = post_id, act_id = current_user.id)
            new_action = Actions(interested=True)
            post_action.vertified = True
            db.session.commit()
            db.session.add(new_action)
            db.session.commit()
            return jsonify({"status": 200, "Message": "You have react"}), 200
        return jsonify({"status": 404, "message": "Post not found"}), 404
# @post.route("/save/<string:post_id>", methods=["PUT"])
# def save_post(post_id):
#     if request.method == "PUT":
#         post_action = Posts(post_id = post_id, act_id = current_user.id)
#         new_save = Actions(save = True, act_id = current_user.id)
#         post_action.vertified = True
#         db.session.commit()
#         db.session.add(new_save)
#         db.session.commit()
#         return jsonify({"status": 200, "message": "Saved"}), 200