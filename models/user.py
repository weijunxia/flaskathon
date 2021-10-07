from datetime import datetime
from models.db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    posts = db.relationship('Post', cascade='all',
                            backref=db.backref('posts', lazy=True))

    def __init__(self, username):
        self.username = username

    def json(self):
        return {'id': self.id, 'username': self.username, 'created_at': str(self.created_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return User.query.all()

    @classmethod
    def find_by_id(cls, user_id):
        user = User.query.filter_by(id=user_id).first()
        return user
