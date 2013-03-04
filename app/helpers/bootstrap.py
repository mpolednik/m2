from flask import session
from app.helpers.middleware import db

from app.models.user import User

try:
    candidate = db.session.query(User).filter_by(id=session['user']).one()
except:
    current_user = None
else:
    current_user = candidate
