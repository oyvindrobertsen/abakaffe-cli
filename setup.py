# -*- coding: latin-1 -*-
from setuptools import setup

setup(name = 'abakaffe-cli',
      version = '0.2',
      description = 'A CLI for the Abakus Coffee API',
      author = 'Øyvind Robertsen, Martin Hallén',
      author_email = ['oyvindrobertsen@gmail.com', 'marthall@outlook.com'],
      url = 'http://github.com/oyvindrobertsen/abakaffe-cli',
      py_modules = ['abakaffe'],
      install_requires = ['simplejson'],
      license = 'MIT',
      keywords = 'Abakus coffee API',
      scripts = ['abakaffe'], 
      )
