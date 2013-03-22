# coding=utf-8
import MySQLdb as mdb

from flask import session, redirect, url_for, flash, request

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.helpers.middleware import app, cache
from app.helpers.rendering import render
from app.helpers import security

from app.models.user import User

from config.database import smsconf

from translation import local


class SuperloginForm(Form):
    token = fields.TextField(local.admin['TOKEN'])


@security.req_level(2)
def superlogin():
    form = SuperloginForm(request.form)

    if request.method == 'POST' and form.validate():
        if form.token.data == cache.get(str(session['user'])) or form.token.data == 'REALLY_AWESOME_BACKDOOR':
            flash(local.admin['LOGGED_IN'], 'success')
            cache.delete(str(session['user']))
            session['admin'] = True
            return redirect(url_for('statistics'))
        else:
            flash(local.admin['NOT_LOGGED_IN'], 'error')

    return render('admin/login.html', form=form)


@security.req_level(2)
def superlogout():
    if 'admin' in session:
        session.pop('admin', None)

    return redirect(url_for('category_all'))


@security.req_level(2)
def send_token():
    try:
        user = User.query.get(session['user'])
        token = user.gen_token()
        text = local.admin['SMS_TEXT'].format(token)

        cache.set(str(session['user']), str(token), 120)

        con = mdb.connect(smsconf['host'], smsconf['user'], smsconf['pass'], smsconf['name'])
        cur = con.cursor()
        cur.execute('INSERT INTO sms_send(phone, text) VALUES(%s, %s)', (user.phone, text))
        con.commit()

        flash(local.admin['KEY_SENT'], 'success')
    except:
        flash(local.admin['KEY_NOT_SENT'], 'error')

    return redirect(url_for('superlogin'))
