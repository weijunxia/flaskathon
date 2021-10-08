from middleware import read_token, strip_token
from flask import request
from flask_restful import Resource
from models.user import User
from models.db import db
from sqlalchemy.orm import joinedload


class Users(Resource):
    def get(self):
        token = strip_token(request)
        if read_token(token)['data']:
            users = User.find_all()
            return [u.json() for u in users]
        else:
            return read_token(token)['payload']


class UserDetail(Resource):
    def get(self, user_id):
        token = strip_token(request)
        if read_token(token)['data']:
            user = User.query.options(joinedload(
                'posts')).filter_by(id=user_id).first()
            posts = [m.json() for m in user.posts]
            return {**user.json(), 'posts': posts}
        else:
            return read_token(token)['payload']

    def put(self, user_id):
        token = strip_token(request)
        if read_token(token)['data']:
            data = request.get_json()
            user = User.find_by_id(user_id)
            for key in data:
                setattr(user, key, data[key])
            db.session.commit()
            return user.json()

    def delete(self, user_id):
        token = strip_token(request)
        if read_token(token)['data']:
            user = User.find_by_id(user_id)
            if not user:
                return {'msg': 'User not found'}, 404
            db.session.delete(user)
            db.session.commit()
            return {'msg': 'User deleted', 'payload': user_id}
        else:
            read_token(token)['payload']
