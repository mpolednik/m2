
from flask import redirect, url_for, request, session, flash

from app.helpers.middleware import db, app
from app.helpers.rendering import render

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.image import Image
from app.models.category import Category


class SubmitForm(Form):
    name = fields.TextField('Jmeno')
    text = fields.TextAreaField('Text')
    link = fields.TextAreaField('link')
    image = fields.FileField('Image')


class EditForm(Form):
    text = fields.TextAreaField('Text')


def category_all(page = 1):
    images = Image.query.order_by(Image.score.desc(), Image.ts.desc()).paginate(page, 20)

    return render('category.html', title='test', images=images)


def category_one(name, page = 1):
    category = Category.query.filter_by(name=name).one()
    images = Image.query.filter_by(id_category=category.id).order_by(Image.score.desc(), Image.ts.desc()).paginate(page, 20)

    return render('category.html', title='test', category=category, images=images)


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
            flash('Spatny format obrazku', 'error')
            return redirect(url_for('category_submit', name=name))

        image.save_thumbnail()
        image.save_exif()
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
