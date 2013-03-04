from app.helpers.middleware import db

class Rating(db.Model):
    __tablename__ = 'rating'

    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, autoincrement=False)
    id_target = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    ts = db.Column(db.DateTime)

    def __init__(self, id_user, id_target, value):
        self.id_user = id_user
        self.id_target = name
        self.value = value

    def __repr__(self):
        return '<Rating({}, {}, {}, {})>'.format(self.owner, self.id_target, self.value, self.ts)
