import functools
from string import Template
from datetime import datetime, timedelta
from os.path import dirname
from pathlib import Path

try:
    import ujson as json
except ImportError:
    import json

import yaml


def timed_cache(**timedelta_kwargs):
    def _wrapper(f):
        update_delta = timedelta(**timedelta_kwargs)
        next_update = datetime.utcnow() - update_delta
        # Apply @lru_cache to f with no cache size limit
        f = functools.lru_cache(None)(f)

        @functools.wraps(f)
        def _wrapped(*args, **kwargs):
            nonlocal next_update
            now = datetime.utcnow()
            if now >= next_update:
                f.cache_clear()
                next_update = now + update_delta
            return f(*args, **kwargs)

        return _wrapped

    return _wrapper


@timed_cache(seconds=1)
def load_spec_file(spec_path):
    with open(spec_path, 'r') as fp:
        content = yaml.load(fp)
    return content


@timed_cache(seconds=1)
def load_api_index_html(*, static_url: str, template_path: str, spec_url: str,
                        api_title: str):
    with open(template_path) as fp:
        content = fp.read()
    if not static_url.endswith('/'):
        static_url = ''.join([static_url, '/'])
    return Template(content).substitute(
        SPEC_URL=spec_url,
        API_TITLE=api_title,
        STATIC_URL=static_url,
    )


@timed_cache(seconds=1)
def read_version(file_path):
    with open(file_path) as fp:
        return fp.read().strip()


def get_static_path():
    return Path(dirname(__file__)) / 'static'
