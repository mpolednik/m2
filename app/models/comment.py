from app.helpers.middleware import db

class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_father= db.Column(db.Integer, db.ForeignKey('comment.id'))
    id_image= db.Column(db.Integer, db.ForeignKey('image.id'))
    text = db.Column(db.String(1000))
    rating = db.Column(db.Integer, default=0)
    ts = db.Column(db.DateTime)

    father = db.relationship('Comment')

    def __init__(self, owner, image, text, father = None):
        self.owner = owner
        self.image = image 
        self.text = text
        self.id_father = father

    def __repr__(self):
        return '<Comment({}, {}, {}, {}, {}, {}, {})>'.format(self.id, self.owner, self.id_father, self.id_image, self.text, self.rating, self.ts)
