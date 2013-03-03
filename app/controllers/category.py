from app.helpers.middleware import db, app
from app.helpers.rendering import render

from app.models.image import Image
from app.models.category import Category

def category_all():
    images = db.session.query(Image).all()

    return render('category.html', title='test', images=images)

def category_one(name):
    category = db.session.query(Category).filter_by(name=name).one()
    images = db.session.query(Image).filter_by(category=category).all()

    return render('category.html', title='test', category=category, images=images)
