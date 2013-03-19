from flask import request
from app.helpers.middleware import db

from app.helpers.rendering import render

from app.models.user import User
from app.models.image import Image
from app.models.category import Category

def search(upage=1, ipage=1):
    q = request.args.get('q')
    categories = Category.query.filter(Category.name.like('%{}%'.format(q))).paginate(upage, 20)
    users = User.query.filter(User.name.like('%{}%'.format(q))).paginate(upage, 20)
    images = Image.query.filter(Image.name.like('%{}%'.format(q))).paginate(ipage, 20)

    return render('search.html', q=q, categories=categories, users=users, images=images)
