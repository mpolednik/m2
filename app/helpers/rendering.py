from flask import render_template, session
from app.helpers.middleware import db

from app.models.category import Category
from app.models.user import User

def render(template, **context):
    categories = db.session.query(Category).all()

    if 'user' in session:
        user = session['user']
    else:
        user = None

    return render_template(template, DEF_user=user, DEF_categories=categories, **context)
