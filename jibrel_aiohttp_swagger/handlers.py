from aiohttp.web import Request, Response, json_response

from .utils import load_spec_file, load_api_index_html, read_version


async def spec_handler(request: Request, spec_path: str, version_file_path = None):
    """Return response with spec.

    Spec version will be substituted from `version_file_path` if provided.
    """
    json_content = load_spec_file(spec_path)
    if version_file_path:
        version = read_version(version_file_path)
        if version:
            json_content['info']['version'] = version
    return json_response(json_content)


async def home_handler(request: Request, *, static_url, template_path, spec_url, api_title):
    """Render swagger UI html.
    """
    return Response(text=load_api_index_html(
        static_url=static_url,
        template_path=template_path,
        spec_url=spec_url,
        api_title=api_title,
    ), content_type='text/html')
