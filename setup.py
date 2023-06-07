#!/usr/bin/env python

from setuptools import setup

setup(name='keeptalking',
      version='0.0.1',
      description='Forensic audio analysis tool focused on voice identification and enhancement',
      maintainer='Subliminal Industries',
      maintainer_email='subliminalindustries@pm.me',
      url='https://github.com/subliminalindustries/keeptalking',
      packages=['keeptalking'],
      keywords=['forensic', 'audio', 'analysis', 'voice', 'enhancement'],
      install_requires=[
          'audeer>=1.20.1',
          'audiofile>=1.2.1',
          'audmath>=1.2.1',
          'build>=0.10.0',
          'cffi>=1.15.1',
          'contourpy>=1.0.7',
          'cycler>=0.11.0',
          'fonttools>=4.39.4',
          'kiwisolver>=1.4.4',
          'matplotlib>=3.7.1',
          'numpy>=1.24.3',
          'packaging>=23.1',
          'Pillow>=9.5.0',
          'pycparser>=2.21',
          'pyparsing>=3.0.9',
          'pyproject_hooks>=1.0.0',
          'python-dateutil>=2.8.2',
          'scipy>=1.10.1',
          'six>=1.16.0',
          'sklearn>=0.0.post5',
          'soundfile>=0.12.1',
          'tqdm>=4.65.0'
      ],
      license='MIT License'
)
