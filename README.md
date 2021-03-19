# Django Encore

This library integrates [Webpack Encore][1] into your Django application like
it does [Webpack Encore Bundle][2] for Symfony.

## Usage

1) Install the library from PyPI:

```shell
pip install django-encore
```

2) Configure your **settings.py** file:

Include the library:

```python
INSTALLED_APPS = [
    # ...
    'encore',
]
```

Add **ENCORE_ENTRYPOINTS_FILE** and change **STATICFILES_DIRS**:

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets_build'),
]

ENCORE_ENTRYPOINTS_FILE = os.path.join(BASE_DIR, 'assets_build') + '/build/entrypoints.json'
```

3) Use template tags in your templates:

```text
{% load encore %}

{% block javascripts %}
    {{ block.super }}
    {% encore_entry_script_tags 'demo1' %}
{% endblock %}

{% block stylesheets %}
    {{ block.super }}
    {% encore_entry_link_tags 'demo1' %}
{% endblock %}
```

See the **example** folder for more details.

## Development

First of all, install dependencies by pipenv:

```
cd example/webapp

pipenv install --dev
pipenv shell # to shell with virtual environment
```

Second, build files using Encore:

```
npm run dev
```

Then you can start the web server:

```
python manage.py runserver
```

[1]: https://github.com/symfony/webpack-encore
[2]: https://github.com/symfony/webpack-encore-bundle
