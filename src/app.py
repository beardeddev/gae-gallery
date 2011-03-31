# -*- coding: utf-8 -*-
'''
Created on 27.03.2011

@author: ded
'''

from flask import Flask, redirect, render_template, request, url_for, make_response, send_file
from google.appengine.ext.webapp.util import run_wsgi_app
from models import *
from forms import *
from google.appengine.api import images

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    pictures = Picture.all()
    return render_template('index.html', pictures=pictures, title='My Page')

@app.route("/edit.html", methods=['GET', 'POST'])
def create():
    picture = Picture()
    
    if request.method == 'GET':
        form = PictureForm()  
        return render_template('edit.html', title=u'Добавить рисунок', form=form, picture=picture)
    
    if request.method == 'POST':                
        form = PictureForm(request.form, picture)
        if form.validate() and request.files['file']:
            form.populate_obj(picture)
            picture.data = request.files['file'].read()
            picture.ext = request.files['file'].filename.rsplit('.', 1)[1]
            picture.content_type = request.files['file'].content_type
            picture.put()
            return redirect(url_for("edit", id=picture.key()))
        else:
            return render_template('edit.html', title=u'Добавить рисунок', form=form, picture=picture)
        

@app.route("/edit/<id>.html", methods=['GET', 'POST'])
def edit(id):
    picture = Picture.get(id)
    form  = PictureForm(request.form, picture)
    return render_template('edit.html', title=u'Редактировать рисунок', form=form, picture=picture)

@app.route("/<id>.html")
def image(id):
    picture = Picture.get(id)
    return render_template('show.html', picture=picture)      

@app.route('/thumb/<id>/<width>x<height>.<ext>')
def thumb(id, width, height, ext):
    picture = Picture.get(id)
    img = images.Image(picture.data)  
    w = int(width)
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

if __name__ == "__main__":
    run_wsgi_app(app)