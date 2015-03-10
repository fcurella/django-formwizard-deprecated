import os
from setuptools import setup, find_packages

__version__ = "0.0.1"


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = []

setup(
    name = "django-formwizard-deprecated",
    version = __version__,
    description = "Original django.contrib.formtools.legacy.FormWizard from Django 1.5.12",
    long_description = read('README.rst'),
    url = 'https://github.com/fcurella/django-formwizard-deprecated',
    license = 'BSD',
    maintainer = 'Flavio Curella',
    maintainer_email = 'flavio.curella@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    classifiers = [
        'Development Status :: 7 - Inactive',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
