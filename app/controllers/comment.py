from flask import redirect, url_for, request, session, flash

from app.helpers.middleware import db
from app.helpers.rendering import render
from app.helpers import security

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.comment import Comment, construct_comment_tree
from app.models.image import Image
from app.models.user import User


class CommentForm(Form):
    text = fields.TextAreaField('Text')


class EditForm(Form):
    text = fields.TextAreaField('Text')


def comment(id, cid = None):
    form = CommentForm(request.form)

    image = db.session.query(Image).get(id)

    comments = construct_comment_tree(image.comments, cid)
    return render('comment.html', id=id, cid=cid, comments=comments, form=form)


@security.req_login
def comment_submit(id, cid = None):
    form = CommentForm(request.form)

    user = db.session.query(User).get(session['user'])
    image = db.session.query(Image).filter_by(id=id).one()

    if request.method == 'POST' and form.validate():
        comment = Comment(session['user'], image, form.text.data, cid)

        if user.already_commented(image, cid): 
            flash('Komentar neulozen', 'error')
        else:
            db.session.add(comment)
            db.session.commit()
            flash('Komentar ulozen', 'success')

        # Return user to image or comment controllers depending on ref
        if cid is None:
            return redirect(url_for('image', id=image.id))
        else:
            return redirect(url_for('comment', id=image.id, cid=cid))


@security.req_owner(Comment)
def comment_edit(id, cid):
    comment = db.session.query(Comment).filter_by(id=cid).one()

    form = EditForm(request.form, comment)

    image = db.session.query(Image).filter_by(id=id).one()

    if request.method == 'POST' and form.validate():
        comment.text = form.text.data

        db.session.commit()
        flash('Komentar editovan', 'success')

        return redirect(url_for('image', id=id))

    comments = construct_comment_tree(image.comments, comment.id)

    return render('comment.html', edit=True, id=id, cid=cid, comments=comments, form=form)


@security.req_owner(Comment)
def comment_delete(id, cid):
    comment = db.session.query(Comment).filter_by(id=cid).one()
    comment.state = 0

    db.session.commit()
    flash('Komentar smazan', 'success')

    return redirect(url_for('image', id=id))


@security.req_login
def comment_vote(id, cid):
    comment = db.session.query(Comment).filter_by(id=cid).one()

    if 'v' in request.args:
        if request.args['v'] == 'up':
            rating = 1
        else:
            rating = -1

    comment.vote(rating)

    db.session.commit()
    flash('Komentar hodnocen', 'success')

    return redirect(url_for('image', id=id))
