import json

from aiohttp import web
from aiohttp.web_response import json_response
from aiohttp_cors import CorsViewMixin

from parser import URL_Parser


routes = web.RouteTableDef()


@routes.view("/api/check_url/")
class TEST_URL_ViewSet(web.View, CorsViewMixin):

    async def post(self):
        _data = await self.request.json()
        URL = _data.get('url', None)
        if not URL:
            return json_response({"error": "url field is None"})

        return json_response(URL_Parser(URL).make_data())