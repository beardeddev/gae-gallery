# -*- coding: utf-8 -*-

from google.appengine.ext import db

class User(db.Model):
    login = db.StringProperty(verbose_name=u'Логин')
    email = db.EmailProperty(verbose_name=u'Эл. адресс')
    password_salt = db.StringProperty()
    password_hash = db.StringProperty()
    status = db.IntegerProperty(verbose_name=u'Состояние')
    created_at = db.DateTimeProperty(verbose_name=u'Создано', auto_now_add=True)
    updated_at = db.DateTimeProperty(verbose_name=u'Обновлено', auto_now=True)
    
class Picture(db.Model):
    title = db.StringProperty(verbose_name=u'Название')
    sub_title = db.StringProperty(verbose_name=u'Подзаголовок')
    description = db.TextProperty(verbose_name=u'Описание')
    data = db.BlobProperty(verbose_name=u'Файл изображения')
    ext = db.StringProperty(verbose_name=u'Расширение')
    content_type = db.StringProperty(verbose_name=u'Тип')
    status = db.IntegerProperty(verbose_name=u'Состояние')
    created_at = db.DateTimeProperty(verbose_name=u'Создано', auto_now=False, auto_now_add=True)
    updated_at = db.DateTimeProperty(verbose_name=u'Обновлено', auto_now=True, auto_now_add=True)

class Page(db.Model):
    title = db.StringProperty(verbose_name=u'Название')
    url = db.StringProperty(verbose_name=u'Ссылка')
    keywords = db.StringProperty(verbose_name=u'Ключевые слова')
    description = db.StringProperty(verbose_name=u'Описание')
    body = db.TextProperty(verbose_name=u'Текст страницы')
    status = db.IntegerProperty(verbose_name=u'Состояние')
    created_at = db.DateTimeProperty(verbose_name=u'Создано', auto_now=False, auto_now_add=True)
    updated_at = db.DateTimeProperty(verbose_name=u'Обновлено', auto_now=True, auto_now_add=True)