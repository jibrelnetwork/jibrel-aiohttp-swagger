#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['pyyaml', 'aiohttp']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Roman Tolkachyov",
    author_email='roman.tolkachyov@jibrel.network',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Plugin for aiohttp with swagger support a",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='jibrel_aiohttp_swagger',
    name='jibrel_aiohttp_swagger',
    packages=find_packages(include=['jibrel_aiohttp_swagger']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jibrelnetwork/jibrel-aiohttp-swagger',
    version='0.1.0',
    zip_safe=False,
)
