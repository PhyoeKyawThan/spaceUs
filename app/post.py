from flask import Blueprint, request, jsonify, current_app
from flask_login import current_user, login_required
from . import db
from .models import Posts
from uuid import uuid4
from datetime import datetime
# from werkzeug import secure_filename

post = Blueprint("post", __name__)

@post.route("/upload_post", methods=["POST"])
@login_required
def upload_post():
    if request.method == "POST":
        caption = request.form["caption"]
        image = request.files["image"]
        # image.save(current_app.config['UPLOAD_FOLDER'] + image.filename)
        new_post = Posts(post_id = uuid4(), caption=caption, image_path=current_app.config["UPLOAD_FOLDER"] + image.filename, date = datetime.now())
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"status": 200, "message": "Upload Success"}), 200
