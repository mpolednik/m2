from flask import render_template, session
from app.helpers.middleware import db
from app.helpers.bootstrap import current_user

from app.models.category import Category
from app.models.user import User

def render(template, **context):
    categories = db.session.query(Category).all()

    return render_template(template, DEF_user=current_user, DEF_categories=categories, **context)
