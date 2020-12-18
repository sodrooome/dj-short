import io
import os
import re
from setuptools import setup, find_packages

with io.open('dj/version.py', 'rt', encoding='utf-8') as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dj-short',
    version=version,
    author="Ryan Febriansyah",
    author_email="15523163@students.uii.ac.id",
    description="Simple CLI for shortcutting Django command",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Click',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.5',
    entry_points='''
        [console_scripts]
        dj=dj.main:dj
    ''',
)