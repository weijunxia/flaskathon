from datetime import datetime
from models.db import db


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(280), nullable=False)
    image = db.Column(db.String(280), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('users', lazy=True))

    def __init__(self, caption, image, likes, user_id):
        self.caption = caption
        self.image = image
        self.likes = likes
        self.user_id = user_id

    def json(self):
        return {"id": self.id, "caption": self.caption, "image": self.image, "likes": self.likes, "user_id": self.user_id, "created_at": str(self.created_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        posts = Post.query.all()
        return [p.json() for p in posts]

    @classmethod
    def find_by_id(cls, id):
        post = Post.query.filter_by(id=id).first()
        return post
