from app.helpers.middleware import db

from app.models.comment import Comment
from app.models.rating import VotableObject, calculate_score


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
    value = db.Column(db.String(200))

    def __init__(self, key, value):
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
    kind = db.Column(db.String(4))
    rating = db.Column(db.Integer, default=0)
    score = db.Column(db.Integer, default=0)
    ts = db.Column(db.DateTime)

    RatingClass = ImageRating

    exif = db.relationship('Exif', backref='image')
    # id.father order desc to optimize tree generating algorithm
    comments = db.relationship('Comment', backref='image', order_by=(Comment.id_father.desc(), Comment.rating.desc(), Comment.ts.desc()),
                               cascade='all, delete-orphan', passive_deletes=True)

    def __init__(self, id_user, category, name, text):
        self.id_user = id_user
        self.category = category
        self.name = name
        self.text = text

    def __repr__(self):
        return '<Image({}, {}, {}, {}, {}, {}, {}, {})>'.format(self.id, self.owner, self.category, self.name, self.text, self.score, self.rating, self.ts)

    @property
    def filename(self):
        return '{}.{}'.format(self.id, self.kind)
