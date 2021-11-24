from distutils.core import setup
from setuptools import find_packages

setup(
    name='Miniservice',
    version='0.0.1',
    description='A tiny wsgi service for testing the oslo_service library',
    packages=find_packages(include=['miniservice', 'oslo_service']),
    install_requires=['flask','oslo_config', 'eventlet', 'oslo_concurrency',
                      'oslo_utils', 'oslo_log', 'yappi']
)
