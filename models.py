import os
import asyncio

from gino import Gino
from sqlalchemy.dialects.postgresql import JSONB


DATABASE = {
    'USERNAME': os.environ.get("SQL_USER", 'postgres'),
    'PASSWORD': os.environ.get("SQL_PASSWORD", 'password'),
    'HOST': os.environ.get("SQL_HOST", 'localhost'),
    'NAME': os.environ.get("SQL_DATABASE", 'test'),
}


db = Gino()


async def connect():
    await db.set_bind('postgresql://{}:{}@{}/{}'.format(
        DATABASE["USERNAME"], DATABASE["PASSWORD"], DATABASE["HOST"], DATABASE["NAME"]
    ))

asyncio.get_event_loop().run_until_complete(connect())


class URL_Information(db.Model):
    __tablename__ = 'url_information'

    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(unique=True)
    data = db.Column()
