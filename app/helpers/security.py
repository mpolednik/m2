from flask import session

from app.helpers.middleware import app
from app.models.user import User
from app.models.category import Category
from app.models.request import Request

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

def req_level(level):
    def decorator(f):
        def inner(*args, **kwargs):
            user = User.query.get(session['user'])
            if user.level >= level:
                return f(*args, **kwargs)
            else:
                raise SecurityException
        return inner
    return decorator

def req_mod(f):
    @req_login
    def inner(*args, **kwargs):
        category = Category.query.filter_by(name=kwargs['name']).one()
        user = User.query.get(session['user'])
        if user.level > 1 or user in category.moderators:
            return f(*args, **kwargs)
        else:
            raise SecurityException
    return inner


def req_owner(Object):
    def decorator(f):
        @req_login
        def inner(*args, **kwargs):
            if 'cid' in kwargs:
                id = kwargs['cid']
            elif 'id' in kwargs:
                id = kwargs['id']

            obj = Object.query.filter_by(id=id).one()

            # Get parent object's moderators (assuming object is either comment or image)
            try:
                mod = obj.category.moderators
            except:
                mod = obj.image.category.moderators

            user = User.query.get(session['user'])
            if user.level > 1 or user == mod  or user == obj.owner:
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
            if user.level > 1 or user in request.category.moderators:
                return f(*args, **kwargs)
            else:
                raise SecurityException
        except:
            return f(*args, **kwargs)
    return inner
