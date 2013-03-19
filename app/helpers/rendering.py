# coding=utf-8
from flask import render_template, session
from app.helpers.middleware import db

from app.models.category import Category
from app.models.user import User

from translation import local

def render(template, **context):
    categories = db.session.query(Category).all()
    try:
        user = db.session.query(User).get(session['user'])
    except:
        user = None

    return render_template(template, local=local, DEF_user=user, DEF_categories=categories, **context)
