from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.urls import url_decode
db = SQLAlchemy()


def app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    # manage blue print
    from .models import Users
    from .auth import auth
    app.register_blueprint(auth, __name__, url_prefix="/auth")
    # login  manager
    @login_manager.user_loader
    def load_user(user_id):
        return Users.get(user_id)
    
    with app.app_context():
        db.create_all()
    return app