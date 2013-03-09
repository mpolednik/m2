from app.helpers.middleware import db

from app.models.request import Request
from app.models.image import Image


moderator = db.Table('moderator',
    db.Column('id_user', db.Integer, db.ForeignKey('user.id'), primary_key = True),
    db.Column('id_category', db.Integer, db.ForeignKey('category.id'), primary_key = True))


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, default=0)
    name = db.Column(db.String(30))
    text = db.Column(db.Text)
    ts = db.Column(db.DateTime)

    moderators = db.relationship('User', secondary=moderator)
    images = db.relationship('Image', backref='category', order_by=(Image.score.desc(), Image.ts.desc()))
    requests = db.relationship('Request', backref='category')

    def __init__(self, name, text):
        self.name = name
        self.text = text

    def __repr__(self):
        return '<Category({}, {}, {}, {}, {})>'.format(self.id, self.rating, self.name, self.text, self.ts)
