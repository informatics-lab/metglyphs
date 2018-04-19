#!/usr/bin/env python3
import os
from setuptools import setup, find_packages

__version__ = '0.1.0'

PACKAGE_NAME = 'metglyphs'
HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.md'), encoding="utf8").read()

PACKAGES = find_packages(exclude=['tests', 'tests.*', 'modules',
                                  'modules.*', 'docs', 'docs.*'])


# For now we simply define the install_requires based on the contents
# of requirements.txt. In the future, install_requires may become much
# looser than the (automatically) resolved requirements.txt.
with open(os.path.join(HERE, 'requirements.txt'), 'r') as fh:
    REQUIRES = [line.strip() for line in fh]


setup(
    name=PACKAGE_NAME,
    version=__version__,
    license='BSD-3-Clause ',
    url='',
    download_url='',
    author='Jacob Tomlinson',
    author_email='jacob.tomlinson@informaticslab.co.uk',
    description='A library for converting between weather codes, symbols and phrases.',
    long_description=README,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=REQUIRES,
    test_suite='tests',
)
