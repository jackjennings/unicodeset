from setuptools import setup
from unicodeset import __version__

setup(
    name='unicodeset',
    version=__version__,
    author='Jack Jennings',
    author_email='j@ckjennin.gs',
    py_modules=['unicodeset'],
    url='http://github.com/jackjennings/unicodeset',
    license='LICENSE',
    description='set superclass for unicode character sets',
    long_description=open('README.rst').read(),
    include_package_data=True
)
