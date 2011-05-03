#!/usr/bin/python
# -*- coding: utf-8 -*-

from gallery.models import User
from wtforms import Form, TextField, TextAreaField, validators, ValidationError, PasswordField, SelectField, FileField
from google.appengine.ext import db
from google.appengine.api.datastore_types import Key

class UserForm(Form):
	key = Key()
	login = TextField(u'Логин', [validators.Length(message=u'Поле логин не может содержать более 64 символов', max=64), validators.Required(u'Логин обязателен')])
	email = TextField(u'Электронный адрес', [validators.Length(message=u'Поле электронный адрес не может содержать более 64 символов',max=64), validators.Required(u'Электронный адрес обязателен'), validators.Email(u'Введен недопустимы электронный адрес')])
	password = PasswordField(u'Пароль', [validators.Length(message=u'Пароль не может содержать менее 6 и более 64 символов',min=6, max=64), validators.Required(u'Пароль обязателен')])
	password_confirmation = PasswordField(u'Подтверждение пароля', [validators.Required(u'Подтверждение пароля обязателено')])
	status = SelectField(u'Статус', [validators.Required(u'Подтверждение пароля обязателено')], choices=[(1, 'Активно'), (0, 'Заблокировано')], coerce=int)
	
	def validate_password_confirmation(form, field):
		if field.data != form.password.data:
			raise ValidationError('Пароль и подтверждение пароля не совпадают')
	
	def validate_login(form, field):
		user = User.all().filter('login = ', field.data).get()
		if user is not None and form.key.data != user.key():
			raise ValidationError('Такой Логин уже существует')
	
	def validate_email(form, field):
		user= User.all().filter('email = ', field.data).get()
		if user is not None and form.key.data != user.key():
			raise ValidationError('Такой Электронный адрес уже существует')
		
class PictureForm(Form):
    title = TextField(u'Название', [validators.Required(u'Название фото обязательно')])
    sub_title = TextField(u'Короткое описание', [validators.Required(u'Короткое описание обязательно')])
    description = TextAreaField(u'Описание', [validators.Required(u'Описание обязательно')])
    status = SelectField(u'Статус', [validators.Required(u'Выберите статус публикации')],  choices=[(1, u'Активно'), (2, u'Заблокировано')], coerce=int)
    file = FileField(u'Изображение')
    
class PageForm(Form):
    title = TextField(u'Название', [validators.Required(u'Название обязательно')])
    url = TextField(u'Ссылка', [validators.Required(u'Ссылка обязательна')])
    keywords = TextAreaField(u'Ключевые слова', [validators.Required(u'Ключевые слова обязательны')])
    description = TextAreaField(u'Описание', [validators.Required(u'Описание обязательно')])
    body = TextAreaField(u'Текст страницы', [validators.Required(u'Текст страницы обязателен')])
    status = SelectField(u'Статус', [validators.Required(u'Выберите статус публикации')],  choices=[(1, u'Активно'), (2, u'Заблокировано')], coerce=int)
		
