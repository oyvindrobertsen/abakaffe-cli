# -*- coding: latin-1 -*-
from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), 'VERSION'), 'r') as f:
    version = f.read()

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'r') as f:
    readme = f.read()

setup(name = 'abakaffe-cli',
      version = version,
      description = 'A CLI for the Abakus Coffee API',
      long_description = readme,
      author = 'Øyvind Robertsen, Martin Hallén',
      author_email = ['oyvindrobertsen@gmail.com', 'marthall@outlook.com'],
      url = 'http://github.com/oyvindrobertsen/abakaffe-cli',
      install_requires = ['simplejson'],
      license = 'MIT',
      keywords = 'Abakus coffee API',
      scripts = ['abakaffe'], 
      )
