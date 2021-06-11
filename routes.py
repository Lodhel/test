import json

from aiohttp import web
from aiohttp.web_response import json_response
from aiohttp_cors import CorsViewMixin

from parser import URL_Parser
from models import URL_Information


routes = web.RouteTableDef()


@routes.view("/api/check_url/")
class CHECK_URL_ViewSet(web.View, CorsViewMixin):

    async def post(self):
        _data = await self.request.json()
        URL = _data.get('url', None)
        if not URL:
            return json_response({"error": "url field is None"})

        _result = await URL_Parser(URL).make_data()
        return json_response(_result)

    async def get(self):
        _data = await self.request.json()
        try:
            _pk: int = _data.get('pk', None)
        except Exception as ex:
            return json_response({'error': str(ex)})
        if not _pk:
            return json_response({"error": "pk field is None"})
        instance = await URL_Information.get(_pk)
        if instance:
            return json_response({"data": eval(instance.data)})
        else:
            return json_response({"data": None})