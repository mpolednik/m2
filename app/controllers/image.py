# coding=utf-8
from flask import request, redirect, url_for, flash, session, jsonify
import sqlalchemy.exc

from app.helpers.middleware import db
from app.helpers.rendering import render
from app.helpers import security
from app.helpers.forms import flash_errors

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.image import Image
from app.models.user import User
from app.models.comment import Comment, construct_comment_tree
from app.controllers.comment import CommentForm

from translation import local


class EditForm(Form):
    text = fields.TextAreaField('Text')


def image(id):
    form = CommentForm(request.form)

    image = db.session.query(Image).filter_by(id=id).one()
    comments = construct_comment_tree(image.comments)

    try:
        commented = Comment.query.filter_by(id_user=session['user'], image=image, id_father=None).one()
    except:
        commented = False

    return render('image.html', title=image.name, commented=commented, image=image, form=form, comments=comments)


@security.req_owner(Image)
def image_edit(id):
    image = db.session.query(Image).filter_by(id=id).one()

    form = EditForm(request.form, image)

    if request.method == 'POST' and form.validate():
        image.text = form.text.data

        db.session.commit()
        flash(local.image['EDITED'], 'success')

        return redirect(url_for('image', id=id))

    flash_errors(form)
    return render('image_edit.html', title=local.image['TITLE_EDIT'], image=image, form=form)


def image_delete(id, ref=None):
    image = Image.query.get(id)
    user = User.query.get(session['user'])

    if image.owner != user and 'admin' not in session and user not in image.category.moderators:
        raise security.SecurityException

    try:
        category = image.category.name
    except:
        category = False

    try:
        db.session.delete(image)
    except:
        pass
    else:
        try:
            image.delete_files()
        except:
            pass

    db.session.commit()
    flash(local.image['DELETED'], 'success')

    if ref:
        return redirect(ref)
    elif category:
        return redirect(url_for('category_one', name=category))
    else:
        return redirect(url_for('category_all'))


@security.req_login
def image_vote():
    id = int(request.args.get('id'))
    rating = int(request.args.get('rating'))
    image = db.session.query(Image).get(id)

    image.vote(rating, session['user'])
    db.session.commit()

    user = db.session.query(User).get(session['user'])

    return jsonify(rating=image.rating, rated=user.voted(image))
