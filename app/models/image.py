from app.helpers.middleware import db

from app.models.category import Category
from app.models.comment import Comment

class Exif(db.Model):
    __tablename__ = 'exif'

    id_image = db.Column(db.Integer, db.ForeignKey('image.id'), primary_key=True, autoincrement=False)
    key = db.Column(db.String(40), primary_key=True)
    value = db.Column(db.String(200))

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return '<User({}, {}, {})>'.format(self.image, self.key, self.value)

class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'))
    name = db.Column(db.String(30))
    text = db.Column(db.String(1024))
    path = db.Column(db.String(200))
    rating = db.Column(db.Integer, default=0)
    ts = db.Column(db.DateTime)

    exif = db.relationship('Exif', backref='image')
    comments = db.relationship('Comment', backref='image', order_by=Comment.id_father)

    def __init__(self, owner, category, name, text, path):
        self.owner = owner
        self.category = category
        self.name = name
        self.text = text
        self.path = path 

    def __repr__(self):
        return '<Image({}, {}, {}, {}, {}, {}, {}, {})>'.format(self.id, self.owner, self.category, self.name, self.text, self.path, self.rating, self.ts)
