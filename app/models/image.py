# coding=utf-8
import os
import urllib
from PIL import Image as Img
from PIL.ExifTags import TAGS
import pickle

import config.upload

from app.helpers.middleware import db, app

from app.models.comment import Comment
from app.models.rating import VotableObject


class ImageRating(db.Model):
    __tablename__ = 'image_rating'

    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, autoincrement=False)
    id_target = db.Column(db.Integer, db.ForeignKey('image.id'), primary_key=True)
    value = db.Column(db.Integer)

    def __init__(self, id_user, id_target, value):
        self.id_user = id_user
        self.id_target = id_target
        self.value = value


class Exif(db.Model):
    __tablename__ = 'exif'

    id_image = db.Column(db.Integer, db.ForeignKey('image.id'), primary_key=True, autoincrement=False)
    key = db.Column(db.String(40), primary_key=True)
    _value = db.Column('value', db.String(200))

    @property
    def value(self):
        try:
            return pickle.loads(self._value)
        except:
            return None

    @value.setter
    def value(self, v):
        self._value = pickle.dumps(v)

    def __init__(self, image, key, value):
        self.image = image
        self.key = key
        self.value = value

    def __repr__(self):
        return '<User({}, {}, {})>'.format(self.image, self.key, self.value)


class Image(db.Model, VotableObject):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'))
    name = db.Column(db.String(30))
    text = db.Column(db.String(1024))
    link = db.Column(db.String(200))
    kind = db.Column(db.String(4))
    rating = db.Column(db.Integer, default=0)
    score = db.Column(db.Float, default=0)
    ts = db.Column(db.DateTime)

    RatingClass = ImageRating

    exif = db.relationship('Exif', backref='image', cascade='delete')
    # id.father order desc to optimize tree generating algorithm
    comments = db.relationship('Comment', backref='image', order_by=(Comment.id_father.desc(), Comment.rating.desc(), Comment.ts.desc()),
                               cascade='all, delete-orphan', passive_deletes=True)


    def __init__(self, id_user, category, name, text, link, filename):
        self.id_user = id_user
        self.category = category
        self.name = name
        self.text = text
        self.link = link
        self.kind = self._extension(filename)


    def __repr__(self):
        return '<Image({}, {}, {}, {}, {}, {}, {}, {}, {})>'.format(self.id, self.owner, self.category, self.name, self.text, self.link, self.score, self.rating, self.ts)


    @property
    def filename(self):
        return '{}.{}'.format(self.id, self.kind)


    @property
    def allowed(self):
        return '.' in self.filename and \
            self.kind.lower() in app.config['ALLOWED_EXTENSIONS']


    @staticmethod
    def _extension(filename):
        return filename.rsplit('.', 1)[1]


    def save(self, file = None):
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], self.filename))
        else:
            urllib.urlretrieve(self.link, os.path.join(app.config['UPLOAD_FOLDER'], self.filename))


    def save_thumbnail(self):
        im = Img.open(os.path.join(app.config['UPLOAD_FOLDER'], self.filename))
        im.thumbnail(app.config['THUMBNAIL_SIZE'], Img.ANTIALIAS)
        im.save(os.path.join(app.config['THUMB_UPLOAD_FOLDER'], self.filename))


    def save_exif(self):
        if self.kind in app.config['EXIF_EXTENSIONS']:
            try:
                for (k, v) in Img.open(os.path.join(app.config['UPLOAD_FOLDER'], self.filename))._getexif().iteritems():
                    db.session.add(Exif(self, TAGS.get(k), v))
            except:
                return


    def delete_files(self):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], self.filename))
        os.remove(os.path.join(app.config['THUMB_UPLOAD_FOLDER'], self.filename))
