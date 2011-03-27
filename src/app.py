# -*- coding: utf-8 -*-
'''
Created on 27.03.2011

@author: ded
'''

from flask import Flask, redirect, render_template, request, url_for, make_response
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
            if request.files['image']:
                print request.files['image'].name
                image.file = request.files['image'].read()
            image.put()
            return redirect(url_for("edit", id=image.key()))
        else:
            return render_template('edit.html', title=u'Добавить рисунок', form=form)
        

@app.route("/edit/<id>.html", methods=['GET', 'POST'])
def edit(id):
    image = Image.get(id) 
    form  = ImageForm(request.form, image)
    return render_template('edit.html', title=u'Редактировать рисунок', form=form)      

if __name__ == "__main__":
    run_wsgi_app(app)