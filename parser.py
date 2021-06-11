import requests
from bs4 import BeautifulSoup

from models import URL_Information
from asyncpg.exceptions import UniqueViolationError


class URL_Parser:

    def __init__(self, url):

        self.URL = url

    def get_url_request(self):
        try:
            request = requests.get(self.URL)
        except Exception as ex:
            return False, {'error': str(ex)}
        if request.status_code == 200:
            return True, BeautifulSoup(request.text, 'html.parser')
        else:
            if request.text:
                return False, {'status_code': request.status_code, 'text': request.text}
            return False, {'status_code': request.status_code}

    def get_nested(self, _name_tag, soup):
        return len([i for i in soup.findChild(_name_tag).children if i.name])

    async def make_data(self):
        soup = self.get_url_request()
        if not soup[0]:
            return soup[1]
        tags_array = sorted(set(child.name for child in soup[1].recursiveChildGenerator() if child.name))
        DATA = [
            {
                name_tag:
                    {
                        'count': len(soup[1].find_all(name_tag)),
                        'nested': self.get_nested(name_tag, soup[1])
                    }
            }
            for name_tag in tags_array
        ]

        try:
            instance = await URL_Information.create(data=str(DATA), url=self.URL)
            return {'id': instance.id}
        except UniqueViolationError:
            return {'error': 'Key (url)=({}) already exists'.format(self.URL)}
