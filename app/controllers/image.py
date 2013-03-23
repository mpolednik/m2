# coding=utf-8
from flask import request, redirect, url_for, flash, session
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
        flash(local.image['EDITTED'], 'success')

        return redirect(url_for('image', id=id))

    flash_errors(form)
    return render('image_edit.html', title=local.image['TITLE_EDIT'], image=image, form=form)


@security.req_owner(Image)
def image_delete(id, ref=None):
    image = db.session.query(Image).filter_by(id=id).one()
    category = image.category.name

    try:
        db.session.delete(image)
    except:
        pass
    else:
        image.delete_files()

    db.session.commit()
    flash(local.image['DELETED'], 'success')

    if ref:
        return redirect(ref)
    else:
        return redirect(url_for('category_one', name=category))


@security.req_login
def image_vote(id, name=None, page=1):
    image = db.session.query(Image).get(id)

    if 'v' in request.args:
        if request.args['v'] == 'up':
            rating = 1
        else:
            rating = -1

    image.vote(rating, session['user'])

    db.session.commit()
    flash(local.image['VOTED'], 'success')

    if name:
        return redirect(url_for('category_one', name=name, page=page))
    else:
        if 'ref' in request.args:
            return redirect(url_for('category_all', page=page))
        return redirect(url_for('image', id=id))
