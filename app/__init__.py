from flask import Flask, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv(filename=".env")) # environment variables akan masuk ke modul os, jadi perlu import modul os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory="app/migrations")

from app.models import Todo, User # need to import the models for migrating here (the order matters)
