from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    salt = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username
