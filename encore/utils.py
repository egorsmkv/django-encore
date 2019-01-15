import os
import json
from functools import lru_cache

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


@lru_cache(maxsize=32)
def get_entries_data():
    filename = settings.ENCORE_ENTRYPOINTS_FILE

    if not os.path.exists(filename):
        raise ImproperlyConfigured('The encore entrypoints file does not exist')

    with open(filename) as handle:
        entry = json.load(handle)

        return entry['entrypoints']


def get_files(entry='app', ftype='js'):
    data = get_entries_data()

    if entry not in data:
        raise ImproperlyConfigured(f'The entry key "{entry}" does not exist in the encore entrypoints file')

    if ftype not in data[entry]:
        return []

    return data[entry][ftype]
