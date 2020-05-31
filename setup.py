from setuptools import setup, find_packages

setup(
    name='pygooey',
    version='1.0.0',
    url='https://github.com/pmfrank/pygooey.git',
    author='metulburr',
    author_email='none@unknown.com',
    description='A text input and button interface GUI frame work for PyGame',
    packages=find_packages(),    
    install_requires=['pygame >= 1.9.6'],
)
