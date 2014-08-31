#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Confu is a configuration management library.
#    Copyright © 2014  Andrey Mikhaylenko
#
#    This file is part of Confu.
#
#    Confu is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Confu is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Confu.  If not, see <http://gnu.org/licenses/>.

from setuptools import setup


setup(
    # overview
    name  = 'confu',
    description = 'Configuration management without the "FUUU~"',
    long_description = 'TODO',

    # technical info
    version = '0.0.2',
    packages = ['confu'],
    provides = ['confu'],
    install_requires = ['monk>=0.11'],

    # copyright
    author = 'Andrey Mikhaylenko',
    author_email = 'neithere@gmail.com',
    license  = 'GNU Lesser General Public License (LGPL), Version 3',

    # more info
    url = 'http://github.com/neithere/confu/',

    # categorization
    keywords = ('configuration settings modular application management'),
    classifiers  = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
