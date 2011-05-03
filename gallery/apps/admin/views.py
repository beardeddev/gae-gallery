# -*- coding: utf-8 -*-

from flask import Module, render_template, redirect, request, url_for, flash
from gallery.models import User, Picture, Page
from gallery.forms import UserForm, PictureForm, PageForm
from google.appengine.ext import db
import os, hashlib

admin = Module(__name__, 'admin')

@admin.route('/')
def index():
    return render_template('admin/index.html', title=u'Управление сайтом')

@admin.route('/users/')
def users():
    users = User.all()
    return render_template('admin/users/index.html', title=u'Пользователи', users=users)

@admin.route('/users/new/')
def new_user():
    form = UserForm()
    return render_template('admin/users/new.html', title=u'Добавить пользователя', form=form)

@admin.route('/users/create/', methods=['POST'])
def create_user():    
    user = User()    
    form = UserForm(request.form, user)
    form.key.data = None
    if form.validate():
        form.populate_obj(user)
        user.password_salt = str(hashlib.md5(os.urandom(124)))
        user.password_hash = str(hashlib.md5(form.password.data + user.password_salt).hexdigest())
        user.put()
        flash('Пользователь успешно сохранен', 'correct')
        return redirect(url_for('edit_user', id=user.key()))
    else:
        return render_template('admin/users/new.html', title=u'Добавить пользователя', form=form)
    
@admin.route('/users/edit/<id>/')
def edit_user(id):
    key = db.Key(id)
    user = User.get(key)
    form = UserForm(request.form, user)
    form.key.data = key    
    return render_template('admin/users/edit.html', title=u'Редактировать пользователя', form=form, user=user)

@admin.route('/users/update/<id>/', methods=['POST'])
def update_user(id):
    key = db.Key(id)
    user = User.get(key)
    form = UserForm(request.form, user)
    form.key.data = key
    if form.validate():
        form.populdate_obj(user)
        user.put()
        flash('Пользователь успешно сохранен', 'correct')
        redirect(url_for('edit_user', id=user.key()))
    else:
        return render_template('admin/users/edit.html', title=u'Редактировать пользователя', form=form, user=user)
    
@admin.route('/users/delete/<id>/')
def delete_user(id):
    key = db.Key(id)
    db.delete(key)
    flash('Пользователь успешно удален', 'correct')
    return redirect(url_for('users'))

@admin.route('/users/destroy/', methods=['POST'])
def destroy_users():
    pass

@admin.route('/pictures/')
def pictures():
    pictures = Picture.all()
    return render_template('admin/pictures/index.html', pictures=pictures, title=u'Рисунки')

@admin.route('/pictures/new/')
def new_picture():
        form = PictureForm()  
        return render_template('admin/pictures/new.html', title=u'Добавить рисунок', form=form)

@admin.route('/pictures/create/', methods=['POST'])
def create_picture():
    picture = Picture()
    form = PictureForm(request.form, picture)
    if form.validate() and request.files['file']:            
        form.populate_obj(picture)            
        picture.data = request.files['file'].read()
        picture.ext = request.files['file'].filename.rsplit('.', 1)[1]
        picture.content_type = request.files['file'].content_type
        picture.put()
        flash(u'Рисунок успешно добавлен', 'correct')
        return redirect(url_for("edit_picture", id=picture.key()))
    else:
        return render_template('admin/pictures/new.html', title=u'Добавить рисунок', form=form)
    
@admin.route('/pictures/edit/<id>/')
def edit_picture(id):
    key = db.Key(id)
    picture = Picture.get(key)
    form  = PictureForm(request.form, picture)     
    return render_template('admin/pictures/edit.html', title=u'Редактировать рисунок', form=form, picture=picture)

@admin.route('/pictures/update/<id>/', methods=['POST'])
def update_picture(id):
    key = db.Key(id)
    picture = Picture.get(key)
    form  = PictureForm(request.form, picture)
    if form.validate():
        form.populate_obj(picture)
        if request.files['file']:
            picture.data = request.files['file'].read()
            picture.ext = request.files['file'].filename.rsplit('.', 1)[1]
            picture.content_type = request.files['file'].content_type                
        picture.put()
        flash(u'Рисунок успешно сохранен', 'correct')
        return redirect(url_for("edit_picture", id=picture.key()))
    else:
        return render_template('admin/pictures/edit.html', title=u'Редактировать рисунок', form=form, picture=picture)

@admin.route('/pictures/delete/<id>/')
def delete_picture(id):
    key = db.Key(id)
    db.delete(key)
    flash(u'Рисунок успешно удален', 'correct')
    return redirect(url_for('pictures'))

@admin.route('/pictures/destroy/', methods=['POST'])
def destroy_pictures():
    pass

@admin.route('/pages/')
def pages():
    pages = Page.all()
    return render_template('admin/pages/index.html', title=u'Страницы', pages=pages)

@admin.route('/pages/new/')
def new_page():
        form = PageForm()  
        return render_template('admin/pages/new.html', title=u'Добавить рисунок', form=form)

@admin.route('/pages/create/', methods=['POST'])
def create_page():
    page = Page()
    form = PageForm(request.form, page)
    if form.validate():             
        form.populate_obj(page)
        page.put()
        flash(u'Страница успешно добавлен', 'correct')
        return redirect(url_for("edit_page", id=page.key()))
    else:
        return render_template('admin/pages/new.html', title=u'Добавить рисунок', form=form)
    
@admin.route('/pages/edit/<id>/')
def edit_page(id):
    key = db.Key(id)
    page = Page.get(key)
    form  = PageForm(request.form, page)     
    return render_template('admin/pages/edit.html', title=u'Редактировать рисунок', form=form, page=page)

@admin.route('/pages/update/<id>/', methods=['POST'])
def update_page(id):
    key = db.Key(id)
    page = Page.get(key)
    form  = PageForm(request.form, page)
    if form.validate():
        form.populate_obj(page)
        page.put()
        flash(u'Страница успешно сохранен', 'correct')
        return redirect(url_for("edit_page", id=page.key()))
    else:
        return render_template('admin/pages/edit.html', title=u'Редактировать рисунок', form=form, page=page)

@admin.route('/pages/delete/<id>/')
def delete_page(id):
    key = db.Key(id)
    db.delete(key)
    flash(u'Страница успешно удален', 'correct')
    return redirect(url_for('pages'))

@admin.route('/pages/destroy/', methods=['POST'])
def destroy_pages():
    pass
    