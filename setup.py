#!/usr/bin/env python
# 
# Setup.py for pymtp
#

from distutils.core import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = "pymtp",
      version = "0.0.5",
      description = "LibMTP bindings in Python",
      long_description=read('README'),
      author = "Nick Devito",
      author_email = "nick@nick125.com",
      url = "https://pypi.python.org/pypi/pymtp",
      py_modules = ["pymtp"],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
)
