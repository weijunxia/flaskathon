from middleware import read_token, strip_token
from models.db import db
from models.post import *
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload


class Posts(Resource):
    def get(self):
        token = strip_token(request)
        if read_token(token)['data']:
            posts = Post.find_all()
            return posts
        else:
            return read_token(token)['payload']

    def post(self):
        token = strip_token(request)
        if read_token(token)['data']:
            data = request.get_json()
            params = {}
            for k in data.keys():
                params[k] = data[k]
            post = Post(**params)
            post.create()
            return post.json(), 201
        else:
            return read_token(token)['payload']


class PostDetails(Resource):
    def get(self, post_id):
        token = strip_token(request)
        if read_token(token)['data']:
            post = Post.query.options(joinedload(
                "user")).filter_by(id=post_id).first()
            return {**post.json(), "user": post.user.json()}
        else:
            return read_token(token)['payload']

    def put(self, post_id):
        data = request.get_json()
        post = Post.find_by_id(post_id)
        for key in data:
            setattr(post, key, data[key])
        db.session.commit()
        return post.json()

    def delete(self, post_id):
        token = strip_token(request)
        if read_token(token)['data']:
            post = Post.find_by_id(post_id)
            if not post:
                return {"Message": "Not Found"}, 404
            db.session.delete(post)
            db.session.commit()
            return {"Message": "Post Deleted", "payload": post_id}
        else:
            return read_token(token)['payload']
