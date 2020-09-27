"""
Setup Module to setup Python Handlers (Git Handlers) for the Git Plugin.
"""
import setuptools
import os

requirements_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements.txt')
with open(requirements_file, 'r') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='featurize',
    version='0.0.1',
    author='chenglu',
    description='',
    packages=setuptools.find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': ['featurize = featurize:cli']
    }
)
