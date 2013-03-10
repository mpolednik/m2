from flask import request, session, flash, redirect, url_for

from app.helpers.middleware import db
from app.helpers.rendering import render
from app.helpers import security

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.request import Request
from app.models.category import Category


class RequestForm(Form):
    name = fields.TextField('Jmeno')
    text = fields.TextAreaField('Text')


def request_all():
    requests = db.session.query(Request).all()

    return render('request_list.html', requests=requests)


def request_one(id):
    request = db.session.query(Request).filter_by(id=id).one()

    return render('request.html', request=request)


def request_submit(name = None):
    form = RequestForm()

    if request.method == 'POST' and form.validate():
        if name:
            category = db.session.query(Category).filter_by(name=name).one()
            type = 1
        else:
            category = None
            type = 0
        req = Request(session['user'], category, type, form.name.data, form.text.data)
        db.session.add(req)

        db.session.commit()
        flash('request odeslan', 'success')

        return redirect(url_for('category_all'))

    return render('request_form.html', form=form)
    return 'In progress...'


def request_accept(id):
    request = db.session.query(Request).get(id)
    if request.state == 0:
        request.state = 1
    
        # Type: new category
        if request.type == 0:
            category = Category(request.name)
        # Type: new moderator
        elif request.type == 1:
            category = db.session.query(Category).get(request.category.id)
            category.moderators.append(request.owner)

        db.session.commit()
        flash('Request schvalen', 'success')

    return redirect(url_for('request_all'))


def request_decline(id):
    request = db.session.query(Request).get(id)
    if request.state == 0:
        request.state = -1
        db.session.commit()
        flash('Request neschvalen', 'success')

    return redirect(url_for('request_all'))
