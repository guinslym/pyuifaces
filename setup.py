#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from distutils.core import setup
from setuptools import find_packages

setup(
    name='pyuifaces',
    version='0.0.5',
    keywords=['uifaces', 'avatar', 'picture', 'image'],
    url='https://github.com/guinslym/pyuifaces',
    license='MIT',
    author='Guinsly Mondésir',
    author_email='agmond@gmx.com.br',
    description="This package uses UIfaces.com ( https://www.uifaces.com/ ) to fake user picture on your app. ",
    packages=find_packages(),
    requires=["requests"],
    install_requires=["requests"],

    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        "Intended Audience :: End Users/Desktop",
        "Operating System :: OS Independent",
        "License :: Public Domain",
        "Development Status :: 4 - Beta",
        "Topic :: Internet :: WWW/HTTP",
        "Environment :: Console"
                 ],
)
