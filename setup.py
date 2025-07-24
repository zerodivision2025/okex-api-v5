#!/usr/bin/env python3
from setuptools import setup

setup(
    name='okex-api-v5',
    version='1.1.21',
    packages=['okex'],
    install_requires=['httpx[http2]'],
    author='zerodivision',
    author_email='zerodivision@zerodivision.tech',
    url='https://www.zerodivision.tech/'
)
