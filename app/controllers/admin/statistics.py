# vim: set fileencoding=utf-8 :
import os, psutil, time, collections, datetime

from app.helpers.middleware import db, cache, app
from app.helpers.rendering import render
from app.helpers import security

from app.models.category import Category
from app.models.user import User
from app.models.image import Image, ImageRating
from app.models.request import Request
from app.models.comment import Comment, CommentRating

from translation import local


def _timeformat(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)


def _vp(part, whole):
  return '{} ({} %)'.format(part, int(100 * float(part)/float(whole)))


def _avg(a, b):
    return int(a / b)


@security.req_admin
def statistics():
    stats = cache.get('statistics')
    if not stats:
        uptime = _timeformat(time.time() - psutil.Process(os.getpid()).create_time)
        sys = os.uname()
        categories = Category.query.count() 
        users = User.query.count() 
        moderators = User.query.filter_by(level=1).count() 
        admins = User.query.filter_by(level=2).count() 
        images = Image.query.count() 
        requests = Request.query.count() 
        requests_non = Request.query.filter_by(state=0).count() 
        requests_acc = Request.query.filter_by(state=1).count() 
        requests_dec = requests - (requests_non + requests_acc)
        comments = Comment.query.count() 
        comments_del = Comment.query.filter_by(state=0).count() 
        comments_act = comments - comments_del
        image_ratings = ImageRating.query.count()
        image_ratings_pos = ImageRating.query.filter_by(value=1).count()
        image_ratings_neu = ImageRating.query.filter_by(value=0).count()
        image_ratings_neg = ImageRating.query.filter_by(value=-1).count()
        comment_ratings = CommentRating.query.count()
        comment_ratings_pos = CommentRating.query.filter_by(value=1).count()
        comment_ratings_neu = CommentRating.query.filter_by(value=0).count()
        comment_ratings_neg = CommentRating.query.filter_by(value=-1).count()

        stats = collections.OrderedDict((
            (local.statistics['GENERATED'], datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            (local.statistics['UPTIME'], uptime),
            (local.statistics['DEBUG'], app.config['DEBUG']),
            (local.statistics['OS'], '<br>'.join(sys)),
            (local.statistics['UPLOAD_FOLDER'], app.config['UPLOAD_FOLDER']),
            (local.statistics['THUMB_UPLOAD_FOLDER'], app.config['THUMB_UPLOAD_FOLDER']),
            (local.statistics['THUMBNAIL_SIZE'], 'W: {}px H: {}px'.format(app.config['THUMBNAIL_SIZE'][0], app.config['THUMBNAIL_SIZE'][1])),
            (local.statistics['NUM_CATEGORIES'], categories),
            (local.statistics['NUM_USERS'], users),
            (local.statistics['NUM_USERS_ADMIN'], _vp(admins, users)),
            (local.statistics['NUM_USERS_MOD'], _vp(moderators, users)),
            (local.statistics['NUM_REQUESTS'], requests),
            (local.statistics['NUM_REQUESTS_ACCEPTED'], _vp(requests_acc, requests)),
            (local.statistics['NUM_REQUESTS_DECLINED'], _vp(requests_dec, requests)),
            (local.statistics['NUM_REQUESTS_NOACTION'], _vp(requests_non, requests)),
            (local.statistics['NUM_IMAGES'], images),
            (local.statistics['NUM_RATING_IMAGES'], image_ratings),
            (local.statistics['IMAGE_RATING_POSITIVE'], _vp(image_ratings_pos, image_ratings)),
            (local.statistics['IMAGE_RATING_NEGATIVE'], _vp(image_ratings_neg, image_ratings)),
            (local.statistics['IMAGE_RATING_NEUTRAL'], _vp(image_ratings_neu, image_ratings)),
            (local.statistics['NUM_COMMENTS'], comments),
            (local.statistics['NUM_COMMENTS_ACTIVE'], _vp(comments_act, comments)),
            (local.statistics['NUM_COMMENTS_DELETED'], _vp(comments_del, comments)),
            (local.statistics['NUM_RATING_COMMENTS'], comment_ratings),
            (local.statistics['COMMENT_RATING_POSITIVE'], _vp(comment_ratings_pos, comment_ratings)),
            (local.statistics['COMMENT_RATING_NEGATIVE'], _vp(comment_ratings_neg, comment_ratings)),
            (local.statistics['COMMENT_RATING_NEUTRAL'], _vp(comment_ratings_neu, comment_ratings)),
            (local.statistics['AVG_CATEGORY_IMAGE'], _avg(images, categories)),
            (local.statistics['AVG_COMMENT_IMAGE'], _avg(comments, images)),
            (local.statistics['AVG_RATING_IMAGE'], _avg(image_ratings, images)),
            (local.statistics['AVG_RATING_COMMENT'], _avg(comment_ratings, comments)),
        ))

        cache.set('statistics', stats, 300) # 5 min cache

    return render('admin/statistics.html', title=local.statistics['TITLE'], stats=stats)
