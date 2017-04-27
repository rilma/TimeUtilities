#!/usr/bin/env python
req=['nose','numpy','matplotlib']
# %%
import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception:
    pip.main(['install'] + req)
# %%
import setuptools  # enables develop
from distutils.core import setup

if __name__ == '__main__':

    setup( name='timeutil',
        packages=['timeutil'],
        version='2.1.0',
        description='Utilitities to deal with time-series lists',
        author='Ronald Ilma',
        classifiers=[
          'Intended Audience :: Science/Research',
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering :: Atmospheric Science',
          'Programming Language :: Python :: 3',
          ],
        )
