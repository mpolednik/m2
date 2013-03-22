from flask import redirect, url_for

from app.helpers.middleware import db, cache
from app.helpers.rendering import render
from app.helpers import security

from app.models.category import Category

@security.req_admin
def admin_category(page=1):
    categories = Category.query.paginate(page, 20)

    return render('admin/category.html', categories=categories)

@security.req_admin
def admin_category_delete(id, page):
    category = db.session.query(Category).get(id)
    db.session.delete(category)
    db.session.commit()
    cache.delete('categories')

    return redirect(url_for('admin_category', page=page))
