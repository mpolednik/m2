from app.helpers.middleware import db

from app.models.rating import VotableObject


class Comment(db.Model, VotableObject):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_father= db.Column(db.Integer, db.ForeignKey('comment.id'))
    id_image= db.Column(db.Integer, db.ForeignKey('image.id'))
    text = db.Column(db.String(1000))
    rating = db.Column(db.Integer, default=0)
    state = db.Column(db.Integer, default=1)
    ts = db.Column(db.DateTime)

    father = db.relationship('Comment')

    def __init__(self, id_user, image, text, father = None):
        self.id_user = id_user
        self.image = image 
        self.text = text
        self.id_father = father

    def __repr__(self):
        return '<Comment({}, {}, {}, {}, {}, {}, {}, {})>'.format(self.id, self.owner, self.id_father, self.id_image, self.text, self.rating, self.state, self.ts)


def construct_comment_tree(comments, father = None):
    tree = []

    for comment in comments:
        if comment.id == father or father is None and comment.id_father == father:
            comment.depth = 1
            tree.append(comment)
            _find_nodes(2, tree, comment, comments)

    return tree


def _find_nodes(depth, tree, father, comments):
    for comment in comments:
        if comment.id_father == father.id:
            comment.depth = depth
            tree.append(comment)
            _find_nodes(depth+1, tree, comment, comments)
