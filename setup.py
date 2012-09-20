
from distutils.core import setup
from setuptools import find_packages

MAJOR_VERSION = '1'
MINOR_VERSION = '0a1'

data_files=[]

setup(
    name='vavista-rpc',
    version='%s.%s' % (MAJOR_VERSION, MINOR_VERSION),
    author='Conor Dowling, Kevin Gill',
    author_email='kevin.gill@openapp.ie',
    license="TO BE DETERMINED",
    platforms=["linux"],
    url='http://www.python.org/doc/current/ext/building.html',
    description='VAVista RPC interface',
    long_description='''
    This is a simple Pythonic mechanism for invoking VistA RPCs.
    The code was developed by Conor Dowling as part of the FMQL
    project.
    ''',
    namespace_packages=['vavista'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False)

