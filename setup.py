import setuptools
from setuptools import setup

setup(
    name='pupy',
    version='0.0.1',
    maintainer='Folgert Karsdorp',
    packages=['pupy'],
    license='see LICENCE.md',
    long_description=open('README.md').read(),
    install_requires=[
        'numpy>=1.7.1',
    ],
)