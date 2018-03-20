#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'sudo'
SITENAME = u'Criticón '
HIDE_SITENAME = True
SITEURL = ''
SITELOGO = 'images/logo-criticon-sm.png'
PATH = 'content'
OUTPUT_PATH = '../docs'
TIMEZONE = 'America/Bogota'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Repositorio del Proyecto', 'https://github.com/semillero-obsolescencia/criticon'),
         ('Semillero Universitario de Obsolescencia - SUDO', 'https://github.com/semillero-obsolescencia'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "theme/pelican-bootstrap3"

PLUGIN_PATHS = ['pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
