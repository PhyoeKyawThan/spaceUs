from .auth import auth

# register
class Handle_Blueprint:
    def __init__(self, app):
        self.app.register_blueprint(auth, __name__, url_prefix="/auth")

blueprints = Handle_Blueprint