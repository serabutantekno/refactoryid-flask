from app import app, redirect, request, url_for
from werkzeug.utils import secure_filename
import os


ALLOWED_EXTENSION = {"pdf", "png", "jpg", "jpeg"}


@app.route("/")
def hello():
    return "Hello Refactory! Development mode."


@app.route("/greet/<username>", methods=["PUT", "POST"])
def greet(username):
    return f"Hello, {username}!"


@app.route("/about")  # Jika diakses dengan trailing slash, hasil 404 Not Found.
def about():
    return "ABOUT PAGE"


@app.route("/contact/")  # Diakses tanpa trailing slash akan diredirect ke /contact.
def contact():
    return "CONTACT PAGE"


@app.route("/image")
def image():
    return redirect(url_for("static", filename="images/toko.jpg"))


@app.route("/index")
def index():
    return redirect(url_for("static", filename="index.html"))


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSION


@app.route("/user", methods=["POST"])
def user():
    UPLOAD_FOLDER = "./app/static/uploads"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    if "image" not in request.files:
        return {"message": "no selected file"}, 400
    image = request.files["image"]
    if allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return {"message": "success"}, 201
    else:
        return {"message": {"type": list(ALLOWED_EXTENSION)}}, 415


# Uncomment code below if you do not export FLASK_APP to your environment
# WARNING: not recommended
# Run with `$ python3 main.py`
# if __name__ == "__main__":
#     app.run()


# Export these to your environment
# or see more details with `$ flask --help`
# Run with `$ flask run`
# $ EXPORT FLASK_APP = main.py
