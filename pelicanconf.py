#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Josh Levin'
SITENAME = "Go When You're Ready"
SITEURL = 'https://jlevski.github.io/pelicanblog'

PATH = 'content'
ARTICLE_PATHS = ['Posts']
PAGE_PATHS = ['pages']
STATIC_PATHS = [
                'images',
                'extra',
]
EXTRA_PATHS_METADATA = {
                        'extra/favicon.ico': {'path': 'favicon.ico'},
                        'extra/robots.txt': {'path': 'robots.txt'},
}

THEME = "theme/pelican-themes/pelican-bootstrap3"
BOOTSTRAP_NAVBAR_INVERSE = False
FAVICON = 'extra/favicon.ico'

PLUGIN_PATHS = ['plugins/pelican-plugins']
PLUGINS = ['i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('Follow me on Twitter', 'https://twitter.com/popt_culture'),
          ('Github', 'https://github.com/JLevski'),
          )

DEFAULT_PAGINATION = 5

DISPLAY_PAGES_ON_MENU = True

RELATIVE_URLS = True

# To be added - archives
# YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
