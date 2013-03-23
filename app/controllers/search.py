# coding=utf-8
from flask import request
from app.helpers.middleware import db

from app.helpers.rendering import render

from app.models.user import User
from app.models.image import Image
from app.models.category import Category

from translation import local


def search(upage=1, ipage=1):
    q = request.args.get('q')
    categories = Category.query.filter(Category.name.like('%{}%'.format(q))).all()
    categories_related = Category.query.filter(Category.text.like('%{}%'.format(q))).all()
    users = User.query.filter(User.name.like('%{}%'.format(q))).paginate(upage, 20)
    images = Image.query.filter(db.or_(Image.name.like('%{}%'.format(q)), 
                                       Image.text.like('%{}%'.format(q)))).paginate(ipage, 20)

    return render('search.html', title=local.search['TITLE_SEARCH'], q=q, categories=categories, categories_related=categories_related, users=users, images=images)
