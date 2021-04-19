from app import app
from app.controllers.AuthController import AuthController as Auth
from app.middlewares.ExampleMiddleware import saySomething


auth = Auth()


@app.route("/")
@saySomething
def home():
    return {
        "message": "welcome to flask app"
    }


@app.route("/login", methods=["POST"])
@saySomething
def login():
    return auth.login()
