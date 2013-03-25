import os
from flask import Flask, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.kvsession import KVSessionExtension
from simplekv.db.sql import SQLAlchemyStore
from flask.ext.lazyviews import LazyViews
from werkzeug.contrib.cache import MemcachedCache

from config.database import dbconf

# Flask + Jinja
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../views')
app = Flask('m2', template_folder=tmpl_dir)

# SQLAlchemy
app.config['DEBUG'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(dbconf['user'], dbconf['pass'], dbconf['host'], dbconf['name'])
db = SQLAlchemy(app)

# Bcrypt
bcrypt = Bcrypt(app)

# Lazyviews
views = LazyViews(app)

# Memcached
cache = MemcachedCache(['127.0.0.1:11211'])

# KVSession
app.config['SECRET_KEY'] = '1234'
store = SQLAlchemyStore(db.engine, db.metadata, 'session')
KVSessionExtension(store, app)
