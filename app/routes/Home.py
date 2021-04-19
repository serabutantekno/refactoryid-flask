from app import app
from app.controllers.AuthController import AuthController as Auth
from app.middlewares.ExampleMiddleware import saySomething
from app.middlewares.AuthJwt import token_required


auth = Auth()


@app.route("/home")
@token_required
def home():
    return {
        "message": "welcome to home"
    }


@app.route("/")
@saySomething
def index():
    return {
        "message": "welcome to flask app"
    }


@app.route("/login", methods=["POST"])
@saySomething
def login():
    return auth.login()
