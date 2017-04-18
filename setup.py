'''Setup file for the minimally_useful_application program.'''
from setuptools import setup, find_packages


with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

setup(
    name='minimally_useful_application',
    version='0.1.0',
    description='A minimally useful application demonstrating common \
                 requirements for a program in Python.',
    long_description=README,
    author='Eugene Kovalev',
    author_email='euge.kovalev@gmail.com',
    url='https://github.com/Abraxos/minimally_useful_application',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=REQUIREMENTS,
    entry_points={'console_scripts' : ['mua-timing = minimally_useful_application.core:main']}
)
