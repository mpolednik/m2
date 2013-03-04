from flask import request, session, flash, redirect, url_for

from app.helpers.middleware import db
from app.helpers.bootstrap import current_user
from app.helpers.rendering import render

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.request import Request

class RequestForm(Form):
    name = fields.TextField('Jmeno')
    text = fields.TextAreaField('Text')
    type = fields.SelectField('Typ', choices=[('0', 'Category'), ('1', 'Moderator')])

def request_all():
    requests = db.session.query(Request).all()

    return render('request_list.html', requests=requests)

def request_one(id):
    request = db.session.query(Request).filter_by(id=id).one()

    return render('request.html', request=request)

def request_submit(category = None):
    form = RequestForm()

    if request.method == 'POST' and form.validate():
        req = Request(current_user, None, form.type.data, form.name.data, form.text.data)
        db.session.add(req)
        db.session.commit()
        flash('request odeslan')
        return redirect('/')

    return render('request_form.html', form=form)
    return 'In progress...'

def request_accept(request):
    pass
