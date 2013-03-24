# coding=utf-8
from flask import redirect, url_for, request, session, flash

from app.helpers.middleware import db, app, cache
from app.helpers.rendering import render
from app.helpers import security
from app.helpers.forms import flash_errors

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.image import Image
from app.models.category import Category
from app.models.user import User

from translation import local


class CreateForm(Form):
    name = fields.TextField(local.NAME, [validators.Length(min=2, max=30, message=local.category['INVALID_NAME'])])
    text = fields.TextAreaField(local.TEXT, [validators.Length(max=1024, message=local.category['INVALID_TEXT'])])


class EditForm(Form):
    text = fields.TextAreaField(local.TEXT, [validators.Length(max=1024, message=local.category_submit['INVALID_TEXT'])])


class SubmitForm(EditForm):
    name = fields.TextField(local.NAME, [validators.Length(min=2, max=50, message=local.category_submit['INVALID_NAME'])])
    link = fields.TextField(local.LINK, [validators.Optional(), validators.Length(max=200, message=local.category_submit['INVALID_LINK'])])
    image = fields.FileField(local.FILE, [validators.Optional()])


def category_all(page=1):
    images = Image.query.order_by(Image.score.desc(), Image.ts.desc()).paginate(page, 20)

    return render('category.html', title=local.category['TITLE_ALL'], images=images)


def category_one(name, page=1):
    category = Category.query.filter_by(name=name).one()
    images = Image.query.filter_by(id_category=category.id).order_by(Image.score.desc(), Image.ts.desc()).paginate(page, 20)

    return render('category.html', title=category.name, category=category, images=images)


@security.req_login
def category_submit(name):
    form = SubmitForm(request.form)

    category = db.session.query(Category).filter_by(name=name).one()

    if request.method == 'POST' and form.validate():
        file = request.files['image']
        if not file:
            filename = form.link.data
        else:
            filename = file.filename

        image = Image(session['user'], category, form.name.data, form.text.data, form.link.data, filename)
        db.session.add(image)
        db.session.flush()

        if file and image.allowed:
            image.save(file)
        elif image.allowed:
            image.save()
        else:
            db.session.rollback()
            flash(local.category_submit['INVALID_IMAGE'], 'error')
            return render('category_submit.html', title=local.category['TITLE_SUBMIT'], category=category, form=form)

        image.save_thumbnail()
        image.save_exif()
        # Self upvote 
        image.vote(1, session['user'])
        db.session.commit()
        flash(local.category_submit['IMAGE_POSTED'], 'success')

        return redirect(url_for('category_one', name=name))

    flash_errors(form)
    return render('category_submit.html', title=local.category['TITLE_SUBMIT'], category=category, form=form)


@security.req_mod
def category_edit(name):
    category = db.session.query(Category).filter_by(name=name).one()

    form = EditForm(request.form, category)

    if request.method == 'POST' and form.validate():
        category.text = form.text.data

        db.session.commit()
        flash(local.category['EDITTED'], 'success')

        return redirect(url_for('category_one', name=name))

    flash_errors(form)
    return render('category_edit.html', title=local.category['TITLE_EDIT'], form=form, category=category)


@security.req_mod
def category_pass_mod(name):
    category = db.session.query(Category).filter_by(name=name).one()
    user = User.query.get(session['user'])
    category.moderators.remove(user)
    if len(user.categories) < 2 and user.level < 2:
        user.level = 0
    db.session.commit()
    return redirect(url_for('category_one', name=name))


@security.req_admin
def category_become_mod(name):
    category = db.session.query(Category).filter_by(name=name).one()
    user = User.query.get(session['user'])
    category.moderators.append(user)
    db.session.commit()
    return redirect(url_for('category_one', name=name))


@security.req_admin
def category_create():
    form = CreateForm(request.form)

    if request.method == 'POST' and form.validate():
        category = Category(form.name.data, form.text.data)
        db.session.add(category)
        db.session.commit()
        cache.delete('categories')
        flash(local.category['CREATED'], 'success')

        return redirect(url_for('category_all'))

    flash_errors(form)
    return render('category_create.html', title=local.category['TITLE_NEW'], form=form)
