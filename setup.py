from distutils.core import setup

setup(name='abakaffe-cli',
      version='0.1',
      description='A CLI for the Abakus Coffee API',
      author='Øyvind Robertsen',
      url='http://github.com/oyvindrobertsen/abakaffe-cli',
      py_modules=['abakaffe'],
      install_requires=['simplejson'],
      )
