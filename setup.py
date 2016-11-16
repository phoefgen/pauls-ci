#!/usr/bin/env python

import os
from setuptools import find_packages, setup


if __name__ == '__main__':
    setup(
        name = 'pauls_ci',
        packages = find_packages(),
        package_data = {'': ['*.j2']},
        entry_points={'console_scripts': ['paulsci = pauls_ci.main:__main__']},
        version = '0.0.1',
        author = 'Paul Hoefgen',
        author_email = '',
        description = ('blah blah marketing copy'),
    )
