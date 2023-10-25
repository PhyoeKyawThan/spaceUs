from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.urls import url_decode
from flask_migrate import Migrate
db = SQLAlchemy()


def app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    Migrate(app, db)

    # manage blue print
    from .models import Users
    from .auth import auth
    from .views import views
    from .post import post
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(post, url_prefix="/post")
    with app.app_context():
        db.create_all()
    
    # login  manager
    @login_manager.user_loader
    def load_user(username):
        return Users.query.get(username)
    
    return app

app = app()