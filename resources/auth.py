from flask_restful import Resource
from flask import request
from models.user import User
from middleware import create_token, gen_password, strip_token, read_token, compare_password


class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.find_by_username(data["username"])
        if compare_password(data["password"], user.json()["password_digest"]):
            token = create_token(
                {"id": str(user.json()["id"]), "username": str(user.json()["username"])})
            return token, 200

    def get(self):
        data = request.get_json()
        if read_token(data["token"]) == "Signature Invalid" or read_token(data["token"]) == "Token Invalid":
            return {"message": "unauthorized"}, 404
        return read_token(data["token"]), 200


class Register(Resource):
    def post(self):
        data = request.get_json()
        params = {
            "username": data['username'],
            "password_digest": gen_password(data['password'])
        }
        user = User(**params)
        user.create()
        return user.json(), 201
