from flask import redirect, url_for

from app.helpers.middleware import db

from app.helpers.rendering import render

from app.models.image import Image

def admin_image(page=1):
    categories = Image.query.paginate(page, 20)

    return render('admin/category.html', categories=categories)
