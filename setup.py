#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

VERSION = [l for l in read('procfs/__init__.py').splitlines()
           if l.startswith('__version__ =')][0].split("'")[1]

kw = {}
if sys.version_info >= (3,):
    kw['use_2to3'] = True

setup(
    name='procfs',
    version=VERSION,
    packages=find_packages(),
    author='Philippe Muller',
    author_email='philippe.muller@gmail.com',
    description='Python API for the Linux /proc virtual filesystem',
    long_description=read('README.rst'),
    license='BSD',
    keywords='linux proc procfs system kernel',
    url='https://github.com/pmuller/procfs',
    platforms=['Linux'],
    entry_points={
        'console_scripts': [
            'procfs = procfs.cli:run',
            'procfsd = procfs.http:run',
        ]},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Operating System Kernels :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    **kw
)
