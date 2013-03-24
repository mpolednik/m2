# coding=utf-8
import MySQLdb as mdb

from flask import session, redirect, url_for, flash, request, jsonify

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
            session.pop('id', None)
            return redirect(url_for('statistics'))
        else:
            flash(local.admin['NOT_LOGGED_IN'], 'error')

    return render('admin/login.html', title=local.admin['TITLE_LOGIN'], form=form)


@security.req_level(2)
def superlogout():
    if 'admin' in session:
        session.pop('admin', None)

    return redirect(url_for('category_all'))


@security.req_level(2)
def send_token():
    user = User.query.get(session['user'])
    if user.phone and len(user.phone) >= 9 and len(user.phone) <= 16:
        try:
            token = user.gen_token()
            text = local.admin['SMS_TEXT'].format(token)

            cache.set(str(session['user']), str(token), 120)

            con, cur = _mysqldb_connect()
            # Send sms and save its id to session
            cur.execute('INSERT INTO sms_send(phone, text) VALUES(%s, %s)', (user.phone, text))
            session['id'] = cur.lastrowid
            con.commit()

            flash(local.admin['KEY_SENT'], 'success')
        except:
            flash(local.admin['KEY_NOT_SENT'], 'error')
    else:
        flash(local.admin['PHONE_NOT_SET'], 'error')

    return redirect(url_for('superlogin'))


@security.req_level(2)
def get_sms_state():
    if 'id' in session:
        con, cur = _mysqldb_connect()

        # Fetch state of the sms
        cur.execute('SELECT state FROM sms_send WHERE id = %s', (session['id']))
        status = cur.fetchone()[0]

        states = (local.sms['STATE_UNPROCESSED'], local.sms['STATE_PROCESSED'], local.sms['STATE_SENT'], local.sms['STATE_ERROR'])

        try:
            state = states[status]
        except KeyError:
            state = local.sms['STATE_UNKNOWN']

        # Push it to client
        return jsonify(state=state)
    else:
        return jsonify(state=-1)


def _mysqldb_connect():
    con = mdb.connect(smsconf['host'], smsconf['user'], smsconf['pass'], smsconf['name'], smsconf['port'])
    cur = con.cursor()

    return (con, cur)
