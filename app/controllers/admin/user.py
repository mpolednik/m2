from flask import redirect, url_for

from app.helpers.middleware import db

from app.helpers.rendering import render

from app.models.user import User

def admin_user(page=1):
    categories = User.query.paginate(page, 20)

    return render('admin/category.html', categories=categories)
