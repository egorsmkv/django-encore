from django import template
from django.utils.safestring import mark_safe

from ..utils import get_files

register = template.Library()


@register.simple_tag
def encore_entry_js_files(entry='app'):
    return get_files(entry, 'js')


@register.simple_tag
def encore_entry_css_files(entry='app'):
    return get_files(entry, 'css')


@register.simple_tag
def encore_entry_script_tags(entry):
    scripts = []
    for url in get_files(entry, 'js'):
        scripts.append(f'<script src="{url}"></script>')

    return mark_safe('\n'.join(scripts))


@register.simple_tag
def encore_entry_link_tags(entry):
    links = []
    for url in get_files(entry, 'css'):
        links.append(f'<link rel="stylesheet" href="{url}">')

    return mark_safe('\n'.join(links))
