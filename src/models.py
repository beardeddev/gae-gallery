# -*- coding: utf-8 -*-
'''
Created on 27.03.2011

@author: ded
'''

import datetime
from google.appengine.ext import db

class Image(db.Model):
    title = db.StringProperty(verbose_name=u'Название')
    sub_title = db.StringProperty(verbose_name=u'Подзаголовок')
    description = db.TextProperty(verbose_name=u'Описание')
    file = db.BlobProperty(verbose_name=u'Файл изображения')
    created_at = db.DateTimeProperty(verbose_name=u'Создано', auto_now=False, auto_now_add=True)
    updated_at = db.DateTimeProperty(verbose_name=u'Обновлено', auto_now=True, auto_now_add=True)
    