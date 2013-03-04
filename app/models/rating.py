from flask import session

from app.helpers.middleware import db


class CommentRating(db.Model):
    __tablename__ = 'comment_rating'

    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, autoincrement=False)
    id_target = db.Column(db.Integer, db.ForeignKey('comment.id'), primary_key=True)
    value = db.Column(db.Integer)

    def __init__(self, id_user, id_target, value):
        self.id_user = id_user
        self.id_target = id_target
        self.value = value


class ImageRating(db.Model):
    __tablename__ = 'image_rating'

    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, autoincrement=False)
    id_target = db.Column(db.Integer, db.ForeignKey('image.id'), primary_key=True)
    value = db.Column(db.Integer)

    def __init__(self, id_user, id_target, value):
        self.id_user = id_user
        self.id_target = id_target
        self.value = value


class VotableObject(object):

    def vote(self, rating):
        try:
            rate = db.session.query(self.RatingClass).get((session['user'], self.id))
            if (rate.value + rating) > 1 or (rate.value + rating < -1):
                change = 0
            else:
                change = rating
                rate.value += change
        except:
            rate = self.RatingClass(session['user'], self.id, rating)
            db.session.add(rate)
            change = rating

        self.rating += change
