from app import app
from app.middlewares.ExampleMiddleware import saySomething


@app.route("/")
@saySomething
def home():
    return {
        "message": "welcome to flask app"
    }


@app.route("/login")
@saySomething
def login():
    return {
        "message": "login success"
    }
