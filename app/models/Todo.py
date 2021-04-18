from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo  = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    status = db.Column(db.Boolean)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('todo', lazy=True))

    def __repr__(self):
        return '<Todo %r>' % self.todo


    def data_to_json(self):
        return {
            "id": self.id,
            "todo": self.todo,
            "description": self.description,
            "status": self.status,
        }
