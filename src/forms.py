# -*- coding: utf-8 -*-
'''
Created on 27.03.2011

@author: ded
'''

from wtforms import Form, TextField, TextAreaField, FileField, SelectField, validators

class PictureForm(Form):
    title = TextField(u'Название', [validators.Required(u'Название фото обязательно')])
    sub_title = TextField(u'Короткое описание', [validators.Required(u'Короткое описание обязательно')])
    description = TextAreaField(u'Описание', [validators.Required(u'Описание обязательно')])
    status = SelectField(u'Статус', [validators.Required(u'Выберите статус публикации')],  choices=[('1', u'Активно'), ('1', u'Заблокировано')])
    file = FileField(u'Изображение')
    
