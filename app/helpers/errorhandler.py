# coding=utf-8
from app.helpers.middleware import app
from app.helpers.rendering import render


@app.errorhandler(404)
def page_error(error):
    return render('errors/404.html')

@app.errorhandler(500)
def page_error(error):
    return render('errors/500.html', error=error)
