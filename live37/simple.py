import sys, os
def oass():
     pass
from configparser import ConfigParser

from requests import get

d = {'verbose': 0,
     'url': 'http://google.com',
     'port': 8000,
     'bananas': 'pijamas'}

e = {'verbose': 0,
     'url': 'http://google.com',
     'port': 8000,
     'bananas': 'pijamas'}

config = ConfigParser(d,
                      allow_no_value=True,
                      delimiters=('=', ':', '-'),
                      comment_prefixes=('#', ';'),
                      inline_comment_prefixes='#',
                      strict=False)

config['DEFAULT'] = e
config.read('example.ini')
default_config = dict(config['default'])
xpto_config = dict(config['xpto'])

print(xpto_config)
print(default_config)
print(default_config['url'],
      get(default_config['url']))