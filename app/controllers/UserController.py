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
        if request.form:
            try:
                data_update = request.form
                data = model_user.User.query.filter_by(id=id)
                data.update(data_update)
                db.session.commit()
            except Exception as err:
                print(err)
                return {
                    "message": "failed to update"
                }
            return {
                "message": "a user data updated",
                "data": [model_user.User.data_to_json(data) for data in data]
            }, 200


    def delete(self, id):
        try:
            data = model_user.User.query.get(id)
            db.session.delete(data)
            db.session.commit()
        except Exception as err:
            print(err)
            return {
                "message": "data not found"
            }
        return {
            "message": "success deleting a user"
        }, 200
    

    def get_all(self):
        data = model_user.User.query.all()
        result = [model_user.User.data_to_json(user) for user in data]
        return {
            "message": "get all users",
            "data": result
        }
    
    
    def get_by_id(self, id):
        data = model_user.User.query.get(id)
        result = data.data_to_json()
        return {
            "message": f"get by id {id}",
            "data": result
        }, 200
