# -*- coding: utf-8 -*-
'''
Created on 27.03.2011

@author: ded
'''

from google.appengine.ext import db

class Picture(db.Model):
    title = db.StringProperty(verbose_name=u'Название')
    sub_title = db.StringProperty(verbose_name=u'Подзаголовок')
    description = db.TextProperty(verbose_name=u'Описание')
    data = db.BlobProperty(verbose_name=u'Файл изображения')
    ext = db.StringProperty(verbose_name=u'Расширение')
    content_type = db.StringProperty(verbose_name=u'Тип')
    created_at = db.DateTimeProperty(verbose_name=u'Создано', auto_now=False, auto_now_add=True)
    updated_at = db.DateTimeProperty(verbose_name=u'Обновлено', auto_now=True, auto_now_add=True)
    