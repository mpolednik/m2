from flask import request, session, flash, redirect, url_for

from app.helpers.middleware import db
from app.helpers.rendering import render
from app.helpers import security
from app.helpers.forms import flash_errors

from flask.ext.wtf import Form
from wtforms import fields, validators

from app.models.request import Request
from app.models.category import Category
from app.models.user import User

from translation import local


class RequestForm(Form):
    name = fields.TextField(local.NAME, [validators.Length(min=4, max=30, message=local.request['INVALID_NAME'])])
    text = fields.TextAreaField(local.TEXT, [validators.Length(max=1024, message=local.request['INVALID_TEXT'])])


@security.req_level(1)
def request_all():
    # Display every request visible to user (admin or moderator of categories)
    user = User.query.get(session['user'])
    if user.level > 1:
        requests = db.session.query(Request).all()
    else:
        keys = [cat.id for cat in user.categories]
        requests = db.session.query(Request).filter(Request.id_category.in_(keys))

    return render('admin/request_list.html', title=local.request['TITLE_LIST'], requests=requests)


@security.req_requested_category_mod
def request_one(id):
    request = db.session.query(Request).filter_by(id=id).one()

    return render('admin/request.html', title=local.request['TITLE_DETAILS'], request=request)


@security.req_login
def request_submit(name = None):
    form = RequestForm(request.form)

    if request.method == 'POST' and form.validate():
        if name:
            category = db.session.query(Category).filter_by(name=name).one()
            # Only allow single unaccepted request for moderator of category
            try: 
                test = Request.query.filter_by(type=1, id_user=session['user'], category=category, state=0).one()
            except:
                category = db.session.query(Category).filter_by(name=name).one()
                type = 1
            else:
                flash(local.request['MOD_REQUESTED'], 'error')
                return render('request_submit.html', title=local.request['TITLE_NEW'], form=form)
        else:
            category = None
            type = 0
        req = Request(session['user'], category, type, form.name.data, form.text.data)
        db.session.add(req)

        db.session.commit()
        flash(local.request['OK'], 'success')

        return redirect(url_for('category_all'))

    flash_errors(form)
    return render('request_submit.html', title=local.request['TITLE_NEW'], form=form)


@security.req_requested_category_mod
def request_accept(id):
    request = db.session.query(Request).get(id)
    user = User.query.get(request.owner.id)
    if request.state == 0:
        request.state = 1
    
        # Type: new category
        if request.type == 0:
            if user.level < 2:
                user.level = 1
            category = Category(request.name, request.text)
            category.moderators.append(request.owner)
            db.session.add(category)
        # Type: new moderator
        elif request.type == 1:
            if user.level < 2:
                user.level = 1
            category = db.session.query(Category).get(request.category.id)
            category.moderators.append(request.owner)

        db.session.commit()
        flash(local.request['ACCEPTED'], 'success')

    return redirect(url_for('request_all'))


@security.req_requested_category_mod
def request_decline(id):
    request = db.session.query(Request).get(id)
    if request.state == 0:
        request.state = -1
        db.session.commit()
        flash(local.request['DECLINED'], 'success')

    return redirect(url_for('request_all'))
