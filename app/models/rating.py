from datetime import datetime, timedelta
from math import log, sqrt

from flask import session, request

from app.helpers.middleware import db


class VotableObject(object):

    def vote(self, rating):
        try:
            rate = db.session.query(self.RatingClass).get((session['user'], self.id))
            if (rate.value + rating) > 1 or (rate.value + rating) < -1:
                change = 0
            else:
                change = rating
                rate.value += change
        except:
            rate = self.RatingClass(session['user'], self.id, rating)
            db.session.add(rate)
            change = rating

        if self.RatingClass.__tablename__ == 'comment':
            self.owner.rating_comment += change
        else:
            self.owner.rating_image += change

        self.rating += change
        time = datetime.now() if not self.ts else self.ts

        self.score = calculate_score(self.rating, time)


epoch = datetime(1970, 1, 1)

def _epoch_seconds(date):
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)

def calculate_score(rating, date):
    order = log(max(abs(rating), 1), 10)
    sign = 1 if rating > 0 else -1 if rating < 0 else 0
    seconds = _epoch_seconds(date) - 1134028003
    return round(order + sign * seconds / 45000, 7)
