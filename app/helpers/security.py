from werkzeug.exceptions import HTTPException
from flask import session, redirect, url_for

from app.helpers.middleware import app
from app.models.user import User
from app.models.category import Category
from app.models.request import Request

class SecurityException(Exception):
    code = 1000

    def __str__(self):
        return repr(self.code)


def req_login(f):
    def inner(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            raise SecurityException
    return inner


def req_nologin(f):
    def inner(*args, **kwargs):
        if 'user' not in session:
            return f(*args, **kwargs)
        else:
            raise SecurityException
    return inner


def req_admin(f):
    def inner(*args, **kwargs):
        if 'admin' in session and session['admin']:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('superlogin'))
    return inner


def req_level(level):
    def decorator(f):
        @req_login
        def inner(*args, **kwargs):
            user = User.query.get(session['user'])
            if user.level >= level:
                return f(*args, **kwargs)
            else:
                raise SecurityException
        return inner
    return decorator


def req_mod(Object=None):
    def decorator(f):
        @req_login
        def inner(*args, **kwargs):
            category = Category.query.filter_by(name=kwargs['name']).one()
            user = User.query.get(session['user'])

            if 'admin' in session or user in category.moderators:
                return f(*args, **kwargs)
            else:
                raise SecurityException
        return inner
    return decorator


def req_owner(Object):
    def decorator(f):
        @req_login
        def inner(*args, **kwargs):
            if 'cid' in kwargs:
                id = kwargs['cid']
            elif 'id' in kwargs:
                id = kwargs['id']

            user = User.query.get(session['user'])
            obj = Object.query.get(id)

            # Try ownership and adminship...
            if user == obj.owner or 'admin' in session:
                return f(*args, **kwargs)
            else:
                raise SecurityException
        return inner
    return decorator


def req_requested_category_mod(f):
    def inner(*args, **kwargs):
        try:
            request = Request.query.get(kwargs['id'])
            user = User.query.get(session['user'])
            if 'admin' in session or user in request.category.moderators:
                return f(*args, **kwargs)
            else:
                raise SecurityException
        except:
            return f(*args, **kwargs)
    return inner
