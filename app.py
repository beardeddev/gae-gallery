# -*- coding: utf-8 -*-

from flask import Flask
from google.appengine.ext.webapp.util import run_wsgi_app

secret_key = '\x06\x00(\xcd\xf5\xdffn\x87\xbd\xd1\xe3f\x19\xb9|\xc7\xef\x98o\x95\x1e\x85\xdf'

app = Flask(__name__)
app.secret_key = secret_key

from gallery.apps.admin.views import admin
from gallery.apps.frontend.views import frontend

app.register_module(admin, url_prefix='/admin')
app.register_module(frontend)

app.debug = True

if __name__ == "__main__":
    run_wsgi_app(app)

