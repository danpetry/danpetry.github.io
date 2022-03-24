#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Petry'
SITENAME = 'Dan Petry'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['img', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/apple-touch-icon-57x57.png': {'path': 'apple-touch-icon-57x57.png'},
    'extra/apple-touch-icon-72x72.png': {'path': 'apple-touch-icon-72x72.png'},
    'extra/apple-touch-icon-76x76.png': {'path': 'apple-touch-icon-76x76.png'},
    'extra/apple-touch-icon-114x114.png': {'path': 'apple-touch-icon-114x114.png'},
    'extra/apple-touch-icon-120x120.png': {'path': 'apple-touch-icon-120x120.png'},
    'extra/apple-touch-icon-144x144.png': {'path': 'apple-touch-icon-144x144.png'},
    'extra/apple-touch-icon-152x152.png': {'path': 'apple-touch-icon-152x152.png'},
    'extra/apple-touch-icon-180x180.png': {'path': 'apple-touch-icon-180x180.png'},
}

MEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/danpetry'),
    ('resident-advisor',
        'https://www.residentadvisor.net/profile/danielpetry/contrib'),
    ('soundcloud', 'https://soundcloud.com/danielpetry'),
)

DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = False

USE_LESS = True
THEME = './my-theme'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
