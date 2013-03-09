from app.helpers.middleware import app

app.config['UPLOAD_FOLDER'] = 'static/img/upload'
app.config['THUMB_UPLOAD_FOLDER'] = 'static/img/thumb'
app.config['ALLOWED_EXTENSIONS'] = ('jpg', 'jpeg', 'png')
app.config['THUMBNAIL_SIZE'] = (256, 256)
