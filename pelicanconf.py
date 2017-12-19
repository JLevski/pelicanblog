#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Josh Levin'
SITENAME = "Go When You're Ready"
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['Posts']
STATIC_PATHS = [
                'images',
                'extra',
]
EXTRA_PATHS_METADATA = {
                        'extra/favicon.ico': {'path': 'favicon.ico'},
                        'extra/robots.txt': {'path': 'robots.txt'},
}

PLUGIN_PATHS = ['plugins']

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('Follow me on Twitter', 'https://twitter.com/popt_culture'),
          ('Github', 'https://github.com/JLevski'),
          )

DEFAULT_PAGINATION = 5

DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
