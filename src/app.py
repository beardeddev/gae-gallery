# -*- coding: utf-8 -*-
'''
Created on 27.03.2011

@author: ded
'''

from flask import Flask, redirect, render_template, request, url_for, make_response, send_file
from google.appengine.ext.webapp.util import run_wsgi_app
from models import *
from forms import *

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    images = Image.all()
    return render_template('index.html', images = images, title='My Page')

@app.route("/edit.html", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        form = ImageForm()  
        return render_template('edit.html', title=u'Добавить рисунок', form=form)
    
    if request.method == 'POST':
        image = Image()        
        form = ImageForm(request.form, image)
        if form.validate() and request.files['image']:
            form.populate_obj(image)
            image.file = request.files['image'].read()
            image.content_type = request.files['image'].content_type
            image.put()
            return redirect(url_for("edit", id=image.key()))
        else:
            return render_template('edit.html', title=u'Добавить рисунок', form=form)
        

@app.route("/edit/<id>.html", methods=['GET', 'POST'])
def edit(id):
    image = Image.get(id) 
    form  = ImageForm(request.form, image)
    return render_template('edit.html', title=u'Редактировать рисунок', form=form)      

@app.route('/thumb/<id>.html')
def thumb(id):
    image = Image.get(id)
    response = make_response(image.file)
    response.headers['Content-Type'] = image.content_type
    return response

if __name__ == "__main__":
    run_wsgi_app(app)