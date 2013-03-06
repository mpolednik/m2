from flask import redirect, url_for, request, session, flash
import sqlalchemy.exc

from app.helpers.middleware import db
from app.helpers.rendering import render

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.user import User


class LoginForm(Form):
    mail = fields.TextField('Mail')
    password = fields.PasswordField('Pass')


class RegistrationForm(Form):
    name = fields.TextField('name')
    mail = fields.TextField('Mail')
    password = fields.PasswordField('Pass')


class EditForm(Form):
    name = fields.TextField('name')
    mail = fields.TextField('Mail')
    password = fields.PasswordField('pass')
    phone = fields.TextField('Phone')


def user(id):
    user = db.session.query(User).filter_by(id=id).one()
    return render('user.html', user=user)


def account():
    user = db.session.query(User).get(session['user'])

    form = EditForm(request.form, user)

    if request.method == 'POST' and form.validate():
        user.name = form.name.data
        user.mail = form.mail.data
        if form.password.data:
            user.password = form.password.data
        user.phone = form.phone.data

        try:
            db.session.commit()
            flash('User editovan', 'success')
        except sqlalchemy.exc.IntegrityError:
            flash('User needitovan', 'error')

    return render('account.html', form=form)


def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        User.login(form.mail.data, form.password.data)

        flash('User nalogovan', 'success')
        return redirect(url_for('category_all'))

    return render('login.html', form=form)


def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User(form.name.data, form.mail.data, form.password.data)
        db.session.add(user)

        try:
            db.session.commit()
            User.login(form.mail.data, form.password.data)
            flash('User registrovan a nalogovan', 'success')

            return redirect(url_for('category_all'))
        except:
            flash('neregistrovan', 'error')

    return render('register.html', form=form)


def logout():
    User.logout()

    flash('User odlogovan', 'success')
    return redirect(url_for('category_all'))
