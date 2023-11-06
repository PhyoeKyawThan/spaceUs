from flask import Blueprint, request, jsonify, current_app
from flask_login import current_user, login_required
from . import db
from .models import Posts, Actions
from uuid import uuid4
from datetime import datetime
# from flask_cors import CORS
from werkzeug.utils import secure_filename

post = Blueprint("post", __name__)
# CORS(post)


@post.route("/upload_post", methods=["POST"])
@login_required
def upload_post():
    if request.method == "POST":
        caption = request.form.get("caption", "")
        post_id = str(uuid4())
        if "image" not in request.files:
            new_post = Posts(post_id = post_id, caption=caption, date = datetime.now(), user_id=current_user.id, act_id = current_user.id)
            new_action = Actions(post_id = post_id)
            db.session.add(new_post)
            db.session.add(new_action)
            db.session.commit()
            return jsonify({"status": 200, "message": "Upload Success"}), 200
        else:
            image = request.files["image"]
            new_post = Posts(post_id = post_id, caption=caption, image_path= "static/post_image/" + secure_filename(image.filename), date = datetime.now(), user_id=current_user.id)
            image.save(current_app.config['UPLOAD_FOLDER'] + "/" + secure_filename(image.filename))
            # new_post = Posts(post_id = str(uuid4()), caption=caption, image_path=current_app.config["UPLOAD_FOLDER"] + secure_filename(image.filename), date = datetime.now(), user_id=current_user.id)
            new_action = Actions(post_id = post_id)
            db.session.add(new_action)
            db.session.add(new_post)
            db.session.commit()
            return jsonify({"status": 200, "message": "Upload Success"}), 200

@post.route("/react/love/<string:post_id>", methods=['PUT'])
@login_required
# @cross_origin
def love_react(post_id):
    if request.method == "PUT":
        post_exist = Posts.query.filter_by(post_id=post_id).first()
        if not post_exist:
            return jsonify({"status": 404, "message": "Post not found"}), 404
        current_love = Actions.query.filter_by(post_id = post_exist.post_id).first()
        if current_love.love == True:
            current_love.love = False
            current_love.vertified = True
            db.session.commit()
            return jsonify({"status": 200, "message": "Unloved"}), 200
        post_action = Posts(post_id = post_id, act_id = current_user.id)
        current_love.love = True
        current_love.vertified = True
        post_action.vertified = True
        db.session.commit()
        db.session.commit()
        return jsonify({"status": 200, "Message": "Loved"}), 200

@post.route("/interested/<string:post_id>", methods=["PUT"])
@login_required
def interested(post_id):
      if request.method == "PUT":
        post_exist = Posts.query.filter_by(post_id=post_id).first()
        if not post_exist:
            return jsonify({"status": 404, "message": "Post not found"}), 404
        current_interested = Actions.query.filter_by(post_id = post_exist.post_id).first()
        if current_interested.interested == True:
            current_interested.interested = False
            current_interested.vertified = True
            db.session.commit()
            return jsonify({"status": 200, "message": "Uninterested"})
        if post_exist:
            current_interested.interested = True
            current_interested.vertified = True
            db.session.commit()
            return jsonify({"status": 200, "Message": "Interested"}), 200
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