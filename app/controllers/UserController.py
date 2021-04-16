from app import app, db, redirect, request, url_for
from app.models import User as model_user
from app.controllers.AuthController import AuthController as Auth
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
    

    def create(self):
        auth = Auth()
        if request.form:
            try:
                data = request.form
                user = data.copy()
                user["password"], user["salt"] = auth.encrypt(user["password"])
                post = model_user.User(**user)
                db.session.add(post)
                db.session.commit()
                result = model_user.User.data_to_json(post)
            except Exception as error:
                print(error)
                return {
                    "message": "something error"
                }, 500
            return {
                "message": "user is created",
                "data": result
            }, 201
    
    
    def update(self, id):
        return {
            "message": f"update by id {id}"
        }, 200
    
    def delete(self, id):
        return {
            "message": f"delete by id {id}"
        }, 200
    
    def get_by_id(self, id):
        return {
            "message": f"get by id {id}"
        }, 200
