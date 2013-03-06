from flask import redirect, url_for, request, session, flash

from app.helpers.middleware import db, app
from app.helpers.rendering import render

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.image import Image
from app.models.category import Category
from app.controllers.image import image_vote


class SubmitForm(Form):
    name = fields.TextField('Jmeno')
    text = fields.TextAreaField('Text')
    path = fields.TextAreaField('Path')
    file = fields.FileField('Image')


class EditForm(Form):
    text = fields.TextAreaField('Text')


def category_all():
    images = sorted(db.session.query(Image).all(), key=lambda image: image.score, reverse=True)

    return render('category.html', title='test', images=images)


def category_one(name):
    category = db.session.query(Category).filter_by(name=name).one()
    images = sorted(db.session.query(Image).filter_by(category=category).all(), key=lambda image: image.score, reverse=True)

    return render('category.html', title='test', category=category, images=images)


def category_submit(name):
    form = SubmitForm(request.form)

    category = db.session.query(Category).filter_by(name=name).one()

    if request.method == 'POST' and form.validate():
        image = Image(session['user'], category, form.name.data, form.text.data, form.path.data)
        db.session.add(image)

        flash('Obrazek postnut', 'success')
        return redirect(url_for('category_one', name=name))

    return render('category_submit.html', title='test', form=form)


def category_edit(name):
    form = EditForm()

    category = db.session.query(Category).filter_by(name=name).one()

    if request.method == 'POST' and form.validate():
        category.text = form.text.data

        flash('Kategorie editovana', 'success')
        return redirect(url_for('category_one', name=name))

    return render('category_edit.html', title='test', form=form, category=category)
