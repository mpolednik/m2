from flask import redirect, url_for, request

from app.helpers.middleware import db
from app.helpers.rendering import render
from app.helpers import security

from app.models.image import Image

from app.controllers.image import image_delete

from translation import local


@security.req_admin
def admin_image(page=1):
    if 'q' in request.args:
        q = request.args.get('q')
        images = Image.query.filter(Image.name.like('%{}%'.format(q))).paginate(page, 20)
    else:
        images = Image.query.paginate(page, 20)

    return render('admin/image.html', title=local.image['TITLE_ADMIN_LIST'], images=images)


@security.req_admin
def admin_image_delete(id, page):
    return image_delete(id=id, ref=url_for('admin_image', page=page))
