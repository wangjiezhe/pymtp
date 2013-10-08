#!/usr/bin/env python
# 
# Setup.py for Pymtp
#

from distutils.core import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = "PyMTP",
      version = "0.1.0",
      description = "LibMTP bindings in Python",
      long_description=read('README'),
      author = "Nick Devito",
      author_email = "nick@nick125.com",
      url = "https://pypi.python.org/pypi/PyMTP",
      py_modules = ["pymtp"])
