# -*- coding: utf-8 -*-
'''
Created on 27.03.2011

@author: ded
'''

import datetime
from google.appengine.ext import db

class Status(db.Model):
    title = db.StringProperty(verbose_name=u'Заголовок')
    created_at = db.DateTimeProperty(verbose_name=u'Создано', auto_now=False, auto_now_add=True)
    updated_at = db.DateTimeProperty(verbose_name=u'Обновлено', auto_now=True, auto_now_add=True)

class Image(db.Model):
    title = db.StringProperty(verbose_name=u'Название', required=True)
    sub_title = db.StringProperty(verbose_name=u'Подзаголовок', required=True)
    description = db.TextProperty(verbose_name=u'Описание', required=True)
    status = db.ReferenceProperty(Status, verbose_name=u'Статус')
    file = db.BlobProperty(verbose_name=u'Файл изображения')
    created_at = db.DateTimeProperty(verbose_name=u'Создано', auto_now=False, auto_now_add=True)
    updated_at = db.DateTimeProperty(verbose_name=u'Обновлено', auto_now=True, auto_now_add=True)
    