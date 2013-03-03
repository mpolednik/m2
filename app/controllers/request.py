from app.helpers.middleware import db
from app.helpers.rendering import render

from app.models.request import Request

def request_all():
    requests = db.session.query(Request).all()

    return render('request_list.html', requests=requests)

def request_one(id):
    request = db.session.query(Request).filter_by(id=id).one()

    return render('request.html', request=request)

def request_new():
    return 'In progress...'
