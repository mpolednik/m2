from flask import redirect, url_for, request, flash

from app.helpers.middleware import db
from app.helpers.rendering import render
from app.helpers import security

from app.models.comment import Comment

from translation import local


@security.req_admin
def admin_comment(page=1):
    if 'q' in request.args:
        q = request.args.get('q')
        comments = Comment.query.filter(Comment.text.like('%{}%'.format(q))).paginate(page, 20)
    else:
        comments = Comment.query.paginate(page, 20)

    return render('admin/comment.html', title=local.comment['TITLE_ADMIN_LIST'], comments=comments)


@security.req_admin
def admin_comment_delete(id, page):
    comment = db.session.query(Comment).get(id)
    comment.state = 0
    db.session.commit()
    flash(local.admin['COMMENT_DELETED'], 'success')

    return redirect(url_for('admin_comment', page=page))
