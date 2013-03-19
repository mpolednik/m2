from flask import redirect, url_for

from app.helpers.middleware import db

from app.helpers.rendering import render

from app.models.image import Image

from app.controllers.image import image_delete

def admin_image(page=1):
    images = Image.query.paginate(page, 20)

    return render('admin/image.html', images=images)

def admin_image_delete(id, page):
    return image_delete(id=id, ref=url_for('admin_image', page=page))
