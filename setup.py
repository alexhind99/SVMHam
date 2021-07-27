# -*- coding: utf-8 -*-

"""
Created on Thu Jul 22 08:28:49 2021

@author: alexa
"""

from setuptools import find_packages
from distutils.core import setup

import os
on_rtd = os.environ.get('READTHEDOCS') == 'True'

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

package_name = 'svmds'
version_num = '0.1.0'

def main():
    install_requires = ['m2r'] if on_rtd else []
    setup(
        name = package_name,

        version = version_num,
        
        description = 'Python package for computing DS with SVM',
        
        long_description = readme,
        
        author = 'Alexander Hind',
        
        author_email = 'vg18523@bristol.ac.uk',
        
        url = 'https://github.com/alexhind99/SVMHam',
        
        license = license,
        
        packages=['svmham'],
        package_dir={'svmham': 'src'},

        install_requires = requirements
    )


if __name__ == '__main__':
    main()