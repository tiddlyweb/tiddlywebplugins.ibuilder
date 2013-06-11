AUTHOR = 'Chris Dent'
AUTHOR_EMAIL = 'cdent@peermore.com'
NAME = 'tiddlywebplugins.ibuilder'
DESCRIPTION = 'Build TiddlyWeb instance packages'
VERSION = '0.1.3'


import os

from setuptools import setup, find_packages


# You should carefully review the below (install_requires especially).
setup(
    namespace_packages = ['tiddlywebplugins'],
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    scripts = ['twibuilder'],
    url = 'http://pypi.python.org/pypi/%s' % NAME,
    platforms = 'Posix; MacOS X; Windows',
    packages = find_packages(exclude=['test', 'testpackage']),
    install_requires = ['tiddlyweb',
        'tiddlywebplugins.pkgstore',
        'tiddlywebplugins.twimport'
        ],
    zip_safe = False
)
