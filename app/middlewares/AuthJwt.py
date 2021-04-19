import jwt
import os
import datetime
from functools import wraps
from flask import request


def encode(username, password):
    payload = {
        "username": username,
        "password": password,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
    }
    token = jwt.encode(payload, key=os.getenv("JWT_SECRET"), algorithm="HS256")
    return token


def decode(token):
    return jwt.decode(token, key=os.getenv("JWT_SECRET"), algorithms="HS256")


def token_required(func):
    @wraps(func)
    def decorator():
        if "authorization" in request.headers:
            try:
                dirty_token = request.headers["authorization"]
                token = dirty_token.rsplit(" ", 1)[1] # to take token only, without prefix "Bearer"
                decode(token)
            except jwt.exceptions.ExpiredSignatureError as error:
                return {
                    "message": "token is expired"
                }
            except jwt.exceptions.DecodeError as error:
                return {
                    "message": "invalid token"
                }
            return func()
        else:
            return {
                "message": "token is required"
            }
    return decorator
