import os
import cloudinary
from cloudinary.uploader import upload
from flask import request


cloudinary.config(
    cloud_name = os.getenv("CLOUD_NAME"),
    api_key = os.getenv("CLOUD_API_KEY"),
    api_secret = os.getenv("CLOUD_API_SECRET")
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
