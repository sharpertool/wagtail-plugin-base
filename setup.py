#!/usr/bin/env python
"""
Replace the values in setup to correspond to your own plugin information.
Information entered here will be used for your PyPi package page and the package build.
"""

from setuptools import setup, find_packages

setup(name='plugin-base',
      version='1.0.0',
      description='A blank template for creating Wagtail plugins.',
      url='https://github.com/vixdigital/wagtail-plugin-base',
      author='VIX Digital',
      author_email='info@vix.digital',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'wagtail>=2.0',
      ],
      zip_safe=False)
