from app.helpers.middleware import db
from app.helpers.rendering import render

from app.models.user import User

def user(id):
    user = db.session.query(User).filter_by(id=id).one()
    return render('user.html', user=user)
    pass
