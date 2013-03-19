from flask import redirect, url_for

from app.helpers.middleware import db

from app.helpers.rendering import render

from app.models.comment import Comment

def admin_comment(page=1):
    comments = Comment.query.paginate(page, 20)

    return render('admin/comment.html', comments=comments)

def admin_comment_delete(id, page):
    comment = db.session.query(Comment).get(id)
    comment.state = 0
    db.session.commit()
    return redirect(url_for('admin_comment', page=page))
