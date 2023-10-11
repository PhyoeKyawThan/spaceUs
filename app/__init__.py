from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    # import blueprint
    from .views import views

    # register blueprint
    app.register_blueprint(views, url_prefix="/")
    return app