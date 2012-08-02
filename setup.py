# -*- coding: utf-8 -*-
from distutils.core import setup

setup(name='yelp-py',
      version='0.1',
      description='Python wrapper for yelp api 2.0',
      author='Kirill Nikolenko',
      author_email='kirill.nikolenko@gmail.com',
      url='https://github.com/mobedigg/Yelp-py',
      py_modules=['yelp'],
      install_requires=['oauth2',]
     )