#!/usr/bin/env python
import setuptools  # enables develop
from distutils.core import setup

if __name__ == '__main__':

    setup( name='timeutil',
        packages=['timeutil'],
        version='2.0.0',
        description='Utilitities to deal with time-series lists', 
        author='Ronald Ilma', 
        author_email='rri5@cornell.edu',
        )
