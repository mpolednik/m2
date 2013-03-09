from flask import request, redirect, url_for, flash
import sqlalchemy.exc

from app.helpers.middleware import db
from app.helpers.rendering import render

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.image import Image
from app.models.user import User
from app.models.comment import Comment, construct_comment_tree
from app.controllers.comment import CommentForm


class EditForm(Form):
    text = fields.TextAreaField('Text')


def image(id):
    form = CommentForm(request.form)

    image = db.session.query(Image).filter_by(id=id).one()
    comments = construct_comment_tree(image.comments)

    return render('image.html', image=image, form=form, comments=comments)


def image_edit(id):
    image = db.session.query(Image).filter_by(id=id).one()

    form = EditForm(request.form, image)

    if request.method == 'POST' and form.validate():
        image.text = form.text.data

        db.session.commit()
        flash('Image dited', 'success')

        return redirect(url_for('image', id=id))

    return render('image_edit.html', image=image, form=form)


def image_delete(id):
    image = db.session.query(Image).filter_by(id=id).one()
    category = image.category.name

    db.session.delete(image)

    db.session.commit()
    flash('Image deleted', 'success')

    return redirect(url_for('category_one', name=category))


def image_vote(id, name=None, page=None):
    image = db.session.query(Image).filter_by(id=id).one()

    if 'v' in request.args:
        if request.args['v'] == 'up':
            rating = 1
        else:
            rating = -1

    image.vote(rating)

    db.session.commit()
    flash('Obrazek hodnocen', 'success')

    if name:
        return redirect(url_for('category_one', name=name, page=page))
    else:
        if 'ref' in request.args:
            return redirect(url_for('category_all'))
        return redirect(url_for('image', id=id))
