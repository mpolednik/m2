import os
import Image as Img
from datetime import datetime
import urllib

from flask import redirect, url_for, request, session, flash

from app.helpers.middleware import db, app
from app.helpers.rendering import render

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.image import Image
from app.models.category import Category
from app.controllers.image import image_vote
from app.models.rating import calculate_score


class SubmitForm(Form):
    name = fields.TextField('Jmeno')
    text = fields.TextAreaField('Text')
    path = fields.TextAreaField('Path')
    image = fields.FileField('Image')


class EditForm(Form):
    text = fields.TextAreaField('Text')


def category_all():
    images = db.session.query(Image).order_by(Image.score.desc(), Image.ts.desc()).paginate()

    return render('category.html', title='test', images=images)


def category_one(name):
    category = db.session.query(Category).filter_by(name=name).one()
    images = category.images

    return render('category.html', title='test', category=category, images=images)

FOLDER = 'static/img/upload'
THUMB_FOLDER = 'static/img/thumb'
EXTENSIONS = ('jpg', 'jpeg', 'png')
size = (256, 256)
app.config['UPLOAD_FOLDER'] = FOLDER
app.config['THUMB_UPLOAD_FOLDER'] = THUMB_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           ext(filename) in EXTENSIONS

def create_name(id, filename):
    return '{}.{}'.format(id, ext(filename))

def ext(filename):
    return filename.rsplit('.', 1)[1]

def genthumbnail(id, filename):
    im = Img.open(os.path.join(app.config['UPLOAD_FOLDER'], create_name(id, filename)))
    im.thumbnail(size, Img.ANTIALIAS)
    im.save(os.path.join(app.config['THUMB_UPLOAD_FOLDER'], create_name(id, filename)))

def category_submit(name):
    form = SubmitForm(request.form)

    category = db.session.query(Category).filter_by(name=name).one()

    if request.method == 'POST' and form.validate():
        image = Image(session['user'], category, form.name.data, form.text.data)
        db.session.add(image)
        db.session.flush()

        # Save image
        file = request.files['image']

        if file and allowed_file(file.filename):
            image.kind = ext(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], create_name(image.id, file.filename)))

            genthumbnail(image.id, file.filename)
        elif form.path and allowed_file(form.path.data):
            image.kind = ext(form.path.data)
            urllib.urlretrieve(form.path.data, os.path.join(app.config['UPLOAD_FOLDER'], create_name(image.id, form.path.data)))

            genthumbnail(image.id, form.path.data)
        else:
            db.session.rollback()
            flash('Obrazek nepostnut', 'error')

        db.session.commit()
        flash('Obrazek postnut', 'success')

        return redirect(url_for('category_one', name=name))

    return render('category_submit.html', title='test', form=form)


def category_edit(name):
    category = db.session.query(Category).filter_by(name=name).one()

    form = EditForm(request.form, category)

    if request.method == 'POST' and form.validate():
        category.text = form.text.data

        db.session.commit()
        flash('Kategorie editovana', 'success')

        return redirect(url_for('category_one', name=name))

    return render('category_edit.html', title='test', form=form, category=category)
