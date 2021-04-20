import cloudinary
from cloudinary.uploader import upload
from flask import request
from app import app


cloudinary.config(
    cloud_name = app.config["CLOUD_NAME"],
    api_key = app.config["CLOUD_API_KEY"],
    api_secret = app.config["CLOUD_API_SECRET"]
)


def cloudinary_upload_image():
    """
    upload files to cloudinary
    """
    try:
        upload_image = upload(request.files["image"])
    except Exception as error:
        print(error)
        return None
    print(upload_image)
    return upload_image["secure_url"]
