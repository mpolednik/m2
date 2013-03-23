from app.helpers.middleware import db


class Request(db.Model):
    __tablename__ = 'request'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'))
    type = db.Column(db.Integer)
    name = db.Column(db.String(30))
    text = db.Column(db.String(1000))
    state = db.Column(db.Integer, default=0)
    ts = db.Column(db.DateTime)


    def __init__(self, id_user, category, type, name, text):
        self.id_user = id_user
        self.category = category 
        self.type = type
        self.name = name
        self.text = text


    def __repr__(self):
        return '<Request({}, {}, {}, {}, {}, {}, {}, {})>'.format(self.id, self.owner, self.category, self.type, self.name, self.text, self.state, self.ts)
