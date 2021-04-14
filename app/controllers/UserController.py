from app import app, redirect, request, url_for
from werkzeug.utils import secure_filename
import os


class User:

    ALLOWED_EXTENSION = {"pdf", "png", "jpg", "jpeg"}

    def index(self):
        return redirect(url_for("static", filename="example-template/index.html"))


    def allowed_file(self, filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in self.ALLOWED_EXTENSION


    def upload(self):
        UPLOAD_FOLDER = "./app/static/uploads"
        app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
        if "image" not in request.files:
            return {"message": "no selected file"}, 400
        image = request.files["image"]
        if self.allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return {"message": "success"}, 201
        else:
            return {"message": {"type": list(self.ALLOWED_EXTENSION)}}, 415