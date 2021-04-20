from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(filename=".env")) # environment variables akan masuk ke modul os, jadi perlu import modul os


import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    JWT_SECRET = os.getenv("JWT_SECRET")
    CLOUD_NAME = os.getenv("CLOUD_NAME")
    CLOUD_API_KEY = os.getenv("CLOUD_API_KEY")
    CLOUD_API_SECRET = os.getenv("CLOUD_API_SECRET")


class Production(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_PRODUCTION")


class Production(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_LOCAL")
