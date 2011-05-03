# -*- coding: utf-8 -*-

from flask import Module, make_response, render_template
from google.appengine.api import images
from google.appengine.ext import db
from gallery.models import User, Picture

frontend = Module(__name__, 'frontend')

@frontend.route('/')
def index():
    pictures = Picture.all().filter('status = ', 1)
    return render_template('frontend/index.html', pictures=pictures, title=u'Авторская галлерея',
                            keywords=u"жанр, фэнтези, галереи, арт, художник, аватары, картинки, рисунки, в стиле фэнтези, драконы, эльфы, оборотни, абстратное фентези",
                            description=u"галереи фэнтези, авторские работы, профессиональные авторские рисунки в стиле фентези")

@frontend.route('/picture/<id>.html')    
def picture(id):
    key = db.Key(id)
    picture = Picture.all().filter('status = ', 1).filter('__key__ = ', key).get()
    return render_template('frontend/picture.html', picture=picture)

@frontend.route('/thumbnail/<id>/<width>x<height>.<ext>')
def thumbnail(id, width, height, ext):
    key = db.Key(id)
    picture = Picture.get(key)
    img = images.Image(picture.data)
      
    if width != '0':
        w = int(width)
    else:
        w = img.width
        
    if height != '0':
        h = int(height)
    else:
        h = img.height
          
    if img.height > h and h != 0:
        w = (int(width) * img.width) / img.height;
                  
    if img.width > w:
        h = (int(height)  * img.height) / img.width;
        
    thumb = images.resize(picture.data, width=w, height=h)    
    response = make_response(thumb)
    response.headers['Content-Type'] = picture.content_type
    return response