from flask import session

from app.helpers.middleware import app
from app.models.user import User
from app.models.category import Category

class SecurityException(Exception):
    pass

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

def req_level(f, level):
    def inner(*args, **kwargs):
        user = User.query.get(session['user'])
        if user.level > level:
            return f(*args, **kwargs)
        else:
            raise SecurityException
    return inner

def req_mod(f):
    @req_login
    def inner(*args, **kwargs):
        category = Category.query.filter_by(name=kwargs['name']).one()
        user = User.query.get(session['user'])
        if user in category.moderators or user.level > 1:
            return f(*args, **kwargs)
        else:
            raise SecurityException
    return inner
