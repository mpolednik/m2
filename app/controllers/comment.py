# coding=utf-8
from flask import redirect, url_for, request, session, flash, jsonify

from app.helpers.middleware import db
from app.helpers.rendering import render
from app.helpers import security
from app.helpers.forms import flash_errors

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.comment import Comment, construct_comment_tree
from app.models.image import Image
from app.models.user import User

from translation import local


class CommentForm(Form):
    text = fields.TextAreaField(local.CONTENT, [validators.Length(10, 1000, local.comment['INVALID_TEXT'])])


class EditForm(CommentForm):
    pass


def comment(id, cid = None):
    form = CommentForm(request.form)

    image = db.session.query(Image).get(id)

    comments = construct_comment_tree(image.comments, cid)
    return render('comment.html', title=local.comment['TITLE_ONE'], id=id, cid=cid, image=image, comments=comments, form=form)


@security.req_login
def comment_submit(id, cid = None):
    form = CommentForm(request.form)

    user = db.session.query(User).get(session['user'])
    image = db.session.query(Image).filter_by(id=id).one()

    if request.method == 'POST' and form.validate():
        comment = Comment(session['user'], image, form.text.data, cid)

        if user.already_commented(image, cid): 
            flash(local.comment['ALREADY_COMMENTED'], 'error')
        else:
            db.session.add(comment)
            db.session.flush()
            comment.vote(1, session['user'])
            db.session.commit()
            flash(local.comment['POSTED'], 'success')

        # Return user to image or comment controllers depending on ref
        if cid is None:
            return redirect(url_for('image', id=image.id))
        else:
            return redirect(url_for('comment', id=image.id, cid=cid))

    flash_errors(form)
    comments = construct_comment_tree(image.comments)
    if cid is None:
        try:
            commented = Comment.query.filter_by(id_user=session['user'], image=image, id_father=None).one()
        except:
            commented = False
        return render('image.html', title=image.name, commented=commented, image=image, form=form, comments=comments)
    else:
        return render('comment.html', title=local.comment['TITLE_ONE'], id=id, cid=cid, comments=comments, form=form)


@security.req_owner(Comment)
def comment_edit(id, cid):
    comment = db.session.query(Comment).filter_by(id=cid).one()

    form = EditForm(request.form, comment)

    image = db.session.query(Image).filter_by(id=id).one()

    if request.method == 'POST' and form.validate():
        comment.text = form.text.data

        db.session.commit()
        flash(local.comment['EDITED'], 'success')

        return redirect(url_for('image', id=id))

    flash_errors(form)
    comments = construct_comment_tree(image.comments, comment.id)

    return render('comment.html', title=local.comment['TITLE_EDIT'], edit=True, image=image, id=id, cid=cid, comments=comments, form=form)


def comment_delete(id):
    comment = Comment.query.get(id)
    user = User.query.get(session['user'])

    if comment.owner != user and 'admin' not in session and user not in comment.image.category.moderators:
        raise security.SecurityException

    comment.state = 0

    db.session.commit()

    return jsonify(text=local.comment['DELETED'])


@security.req_login
def comment_vote():
    id = int(request.args.get('id'))
    rating = int(request.args.get('rating'))
    comment = db.session.query(Comment).get(id)

    if comment.state > 0:
        comment.vote(rating, session['user'])
        db.session.commit()

    user = db.session.query(User).get(session['user'])

    return jsonify(rating=comment.rating, rated=user.voted(comment))
