from flask import redirect, url_for

from app.helpers.middleware import db
from app.helpers.rendering import render
from app.helpers import security

from app.models.user import User

@security.req_admin
def admin_user(page=1):
    users = User.query.paginate(page, 20)

    return render('admin/user.html', users=users)

@security.req_admin
def admin_user_delete(id, page):
    user = db.session.query(User).get(id)
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('admin_user', page=page))
