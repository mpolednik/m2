from flask import session
from app.helpers.middleware import db, bcrypt

from app.models.image import Image
from app.models.comment import Comment
from app.models.request import Request


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    mail = db.Column(db.String(255))
    _password = db.Column('password', db.String(32))
    phone = db.Column(db.String(16))
    rating_image = db.Column(db.Integer, default=0)
    rating_comment = db.Column(db.Integer, default=0)
    ts = db.Column(db.DateTime)
    level = db.Column(db.Integer, default=0)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = bcrypt.generate_password_hash(password)

    images = db.relationship('Image', backref='owner')
    comments = db.relationship('Comment', backref='owner')
    requests = db.relationship('Request', backref='owner')

    def __init__(self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password

    def __repr__(self):
        return '<User({}, {}, {}, {}, {}, {}, {}, {}, {})>'.format(self.id, self.name, self.mail, self.password, self.phone, self.rating_image, self.rating_comment, self.ts, self.level)

    def already_commented(self, image, top = False):
        # Check if top-level comment for current image already exists
        if top:
            cnt = 0
        else:
            cnt = db.session.query(Comment).filter_by(image=image, id_user=self.id, id_father=None).count()

        if cnt > 0:
            return True
        else:
            return False

    @staticmethod
    def login(mail, password):
        candidate = db.session.query(User).filter_by(mail=mail).one()

        if (bcrypt.check_password_hash(candidate.password, password)):
            session['user'] = candidate.id
        else:
            raise Exception

    @staticmethod
    def logout():
        session.destroy()
