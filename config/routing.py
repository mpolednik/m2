from app.helpers.middleware import views, app
from app.helpers.rendering import render

views.add('/', 'app.controllers.category.category_all')
views.add('/<int:page>', 'app.controllers.category.category_all')
views.add('/c/<name>', 'app.controllers.category.category_one')
views.add('/c/<name>/<int:page>', 'app.controllers.category.category_one')

views.add('/c/<name>/submit', 'app.controllers.category.category_submit', methods=('GET', 'POST'))
views.add('/c/<name>/edit', 'app.controllers.category.category_edit', methods=('GET', 'POST'))
views.add('/c/<name>/i/<int:id>/vote/<int:page>', 'app.controllers.image.image_vote')

views.add('/i/<int:id>', 'app.controllers.image.image')
views.add('/i/<int:id>/edit', 'app.controllers.image.image_edit', methods=('GET', 'POST'))
views.add('/i/<int:id>/delete', 'app.controllers.image.image_delete')
views.add('/i/<int:id>/vote', 'app.controllers.image.image_vote')
views.add('/i/<int:id>/submit', 'app.controllers.comment.comment', methods=('GET', 'POST'))

views.add('/i/<int:id>/c/<int:cid>', 'app.controllers.comment.comment', methods=('GET', 'POST'))
views.add('/i/<int:id>/c/<int:cid>/edit', 'app.controllers.comment.comment_edit', methods=('GET', 'POST'))
views.add('/i/<int:id>/c/<int:cid>/delete', 'app.controllers.comment.comment_delete')
views.add('/i/<int:id>/c/<int:cid>/vote', 'app.controllers.comment.comment_vote')

views.add('/r', 'app.controllers.request.request_all')
views.add('/r/submit', 'app.controllers.request.request_submit', methods=('GET', 'POST'))
views.add('/r/<int:id>', 'app.controllers.request.request_one')
views.add('/r/<int:id>/accept', 'app.controllers.request.request_accept')
views.add('/r/<int:id>/decline', 'app.controllers.request.request_decline')

views.add('/u/<int:id>', 'app.controllers.user.user')
views.add('/login', 'app.controllers.user.login', methods=('GET', 'POST'))
views.add('/register', 'app.controllers.user.register', methods=('GET', 'POST'))
views.add('/account', 'app.controllers.user.account', methods=('GET', 'POST'))
views.add('/logout', 'app.controllers.user.logout')

@app.errorhandler(404)
def page_error(error):
    return render('errors/404.html')

@app.errorhandler(500)
def page_error(error):
    return render('errors/500.html', error=error)
