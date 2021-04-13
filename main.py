from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Refactory! Development mode."

@app.route("/greet/<username>", methods=["PUT", "POST"])
def greet(username):
    return f"Hello, {username}!"

@app.route("/user", methods=["POST"])
def user():
    name = request.json["name"]
    data = {
        "name"   : name,
        "message": "Success!"
    }
    return data, 201, {"author": "refactory"}

@app.route("/about")  # Jika diakses dengan trailing slash, hasil 404 Not Found.
def about():
    return "ABOUT PAGE"

@app.route("/contact/")  # Diakses tanpa trailing slash akan diredirect ke /contact.
def contact():
    return "CONTACT PAGE"


# Uncomment code below if you do not export FLASK_APP to your environment
# WARNING: not recommended
# Run with `$ python3 main.py`
# if __name__ == "__main__":
#     app.run()


# Export these to your environment
# or see more details with `$ flask --help`
# Run with `$ flask run`
# $ EXPORT FLASK_APP = main.py
