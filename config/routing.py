from app.helpers.middleware import views

views.add('/', 'app.controllers.category.category_all')
views.add('/c/<name>', 'app.controllers.category.category_one')
views.add('/i/<id>', 'app.controllers.image.image')
views.add('/u/<id>', 'app.controllers.user.user')
views.add('/r', 'app.controllers.request.request_all')
views.add('/r/new', 'app.controllers.request.request_new')
views.add('/r/<id>', 'app.controllers.request.request_one')
