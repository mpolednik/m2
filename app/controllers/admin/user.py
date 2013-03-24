from flask import redirect, url_for, request

from app.helpers.middleware import db
from app.helpers.rendering import render
from app.helpers import security

from app.models.user import User

from translation import local


@security.req_admin
def admin_user(page=1):
    if 'q' in request.args:
        q = request.args.get('q')
        print q.split(';')
        users = User.query.filter(User.name.like('%{}%'.format(q))).paginate(page, 20)
    else:
        users = User.query.paginate(page, 20)

    return render('admin/user.html', title=local.user['TITLE_ADMIN_LIST'], users=users)


@security.req_admin
def admin_user_delete(id, page):
    user = db.session.query(User).get(id)
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('admin_user', page=page))


@security.req_admin
def admin_user_promote(id, page):
    user = db.session.query(User).get(id)
    user.level = 2
    db.session.commit()

    return redirect(url_for('admin_user', page=page))


@security.req_admin
def admin_user_demote(id, page):
    user = db.session.query(User).get(id)
    if len(user.categories) < 2:
        user.level = 0
    else:
        user.level = 1
    db.session.commit()

    return redirect(url_for('admin_user', page=page))
