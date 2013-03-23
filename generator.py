# coding=utf-8
import random, string

from app.helpers.middleware import db

from app.models.user import User
from app.models.image import Image
from app.models.comment import Comment
from app.models.category import Category


def gen_user():
    name = ''.join(random.choice(string.ascii_lowercase + ' -_') for x in range(1, random.randint(4, 15)))
    mail = ''.join(random.choice(string.ascii_lowercase + ' -_') for x in range(1, random.randint(4, 15)))+'@'+'neco.com'
    password = '1234'

    return User(name, mail, password)


def vote_object(user, obj):
    chance = random.randint(1, 10)
    if chance > 3:
        vote = 1
    else:
        vote = -1

    obj.vote(vote, user.id)


def gen_comment(user, image, father=None):
    text = ''.join(random.choice(string.ascii_lowercase + ' -_') for x in range(1, random.randint(20, 200)))

    comment = Comment(user, image, text, father)
    db.session.add(comment)
    

genusers = False
imageactions = True
uploadimages =  False
commentactions = True

if genusers:
    # Generate users
    for i in range(1, 600):
        user = gen_user()
        db.session.add(user)
        db.session.commit()

if uploadimages:
    users = User.query.all()
    categories = Category.query.all()
    for user in users:
        chance = random.randint(1, 100)
        if chance > 95:
            try:
                # Add image
                name = ''.join(random.choice(string.ascii_lowercase + ' -_') for x in range(1, random.randint(4, 30)))
                text = ''.join(random.choice(string.ascii_lowercase + ' -_') for x in range(1, random.randint(20, 200)))
                filename = 'http://i.imgur.com/7ZVtcSs.jpg'
                image = Image(user.id, categories[random.randint(0, len(categories)-1)], name, text, filename, filename)
                db.session.add(image)
                db.session.flush()
                image.save()
                image.save_thumbnail()
                image.save_exif()
                image.vote(1, user.id)
                db.session.commit()
            except:
                pass


if imageactions:
    users = User.query.all()
    images = Image.query.all()
    i = 0

    for user in users:
        i += 1

        print 'User {} of {}'.format(i, len(users))
        j = 0

        for image in images:
            j += 1
            print 'Image {} of {}'.format(j, len(images))
            chance = random.randint(1, 100)
            if chance > 70:
                # Cast vote on 30%
                vote_object(user, image)
                print 'Voted {}'.format(image.id)
            #if chance > 99:
                # Comment uncommented (10% of all)
                #if not user.already_commented(image):
                #    gen_comment(user.id, image)

    print 'Comitting'
    db.session.commit()

if commentactions:
    users = User.query.all()

    i = 0
    for user in users:
        i += 1
        print 'User {} of {}'.format(i, len(users))

        comments = Comment.query.all()
        j = 0
        for comment in comments:
            j += 1
            print 'Comment {} of {}'.format(j, len(comments))
            chance = random.randint(1, 100)
            if chance > 70:
                # Cast vote on 30%
                vote_object(user, comment)
                print 'Voted {}'.format(comment.id)
            if chance > 99:
                gen_comment(user.id, comment.image, comment.id)
                print 'Commented {}'.format(comment.id)

        print 'Comitting'
        db.session.commit()

    print 'Comitting'
    db.session.commit()
