#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Josh Levin'
SITENAME = "Go When Ready"
SITEURL = 'https://jlevski.github.io/pelicanblog'

PATH = 'content'
ARTICLE_PATHS = ['Posts']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

THEME = 'theme/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'lovers'
AVATAR = 'images/profile_pic.png'
ABOUT_ME = 'Just trying to figure my life out. One country at a time. Also, I built this blog myself so it reflects my lack of a design aesthetic.'
BANNER = 'images/banner.png'
# BANNER_SUBTITLE = 'Testing... 1, 2, 3'
BANNER_ALL_PAGES = True
# BOOTSTRAP_NAVBAR_INVERSE = True
# FAVICON = 'extra/favicon.ico'

# DISPLAY_ARCHIVE_ON_SIDEBAR = True
# MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%b}/index.html'
# SIDEBAR_ON_LEFT = False
AUTHORS_SAVE_AS = ''


PLUGIN_PATHS = ['plugins/pelican-plugins']
PLUGINS = ['i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

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
