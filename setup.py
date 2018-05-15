#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='xdict',
    version='0.0',
    author='Dongjie Chen',
    author_email='midwinter1993@gmail.com',
    packages=['xdict']
    scripts=['xdict/xdict'],
    url='http://github.com/midwinter1993/xdict',
    license='LICENSE',
    description='My simple translato .',
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read().strip().split('\n')
)
