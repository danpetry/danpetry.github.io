#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Petry'
SITENAME = 'Dan Petry'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

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

MENUITEMS = (('Production', '/production.html'),
             ('Coding', '/coding.html'),)

DEFAULT_PAGINATION = False

USE_LESS = True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
