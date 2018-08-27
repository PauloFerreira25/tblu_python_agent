#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'click-log>=0.3.2',
                'apscheduler>=3.5.1', 'tblu_module_so>=0.1.2']

setup_requirements = []

test_requirements = []

setup(
    author="TBlu-Company",
    author_email='dev@tblu.com.br',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="TBlu Python Agent",
    entry_points={
        'console_scripts': [
            'tblu_python_agent=tblu_python_agent.cli:cli',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='tblu_python_agent',
    name='tblu_python_agent',
    packages=find_packages(include=['tblu_python_agent']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/TBlu-Company/tblu_python_agent',
    version='0.1.0',
    zip_safe=False,
)
