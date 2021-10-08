from flask import request
from flask_restful import Resource
from datetime import datetime
from models.db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password_digest = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    posts = db.relationship('Post', cascade='all',
                            backref=db.backref('posts', lazy=True))

    def __init__(self, username, password_digest):
        self.username = username
        self.password_digest = password_digest

    def json(self):
        return {'id': self.id, "username": self.username, "password_digest": self.password_digest, 'created_at': str(self.created_at), "updated_at": str(self.updated_at)}

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

    @classmethod
    def find_by_username(cls, username):
        user = User.query.filter_by(username=username).first()
        return user


class SingleUser(Resource):
    def get(self, id):
        user = User.find_by_id(id)
        return user.json(), 200

    def delete(self, id):
        user = User.find_by_id(id)
        if not user:
            return {"Message": "Not Found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"Message": "User Delete", "payload": id}

    def put(self, id):
        data = request.get.json()
        user = User.find_by_id(id)
        for key in data:
            setattr(user, key, data[key])
        db.session.commit()
        return user.json()
