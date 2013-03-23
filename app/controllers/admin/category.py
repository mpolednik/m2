from flask import redirect, url_for, request

from app.helpers.middleware import db, cache
from app.helpers.rendering import render
from app.helpers import security

from app.models.category import Category

from translation import local


@security.req_admin
def admin_category(page=1):
    if 'q' in request.args:
        q = request.args.get('q')
        categories = Category.query.filter(Category.name.like('%{}%'.format(q))).paginate(page, 20)
    else:
        categories = Category.query.paginate(page, 20)

    return render('admin/category.html', title=local.category['TITLE_ADMIN_LIST'], categories=categories)


@security.req_admin
def admin_category_delete(id, page):
    category = db.session.query(Category).get(id)
    db.session.delete(category)
    db.session.commit()
    cache.delete('categories')

    return redirect(url_for('admin_category', page=page))
