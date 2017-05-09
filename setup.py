try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from setuptools import find_packages

setup(
    name='SuperSimpleML',
    version='0.0.1',
    url='https://github.com/carryme9527/SuperSimpleML/',
    license='BSD',
    author='carryme9527',
    author_email='carryme9527@gmail.com',
    description='Super Simple Machine Learning',
    packages=find_packages(),
)
