from flask import Flask, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config.from_object("app.config.Production")

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory="app/migrations")
from app.models import User, Todo # need to import the models for migrating here (the order matters)
from app.routes import Home, User, Todo # order matters, bcs these imported classes need `app` object
