from flask import request
from app.models.User import User
import hashlib, string, random


class AuthController:

    def encrypt(self, password):
        salt = "".join(random.sample(string.ascii_letters, 32))
        new_password = password + salt
        return hashlib.md5(new_password.encode()).hexdigest(), salt


    def login(self):
        if "username" and "password" in request.json:
            username, password = request.json["username"], request.json["password"]
            get_user = User.query.filter_by(username=username).first()
            if get_user:
                salt = get_user.salt
                user_password = get_user.password
                encrypted_password = hashlib.md5((password + salt).encode()).hexdigest()
                if user_password == encrypted_password:
                    return {"message": "success"}, 200
                else:
                    return {"message": "password unmatch"}, 401
            else:
                return {"message": "user not found"}, 404
        else:
            return {"message": "please input username and password"}, 401
