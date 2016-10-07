#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Wynand Booysen'
SITENAME = u'Wynand Booysen'
SITEURL = ''

THEME = '/home/dev/projects/pelican-blue/'

PLUGIN_PATHS = ['/home/dev/projects/pelican-plugins/']
PLUGINS = ['pelican_gist']

PATH = 'content'

TIMEZONE = 'Africa/Johannesburg'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SIDEBAR_DIGEST = 'SysAdmin. Developer. Tinkerer.'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/wynand-booysen-b578a915'),
          ('github', 'https://github.com/wynandbooysen'),
          ('twitter', 'https://twitter.com/wynandbooysen'),)

DEFAULT_PAGINATION = 10

MENUITEMS = [('Blog', '/')]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "wynandbooysen"
