from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models.user import User
from models.post import Post
from resources.user import Users, UserDetail
from resources.post import Posts, PostDetails
app = Flask(__name__)
CORS(app)

api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/flask_finstagram"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(Users, '/users')

api.add_resource(Posts, '/posts')
api.add_resource(PostDetails, '/posts/<int:id>')
api.add_resource(UserDetail, '/users/<user_id>')


if __name__ == '__main__':
    app.run(debug=True)
