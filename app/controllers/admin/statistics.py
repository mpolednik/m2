# vim: set fileencoding=utf-8 :
import os, psutil, time, collections, datetime

from app.helpers.middleware import db, cache
from app.helpers.rendering import render

from app.models.category import Category
from app.models.user import User
from app.models.image import Image
from app.models.request import Request
from app.models.comment import Comment

from translation import local

def timeformat(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)

def statistics():
    stats = cache.get('statistics')
    if not stats:
        uptime = timeformat(time.time() - psutil.Process(os.getpid()).create_time)
        sys = os.uname()
        categories = Category.query.count() 
        users = User.query.count() 
        images = Image.query.count() 
        requests = Request.query.count() 
        comments = Comment.query.count() 

        stats = collections.OrderedDict((
            (local.statistics['GENERATED'], datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            (u'Uptime', uptime),
            (u'Operační systém', '<br>'.join(sys)),
            (u'Počet kategorií', categories),
            (u'Počet uživatelů', users),
            (u'Počet obrázků', images),
            (u'Počet požadavků', requests),
            (u'Počet komentářů', comments),
        ))

        cache.set('statistics', stats, 300) # 5 min cache

    return render('admin/statistics.html', stats=stats)
