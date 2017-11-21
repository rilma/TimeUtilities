#!/usr/bin/env python
req=['nose','numpy']
# %%
from setuptools import setup,find_packages

if __name__ == '__main__':

    setup(name='timeutil',
        packages=find_packages(),
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
        python_requires='>=2.7',
        install_requires=req,
        
        )
