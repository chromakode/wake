#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='wake',
    description='A simple lifestream web frontend to been.',
    version='0.1',
    author='Max Goodman',
    author_email='c@chromakode.com',
    keywords='feed lifestream',
    license='BSD',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ],
    packages=find_packages(),
    install_requires=[
        'CouchDB',
        'Flask',
        'twitter-text-py',
        'been',
    ],
    include_package_data=True,
    zip_safe=False,
)
