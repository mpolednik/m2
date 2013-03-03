from app.helpers.middleware import db
from app.helpers.rendering import render

from app.models.image import Image

def image(id):
    image = db.session.query(Image).filter_by(id=id).one()

    return render('image.html', image=image)

def image_add():
    pass

def image_edit():
    pass

def image_del():
    pass

def image_vote():
    pass
