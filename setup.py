#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-user-analytics',
    version='0.0.2',
    description='A simple way to track (client or server) user-level events asynchronously',
    author='Ragi Burhum',
    author_email='ragi@burhum.com',
    url='https://github.com/RBURHUM/django-user-analytics',
    packages=find_packages(),

    #package_dir = {'':'user_analytics'},   # tell distutils packages are under src

    package_data = {
        # If any package contains *.js files, include them:
        '': ['*.js', '*.py']
    },
    include_package_data=True,
    keywords = ["analytics", "tracking", "dashboard"],
    install_requires = [
      'celery'
    ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: System",
        ],
    long_description = """\

    django-user-analytics - Simple User level tracking and analytics
    -------------------------------------

    Features:
     - A simple middleware that manages cookies
     - Supports tracking the same user from various devices:
       If user logs in from say a phone and laptop, all the traffic from both devices will be associated
       with the same user account.
     - Ties into django's built in user authentication
     - Provides simple javascript library to record client-side events
     - All events are recorded asynchronously through Celery (thus impact to performance will be negligible)
     - Basic admin page that shows user flow
    """
)