from urllib.parse import urljoin

from aiohttp.web import Request, Response

from .utils import load_spec_file, load_api_index_html, read_version


async def spec_handler(request: Request, spec_path: str, version_file_path = None):
    json_content = load_spec_file(spec_path)
    if version_file_path:
        version = read_version(version_file_path)
        if version:
            json_content['info']['version'] = version
    return Response(text=json_content, content_type="application/json")


async def home_handler(request: Request, *, static_url, template_path, spec_url, api_title):
    return Response(text=load_api_index_html(
        static_url=static_url,
        template_path=template_path,
        spec_url=spec_url,
        api_title=api_title,
    ), content_type='text/html')
