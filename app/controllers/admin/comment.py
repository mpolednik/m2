from flask import redirect, url_for

from app.helpers.middleware import db
from app.helpers.rendering import render
from app.helpers import security

from app.models.comment import Comment

from app.controllers.comment import comment_delete

@security.req_admin
def admin_comment(page=1):
    comments = Comment.query.paginate(page, 20)

    return render('admin/comment.html', comments=comments)

@security.req_admin
def admin_comment_delete(id, page):
    return comment_delete(cid=id, ref=url_for('admin_comment', page=page))
