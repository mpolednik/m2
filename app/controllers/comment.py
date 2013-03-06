from flask import redirect, url_for, request, session, flash

from app.helpers.middleware import db
from app.helpers.rendering import render

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.comment import Comment, construct_comment_tree
from app.models.image import Image


class CommentForm(Form):
    text = fields.TextAreaField('Text')


class EditForm(Form):
    text = fields.TextAreaField('Text')


def comment(id, cid):
    form = CommentForm(request.form)

    image = db.session.query(Image).filter_by(id=id).one()
    comment = db.session.query(Comment).filter_by(id=cid).one()

    if request.method == 'POST' and form.validate():
        comment = Comment(session['user'], image, form.text.data, comment.id)
        db.session.add(comment)

        flash('Komentar ulozen')
        return redirect(url_for('image', id=id))

    comments = construct_comment_tree(image.comments, comment.id)

    return render('comment.html', comments=comments, form=form)


def comment_edit(id, cid):
    comment = db.session.query(Comment).filter_by(id=cid).one()

    form = EditForm(request.form, comment)

    image = db.session.query(Image).filter_by(id=id).one()

    if request.method == 'POST' and form.validate():
        comment.text = form.text.data

        flash('Komentar editovan')
        return redirect(url_for('image', id=id))

    comments = construct_comment_tree(image.comments, comment.id)

    return render('comment.html', comments=comments, form=form)


def comment_delete(id, cid):
    comment = db.session.query(Comment).filter_by(id=cid).one()
    comment.state = 0

    flash('Komentar smazan')
    return redirect(url_for('image', id=id))


def comment_vote(id, cid):
    comment = db.session.query(Comment).filter_by(id=cid).one()

    if 'v' in request.args:
        if request.args['v'] == 'up':
            rating = 1
        else:
            rating = -1

    comment.vote(rating)

    flash('Komentar hodnocen')
    return redirect(url_for('image', id=id))
