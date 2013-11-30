# -*- coding: latin-1 -*-
from setuptools import setup, find_packages
from abakaffe.version import __version__

setup(name='abakaffe-cli',
      version=__version__,
      packages=find_packages(),
      entry_points={
          'console_scripts': ['abakaffe=abakaffe.script:main'],
          },
      description='A CLI for the Abakus Coffee API',
      author='Øyvind Robertsen, Martin Hallén',
      author_email=['oyvindrobertsen@gmail.com', 'marthall@outlook.com'],
      url='http://github.com/oyvindrobertsen/abakaffe-cli',
      install_requires=['simplejson', 'nose'],
      license='MIT',
      keywords='Abakus coffee API',
      )
