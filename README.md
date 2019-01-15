# Django Encore

This library integrates [Webpack Encore][1] into your Django application like it does [Webpack Encore Bundle][2] for Symfony.

## Usage

1) Install the library by pip:

```shell
pip install django-encore
```

or add the dependency into your Pipfile:

```text
django-encore = "==0.1.0"
```

2) Include the library in your **settings.py** file.

3) Add template tags in your templates:

```text
{% block javascripts %}
    {{ parent() }}

    {{ encore_entry_script_tags('entry1') }}
{% endblock %}

{% block stylesheets %}
    {{ parent() }}

    {{ encore_entry_link_tags('entry1') }}
{% endblock %}
```

[1]: https://github.com/symfony/webpack-encore
[2]: https://github.com/symfony/webpack-encore-bundle
