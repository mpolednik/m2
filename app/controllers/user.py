from flask import redirect, url_for, request, session, flash
import sqlalchemy.exc

from app.helpers.middleware import db
from app.helpers.rendering import render
from app.helpers import security
from app.helpers.forms import flash_errors

from flask.ext.wtf import Form
from wtforms import fields, validators, ValidationError

from app.models.user import User
from app.models.image import Image

from translation import local


class LoginForm(Form):
    mail = fields.TextField(local.MAIL, [validators.Email(local.user['INVALID_MAIL'])])
    password = fields.PasswordField(local.PASS, [validators.Length(min=4, message=local.user['INVALID_PASS'])])

    def validate_name(form, field):
        if form.data['name'] != field.data:
            try:
                User.query.filter_by(name=field.data).one()
            except:
                pass
            else:
                raise ValidationError(local.user['EXISTS_NAME'])

    def validate_mail(form, field):
        if form.data['mail'] != field.data:
            try:
                User.query.filter_by(mail=field.data).one()
            except:
                pass
            else:
                raise ValidationError(local.user['EXISTS_MAIL'])


class RegistrationForm(LoginForm):
    name = fields.TextField(local.UNAME, [validators.Length(4, 50, local.user['INVALID_NAME'])])

class EditForm(RegistrationForm):
    phone = fields.TextField(local.PHONE)
    password = fields.PasswordField(local.PASS, [validators.Optional(), validators.Length(min=4, message=local.user['INVALID_PASS'])])


def user(id, page=1):
    user = db.session.query(User).filter_by(id=id).one()
    images = Image.query.filter_by(id_user=user.id).order_by(Image.score.desc(), Image.ts.desc()).paginate(page, 20)
    return render('user.html', user=user, images=images)


@security.req_login
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
            flash(local.user['EDITTED'], 'success')
        except sqlalchemy.exc.IntegrityError:
            flash(local.user['NOT_EDITTED'], 'error')

    flash_errors(form)
    return render('account.html', form=form)


@security.req_nologin
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        try:
            User.login(form.mail.data, form.password.data)
            flash(local.user['LOGIN'], 'success')
            return redirect(url_for('category_all'))
        except:
            flash(local.user['NOT_LOGIN'], 'error')

    return render('login.html', form=form)


@security.req_nologin
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User(form.name.data, form.mail.data, form.password.data)
        db.session.add(user)

        try:
            db.session.commit()
            User.login(form.mail.data, form.password.data)
            flash(local.user['REGISTERED'], 'success')

            return redirect(url_for('category_all'))
        except:
            flash(local.user['NOT_REGISTERED'], 'error')

    flash_errors(form)
    return render('register.html', form=form)


@security.req_login
def logout():
    User.logout()

    flash(local.user['LOGOUT'], 'success')
    return redirect(url_for('category_all'))
