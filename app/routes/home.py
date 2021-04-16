from app import app, redirect, request, url_for
from app.controllers.UserController import User


user = User()


@app.route("/user", methods=["GET", "POST"])
def user_route():
    if request.method == "GET":
        return user.get_all()
    elif request.method == "POST":
        return user.create()


@app.route("/user/<int:id>", methods=["GET", "PUT", "DELETE"])
def user_route_id(id):
    if request.method == "GET":
        return user.get_by_id(id)
    elif request.method == "PUT":
        return user.update(id)
    elif request.method == "DELETE":
        return user.delete(id)


# @app.route("/")
# def hello():
#     return "Hello Refactory! Development mode."


# @app.route("/greet/<username>", methods=["PUT", "POST"])
# def greet(username):
#     return f"Hello, {username}!"


# @app.route("/about")  # Jika diakses dengan trailing slash, hasil 404 Not Found.
# def about():
#     return "ABOUT PAGE"


# @app.route("/contact/")  # Diakses tanpa trailing slash akan diredirect ke /contact.
# def contact():
#     return "CONTACT PAGE"


# @app.route("/image")
# def image():
#     return redirect(url_for("static", filename="images/toko.jpg"))


# Uncomment code below if you do not export FLASK_APP to your environment
# WARNING: not recommended
# Run with `$ python3 main.py`
# if __name__ == "__main__":
#     app.run()


# Export these to your environment
# or see more details with `$ flask --help`
# Run with `$ flask run`
# $ EXPORT FLASK_APP = main.py
