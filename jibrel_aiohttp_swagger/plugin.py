# -*- coding: utf-8 -*-

"""Main module."""

from os.path import dirname
from functools import partial
from urllib.parse import urljoin
from pathlib import Path

from aiohttp.web import Application

from .handlers import spec_handler, home_handler
from .utils import get_static_path


DEFAULT_TEMPLATE = str(Path(dirname(__file__)) / 'templates' / 'index.html')

DEFAULT_TITLE = "Swagger UI"


def setup_swagger(app: Application,
                  spec_path: str,
                  *,
                  api_root="/api/doc/",
                  spec_uri=None,
                  serve_static=True,
                  static_url="/api/doc/static",
                  template_path=DEFAULT_TEMPLATE,
                  api_title=DEFAULT_TITLE,
                  version_file_path=None):
    """Setup swagger UI endpoints.

    :param app: application to install swagger endpoints to
    :param spec_path: spec yaml path
    :param api_root: custom base api url
    :param spec_uri: custom spec url
    :param serve_static: serve static using `router.add_static` (by default)
    :param static_url: static base url
    :param template_path: template file path
    :param api_title: api title
    :param version_file_path: version file path to substitute version in spec
    :return:
    """
    if spec_uri is None:
        spec_uri = urljoin(api_root, "swagger.json")

    # add api home (index.html)
    home_handler_instance = partial(home_handler,
                                    static_url=static_url,
                                    spec_url=spec_uri,
                                    template_path=template_path,
                                    api_title=api_title)
    app.router.add_get(api_root, home_handler_instance)

    # serve spec json
    spec_handler_instance = partial(
        spec_handler, spec_path=spec_path, version_file_path=version_file_path
    )
    app.router.add_get(spec_uri, spec_handler_instance)

    if serve_static:
        # add static handler
        app.router.add_static(static_url, get_static_path())
