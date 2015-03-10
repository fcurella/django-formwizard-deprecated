Django FormWizard Deprecated
============================

This package contains the original ``django.contrib.formtools.legacy.FormWizard`` from Django 1.5.12.

It's intended as backward-compatible quick fix for your project if you're upgrading to
Django 1.6, which deprecates the old implementation.


Installation
------------

This package is also available on PyPI.

::

    $ pip install django-formwizard-deprecated

Usage
-----

Replace your imports. Old::

    from django.contrib.formtools import FormWizard

New::

    from formwizard_deprecated import FormWizard


Support
-------

This package will updated only when (and if) ``django.contrib.formtools.legacy.FormWizard`` will ever change in the Django 1.5.x series.
It is only for backward-compatibility purposes and there will be no support nor bugfixes.
