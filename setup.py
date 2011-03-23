#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from distutils.core import setup


def publish():
    """Publish to PyPi"""
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

required = ['clint>=0.2.0', 'github2']

setup(
    name='humble',
    version='0.1.0',
    description='Shows stats on a given GitHub user.',
    long_description=open('README.rst').read(),
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/humble',
    packages= ['humble'],
    install_requires=required,
    license='ISC',
    classifiers=(
#       'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
    ),
    entry_points = {
        'console_scripts': [
            'humble = humble.cli:start'
        ]
    }
)
