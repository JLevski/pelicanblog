#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Josh Levin'
SITENAME = "Go When You're Ready"
SITEURL = 'https://jlevski.github.io/pelicanblog'

PATH = 'content'
ARTICLE_PATHS = ['Posts']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

THEME = 'theme/pelican-bootstrap3-lovers'
BOOTSTRAP_THEME = 'lovers'
PROFILE_PICTURE = 'profile_pic.png'
HEADER_IMAGE = 'profile_pic.png'
# BOOTSTRAP_NAVBAR_INVERSE = False
# FAVICON = 'extra/favicon.ico'

# PLUGIN_PATHS = ['plugins/pelican-plugins']
# PLUGINS = ['i18n_subsites']
#
# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

DISQUS_SITENAME = "Go When You're Ready"  # use this to identify
DISQUS_SHORTNAME = 'https-jlevski-github-io-pelicanblog'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/popt_culture'),
          ('Github', 'https://github.com/JLevski'),
          )

DEFAULT_PAGINATION = 5

DISPLAY_PAGES_ON_MENU = True

RELATIVE_URLS = True

# To be added - archives
# YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
