from flask import Flask, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv(filename=".env")) # environment variables akan masuk ke modul os, jadi perlu import modul os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory="app/migrations")
from app.models import User, Todo # need to import the models for migrating here (the order matters)
from app.routes import Home, User, Todo # order matters, bcs these imported classes need `app` object
