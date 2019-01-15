Django Encore
=============

This library integrates `Webpack Encore`_ into your Django application
like it does `Webpack Encore Bundle`_ for Symfony.

Usage
-----

1) Install the library from PyPI:

.. code:: shell

    pip install django-encore

2) Configure your **settings.py** file:

Include the library:

.. code:: python

    INSTALLED_APPS = [
        # ...
        'encore',
    ]

Add **ENCORE_ENTRYPOINTS_FILE** and change **STATICFILES_DIRS**:

.. code:: python

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'assets_build'),
    ]

    ENCORE_ENTRYPOINTS_FILE = os.path.join(BASE_DIR, 'assets_build') + '/build/entrypoints.json'

3) Use template tags in your templates:

.. code:: text

    {% block javascripts %}
        {{ block.super }}

        {% encore_entry_script_tags 'demo1' %}
    {% endblock %}

    {% block stylesheets %}
        {{ block.super }}
        {% encore_entry_link_tags 'demo1' %}
    {% endblock %}

See the **example** folder for more details.

.. _Webpack Encore: https://github.com/symfony/webpack-encore
.. _Webpack Encore Bundle: https://github.com/symfony/webpack-encore-bundle
