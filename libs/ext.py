# -*- coding: utf-8 -*-

"""
    ext
    ~~~

    Good place for pluggable extensions.

"""

from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment
from flask.ext.mako import MakoTemplates


db = SQLAlchemy()
assets = Environment()
login_manager = LoginManager()


# Almost any modern Flask extension has special init_app()
# method for deferred app binding. But there are a couple of
# popular extensions that no nothing about such use case.

toolbar = lambda app: DebugToolbarExtension(app)  # has no init_app()


mako = lambda app:MakoTemplates(app)
