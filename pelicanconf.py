#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Petry'
SITENAME = 'Dan Petry'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['img']

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
