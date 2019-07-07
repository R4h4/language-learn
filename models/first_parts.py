from shortid import ShortId; short_id = ShortId()

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self,):
        pass

    def __repr__(self):
        return '<User %r>' % self.username
