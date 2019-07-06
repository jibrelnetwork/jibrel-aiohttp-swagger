from urllib.parse import urljoin

from aiohttp.web import Request, Response

from .utils import load_spec_file, load_api_index_html


async def spec_handler(request: Request, spec_path: str):
    json_content = load_spec_file(spec_path)
    return Response(text=json_content, content_type="application/json")


async def home_handler(request: Request, *, static_url, template_path, spec_url, api_title):
    return Response(text=load_api_index_html(
        static_url=static_url,
        template_path=template_path,
        spec_url=spec_url,
        api_title=api_title,
    ), content_type='text/html')
