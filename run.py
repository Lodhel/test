import aiohttp_cors
from aiohttp import web

import asyncio

from routes import routes


class Main:

    def _run(self):
        loop = asyncio.get_event_loop()

        app = web.Application(loop=loop)
        app.router.add_routes(routes)
        cors = aiohttp_cors.setup(app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                    allow_credentials=True,
                    expose_headers="*",
                    allow_headers="*",
                )
        })

        for route in list(app.router.routes()):
            cors.add(route)

        web.run_app(app)


if __name__ == "__main__":
    Main()._run()