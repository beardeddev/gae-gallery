# -*- coding: utf-8 -*-
'''
Created on 27.03.2011

@author: ded
'''

from flask import Flask, redirect, render_template, request, url_for
from google.appengine.ext.webapp.util import run_wsgi_app
from models import *
from forms import *
from wtforms.ext.appengine.db import model_form

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return render_template('index.html', hello="Hello World!", title='My Page')

@app.route("/images/edit.html", methods=['GET', 'POST'])
def create_image():
    if request.method == 'GET':
        form = ImageForm()  
        return render_template('edit_image.html', title=u'Добавить рисунок', form=form)
    
    if request.method == 'POST':
        image = Image()        
        form = ImageForm(request.form, image)
        if form.validate():            
            file = request.files['file']
            if file:
                content = file.stream
            form.populate_obj(image)
            image.file = content.stream.read()
            image.put()
            return redirect(url_for("edit_image", id=image.key()))
        else:
            return render_template('edit_image.html', title=u'Добавить рисунок', form=form)
        

@app.route("/images/edit/<id>.html", methods=['GET', 'POST'])
def edit_image(id):
    image = Image.get(id) 
    form  = ImageForm(request.form, image)
    return render_template('edit_image.html', title=u'Редактировать рисунок', form=form)      

if __name__ == "__main__":
    run_wsgi_app(app)