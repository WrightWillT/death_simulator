#!/usr/bin/env python

from distutils.core import setup
#from pip.req import parse_requirements

#install_reqs = parse_requirements('requirements.txt', session='hack')

setup(name='deathsimulator',
      version='1.0',
      description='Simulates how you will die',
      author='William Wright',
      author_email='wright.will.t@gmail.com',
      url='https://github.com/WrightWillT/death_simulator',
      #packages=['numpy', 
      #          'matplotlib', 
      #          'seaborn', 
      #          'pandas', 
      #          'ipywidgets', 
      #          'jupyterthemes',
      #          'pdfrw',
      #          'scikit-learn',
      #          'setuptools'
      #         ],
      install_requires=['numpy==1.16.*',
                        'matplotlib==3.*',
                        'seaborn==0.8.1',
                        'pandas',
                        'ipywidgets',
                        'jupyterthemes',
                        'pdfrw',
                        'scikit-learn',
                        'setuptools'
                       ]
     )