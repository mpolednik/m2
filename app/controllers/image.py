from flask import request, redirect

from app.helpers.middleware import db
from app.helpers.bootstrap import current_user
from app.helpers.rendering import render

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.image import Image
from app.models.comment import Comment, construct_comment_tree
from app.controllers.comment import CommentForm

class EditForm(Form):
    text = fields.TextAreaField('Text')

def image(id):
    form = CommentForm(request.form)

    image = db.session.query(Image).filter_by(id=id).one()

    if request.method == 'POST' and form.validate():
        comment = Comment(current_user, image, form.text.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('image', id=id))

    comments = construct_comment_tree(image.comments)

    return render('image.html', image=image, form=form, comments=comments)

def image_edit(id):
    image = db.session.query(Image).filter_by(id=id).one()

    form = EditForm(request.form, image)

    if request.method == 'POST' and form.validate():
        image.text = form.text.data
        db.session.commit()
        return redirect(url_for('image', id=id))

    return render('image_edit.html', image=image, form=form)

def image_delete(id):
    image = db.session.query(Image).filter_by(id=id).one()
    category = image.category

    db.session.delete(image)
    db.session.commit()
    return redirect(url_for('category_one', category=name))

def image_vote(id):
    return 'VOTING'
