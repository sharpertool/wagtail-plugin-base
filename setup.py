#!/usr/bin/env python
"""
Replace the values in setup to correspond to your own plugin information.
Information entered here will be used for your PyPi package page and the package build.
"""

from setuptools import setup, find_packages

setup(name='wagtail-katex',
      version='1.0.0',
      description='Add KaTeX rendering to drafttail',
      url='https://github.com/sharpertool/wagtail-katex',
      author='SharperTool',
      author_email='ed@sharpertool.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'wagtail>=2.0',
      ],
      zip_safe=False)
